# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_gateway_spi.client import Client as SPIClient
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_gateway_pds.client import Client as GatewayClientClient
from alibabacloud_pds20220301 import models as pds_20220301_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    _client: SPIClient = None

    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._client = GatewayClientClient()
        self._spi = self._client
        self._signature_algorithm = 'v2'
        self._endpoint_rule = ''

    def authorize(
        self,
        request: pds_20220301_models.AuthorizeRequest,
    ) -> pds_20220301_models.AuthorizeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.authorize_with_options(request, headers, runtime)

    async def authorize_async(
        self,
        request: pds_20220301_models.AuthorizeRequest,
    ) -> pds_20220301_models.AuthorizeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.authorize_with_options_async(request, headers, runtime)

    def authorize_with_options(
        self,
        tmp_req: pds_20220301_models.AuthorizeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.AuthorizeResponse:
        UtilClient.validate_model(tmp_req)
        request = pds_20220301_models.AuthorizeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scope):
            request.scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scope, 'scope', 'simple')
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['client_id'] = request.client_id
        if not UtilClient.is_unset(request.hide_consent):
            query['hide_consent'] = request.hide_consent
        if not UtilClient.is_unset(request.login_type):
            query['login_type'] = request.login_type
        if not UtilClient.is_unset(request.redirect_uri):
            query['redirect_uri'] = request.redirect_uri
        if not UtilClient.is_unset(request.response_type):
            query['response_type'] = request.response_type
        if not UtilClient.is_unset(request.scope_shrink):
            query['scope'] = request.scope_shrink
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Authorize',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/oauth/authorize',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.AuthorizeResponse(),
            self.execute(params, req, runtime)
        )

    async def authorize_with_options_async(
        self,
        tmp_req: pds_20220301_models.AuthorizeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.AuthorizeResponse:
        UtilClient.validate_model(tmp_req)
        request = pds_20220301_models.AuthorizeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scope):
            request.scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scope, 'scope', 'simple')
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['client_id'] = request.client_id
        if not UtilClient.is_unset(request.hide_consent):
            query['hide_consent'] = request.hide_consent
        if not UtilClient.is_unset(request.login_type):
            query['login_type'] = request.login_type
        if not UtilClient.is_unset(request.redirect_uri):
            query['redirect_uri'] = request.redirect_uri
        if not UtilClient.is_unset(request.response_type):
            query['response_type'] = request.response_type
        if not UtilClient.is_unset(request.scope_shrink):
            query['scope'] = request.scope_shrink
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Authorize',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/oauth/authorize',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.AuthorizeResponse(),
            await self.execute_async(params, req, runtime)
        )

    def batch(
        self,
        request: pds_20220301_models.BatchRequest,
    ) -> pds_20220301_models.BatchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_with_options(request, headers, runtime)

    async def batch_async(
        self,
        request: pds_20220301_models.BatchRequest,
    ) -> pds_20220301_models.BatchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_with_options_async(request, headers, runtime)

    def batch_with_options(
        self,
        request: pds_20220301_models.BatchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.BatchResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.requests):
            body['requests'] = request.requests
        if not UtilClient.is_unset(request.resource):
            body['resource'] = request.resource
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Batch',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/batch',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.BatchResponse(),
            self.execute(params, req, runtime)
        )

    async def batch_with_options_async(
        self,
        request: pds_20220301_models.BatchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.BatchResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.requests):
            body['requests'] = request.requests
        if not UtilClient.is_unset(request.resource):
            body['resource'] = request.resource
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Batch',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/batch',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.BatchResponse(),
            await self.execute_async(params, req, runtime)
        )

    def cancel_share_link(
        self,
        request: pds_20220301_models.CancelShareLinkRequest,
    ) -> pds_20220301_models.CancelShareLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_share_link_with_options(request, headers, runtime)

    async def cancel_share_link_async(
        self,
        request: pds_20220301_models.CancelShareLinkRequest,
    ) -> pds_20220301_models.CancelShareLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_share_link_with_options_async(request, headers, runtime)

    def cancel_share_link_with_options(
        self,
        request: pds_20220301_models.CancelShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CancelShareLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CancelShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    async def cancel_share_link_with_options_async(
        self,
        request: pds_20220301_models.CancelShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CancelShareLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CancelShareLinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def clear_recyclebin(
        self,
        request: pds_20220301_models.ClearRecyclebinRequest,
    ) -> pds_20220301_models.ClearRecyclebinResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clear_recyclebin_with_options(request, headers, runtime)

    async def clear_recyclebin_async(
        self,
        request: pds_20220301_models.ClearRecyclebinRequest,
    ) -> pds_20220301_models.ClearRecyclebinResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clear_recyclebin_with_options_async(request, headers, runtime)

    def clear_recyclebin_with_options(
        self,
        request: pds_20220301_models.ClearRecyclebinRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ClearRecyclebinResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ClearRecyclebin',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/recyclebin/clear',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ClearRecyclebinResponse(),
            self.execute(params, req, runtime)
        )

    async def clear_recyclebin_with_options_async(
        self,
        request: pds_20220301_models.ClearRecyclebinRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ClearRecyclebinResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ClearRecyclebin',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/recyclebin/clear',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ClearRecyclebinResponse(),
            await self.execute_async(params, req, runtime)
        )

    def complete_file(
        self,
        request: pds_20220301_models.CompleteFileRequest,
    ) -> pds_20220301_models.CompleteFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.complete_file_with_options(request, headers, runtime)

    async def complete_file_async(
        self,
        request: pds_20220301_models.CompleteFileRequest,
    ) -> pds_20220301_models.CompleteFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.complete_file_with_options_async(request, headers, runtime)

    def complete_file_with_options(
        self,
        request: pds_20220301_models.CompleteFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CompleteFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompleteFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/complete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CompleteFileResponse(),
            self.execute(params, req, runtime)
        )

    async def complete_file_with_options_async(
        self,
        request: pds_20220301_models.CompleteFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CompleteFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompleteFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/complete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CompleteFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def copy_file(
        self,
        request: pds_20220301_models.CopyFileRequest,
    ) -> pds_20220301_models.CopyFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.copy_file_with_options(request, headers, runtime)

    async def copy_file_async(
        self,
        request: pds_20220301_models.CopyFileRequest,
    ) -> pds_20220301_models.CopyFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.copy_file_with_options_async(request, headers, runtime)

    def copy_file_with_options(
        self,
        request: pds_20220301_models.CopyFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CopyFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_rename):
            body['auto_rename'] = request.auto_rename
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.to_parent_file_id):
            body['to_parent_file_id'] = request.to_parent_file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CopyFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/copy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CopyFileResponse(),
            self.execute(params, req, runtime)
        )

    async def copy_file_with_options_async(
        self,
        request: pds_20220301_models.CopyFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CopyFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_rename):
            body['auto_rename'] = request.auto_rename
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.to_parent_file_id):
            body['to_parent_file_id'] = request.to_parent_file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CopyFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/copy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CopyFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_drive(
        self,
        request: pds_20220301_models.CreateDriveRequest,
    ) -> pds_20220301_models.CreateDriveResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_drive_with_options(request, headers, runtime)

    async def create_drive_async(
        self,
        request: pds_20220301_models.CreateDriveRequest,
    ) -> pds_20220301_models.CreateDriveResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_drive_with_options_async(request, headers, runtime)

    def create_drive_with_options(
        self,
        request: pds_20220301_models.CreateDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateDriveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.default):
            body['default'] = request.default
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.drive_name):
            body['drive_name'] = request.drive_name
        if not UtilClient.is_unset(request.drive_type):
            body['drive_type'] = request.drive_type
        if not UtilClient.is_unset(request.owner):
            body['owner'] = request.owner
        if not UtilClient.is_unset(request.owner_type):
            body['owner_type'] = request.owner_type
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.total_size):
            body['total_size'] = request.total_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def create_drive_with_options_async(
        self,
        request: pds_20220301_models.CreateDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateDriveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.default):
            body['default'] = request.default
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.drive_name):
            body['drive_name'] = request.drive_name
        if not UtilClient.is_unset(request.drive_type):
            body['drive_type'] = request.drive_type
        if not UtilClient.is_unset(request.owner):
            body['owner'] = request.owner
        if not UtilClient.is_unset(request.owner_type):
            body['owner_type'] = request.owner_type
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.total_size):
            body['total_size'] = request.total_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_file(
        self,
        request: pds_20220301_models.CreateFileRequest,
    ) -> pds_20220301_models.CreateFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_file_with_options(request, headers, runtime)

    async def create_file_async(
        self,
        request: pds_20220301_models.CreateFileRequest,
    ) -> pds_20220301_models.CreateFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_file_with_options_async(request, headers, runtime)

    def create_file_with_options(
        self,
        request: pds_20220301_models.CreateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not UtilClient.is_unset(request.content_hash):
            body['content_hash'] = request.content_hash
        if not UtilClient.is_unset(request.content_hash_name):
            body['content_hash_name'] = request.content_hash_name
        if not UtilClient.is_unset(request.content_type):
            body['content_type'] = request.content_type
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.hidden):
            body['hidden'] = request.hidden
        if not UtilClient.is_unset(request.image_media_metadata):
            body['image_media_metadata'] = request.image_media_metadata
        if not UtilClient.is_unset(request.local_created_at):
            body['local_created_at'] = request.local_created_at
        if not UtilClient.is_unset(request.local_modified_at):
            body['local_modified_at'] = request.local_modified_at
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parallel_upload):
            body['parallel_upload'] = request.parallel_upload
        if not UtilClient.is_unset(request.parent_file_id):
            body['parent_file_id'] = request.parent_file_id
        if not UtilClient.is_unset(request.part_info_list):
            body['part_info_list'] = request.part_info_list
        if not UtilClient.is_unset(request.pre_hash):
            body['pre_hash'] = request.pre_hash
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.size):
            body['size'] = request.size
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.user_tags):
            body['user_tags'] = request.user_tags
        if not UtilClient.is_unset(request.video_media_metadata):
            body['video_media_metadata'] = request.video_media_metadata
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateFileResponse(),
            self.execute(params, req, runtime)
        )

    async def create_file_with_options_async(
        self,
        request: pds_20220301_models.CreateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not UtilClient.is_unset(request.content_hash):
            body['content_hash'] = request.content_hash
        if not UtilClient.is_unset(request.content_hash_name):
            body['content_hash_name'] = request.content_hash_name
        if not UtilClient.is_unset(request.content_type):
            body['content_type'] = request.content_type
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.hidden):
            body['hidden'] = request.hidden
        if not UtilClient.is_unset(request.image_media_metadata):
            body['image_media_metadata'] = request.image_media_metadata
        if not UtilClient.is_unset(request.local_created_at):
            body['local_created_at'] = request.local_created_at
        if not UtilClient.is_unset(request.local_modified_at):
            body['local_modified_at'] = request.local_modified_at
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parallel_upload):
            body['parallel_upload'] = request.parallel_upload
        if not UtilClient.is_unset(request.parent_file_id):
            body['parent_file_id'] = request.parent_file_id
        if not UtilClient.is_unset(request.part_info_list):
            body['part_info_list'] = request.part_info_list
        if not UtilClient.is_unset(request.pre_hash):
            body['pre_hash'] = request.pre_hash
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.size):
            body['size'] = request.size
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.user_tags):
            body['user_tags'] = request.user_tags
        if not UtilClient.is_unset(request.video_media_metadata):
            body['video_media_metadata'] = request.video_media_metadata
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_group(
        self,
        request: pds_20220301_models.CreateGroupRequest,
    ) -> pds_20220301_models.CreateGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_group_with_options(request, headers, runtime)

    async def create_group_async(
        self,
        request: pds_20220301_models.CreateGroupRequest,
    ) -> pds_20220301_models.CreateGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_group_with_options_async(request, headers, runtime)

    def create_group_with_options(
        self,
        request: pds_20220301_models.CreateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            body['group_name'] = request.group_name
        if not UtilClient.is_unset(request.is_root):
            body['is_root'] = request.is_root
        if not UtilClient.is_unset(request.parent_group_id):
            body['parent_group_id'] = request.parent_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def create_group_with_options_async(
        self,
        request: pds_20220301_models.CreateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            body['group_name'] = request.group_name
        if not UtilClient.is_unset(request.is_root):
            body['is_root'] = request.is_root
        if not UtilClient.is_unset(request.parent_group_id):
            body['parent_group_id'] = request.parent_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_share_link(
        self,
        request: pds_20220301_models.CreateShareLinkRequest,
    ) -> pds_20220301_models.CreateShareLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_share_link_with_options(request, headers, runtime)

    async def create_share_link_async(
        self,
        request: pds_20220301_models.CreateShareLinkRequest,
    ) -> pds_20220301_models.CreateShareLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_share_link_with_options_async(request, headers, runtime)

    def create_share_link_with_options(
        self,
        request: pds_20220301_models.CreateShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateShareLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.disable_download):
            body['disable_download'] = request.disable_download
        if not UtilClient.is_unset(request.disable_preview):
            body['disable_preview'] = request.disable_preview
        if not UtilClient.is_unset(request.disable_save):
            body['disable_save'] = request.disable_save
        if not UtilClient.is_unset(request.download_limit):
            body['download_limit'] = request.download_limit
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.expiration):
            body['expiration'] = request.expiration
        if not UtilClient.is_unset(request.file_id_list):
            body['file_id_list'] = request.file_id_list
        if not UtilClient.is_unset(request.preview_limit):
            body['preview_limit'] = request.preview_limit
        if not UtilClient.is_unset(request.save_limit):
            body['save_limit'] = request.save_limit
        if not UtilClient.is_unset(request.share_name):
            body['share_name'] = request.share_name
        if not UtilClient.is_unset(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    async def create_share_link_with_options_async(
        self,
        request: pds_20220301_models.CreateShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateShareLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.disable_download):
            body['disable_download'] = request.disable_download
        if not UtilClient.is_unset(request.disable_preview):
            body['disable_preview'] = request.disable_preview
        if not UtilClient.is_unset(request.disable_save):
            body['disable_save'] = request.disable_save
        if not UtilClient.is_unset(request.download_limit):
            body['download_limit'] = request.download_limit
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.expiration):
            body['expiration'] = request.expiration
        if not UtilClient.is_unset(request.file_id_list):
            body['file_id_list'] = request.file_id_list
        if not UtilClient.is_unset(request.preview_limit):
            body['preview_limit'] = request.preview_limit
        if not UtilClient.is_unset(request.save_limit):
            body['save_limit'] = request.save_limit
        if not UtilClient.is_unset(request.share_name):
            body['share_name'] = request.share_name
        if not UtilClient.is_unset(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateShareLinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_user(
        self,
        request: pds_20220301_models.CreateUserRequest,
    ) -> pds_20220301_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_user_with_options(request, headers, runtime)

    async def create_user_async(
        self,
        request: pds_20220301_models.CreateUserRequest,
    ) -> pds_20220301_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_user_with_options_async(request, headers, runtime)

    def create_user_with_options(
        self,
        request: pds_20220301_models.CreateUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.avatar):
            body['avatar'] = request.avatar
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.group_info_list):
            body['group_info_list'] = request.group_info_list
        if not UtilClient.is_unset(request.nick_name):
            body['nick_name'] = request.nick_name
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['user_name'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateUserResponse(),
            self.execute(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: pds_20220301_models.CreateUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.avatar):
            body['avatar'] = request.avatar
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.group_info_list):
            body['group_info_list'] = request.group_info_list
        if not UtilClient.is_unset(request.nick_name):
            body['nick_name'] = request.nick_name
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['user_name'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateUserResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_drive(
        self,
        request: pds_20220301_models.DeleteDriveRequest,
    ) -> pds_20220301_models.DeleteDriveResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_drive_with_options(request, headers, runtime)

    async def delete_drive_async(
        self,
        request: pds_20220301_models.DeleteDriveRequest,
    ) -> pds_20220301_models.DeleteDriveResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_drive_with_options_async(request, headers, runtime)

    def delete_drive_with_options(
        self,
        request: pds_20220301_models.DeleteDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteDriveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_drive_with_options_async(
        self,
        request: pds_20220301_models.DeleteDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteDriveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_file(
        self,
        request: pds_20220301_models.DeleteFileRequest,
    ) -> pds_20220301_models.DeleteFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_file_with_options(request, headers, runtime)

    async def delete_file_async(
        self,
        request: pds_20220301_models.DeleteFileRequest,
    ) -> pds_20220301_models.DeleteFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_file_with_options_async(request, headers, runtime)

    def delete_file_with_options(
        self,
        request: pds_20220301_models.DeleteFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteFileResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_file_with_options_async(
        self,
        request: pds_20220301_models.DeleteFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_group(
        self,
        request: pds_20220301_models.DeleteGroupRequest,
    ) -> pds_20220301_models.DeleteGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_group_with_options(request, headers, runtime)

    async def delete_group_async(
        self,
        request: pds_20220301_models.DeleteGroupRequest,
    ) -> pds_20220301_models.DeleteGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_group_with_options_async(request, headers, runtime)

    def delete_group_with_options(
        self,
        request: pds_20220301_models.DeleteGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        request: pds_20220301_models.DeleteGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_revision(
        self,
        request: pds_20220301_models.DeleteRevisionRequest,
    ) -> pds_20220301_models.DeleteRevisionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_revision_with_options(request, headers, runtime)

    async def delete_revision_async(
        self,
        request: pds_20220301_models.DeleteRevisionRequest,
    ) -> pds_20220301_models.DeleteRevisionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_revision_with_options_async(request, headers, runtime)

    def delete_revision_with_options(
        self,
        request: pds_20220301_models.DeleteRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteRevisionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/revision/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteRevisionResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_revision_with_options_async(
        self,
        request: pds_20220301_models.DeleteRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteRevisionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/revision/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteRevisionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_user(
        self,
        request: pds_20220301_models.DeleteUserRequest,
    ) -> pds_20220301_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_user_with_options(request, headers, runtime)

    async def delete_user_async(
        self,
        request: pds_20220301_models.DeleteUserRequest,
    ) -> pds_20220301_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_user_with_options_async(request, headers, runtime)

    def delete_user_with_options(
        self,
        request: pds_20220301_models.DeleteUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteUserResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: pds_20220301_models.DeleteUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteUserResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delta_get_last_cursor(
        self,
        request: pds_20220301_models.DeltaGetLastCursorRequest,
    ) -> pds_20220301_models.DeltaGetLastCursorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delta_get_last_cursor_with_options(request, headers, runtime)

    async def delta_get_last_cursor_async(
        self,
        request: pds_20220301_models.DeltaGetLastCursorRequest,
    ) -> pds_20220301_models.DeltaGetLastCursorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delta_get_last_cursor_with_options_async(request, headers, runtime)

    def delta_get_last_cursor_with_options(
        self,
        request: pds_20220301_models.DeltaGetLastCursorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeltaGetLastCursorResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.sync_root_id):
            body['sync_root_id'] = request.sync_root_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeltaGetLastCursor',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get_last_cursor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeltaGetLastCursorResponse(),
            self.execute(params, req, runtime)
        )

    async def delta_get_last_cursor_with_options_async(
        self,
        request: pds_20220301_models.DeltaGetLastCursorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeltaGetLastCursorResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.sync_root_id):
            body['sync_root_id'] = request.sync_root_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeltaGetLastCursor',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get_last_cursor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeltaGetLastCursorResponse(),
            await self.execute_async(params, req, runtime)
        )

    def download_file(
        self,
        request: pds_20220301_models.DownloadFileRequest,
    ) -> pds_20220301_models.DownloadFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.download_file_with_options(request, headers, runtime)

    async def download_file_async(
        self,
        request: pds_20220301_models.DownloadFileRequest,
    ) -> pds_20220301_models.DownloadFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.download_file_with_options_async(request, headers, runtime)

    def download_file_with_options(
        self,
        request: pds_20220301_models.DownloadFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DownloadFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.office_thumbnail_process):
            body['office_thumbnail_process'] = request.office_thumbnail_process
        if not UtilClient.is_unset(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/download',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DownloadFileResponse(),
            self.execute(params, req, runtime)
        )

    async def download_file_with_options_async(
        self,
        request: pds_20220301_models.DownloadFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DownloadFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.office_thumbnail_process):
            body['office_thumbnail_process'] = request.office_thumbnail_process
        if not UtilClient.is_unset(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/download',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DownloadFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def file_add_permission(
        self,
        request: pds_20220301_models.FileAddPermissionRequest,
    ) -> pds_20220301_models.FileAddPermissionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.file_add_permission_with_options(request, headers, runtime)

    async def file_add_permission_async(
        self,
        request: pds_20220301_models.FileAddPermissionRequest,
    ) -> pds_20220301_models.FileAddPermissionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.file_add_permission_with_options_async(request, headers, runtime)

    def file_add_permission_with_options(
        self,
        request: pds_20220301_models.FileAddPermissionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.FileAddPermissionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.member_list):
            body['member_list'] = request.member_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileAddPermission',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/add_permission',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.FileAddPermissionResponse(),
            self.execute(params, req, runtime)
        )

    async def file_add_permission_with_options_async(
        self,
        request: pds_20220301_models.FileAddPermissionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.FileAddPermissionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.member_list):
            body['member_list'] = request.member_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileAddPermission',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/add_permission',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.FileAddPermissionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def file_delete_user_tags(
        self,
        request: pds_20220301_models.FileDeleteUserTagsRequest,
    ) -> pds_20220301_models.FileDeleteUserTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.file_delete_user_tags_with_options(request, headers, runtime)

    async def file_delete_user_tags_async(
        self,
        request: pds_20220301_models.FileDeleteUserTagsRequest,
    ) -> pds_20220301_models.FileDeleteUserTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.file_delete_user_tags_with_options_async(request, headers, runtime)

    def file_delete_user_tags_with_options(
        self,
        request: pds_20220301_models.FileDeleteUserTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.FileDeleteUserTagsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.key_list):
            body['key_list'] = request.key_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileDeleteUserTags',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/delete_usertags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.FileDeleteUserTagsResponse(),
            self.execute(params, req, runtime)
        )

    async def file_delete_user_tags_with_options_async(
        self,
        request: pds_20220301_models.FileDeleteUserTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.FileDeleteUserTagsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.key_list):
            body['key_list'] = request.key_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileDeleteUserTags',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/delete_usertags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.FileDeleteUserTagsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def file_list_permission(
        self,
        request: pds_20220301_models.FileListPermissionRequest,
    ) -> pds_20220301_models.FileListPermissionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.file_list_permission_with_options(request, headers, runtime)

    async def file_list_permission_async(
        self,
        request: pds_20220301_models.FileListPermissionRequest,
    ) -> pds_20220301_models.FileListPermissionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.file_list_permission_with_options_async(request, headers, runtime)

    def file_list_permission_with_options(
        self,
        request: pds_20220301_models.FileListPermissionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.FileListPermissionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileListPermission',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/list_permission',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            pds_20220301_models.FileListPermissionResponse(),
            self.execute(params, req, runtime)
        )

    async def file_list_permission_with_options_async(
        self,
        request: pds_20220301_models.FileListPermissionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.FileListPermissionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileListPermission',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/list_permission',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            pds_20220301_models.FileListPermissionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def file_put_user_tags(
        self,
        request: pds_20220301_models.FilePutUserTagsRequest,
    ) -> pds_20220301_models.FilePutUserTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.file_put_user_tags_with_options(request, headers, runtime)

    async def file_put_user_tags_async(
        self,
        request: pds_20220301_models.FilePutUserTagsRequest,
    ) -> pds_20220301_models.FilePutUserTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.file_put_user_tags_with_options_async(request, headers, runtime)

    def file_put_user_tags_with_options(
        self,
        request: pds_20220301_models.FilePutUserTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.FilePutUserTagsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.user_tags):
            body['user_tags'] = request.user_tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FilePutUserTags',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/put_usertags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.FilePutUserTagsResponse(),
            self.execute(params, req, runtime)
        )

    async def file_put_user_tags_with_options_async(
        self,
        request: pds_20220301_models.FilePutUserTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.FilePutUserTagsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.user_tags):
            body['user_tags'] = request.user_tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FilePutUserTags',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/put_usertags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.FilePutUserTagsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def file_remove_permission(
        self,
        request: pds_20220301_models.FileRemovePermissionRequest,
    ) -> pds_20220301_models.FileRemovePermissionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.file_remove_permission_with_options(request, headers, runtime)

    async def file_remove_permission_async(
        self,
        request: pds_20220301_models.FileRemovePermissionRequest,
    ) -> pds_20220301_models.FileRemovePermissionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.file_remove_permission_with_options_async(request, headers, runtime)

    def file_remove_permission_with_options(
        self,
        request: pds_20220301_models.FileRemovePermissionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.FileRemovePermissionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.member_list):
            body['member_list'] = request.member_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileRemovePermission',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/remove_permission',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.FileRemovePermissionResponse(),
            self.execute(params, req, runtime)
        )

    async def file_remove_permission_with_options_async(
        self,
        request: pds_20220301_models.FileRemovePermissionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.FileRemovePermissionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.member_list):
            body['member_list'] = request.member_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileRemovePermission',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/remove_permission',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.FileRemovePermissionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_async_task(
        self,
        request: pds_20220301_models.GetAsyncTaskRequest,
    ) -> pds_20220301_models.GetAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_async_task_with_options(request, headers, runtime)

    async def get_async_task_async(
        self,
        request: pds_20220301_models.GetAsyncTaskRequest,
    ) -> pds_20220301_models.GetAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_async_task_with_options_async(request, headers, runtime)

    def get_async_task_with_options(
        self,
        request: pds_20220301_models.GetAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetAsyncTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.async_task_id):
            body['async_task_id'] = request.async_task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAsyncTask',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/async_task/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetAsyncTaskResponse(),
            self.execute(params, req, runtime)
        )

    async def get_async_task_with_options_async(
        self,
        request: pds_20220301_models.GetAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetAsyncTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.async_task_id):
            body['async_task_id'] = request.async_task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAsyncTask',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/async_task/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetAsyncTaskResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_default_drive(
        self,
        request: pds_20220301_models.GetDefaultDriveRequest,
    ) -> pds_20220301_models.GetDefaultDriveResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_default_drive_with_options(request, headers, runtime)

    async def get_default_drive_async(
        self,
        request: pds_20220301_models.GetDefaultDriveRequest,
    ) -> pds_20220301_models.GetDefaultDriveResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_default_drive_with_options_async(request, headers, runtime)

    def get_default_drive_with_options(
        self,
        request: pds_20220301_models.GetDefaultDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetDefaultDriveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDefaultDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/get_default_drive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetDefaultDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def get_default_drive_with_options_async(
        self,
        request: pds_20220301_models.GetDefaultDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetDefaultDriveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDefaultDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/get_default_drive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetDefaultDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_download_url(
        self,
        request: pds_20220301_models.GetDownloadUrlRequest,
    ) -> pds_20220301_models.GetDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_download_url_with_options(request, headers, runtime)

    async def get_download_url_async(
        self,
        request: pds_20220301_models.GetDownloadUrlRequest,
    ) -> pds_20220301_models.GetDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_download_url_with_options_async(request, headers, runtime)

    def get_download_url_with_options(
        self,
        request: pds_20220301_models.GetDownloadUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetDownloadUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.expire_sec):
            body['expire_sec'] = request.expire_sec
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.file_name):
            body['file_name'] = request.file_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDownloadUrl',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get_download_url',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetDownloadUrlResponse(),
            self.execute(params, req, runtime)
        )

    async def get_download_url_with_options_async(
        self,
        request: pds_20220301_models.GetDownloadUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetDownloadUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.expire_sec):
            body['expire_sec'] = request.expire_sec
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.file_name):
            body['file_name'] = request.file_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDownloadUrl',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get_download_url',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetDownloadUrlResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_drive(
        self,
        request: pds_20220301_models.GetDriveRequest,
    ) -> pds_20220301_models.GetDriveResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_drive_with_options(request, headers, runtime)

    async def get_drive_async(
        self,
        request: pds_20220301_models.GetDriveRequest,
    ) -> pds_20220301_models.GetDriveResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_drive_with_options_async(request, headers, runtime)

    def get_drive_with_options(
        self,
        request: pds_20220301_models.GetDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetDriveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def get_drive_with_options_async(
        self,
        request: pds_20220301_models.GetDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetDriveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_file(
        self,
        request: pds_20220301_models.GetFileRequest,
    ) -> pds_20220301_models.GetFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_file_with_options(request, headers, runtime)

    async def get_file_async(
        self,
        request: pds_20220301_models.GetFileRequest,
    ) -> pds_20220301_models.GetFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_file_with_options_async(request, headers, runtime)

    def get_file_with_options(
        self,
        request: pds_20220301_models.GetFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetFileResponse(),
            self.execute(params, req, runtime)
        )

    async def get_file_with_options_async(
        self,
        request: pds_20220301_models.GetFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_group(
        self,
        request: pds_20220301_models.GetGroupRequest,
    ) -> pds_20220301_models.GetGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_group_with_options(request, headers, runtime)

    async def get_group_async(
        self,
        request: pds_20220301_models.GetGroupRequest,
    ) -> pds_20220301_models.GetGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_group_with_options_async(request, headers, runtime)

    def get_group_with_options(
        self,
        request: pds_20220301_models.GetGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def get_group_with_options_async(
        self,
        request: pds_20220301_models.GetGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_link_info(
        self,
        request: pds_20220301_models.GetLinkInfoRequest,
    ) -> pds_20220301_models.GetLinkInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_link_info_with_options(request, headers, runtime)

    async def get_link_info_async(
        self,
        request: pds_20220301_models.GetLinkInfoRequest,
    ) -> pds_20220301_models.GetLinkInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_link_info_with_options_async(request, headers, runtime)

    def get_link_info_with_options(
        self,
        request: pds_20220301_models.GetLinkInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetLinkInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLinkInfo',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/account/get_link_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetLinkInfoResponse(),
            self.execute(params, req, runtime)
        )

    async def get_link_info_with_options_async(
        self,
        request: pds_20220301_models.GetLinkInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetLinkInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLinkInfo',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/account/get_link_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetLinkInfoResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_link_info_by_user_id(
        self,
        request: pds_20220301_models.GetLinkInfoByUserIdRequest,
    ) -> pds_20220301_models.GetLinkInfoByUserIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_link_info_by_user_id_with_options(request, headers, runtime)

    async def get_link_info_by_user_id_async(
        self,
        request: pds_20220301_models.GetLinkInfoByUserIdRequest,
    ) -> pds_20220301_models.GetLinkInfoByUserIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_link_info_by_user_id_with_options_async(request, headers, runtime)

    def get_link_info_by_user_id_with_options(
        self,
        request: pds_20220301_models.GetLinkInfoByUserIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetLinkInfoByUserIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLinkInfoByUserId',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/account/get_link_info_by_user_id',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetLinkInfoByUserIdResponse(),
            self.execute(params, req, runtime)
        )

    async def get_link_info_by_user_id_with_options_async(
        self,
        request: pds_20220301_models.GetLinkInfoByUserIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetLinkInfoByUserIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLinkInfoByUserId',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/account/get_link_info_by_user_id',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetLinkInfoByUserIdResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_revision(
        self,
        request: pds_20220301_models.GetRevisionRequest,
    ) -> pds_20220301_models.GetRevisionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_revision_with_options(request, headers, runtime)

    async def get_revision_async(
        self,
        request: pds_20220301_models.GetRevisionRequest,
    ) -> pds_20220301_models.GetRevisionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_revision_with_options_async(request, headers, runtime)

    def get_revision_with_options(
        self,
        request: pds_20220301_models.GetRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetRevisionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.revision_id):
            body['revision_id'] = request.revision_id
        if not UtilClient.is_unset(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/revision/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetRevisionResponse(),
            self.execute(params, req, runtime)
        )

    async def get_revision_with_options_async(
        self,
        request: pds_20220301_models.GetRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetRevisionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.revision_id):
            body['revision_id'] = request.revision_id
        if not UtilClient.is_unset(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/revision/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetRevisionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_share_link(
        self,
        request: pds_20220301_models.GetShareLinkRequest,
    ) -> pds_20220301_models.GetShareLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_share_link_with_options(request, headers, runtime)

    async def get_share_link_async(
        self,
        request: pds_20220301_models.GetShareLinkRequest,
    ) -> pds_20220301_models.GetShareLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_share_link_with_options_async(request, headers, runtime)

    def get_share_link_with_options(
        self,
        request: pds_20220301_models.GetShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetShareLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    async def get_share_link_with_options_async(
        self,
        request: pds_20220301_models.GetShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetShareLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetShareLinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_share_link_by_anonymous(
        self,
        request: pds_20220301_models.GetShareLinkByAnonymousRequest,
    ) -> pds_20220301_models.GetShareLinkByAnonymousResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_share_link_by_anonymous_with_options(request, headers, runtime)

    async def get_share_link_by_anonymous_async(
        self,
        request: pds_20220301_models.GetShareLinkByAnonymousRequest,
    ) -> pds_20220301_models.GetShareLinkByAnonymousResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_share_link_by_anonymous_with_options_async(request, headers, runtime)

    def get_share_link_by_anonymous_with_options(
        self,
        request: pds_20220301_models.GetShareLinkByAnonymousRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetShareLinkByAnonymousResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetShareLinkByAnonymous',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/get_by_anonymous',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetShareLinkByAnonymousResponse(),
            self.execute(params, req, runtime)
        )

    async def get_share_link_by_anonymous_with_options_async(
        self,
        request: pds_20220301_models.GetShareLinkByAnonymousRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetShareLinkByAnonymousResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetShareLinkByAnonymous',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/get_by_anonymous',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetShareLinkByAnonymousResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_share_link_token(
        self,
        request: pds_20220301_models.GetShareLinkTokenRequest,
    ) -> pds_20220301_models.GetShareLinkTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_share_link_token_with_options(request, headers, runtime)

    async def get_share_link_token_async(
        self,
        request: pds_20220301_models.GetShareLinkTokenRequest,
    ) -> pds_20220301_models.GetShareLinkTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_share_link_token_with_options_async(request, headers, runtime)

    def get_share_link_token_with_options(
        self,
        request: pds_20220301_models.GetShareLinkTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetShareLinkTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.expire_sec):
            body['expire_sec'] = request.expire_sec
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetShareLinkToken',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/get_share_token',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetShareLinkTokenResponse(),
            self.execute(params, req, runtime)
        )

    async def get_share_link_token_with_options_async(
        self,
        request: pds_20220301_models.GetShareLinkTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetShareLinkTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.expire_sec):
            body['expire_sec'] = request.expire_sec
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetShareLinkToken',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/get_share_token',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetShareLinkTokenResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_upload_url(
        self,
        request: pds_20220301_models.GetUploadUrlRequest,
    ) -> pds_20220301_models.GetUploadUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_upload_url_with_options(request, headers, runtime)

    async def get_upload_url_async(
        self,
        request: pds_20220301_models.GetUploadUrlRequest,
    ) -> pds_20220301_models.GetUploadUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_upload_url_with_options_async(request, headers, runtime)

    def get_upload_url_with_options(
        self,
        request: pds_20220301_models.GetUploadUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetUploadUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.part_info_list):
            body['part_info_list'] = request.part_info_list
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUploadUrl',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get_upload_url',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetUploadUrlResponse(),
            self.execute(params, req, runtime)
        )

    async def get_upload_url_with_options_async(
        self,
        request: pds_20220301_models.GetUploadUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetUploadUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.part_info_list):
            body['part_info_list'] = request.part_info_list
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUploadUrl',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get_upload_url',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetUploadUrlResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_user(
        self,
        request: pds_20220301_models.GetUserRequest,
    ) -> pds_20220301_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_with_options(request, headers, runtime)

    async def get_user_async(
        self,
        request: pds_20220301_models.GetUserRequest,
    ) -> pds_20220301_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_with_options_async(request, headers, runtime)

    def get_user_with_options(
        self,
        request: pds_20220301_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetUserResponse(),
            self.execute(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: pds_20220301_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetUserResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_video_preview_play_info(
        self,
        request: pds_20220301_models.GetVideoPreviewPlayInfoRequest,
    ) -> pds_20220301_models.GetVideoPreviewPlayInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_video_preview_play_info_with_options(request, headers, runtime)

    async def get_video_preview_play_info_async(
        self,
        request: pds_20220301_models.GetVideoPreviewPlayInfoRequest,
    ) -> pds_20220301_models.GetVideoPreviewPlayInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_video_preview_play_info_with_options_async(request, headers, runtime)

    def get_video_preview_play_info_with_options(
        self,
        request: pds_20220301_models.GetVideoPreviewPlayInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetVideoPreviewPlayInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.get_without_url):
            body['get_without_url'] = request.get_without_url
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.template_id):
            body['template_id'] = request.template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVideoPreviewPlayInfo',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get_video_preview_play_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetVideoPreviewPlayInfoResponse(),
            self.execute(params, req, runtime)
        )

    async def get_video_preview_play_info_with_options_async(
        self,
        request: pds_20220301_models.GetVideoPreviewPlayInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetVideoPreviewPlayInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.get_without_url):
            body['get_without_url'] = request.get_without_url
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.template_id):
            body['template_id'] = request.template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVideoPreviewPlayInfo',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get_video_preview_play_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetVideoPreviewPlayInfoResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_video_preview_play_meta(
        self,
        domain_id: str,
        request: pds_20220301_models.GetVideoPreviewPlayMetaRequest,
    ) -> pds_20220301_models.GetVideoPreviewPlayMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_video_preview_play_meta_with_options(domain_id, request, headers, runtime)

    async def get_video_preview_play_meta_async(
        self,
        domain_id: str,
        request: pds_20220301_models.GetVideoPreviewPlayMetaRequest,
    ) -> pds_20220301_models.GetVideoPreviewPlayMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_video_preview_play_meta_with_options_async(domain_id, request, headers, runtime)

    def get_video_preview_play_meta_with_options(
        self,
        domain_id: str,
        request: pds_20220301_models.GetVideoPreviewPlayMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetVideoPreviewPlayMetaResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['domain_id'] = domain_id
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVideoPreviewPlayMeta',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get_video_preview_play_meta',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetVideoPreviewPlayMetaResponse(),
            self.execute(params, req, runtime)
        )

    async def get_video_preview_play_meta_with_options_async(
        self,
        domain_id: str,
        request: pds_20220301_models.GetVideoPreviewPlayMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetVideoPreviewPlayMetaResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['domain_id'] = domain_id
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVideoPreviewPlayMeta',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get_video_preview_play_meta',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetVideoPreviewPlayMetaResponse(),
            await self.execute_async(params, req, runtime)
        )

    def import_user(
        self,
        request: pds_20220301_models.ImportUserRequest,
    ) -> pds_20220301_models.ImportUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.import_user_with_options(request, headers, runtime)

    async def import_user_async(
        self,
        request: pds_20220301_models.ImportUserRequest,
    ) -> pds_20220301_models.ImportUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.import_user_with_options_async(request, headers, runtime)

    def import_user_with_options(
        self,
        request: pds_20220301_models.ImportUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ImportUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authentication_display_name):
            body['authentication_display_name'] = request.authentication_display_name
        if not UtilClient.is_unset(request.authentication_type):
            body['authentication_type'] = request.authentication_type
        if not UtilClient.is_unset(request.auto_create_drive):
            body['auto_create_drive'] = request.auto_create_drive
        if not UtilClient.is_unset(request.drive_total_size):
            body['drive_total_size'] = request.drive_total_size
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.nick_name):
            body['nick_name'] = request.nick_name
        if not UtilClient.is_unset(request.parent_group_id):
            body['parent_group_id'] = request.parent_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/import',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ImportUserResponse(),
            self.execute(params, req, runtime)
        )

    async def import_user_with_options_async(
        self,
        request: pds_20220301_models.ImportUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ImportUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authentication_display_name):
            body['authentication_display_name'] = request.authentication_display_name
        if not UtilClient.is_unset(request.authentication_type):
            body['authentication_type'] = request.authentication_type
        if not UtilClient.is_unset(request.auto_create_drive):
            body['auto_create_drive'] = request.auto_create_drive
        if not UtilClient.is_unset(request.drive_total_size):
            body['drive_total_size'] = request.drive_total_size
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.nick_name):
            body['nick_name'] = request.nick_name
        if not UtilClient.is_unset(request.parent_group_id):
            body['parent_group_id'] = request.parent_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/import',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ImportUserResponse(),
            await self.execute_async(params, req, runtime)
        )

    def link_account(
        self,
        request: pds_20220301_models.LinkAccountRequest,
    ) -> pds_20220301_models.LinkAccountResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.link_account_with_options(request, headers, runtime)

    async def link_account_async(
        self,
        request: pds_20220301_models.LinkAccountRequest,
    ) -> pds_20220301_models.LinkAccountResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.link_account_with_options_async(request, headers, runtime)

    def link_account_with_options(
        self,
        request: pds_20220301_models.LinkAccountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.LinkAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LinkAccount',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/account/link',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.LinkAccountResponse(),
            self.execute(params, req, runtime)
        )

    async def link_account_with_options_async(
        self,
        request: pds_20220301_models.LinkAccountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.LinkAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LinkAccount',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/account/link',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.LinkAccountResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_address_groups(
        self,
        request: pds_20220301_models.ListAddressGroupsRequest,
    ) -> pds_20220301_models.ListAddressGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_address_groups_with_options(request, headers, runtime)

    async def list_address_groups_async(
        self,
        request: pds_20220301_models.ListAddressGroupsRequest,
    ) -> pds_20220301_models.ListAddressGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_address_groups_with_options_async(request, headers, runtime)

    def list_address_groups_with_options(
        self,
        request: pds_20220301_models.ListAddressGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListAddressGroupsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAddressGroups',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/list_address_groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListAddressGroupsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_address_groups_with_options_async(
        self,
        request: pds_20220301_models.ListAddressGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListAddressGroupsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAddressGroups',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/list_address_groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListAddressGroupsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_delta(
        self,
        request: pds_20220301_models.ListDeltaRequest,
    ) -> pds_20220301_models.ListDeltaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_delta_with_options(request, headers, runtime)

    async def list_delta_async(
        self,
        request: pds_20220301_models.ListDeltaRequest,
    ) -> pds_20220301_models.ListDeltaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_delta_with_options_async(request, headers, runtime)

    def list_delta_with_options(
        self,
        request: pds_20220301_models.ListDeltaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListDeltaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cursor):
            body['cursor'] = request.cursor
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.sync_root_id):
            body['sync_root_id'] = request.sync_root_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDelta',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/list_delta',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListDeltaResponse(),
            self.execute(params, req, runtime)
        )

    async def list_delta_with_options_async(
        self,
        request: pds_20220301_models.ListDeltaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListDeltaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cursor):
            body['cursor'] = request.cursor
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.sync_root_id):
            body['sync_root_id'] = request.sync_root_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDelta',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/list_delta',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListDeltaResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_drive(
        self,
        request: pds_20220301_models.ListDriveRequest,
    ) -> pds_20220301_models.ListDriveResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_drive_with_options(request, headers, runtime)

    async def list_drive_async(
        self,
        request: pds_20220301_models.ListDriveRequest,
    ) -> pds_20220301_models.ListDriveResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_drive_with_options_async(request, headers, runtime)

    def list_drive_with_options(
        self,
        request: pds_20220301_models.ListDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListDriveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.owner):
            body['owner'] = request.owner
        if not UtilClient.is_unset(request.owner_type):
            body['owner_type'] = request.owner_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def list_drive_with_options_async(
        self,
        request: pds_20220301_models.ListDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListDriveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.owner):
            body['owner'] = request.owner
        if not UtilClient.is_unset(request.owner_type):
            body['owner_type'] = request.owner_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_facegroups(
        self,
        request: pds_20220301_models.ListFacegroupsRequest,
    ) -> pds_20220301_models.ListFacegroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_facegroups_with_options(request, headers, runtime)

    async def list_facegroups_async(
        self,
        request: pds_20220301_models.ListFacegroupsRequest,
    ) -> pds_20220301_models.ListFacegroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_facegroups_with_options_async(request, headers, runtime)

    def list_facegroups_with_options(
        self,
        request: pds_20220301_models.ListFacegroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListFacegroupsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.remarks):
            body['remarks'] = request.remarks
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFacegroups',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/list_facegroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListFacegroupsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_facegroups_with_options_async(
        self,
        request: pds_20220301_models.ListFacegroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListFacegroupsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.remarks):
            body['remarks'] = request.remarks
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFacegroups',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/list_facegroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListFacegroupsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_file(
        self,
        request: pds_20220301_models.ListFileRequest,
    ) -> pds_20220301_models.ListFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_file_with_options(request, headers, runtime)

    async def list_file_async(
        self,
        request: pds_20220301_models.ListFileRequest,
    ) -> pds_20220301_models.ListFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_file_with_options_async(request, headers, runtime)

    def list_file_with_options(
        self,
        request: pds_20220301_models.ListFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.order_direction):
            body['order_direction'] = request.order_direction
        if not UtilClient.is_unset(request.parent_file_id):
            body['parent_file_id'] = request.parent_file_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListFileResponse(),
            self.execute(params, req, runtime)
        )

    async def list_file_with_options_async(
        self,
        request: pds_20220301_models.ListFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.order_direction):
            body['order_direction'] = request.order_direction
        if not UtilClient.is_unset(request.parent_file_id):
            body['parent_file_id'] = request.parent_file_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_group(
        self,
        request: pds_20220301_models.ListGroupRequest,
    ) -> pds_20220301_models.ListGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_group_with_options(request, headers, runtime)

    async def list_group_async(
        self,
        request: pds_20220301_models.ListGroupRequest,
    ) -> pds_20220301_models.ListGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_group_with_options_async(request, headers, runtime)

    def list_group_with_options(
        self,
        request: pds_20220301_models.ListGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def list_group_with_options_async(
        self,
        request: pds_20220301_models.ListGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_my_drives(
        self,
        request: pds_20220301_models.ListMyDrivesRequest,
    ) -> pds_20220301_models.ListMyDrivesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_my_drives_with_options(request, headers, runtime)

    async def list_my_drives_async(
        self,
        request: pds_20220301_models.ListMyDrivesRequest,
    ) -> pds_20220301_models.ListMyDrivesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_my_drives_with_options_async(request, headers, runtime)

    def list_my_drives_with_options(
        self,
        request: pds_20220301_models.ListMyDrivesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListMyDrivesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMyDrives',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/list_my_drives',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListMyDrivesResponse(),
            self.execute(params, req, runtime)
        )

    async def list_my_drives_with_options_async(
        self,
        request: pds_20220301_models.ListMyDrivesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListMyDrivesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMyDrives',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/list_my_drives',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListMyDrivesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_recyclebin(
        self,
        request: pds_20220301_models.ListRecyclebinRequest,
    ) -> pds_20220301_models.ListRecyclebinResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_recyclebin_with_options(request, headers, runtime)

    async def list_recyclebin_async(
        self,
        request: pds_20220301_models.ListRecyclebinRequest,
    ) -> pds_20220301_models.ListRecyclebinResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_recyclebin_with_options_async(request, headers, runtime)

    def list_recyclebin_with_options(
        self,
        request: pds_20220301_models.ListRecyclebinRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListRecyclebinResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRecyclebin',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/recyclebin/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListRecyclebinResponse(),
            self.execute(params, req, runtime)
        )

    async def list_recyclebin_with_options_async(
        self,
        request: pds_20220301_models.ListRecyclebinRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListRecyclebinResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRecyclebin',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/recyclebin/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListRecyclebinResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_revision(
        self,
        request: pds_20220301_models.ListRevisionRequest,
    ) -> pds_20220301_models.ListRevisionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_revision_with_options(request, headers, runtime)

    async def list_revision_async(
        self,
        request: pds_20220301_models.ListRevisionRequest,
    ) -> pds_20220301_models.ListRevisionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_revision_with_options_async(request, headers, runtime)

    def list_revision_with_options(
        self,
        request: pds_20220301_models.ListRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListRevisionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/revision/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListRevisionResponse(),
            self.execute(params, req, runtime)
        )

    async def list_revision_with_options_async(
        self,
        request: pds_20220301_models.ListRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListRevisionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/revision/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListRevisionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_share_link(
        self,
        request: pds_20220301_models.ListShareLinkRequest,
    ) -> pds_20220301_models.ListShareLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_share_link_with_options(request, headers, runtime)

    async def list_share_link_async(
        self,
        request: pds_20220301_models.ListShareLinkRequest,
    ) -> pds_20220301_models.ListShareLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_share_link_with_options_async(request, headers, runtime)

    def list_share_link_with_options(
        self,
        request: pds_20220301_models.ListShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListShareLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creator):
            body['creator'] = request.creator
        if not UtilClient.is_unset(request.include_cancelled):
            body['include_cancelled'] = request.include_cancelled
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.order_direction):
            body['order_direction'] = request.order_direction
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    async def list_share_link_with_options_async(
        self,
        request: pds_20220301_models.ListShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListShareLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creator):
            body['creator'] = request.creator
        if not UtilClient.is_unset(request.include_cancelled):
            body['include_cancelled'] = request.include_cancelled
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.order_direction):
            body['order_direction'] = request.order_direction
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListShareLinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_tags(
        self,
        request: pds_20220301_models.ListTagsRequest,
    ) -> pds_20220301_models.ListTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tags_with_options(request, headers, runtime)

    async def list_tags_async(
        self,
        request: pds_20220301_models.ListTagsRequest,
    ) -> pds_20220301_models.ListTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tags_with_options_async(request, headers, runtime)

    def list_tags_with_options(
        self,
        request: pds_20220301_models.ListTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListTagsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTags',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/list_tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListTagsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_tags_with_options_async(
        self,
        request: pds_20220301_models.ListTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListTagsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTags',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/list_tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListTagsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_uploaded_parts(
        self,
        request: pds_20220301_models.ListUploadedPartsRequest,
    ) -> pds_20220301_models.ListUploadedPartsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_uploaded_parts_with_options(request, headers, runtime)

    async def list_uploaded_parts_async(
        self,
        request: pds_20220301_models.ListUploadedPartsRequest,
    ) -> pds_20220301_models.ListUploadedPartsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_uploaded_parts_with_options_async(request, headers, runtime)

    def list_uploaded_parts_with_options(
        self,
        request: pds_20220301_models.ListUploadedPartsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListUploadedPartsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.part_number_marker):
            body['part_number_marker'] = request.part_number_marker
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUploadedParts',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/list_uploaded_parts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListUploadedPartsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_uploaded_parts_with_options_async(
        self,
        request: pds_20220301_models.ListUploadedPartsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListUploadedPartsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.part_number_marker):
            body['part_number_marker'] = request.part_number_marker
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUploadedParts',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/list_uploaded_parts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListUploadedPartsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_user(
        self,
        request: pds_20220301_models.ListUserRequest,
    ) -> pds_20220301_models.ListUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_with_options(request, headers, runtime)

    async def list_user_async(
        self,
        request: pds_20220301_models.ListUserRequest,
    ) -> pds_20220301_models.ListUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_user_with_options_async(request, headers, runtime)

    def list_user_with_options(
        self,
        request: pds_20220301_models.ListUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListUserResponse(),
            self.execute(params, req, runtime)
        )

    async def list_user_with_options_async(
        self,
        request: pds_20220301_models.ListUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListUserResponse(),
            await self.execute_async(params, req, runtime)
        )

    def move_file(
        self,
        request: pds_20220301_models.MoveFileRequest,
    ) -> pds_20220301_models.MoveFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.move_file_with_options(request, headers, runtime)

    async def move_file_async(
        self,
        request: pds_20220301_models.MoveFileRequest,
    ) -> pds_20220301_models.MoveFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.move_file_with_options_async(request, headers, runtime)

    def move_file_with_options(
        self,
        request: pds_20220301_models.MoveFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.MoveFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.to_parent_file_id):
            body['to_parent_file_id'] = request.to_parent_file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/move',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.MoveFileResponse(),
            self.execute(params, req, runtime)
        )

    async def move_file_with_options_async(
        self,
        request: pds_20220301_models.MoveFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.MoveFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.to_parent_file_id):
            body['to_parent_file_id'] = request.to_parent_file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/move',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.MoveFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def parse_keywords(
        self,
        request: pds_20220301_models.ParseKeywordsRequest,
    ) -> pds_20220301_models.ParseKeywordsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.parse_keywords_with_options(request, headers, runtime)

    async def parse_keywords_async(
        self,
        request: pds_20220301_models.ParseKeywordsRequest,
    ) -> pds_20220301_models.ParseKeywordsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.parse_keywords_with_options_async(request, headers, runtime)

    def parse_keywords_with_options(
        self,
        request: pds_20220301_models.ParseKeywordsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ParseKeywordsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keywords):
            body['keywords'] = request.keywords
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ParseKeywords',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/parse_keywords',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ParseKeywordsResponse(),
            self.execute(params, req, runtime)
        )

    async def parse_keywords_with_options_async(
        self,
        request: pds_20220301_models.ParseKeywordsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ParseKeywordsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keywords):
            body['keywords'] = request.keywords
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ParseKeywords',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/parse_keywords',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ParseKeywordsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def remove_face_group_file(
        self,
        request: pds_20220301_models.RemoveFaceGroupFileRequest,
    ) -> pds_20220301_models.RemoveFaceGroupFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_face_group_file_with_options(request, headers, runtime)

    async def remove_face_group_file_async(
        self,
        request: pds_20220301_models.RemoveFaceGroupFileRequest,
    ) -> pds_20220301_models.RemoveFaceGroupFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_face_group_file_with_options_async(request, headers, runtime)

    def remove_face_group_file_with_options(
        self,
        request: pds_20220301_models.RemoveFaceGroupFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.RemoveFaceGroupFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.face_group_id):
            body['face_group_id'] = request.face_group_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveFaceGroupFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/albums/unassign_facegroup_item',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.RemoveFaceGroupFileResponse(),
            self.execute(params, req, runtime)
        )

    async def remove_face_group_file_with_options_async(
        self,
        request: pds_20220301_models.RemoveFaceGroupFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.RemoveFaceGroupFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.face_group_id):
            body['face_group_id'] = request.face_group_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveFaceGroupFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/albums/unassign_facegroup_item',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.RemoveFaceGroupFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def restore_file(
        self,
        request: pds_20220301_models.RestoreFileRequest,
    ) -> pds_20220301_models.RestoreFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restore_file_with_options(request, headers, runtime)

    async def restore_file_async(
        self,
        request: pds_20220301_models.RestoreFileRequest,
    ) -> pds_20220301_models.RestoreFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restore_file_with_options_async(request, headers, runtime)

    def restore_file_with_options(
        self,
        request: pds_20220301_models.RestoreFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.RestoreFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestoreFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/recyclebin/restore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.RestoreFileResponse(),
            self.execute(params, req, runtime)
        )

    async def restore_file_with_options_async(
        self,
        request: pds_20220301_models.RestoreFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.RestoreFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestoreFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/recyclebin/restore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.RestoreFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def restore_revision(
        self,
        request: pds_20220301_models.RestoreRevisionRequest,
    ) -> pds_20220301_models.RestoreRevisionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restore_revision_with_options(request, headers, runtime)

    async def restore_revision_async(
        self,
        request: pds_20220301_models.RestoreRevisionRequest,
    ) -> pds_20220301_models.RestoreRevisionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restore_revision_with_options_async(request, headers, runtime)

    def restore_revision_with_options(
        self,
        request: pds_20220301_models.RestoreRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.RestoreRevisionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestoreRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/revision/restore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.RestoreRevisionResponse(),
            self.execute(params, req, runtime)
        )

    async def restore_revision_with_options_async(
        self,
        request: pds_20220301_models.RestoreRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.RestoreRevisionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestoreRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/revision/restore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.RestoreRevisionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def scan_file(
        self,
        request: pds_20220301_models.ScanFileRequest,
    ) -> pds_20220301_models.ScanFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scan_file_with_options(request, headers, runtime)

    async def scan_file_async(
        self,
        request: pds_20220301_models.ScanFileRequest,
    ) -> pds_20220301_models.ScanFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.scan_file_with_options_async(request, headers, runtime)

    def scan_file_with_options(
        self,
        request: pds_20220301_models.ScanFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ScanFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScanFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/scan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ScanFileResponse(),
            self.execute(params, req, runtime)
        )

    async def scan_file_with_options_async(
        self,
        request: pds_20220301_models.ScanFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ScanFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScanFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/scan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ScanFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_address_groups(
        self,
        request: pds_20220301_models.SearchAddressGroupsRequest,
    ) -> pds_20220301_models.SearchAddressGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_address_groups_with_options(request, headers, runtime)

    async def search_address_groups_async(
        self,
        request: pds_20220301_models.SearchAddressGroupsRequest,
    ) -> pds_20220301_models.SearchAddressGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_address_groups_with_options_async(request, headers, runtime)

    def search_address_groups_with_options(
        self,
        request: pds_20220301_models.SearchAddressGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchAddressGroupsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address_level):
            body['address_level'] = request.address_level
        if not UtilClient.is_unset(request.address_names):
            body['address_names'] = request.address_names
        if not UtilClient.is_unset(request.br_geo_point):
            body['br_geo_point'] = request.br_geo_point
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.tl_geo_point):
            body['tl_geo_point'] = request.tl_geo_point
        if not UtilClient.is_unset(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchAddressGroups',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/search_address_groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchAddressGroupsResponse(),
            self.execute(params, req, runtime)
        )

    async def search_address_groups_with_options_async(
        self,
        request: pds_20220301_models.SearchAddressGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchAddressGroupsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address_level):
            body['address_level'] = request.address_level
        if not UtilClient.is_unset(request.address_names):
            body['address_names'] = request.address_names
        if not UtilClient.is_unset(request.br_geo_point):
            body['br_geo_point'] = request.br_geo_point
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.tl_geo_point):
            body['tl_geo_point'] = request.tl_geo_point
        if not UtilClient.is_unset(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchAddressGroups',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/search_address_groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchAddressGroupsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_drive(
        self,
        request: pds_20220301_models.SearchDriveRequest,
    ) -> pds_20220301_models.SearchDriveResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_drive_with_options(request, headers, runtime)

    async def search_drive_async(
        self,
        request: pds_20220301_models.SearchDriveRequest,
    ) -> pds_20220301_models.SearchDriveResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_drive_with_options_async(request, headers, runtime)

    def search_drive_with_options(
        self,
        request: pds_20220301_models.SearchDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchDriveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_name):
            body['drive_name'] = request.drive_name
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.owner):
            body['owner'] = request.owner
        if not UtilClient.is_unset(request.owner_type):
            body['owner_type'] = request.owner_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def search_drive_with_options_async(
        self,
        request: pds_20220301_models.SearchDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchDriveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_name):
            body['drive_name'] = request.drive_name
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.owner):
            body['owner'] = request.owner
        if not UtilClient.is_unset(request.owner_type):
            body['owner_type'] = request.owner_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_file(
        self,
        request: pds_20220301_models.SearchFileRequest,
    ) -> pds_20220301_models.SearchFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_file_with_options(request, headers, runtime)

    async def search_file_async(
        self,
        request: pds_20220301_models.SearchFileRequest,
    ) -> pds_20220301_models.SearchFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_file_with_options_async(request, headers, runtime)

    def search_file_with_options(
        self,
        request: pds_20220301_models.SearchFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.return_total_count):
            body['return_total_count'] = request.return_total_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchFileResponse(),
            self.execute(params, req, runtime)
        )

    async def search_file_with_options_async(
        self,
        request: pds_20220301_models.SearchFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.return_total_count):
            body['return_total_count'] = request.return_total_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_share_link(
        self,
        request: pds_20220301_models.SearchShareLinkRequest,
    ) -> pds_20220301_models.SearchShareLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_share_link_with_options(request, headers, runtime)

    async def search_share_link_async(
        self,
        request: pds_20220301_models.SearchShareLinkRequest,
    ) -> pds_20220301_models.SearchShareLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_share_link_with_options_async(request, headers, runtime)

    def search_share_link_with_options(
        self,
        request: pds_20220301_models.SearchShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchShareLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creators):
            body['creators'] = request.creators
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.order_direction):
            body['order_direction'] = request.order_direction
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.return_total_count):
            body['return_total_count'] = request.return_total_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    async def search_share_link_with_options_async(
        self,
        request: pds_20220301_models.SearchShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchShareLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creators):
            body['creators'] = request.creators
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.order_direction):
            body['order_direction'] = request.order_direction
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.return_total_count):
            body['return_total_count'] = request.return_total_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchShareLinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_user(
        self,
        request: pds_20220301_models.SearchUserRequest,
    ) -> pds_20220301_models.SearchUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_user_with_options(request, headers, runtime)

    async def search_user_async(
        self,
        request: pds_20220301_models.SearchUserRequest,
    ) -> pds_20220301_models.SearchUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_user_with_options_async(request, headers, runtime)

    def search_user_with_options(
        self,
        request: pds_20220301_models.SearchUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.nick_name):
            body['nick_name'] = request.nick_name
        if not UtilClient.is_unset(request.nick_name_for_fuzzy):
            body['nick_name_for_fuzzy'] = request.nick_name_for_fuzzy
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_name):
            body['user_name'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchUserResponse(),
            self.execute(params, req, runtime)
        )

    async def search_user_with_options_async(
        self,
        request: pds_20220301_models.SearchUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.nick_name):
            body['nick_name'] = request.nick_name
        if not UtilClient.is_unset(request.nick_name_for_fuzzy):
            body['nick_name_for_fuzzy'] = request.nick_name_for_fuzzy
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_name):
            body['user_name'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchUserResponse(),
            await self.execute_async(params, req, runtime)
        )

    def token(
        self,
        request: pds_20220301_models.TokenRequest,
    ) -> pds_20220301_models.TokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.token_with_options(request, headers, runtime)

    async def token_async(
        self,
        request: pds_20220301_models.TokenRequest,
    ) -> pds_20220301_models.TokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.token_with_options_async(request, headers, runtime)

    def token_with_options(
        self,
        request: pds_20220301_models.TokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.TokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assertion):
            body['assertion'] = request.assertion
        if not UtilClient.is_unset(request.client_id):
            body['client_id'] = request.client_id
        if not UtilClient.is_unset(request.client_secret):
            body['client_secret'] = request.client_secret
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.grant_type):
            body['grant_type'] = request.grant_type
        if not UtilClient.is_unset(request.redirect_uri):
            body['redirect_uri'] = request.redirect_uri
        if not UtilClient.is_unset(request.refresh_token):
            body['refresh_token'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Token',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/oauth/token',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.TokenResponse(),
            self.execute(params, req, runtime)
        )

    async def token_with_options_async(
        self,
        request: pds_20220301_models.TokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.TokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assertion):
            body['assertion'] = request.assertion
        if not UtilClient.is_unset(request.client_id):
            body['client_id'] = request.client_id
        if not UtilClient.is_unset(request.client_secret):
            body['client_secret'] = request.client_secret
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.grant_type):
            body['grant_type'] = request.grant_type
        if not UtilClient.is_unset(request.redirect_uri):
            body['redirect_uri'] = request.redirect_uri
        if not UtilClient.is_unset(request.refresh_token):
            body['refresh_token'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Token',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/oauth/token',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.TokenResponse(),
            await self.execute_async(params, req, runtime)
        )

    def trash_file(
        self,
        request: pds_20220301_models.TrashFileRequest,
    ) -> pds_20220301_models.TrashFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.trash_file_with_options(request, headers, runtime)

    async def trash_file_async(
        self,
        request: pds_20220301_models.TrashFileRequest,
    ) -> pds_20220301_models.TrashFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.trash_file_with_options_async(request, headers, runtime)

    def trash_file_with_options(
        self,
        request: pds_20220301_models.TrashFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.TrashFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TrashFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/recyclebin/trash',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.TrashFileResponse(),
            self.execute(params, req, runtime)
        )

    async def trash_file_with_options_async(
        self,
        request: pds_20220301_models.TrashFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.TrashFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TrashFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/recyclebin/trash',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.TrashFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_drive(
        self,
        request: pds_20220301_models.UpdateDriveRequest,
    ) -> pds_20220301_models.UpdateDriveResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_drive_with_options(request, headers, runtime)

    async def update_drive_async(
        self,
        request: pds_20220301_models.UpdateDriveRequest,
    ) -> pds_20220301_models.UpdateDriveResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_drive_with_options_async(request, headers, runtime)

    def update_drive_with_options(
        self,
        request: pds_20220301_models.UpdateDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateDriveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.drive_name):
            body['drive_name'] = request.drive_name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.total_size):
            body['total_size'] = request.total_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def update_drive_with_options_async(
        self,
        request: pds_20220301_models.UpdateDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateDriveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.drive_name):
            body['drive_name'] = request.drive_name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.total_size):
            body['total_size'] = request.total_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_facegroup(
        self,
        request: pds_20220301_models.UpdateFacegroupRequest,
    ) -> pds_20220301_models.UpdateFacegroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_facegroup_with_options(request, headers, runtime)

    async def update_facegroup_async(
        self,
        request: pds_20220301_models.UpdateFacegroupRequest,
    ) -> pds_20220301_models.UpdateFacegroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_facegroup_with_options_async(request, headers, runtime)

    def update_facegroup_with_options(
        self,
        request: pds_20220301_models.UpdateFacegroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateFacegroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.group_cover_face_id):
            body['group_cover_face_id'] = request.group_cover_face_id
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            body['group_name'] = request.group_name
        if not UtilClient.is_unset(request.remarks):
            body['remarks'] = request.remarks
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFacegroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/update_facegroup_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateFacegroupResponse(),
            self.execute(params, req, runtime)
        )

    async def update_facegroup_with_options_async(
        self,
        request: pds_20220301_models.UpdateFacegroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateFacegroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.group_cover_face_id):
            body['group_cover_face_id'] = request.group_cover_face_id
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            body['group_name'] = request.group_name
        if not UtilClient.is_unset(request.remarks):
            body['remarks'] = request.remarks
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFacegroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/update_facegroup_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateFacegroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_file(
        self,
        request: pds_20220301_models.UpdateFileRequest,
    ) -> pds_20220301_models.UpdateFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_file_with_options(request, headers, runtime)

    async def update_file_async(
        self,
        request: pds_20220301_models.UpdateFileRequest,
    ) -> pds_20220301_models.UpdateFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_file_with_options_async(request, headers, runtime)

    def update_file_with_options(
        self,
        request: pds_20220301_models.UpdateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.hidden):
            body['hidden'] = request.hidden
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        if not UtilClient.is_unset(request.local_modified_at):
            body['local_modified_at'] = request.local_modified_at
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.starred):
            body['starred'] = request.starred
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateFileResponse(),
            self.execute(params, req, runtime)
        )

    async def update_file_with_options_async(
        self,
        request: pds_20220301_models.UpdateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.hidden):
            body['hidden'] = request.hidden
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        if not UtilClient.is_unset(request.local_modified_at):
            body['local_modified_at'] = request.local_modified_at
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.starred):
            body['starred'] = request.starred
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_group(
        self,
        request: pds_20220301_models.UpdateGroupRequest,
    ) -> pds_20220301_models.UpdateGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_group_with_options(request, headers, runtime)

    async def update_group_async(
        self,
        request: pds_20220301_models.UpdateGroupRequest,
    ) -> pds_20220301_models.UpdateGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_group_with_options_async(request, headers, runtime)

    def update_group_with_options(
        self,
        request: pds_20220301_models.UpdateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            body['group_name'] = request.group_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def update_group_with_options_async(
        self,
        request: pds_20220301_models.UpdateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            body['group_name'] = request.group_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_revision(
        self,
        request: pds_20220301_models.UpdateRevisionRequest,
    ) -> pds_20220301_models.UpdateRevisionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_revision_with_options(request, headers, runtime)

    async def update_revision_async(
        self,
        request: pds_20220301_models.UpdateRevisionRequest,
    ) -> pds_20220301_models.UpdateRevisionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_revision_with_options_async(request, headers, runtime)

    def update_revision_with_options(
        self,
        request: pds_20220301_models.UpdateRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateRevisionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.keep_forever):
            body['keep_forever'] = request.keep_forever
        if not UtilClient.is_unset(request.revision_description):
            body['revision_description'] = request.revision_description
        if not UtilClient.is_unset(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/revision/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateRevisionResponse(),
            self.execute(params, req, runtime)
        )

    async def update_revision_with_options_async(
        self,
        request: pds_20220301_models.UpdateRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateRevisionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.keep_forever):
            body['keep_forever'] = request.keep_forever
        if not UtilClient.is_unset(request.revision_description):
            body['revision_description'] = request.revision_description
        if not UtilClient.is_unset(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/revision/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateRevisionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_share_link(
        self,
        request: pds_20220301_models.UpdateShareLinkRequest,
    ) -> pds_20220301_models.UpdateShareLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_share_link_with_options(request, headers, runtime)

    async def update_share_link_async(
        self,
        request: pds_20220301_models.UpdateShareLinkRequest,
    ) -> pds_20220301_models.UpdateShareLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_share_link_with_options_async(request, headers, runtime)

    def update_share_link_with_options(
        self,
        request: pds_20220301_models.UpdateShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateShareLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.disable_download):
            body['disable_download'] = request.disable_download
        if not UtilClient.is_unset(request.disable_preview):
            body['disable_preview'] = request.disable_preview
        if not UtilClient.is_unset(request.disable_save):
            body['disable_save'] = request.disable_save
        if not UtilClient.is_unset(request.download_count):
            body['download_count'] = request.download_count
        if not UtilClient.is_unset(request.download_limit):
            body['download_limit'] = request.download_limit
        if not UtilClient.is_unset(request.expiration):
            body['expiration'] = request.expiration
        if not UtilClient.is_unset(request.preview_count):
            body['preview_count'] = request.preview_count
        if not UtilClient.is_unset(request.preview_limit):
            body['preview_limit'] = request.preview_limit
        if not UtilClient.is_unset(request.report_count):
            body['report_count'] = request.report_count
        if not UtilClient.is_unset(request.save_count):
            body['save_count'] = request.save_count
        if not UtilClient.is_unset(request.save_limit):
            body['save_limit'] = request.save_limit
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.share_name):
            body['share_name'] = request.share_name
        if not UtilClient.is_unset(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.video_preview_count):
            body['video_preview_count'] = request.video_preview_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    async def update_share_link_with_options_async(
        self,
        request: pds_20220301_models.UpdateShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateShareLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.disable_download):
            body['disable_download'] = request.disable_download
        if not UtilClient.is_unset(request.disable_preview):
            body['disable_preview'] = request.disable_preview
        if not UtilClient.is_unset(request.disable_save):
            body['disable_save'] = request.disable_save
        if not UtilClient.is_unset(request.download_count):
            body['download_count'] = request.download_count
        if not UtilClient.is_unset(request.download_limit):
            body['download_limit'] = request.download_limit
        if not UtilClient.is_unset(request.expiration):
            body['expiration'] = request.expiration
        if not UtilClient.is_unset(request.preview_count):
            body['preview_count'] = request.preview_count
        if not UtilClient.is_unset(request.preview_limit):
            body['preview_limit'] = request.preview_limit
        if not UtilClient.is_unset(request.report_count):
            body['report_count'] = request.report_count
        if not UtilClient.is_unset(request.save_count):
            body['save_count'] = request.save_count
        if not UtilClient.is_unset(request.save_limit):
            body['save_limit'] = request.save_limit
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.share_name):
            body['share_name'] = request.share_name
        if not UtilClient.is_unset(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.video_preview_count):
            body['video_preview_count'] = request.video_preview_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateShareLinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_user(
        self,
        request: pds_20220301_models.UpdateUserRequest,
    ) -> pds_20220301_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_user_with_options(request, headers, runtime)

    async def update_user_async(
        self,
        request: pds_20220301_models.UpdateUserRequest,
    ) -> pds_20220301_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_user_with_options_async(request, headers, runtime)

    def update_user_with_options(
        self,
        request: pds_20220301_models.UpdateUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.avatar):
            body['avatar'] = request.avatar
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.group_info_list):
            body['group_info_list'] = request.group_info_list
        if not UtilClient.is_unset(request.nick_name):
            body['nick_name'] = request.nick_name
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateUserResponse(),
            self.execute(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: pds_20220301_models.UpdateUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.avatar):
            body['avatar'] = request.avatar
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.group_info_list):
            body['group_info_list'] = request.group_info_list
        if not UtilClient.is_unset(request.nick_name):
            body['nick_name'] = request.nick_name
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateUserResponse(),
            await self.execute_async(params, req, runtime)
        )
