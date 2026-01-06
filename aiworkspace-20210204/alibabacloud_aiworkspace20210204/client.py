# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aiworkspace20210204 import models as main_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-2-pop': 'aiworkspace.aliyuncs.com',
            'ap-southeast-2': 'aiworkspace.aliyuncs.com',
            'ap-southeast-5': 'aiworkspace-vpc.ap-southeast-5.aliyuncs.com',
            'cn-beijing-finance-1': 'aiworkspace.aliyuncs.com',
            'cn-beijing-finance-pop': 'aiworkspace.aliyuncs.com',
            'cn-beijing-gov-1': 'aiworkspace.aliyuncs.com',
            'cn-beijing-nu16-b01': 'aiworkspace.aliyuncs.com',
            'cn-edge-1': 'aiworkspace.aliyuncs.com',
            'cn-fujian': 'aiworkspace.aliyuncs.com',
            'cn-haidian-cm12-c01': 'aiworkspace.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'aiworkspace.aliyuncs.com',
            'cn-hangzhou-finance': 'aiworkspace.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'aiworkspace.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'aiworkspace.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'aiworkspace.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'aiworkspace.aliyuncs.com',
            'cn-hangzhou-test-306': 'aiworkspace.aliyuncs.com',
            'cn-hongkong-finance-pop': 'aiworkspace.aliyuncs.com',
            'cn-huhehaote': 'aiworkspace.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'aiworkspace.aliyuncs.com',
            'cn-qingdao': 'aiworkspace.aliyuncs.com',
            'cn-qingdao-nebula': 'aiworkspace.aliyuncs.com',
            'cn-shanghai-et15-b01': 'aiworkspace.aliyuncs.com',
            'cn-shanghai-et2-b01': 'aiworkspace.aliyuncs.com',
            'cn-shanghai-inner': 'aiworkspace.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'aiworkspace.aliyuncs.com',
            'cn-shenzhen-finance-1': 'aiworkspace.aliyuncs.com',
            'cn-shenzhen-inner': 'aiworkspace.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'aiworkspace.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'aiworkspace.aliyuncs.com',
            'cn-wuhan': 'aiworkspace.aliyuncs.com',
            'cn-yushanfang': 'aiworkspace.aliyuncs.com',
            'cn-zhangbei': 'aiworkspace.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'aiworkspace.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'aiworkspace.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'aiworkspace.aliyuncs.com',
            'eu-west-1': 'aiworkspace.aliyuncs.com',
            'eu-west-1-oxs': 'aiworkspace.aliyuncs.com',
            'me-east-1': 'aiworkspace.aliyuncs.com',
            'rus-west-1-pop': 'aiworkspace.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('aiworkspace', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def accept_dataworks_event_with_options(
        self,
        request: main_models.AcceptDataworksEventRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AcceptDataworksEventResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.message_id):
            body['MessageId'] = request.message_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AcceptDataworksEvent',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/action/acceptdataworksevent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AcceptDataworksEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_dataworks_event_with_options_async(
        self,
        request: main_models.AcceptDataworksEventRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AcceptDataworksEventResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.message_id):
            body['MessageId'] = request.message_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AcceptDataworksEvent',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/action/acceptdataworksevent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AcceptDataworksEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_dataworks_event(
        self,
        request: main_models.AcceptDataworksEventRequest,
    ) -> main_models.AcceptDataworksEventResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.accept_dataworks_event_with_options(request, headers, runtime)

    async def accept_dataworks_event_async(
        self,
        request: main_models.AcceptDataworksEventRequest,
    ) -> main_models.AcceptDataworksEventResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.accept_dataworks_event_with_options_async(request, headers, runtime)

    def add_image_with_options(
        self,
        request: main_models.AddImageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.image_uri):
            body['ImageUri'] = request.image_uri
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        if not DaraCore.is_null(request.source_id):
            body['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddImage',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/images',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_image_with_options_async(
        self,
        request: main_models.AddImageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.image_uri):
            body['ImageUri'] = request.image_uri
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        if not DaraCore.is_null(request.source_id):
            body['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddImage',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/images',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_image(
        self,
        request: main_models.AddImageRequest,
    ) -> main_models.AddImageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_image_with_options(request, headers, runtime)

    async def add_image_async(
        self,
        request: main_models.AddImageRequest,
    ) -> main_models.AddImageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_image_with_options_async(request, headers, runtime)

    def add_image_labels_with_options(
        self,
        image_id: str,
        request: main_models.AddImageLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddImageLabelsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddImageLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/images/{DaraURL.percent_encode(image_id)}/labels',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddImageLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_image_labels_with_options_async(
        self,
        image_id: str,
        request: main_models.AddImageLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddImageLabelsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddImageLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/images/{DaraURL.percent_encode(image_id)}/labels',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddImageLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_image_labels(
        self,
        image_id: str,
        request: main_models.AddImageLabelsRequest,
    ) -> main_models.AddImageLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_image_labels_with_options(image_id, request, headers, runtime)

    async def add_image_labels_async(
        self,
        image_id: str,
        request: main_models.AddImageLabelsRequest,
    ) -> main_models.AddImageLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_image_labels_with_options_async(image_id, request, headers, runtime)

    def add_member_role_with_options(
        self,
        workspace_id: str,
        member_id: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddMemberRoleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'AddMemberRole',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/members/{DaraURL.percent_encode(member_id)}/roles/{DaraURL.percent_encode(role_name)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMemberRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_member_role_with_options_async(
        self,
        workspace_id: str,
        member_id: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddMemberRoleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'AddMemberRole',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/members/{DaraURL.percent_encode(member_id)}/roles/{DaraURL.percent_encode(role_name)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMemberRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_member_role(
        self,
        workspace_id: str,
        member_id: str,
        role_name: str,
    ) -> main_models.AddMemberRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_member_role_with_options(workspace_id, member_id, role_name, headers, runtime)

    async def add_member_role_async(
        self,
        workspace_id: str,
        member_id: str,
        role_name: str,
    ) -> main_models.AddMemberRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_member_role_with_options_async(workspace_id, member_id, role_name, headers, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/resourcegroups/action/changeresourcegroup',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/resourcegroups/action/changeresourcegroup',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.change_resource_group_with_options(request, headers, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.change_resource_group_with_options_async(request, headers, runtime)

    def create_code_source_with_options(
        self,
        request: main_models.CreateCodeSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCodeSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.code_branch):
            body['CodeBranch'] = request.code_branch
        if not DaraCore.is_null(request.code_commit):
            body['CodeCommit'] = request.code_commit
        if not DaraCore.is_null(request.code_repo):
            body['CodeRepo'] = request.code_repo
        if not DaraCore.is_null(request.code_repo_access_token):
            body['CodeRepoAccessToken'] = request.code_repo_access_token
        if not DaraCore.is_null(request.code_repo_user_name):
            body['CodeRepoUserName'] = request.code_repo_user_name
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.mount_path):
            body['MountPath'] = request.mount_path
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCodeSource',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/codesources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCodeSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_code_source_with_options_async(
        self,
        request: main_models.CreateCodeSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCodeSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.code_branch):
            body['CodeBranch'] = request.code_branch
        if not DaraCore.is_null(request.code_commit):
            body['CodeCommit'] = request.code_commit
        if not DaraCore.is_null(request.code_repo):
            body['CodeRepo'] = request.code_repo
        if not DaraCore.is_null(request.code_repo_access_token):
            body['CodeRepoAccessToken'] = request.code_repo_access_token
        if not DaraCore.is_null(request.code_repo_user_name):
            body['CodeRepoUserName'] = request.code_repo_user_name
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.mount_path):
            body['MountPath'] = request.mount_path
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCodeSource',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/codesources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCodeSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_code_source(
        self,
        request: main_models.CreateCodeSourceRequest,
    ) -> main_models.CreateCodeSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_code_source_with_options(request, headers, runtime)

    async def create_code_source_async(
        self,
        request: main_models.CreateCodeSourceRequest,
    ) -> main_models.CreateCodeSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_code_source_with_options_async(request, headers, runtime)

    def create_connection_with_options(
        self,
        request: main_models.CreateConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConnectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.configs):
            body['Configs'] = request.configs
        if not DaraCore.is_null(request.connection_name):
            body['ConnectionName'] = request.connection_name
        if not DaraCore.is_null(request.connection_type):
            body['ConnectionType'] = request.connection_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.models):
            body['Models'] = request.models
        if not DaraCore.is_null(request.resource_meta):
            body['ResourceMeta'] = request.resource_meta
        if not DaraCore.is_null(request.secrets):
            body['Secrets'] = request.secrets
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConnection',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/connections',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_connection_with_options_async(
        self,
        request: main_models.CreateConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConnectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.configs):
            body['Configs'] = request.configs
        if not DaraCore.is_null(request.connection_name):
            body['ConnectionName'] = request.connection_name
        if not DaraCore.is_null(request.connection_type):
            body['ConnectionType'] = request.connection_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.models):
            body['Models'] = request.models
        if not DaraCore.is_null(request.resource_meta):
            body['ResourceMeta'] = request.resource_meta
        if not DaraCore.is_null(request.secrets):
            body['Secrets'] = request.secrets
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConnection',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/connections',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_connection(
        self,
        request: main_models.CreateConnectionRequest,
    ) -> main_models.CreateConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_connection_with_options(request, headers, runtime)

    async def create_connection_async(
        self,
        request: main_models.CreateConnectionRequest,
    ) -> main_models.CreateConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_connection_with_options_async(request, headers, runtime)

    def create_dataset_with_options(
        self,
        request: main_models.CreateDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.data_count):
            body['DataCount'] = request.data_count
        if not DaraCore.is_null(request.data_size):
            body['DataSize'] = request.data_size
        if not DaraCore.is_null(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.data_type):
            body['DataType'] = request.data_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.edition):
            body['Edition'] = request.edition
        if not DaraCore.is_null(request.import_info):
            body['ImportInfo'] = request.import_info
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.mount_access_read_write_role_id_list):
            body['MountAccessReadWriteRoleIdList'] = request.mount_access_read_write_role_id_list
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.options):
            body['Options'] = request.options
        if not DaraCore.is_null(request.property):
            body['Property'] = request.property
        if not DaraCore.is_null(request.provider):
            body['Provider'] = request.provider
        if not DaraCore.is_null(request.provider_type):
            body['ProviderType'] = request.provider_type
        if not DaraCore.is_null(request.source_dataset_id):
            body['SourceDatasetId'] = request.source_dataset_id
        if not DaraCore.is_null(request.source_dataset_version):
            body['SourceDatasetVersion'] = request.source_dataset_version
        if not DaraCore.is_null(request.source_id):
            body['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        if not DaraCore.is_null(request.version_description):
            body['VersionDescription'] = request.version_description
        if not DaraCore.is_null(request.version_labels):
            body['VersionLabels'] = request.version_labels
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataset',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_with_options_async(
        self,
        request: main_models.CreateDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.data_count):
            body['DataCount'] = request.data_count
        if not DaraCore.is_null(request.data_size):
            body['DataSize'] = request.data_size
        if not DaraCore.is_null(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.data_type):
            body['DataType'] = request.data_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.edition):
            body['Edition'] = request.edition
        if not DaraCore.is_null(request.import_info):
            body['ImportInfo'] = request.import_info
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.mount_access_read_write_role_id_list):
            body['MountAccessReadWriteRoleIdList'] = request.mount_access_read_write_role_id_list
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.options):
            body['Options'] = request.options
        if not DaraCore.is_null(request.property):
            body['Property'] = request.property
        if not DaraCore.is_null(request.provider):
            body['Provider'] = request.provider
        if not DaraCore.is_null(request.provider_type):
            body['ProviderType'] = request.provider_type
        if not DaraCore.is_null(request.source_dataset_id):
            body['SourceDatasetId'] = request.source_dataset_id
        if not DaraCore.is_null(request.source_dataset_version):
            body['SourceDatasetVersion'] = request.source_dataset_version
        if not DaraCore.is_null(request.source_id):
            body['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        if not DaraCore.is_null(request.version_description):
            body['VersionDescription'] = request.version_description
        if not DaraCore.is_null(request.version_labels):
            body['VersionLabels'] = request.version_labels
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataset',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset(
        self,
        request: main_models.CreateDatasetRequest,
    ) -> main_models.CreateDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_dataset_with_options(request, headers, runtime)

    async def create_dataset_async(
        self,
        request: main_models.CreateDatasetRequest,
    ) -> main_models.CreateDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_dataset_with_options_async(request, headers, runtime)

    def create_dataset_file_metas_with_options(
        self,
        dataset_id: str,
        request: main_models.CreateDatasetFileMetasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetFileMetasResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_file_metas):
            body['DatasetFileMetas'] = request.dataset_file_metas
        if not DaraCore.is_null(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatasetFileMetas',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetfilemetas',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetFileMetasResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_file_metas_with_options_async(
        self,
        dataset_id: str,
        request: main_models.CreateDatasetFileMetasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetFileMetasResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_file_metas):
            body['DatasetFileMetas'] = request.dataset_file_metas
        if not DaraCore.is_null(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatasetFileMetas',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetfilemetas',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetFileMetasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset_file_metas(
        self,
        dataset_id: str,
        request: main_models.CreateDatasetFileMetasRequest,
    ) -> main_models.CreateDatasetFileMetasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_dataset_file_metas_with_options(dataset_id, request, headers, runtime)

    async def create_dataset_file_metas_async(
        self,
        dataset_id: str,
        request: main_models.CreateDatasetFileMetasRequest,
    ) -> main_models.CreateDatasetFileMetasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_dataset_file_metas_with_options_async(dataset_id, request, headers, runtime)

    def create_dataset_job_with_options(
        self,
        dataset_id: str,
        request: main_models.CreateDatasetJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.job_action):
            body['JobAction'] = request.job_action
        if not DaraCore.is_null(request.job_mode):
            body['JobMode'] = request.job_mode
        if not DaraCore.is_null(request.job_spec):
            body['JobSpec'] = request.job_spec
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatasetJob',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_job_with_options_async(
        self,
        dataset_id: str,
        request: main_models.CreateDatasetJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.job_action):
            body['JobAction'] = request.job_action
        if not DaraCore.is_null(request.job_mode):
            body['JobMode'] = request.job_mode
        if not DaraCore.is_null(request.job_spec):
            body['JobSpec'] = request.job_spec
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatasetJob',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset_job(
        self,
        dataset_id: str,
        request: main_models.CreateDatasetJobRequest,
    ) -> main_models.CreateDatasetJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_dataset_job_with_options(dataset_id, request, headers, runtime)

    async def create_dataset_job_async(
        self,
        dataset_id: str,
        request: main_models.CreateDatasetJobRequest,
    ) -> main_models.CreateDatasetJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_dataset_job_with_options_async(dataset_id, request, headers, runtime)

    def create_dataset_job_config_with_options(
        self,
        dataset_id: str,
        request: main_models.CreateDatasetJobConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetJobConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.config_type):
            body['ConfigType'] = request.config_type
        if not DaraCore.is_null(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatasetJobConfig',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobconfigs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_job_config_with_options_async(
        self,
        dataset_id: str,
        request: main_models.CreateDatasetJobConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetJobConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.config_type):
            body['ConfigType'] = request.config_type
        if not DaraCore.is_null(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatasetJobConfig',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobconfigs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetJobConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset_job_config(
        self,
        dataset_id: str,
        request: main_models.CreateDatasetJobConfigRequest,
    ) -> main_models.CreateDatasetJobConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_dataset_job_config_with_options(dataset_id, request, headers, runtime)

    async def create_dataset_job_config_async(
        self,
        dataset_id: str,
        request: main_models.CreateDatasetJobConfigRequest,
    ) -> main_models.CreateDatasetJobConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_dataset_job_config_with_options_async(dataset_id, request, headers, runtime)

    def create_dataset_labels_with_options(
        self,
        dataset_id: str,
        request: main_models.CreateDatasetLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetLabelsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatasetLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/labels',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_labels_with_options_async(
        self,
        dataset_id: str,
        request: main_models.CreateDatasetLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetLabelsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatasetLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/labels',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset_labels(
        self,
        dataset_id: str,
        request: main_models.CreateDatasetLabelsRequest,
    ) -> main_models.CreateDatasetLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_dataset_labels_with_options(dataset_id, request, headers, runtime)

    async def create_dataset_labels_async(
        self,
        dataset_id: str,
        request: main_models.CreateDatasetLabelsRequest,
    ) -> main_models.CreateDatasetLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_dataset_labels_with_options_async(dataset_id, request, headers, runtime)

    def create_dataset_version_with_options(
        self,
        dataset_id: str,
        request: main_models.CreateDatasetVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_count):
            body['DataCount'] = request.data_count
        if not DaraCore.is_null(request.data_size):
            body['DataSize'] = request.data_size
        if not DaraCore.is_null(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.import_info):
            body['ImportInfo'] = request.import_info
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.options):
            body['Options'] = request.options
        if not DaraCore.is_null(request.property):
            body['Property'] = request.property
        if not DaraCore.is_null(request.source_id):
            body['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatasetVersion',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_version_with_options_async(
        self,
        dataset_id: str,
        request: main_models.CreateDatasetVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_count):
            body['DataCount'] = request.data_count
        if not DaraCore.is_null(request.data_size):
            body['DataSize'] = request.data_size
        if not DaraCore.is_null(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.import_info):
            body['ImportInfo'] = request.import_info
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.options):
            body['Options'] = request.options
        if not DaraCore.is_null(request.property):
            body['Property'] = request.property
        if not DaraCore.is_null(request.source_id):
            body['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatasetVersion',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset_version(
        self,
        dataset_id: str,
        request: main_models.CreateDatasetVersionRequest,
    ) -> main_models.CreateDatasetVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_dataset_version_with_options(dataset_id, request, headers, runtime)

    async def create_dataset_version_async(
        self,
        dataset_id: str,
        request: main_models.CreateDatasetVersionRequest,
    ) -> main_models.CreateDatasetVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_dataset_version_with_options_async(dataset_id, request, headers, runtime)

    def create_dataset_version_labels_with_options(
        self,
        dataset_id: str,
        version_name: str,
        request: main_models.CreateDatasetVersionLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetVersionLabelsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatasetVersionLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/versions/{DaraURL.percent_encode(version_name)}/labels',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetVersionLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_version_labels_with_options_async(
        self,
        dataset_id: str,
        version_name: str,
        request: main_models.CreateDatasetVersionLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetVersionLabelsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatasetVersionLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/versions/{DaraURL.percent_encode(version_name)}/labels',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetVersionLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset_version_labels(
        self,
        dataset_id: str,
        version_name: str,
        request: main_models.CreateDatasetVersionLabelsRequest,
    ) -> main_models.CreateDatasetVersionLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_dataset_version_labels_with_options(dataset_id, version_name, request, headers, runtime)

    async def create_dataset_version_labels_async(
        self,
        dataset_id: str,
        version_name: str,
        request: main_models.CreateDatasetVersionLabelsRequest,
    ) -> main_models.CreateDatasetVersionLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_dataset_version_labels_with_options_async(dataset_id, version_name, request, headers, runtime)

    def create_experiment_with_options(
        self,
        request: main_models.CreateExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateExperimentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.artifact_uri):
            body['ArtifactUri'] = request.artifact_uri
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExperiment',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_experiment_with_options_async(
        self,
        request: main_models.CreateExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateExperimentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.artifact_uri):
            body['ArtifactUri'] = request.artifact_uri
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExperiment',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_experiment(
        self,
        request: main_models.CreateExperimentRequest,
    ) -> main_models.CreateExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_experiment_with_options(request, headers, runtime)

    async def create_experiment_async(
        self,
        request: main_models.CreateExperimentRequest,
    ) -> main_models.CreateExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_experiment_with_options_async(request, headers, runtime)

    def create_image_build_with_options(
        self,
        request: main_models.CreateImageBuildRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageBuildResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.build_config):
            body['BuildConfig'] = request.build_config
        if not DaraCore.is_null(request.image):
            body['Image'] = request.image
        if not DaraCore.is_null(request.image_build_job_name):
            body['ImageBuildJobName'] = request.image_build_job_name
        if not DaraCore.is_null(request.overwrite_image_tag):
            body['OverwriteImageTag'] = request.overwrite_image_tag
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            body['Resource'] = request.resource
        if not DaraCore.is_null(request.target_registry):
            body['TargetRegistry'] = request.target_registry
        if not DaraCore.is_null(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageBuild',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/imagebuilds',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageBuildResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_build_with_options_async(
        self,
        request: main_models.CreateImageBuildRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageBuildResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.build_config):
            body['BuildConfig'] = request.build_config
        if not DaraCore.is_null(request.image):
            body['Image'] = request.image
        if not DaraCore.is_null(request.image_build_job_name):
            body['ImageBuildJobName'] = request.image_build_job_name
        if not DaraCore.is_null(request.overwrite_image_tag):
            body['OverwriteImageTag'] = request.overwrite_image_tag
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            body['Resource'] = request.resource
        if not DaraCore.is_null(request.target_registry):
            body['TargetRegistry'] = request.target_registry
        if not DaraCore.is_null(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageBuild',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/imagebuilds',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageBuildResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_build(
        self,
        request: main_models.CreateImageBuildRequest,
    ) -> main_models.CreateImageBuildResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_image_build_with_options(request, headers, runtime)

    async def create_image_build_async(
        self,
        request: main_models.CreateImageBuildRequest,
    ) -> main_models.CreateImageBuildResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_image_build_with_options_async(request, headers, runtime)

    def create_member_with_options(
        self,
        workspace_id: str,
        request: main_models.CreateMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMemberResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.members):
            body['Members'] = request.members
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMember',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/members',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_member_with_options_async(
        self,
        workspace_id: str,
        request: main_models.CreateMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMemberResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.members):
            body['Members'] = request.members
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMember',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/members',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_member(
        self,
        workspace_id: str,
        request: main_models.CreateMemberRequest,
    ) -> main_models.CreateMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_member_with_options(workspace_id, request, headers, runtime)

    async def create_member_async(
        self,
        workspace_id: str,
        request: main_models.CreateMemberRequest,
    ) -> main_models.CreateMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_member_with_options_async(workspace_id, request, headers, runtime)

    def create_model_with_options(
        self,
        request: main_models.CreateModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.domain):
            body['Domain'] = request.domain
        if not DaraCore.is_null(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.model_description):
            body['ModelDescription'] = request.model_description
        if not DaraCore.is_null(request.model_doc):
            body['ModelDoc'] = request.model_doc
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.model_type):
            body['ModelType'] = request.model_type
        if not DaraCore.is_null(request.order_number):
            body['OrderNumber'] = request.order_number
        if not DaraCore.is_null(request.origin):
            body['Origin'] = request.origin
        if not DaraCore.is_null(request.parameter_size):
            body['ParameterSize'] = request.parameter_size
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.task):
            body['Task'] = request.task
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModel',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_with_options_async(
        self,
        request: main_models.CreateModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.domain):
            body['Domain'] = request.domain
        if not DaraCore.is_null(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.model_description):
            body['ModelDescription'] = request.model_description
        if not DaraCore.is_null(request.model_doc):
            body['ModelDoc'] = request.model_doc
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.model_type):
            body['ModelType'] = request.model_type
        if not DaraCore.is_null(request.order_number):
            body['OrderNumber'] = request.order_number
        if not DaraCore.is_null(request.origin):
            body['Origin'] = request.origin
        if not DaraCore.is_null(request.parameter_size):
            body['ParameterSize'] = request.parameter_size
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.task):
            body['Task'] = request.task
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModel',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model(
        self,
        request: main_models.CreateModelRequest,
    ) -> main_models.CreateModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_model_with_options(request, headers, runtime)

    async def create_model_async(
        self,
        request: main_models.CreateModelRequest,
    ) -> main_models.CreateModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_model_with_options_async(request, headers, runtime)

    def create_model_labels_with_options(
        self,
        model_id: str,
        request: main_models.CreateModelLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelLabelsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModelLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}/labels',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_labels_with_options_async(
        self,
        model_id: str,
        request: main_models.CreateModelLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelLabelsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModelLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}/labels',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model_labels(
        self,
        model_id: str,
        request: main_models.CreateModelLabelsRequest,
    ) -> main_models.CreateModelLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_model_labels_with_options(model_id, request, headers, runtime)

    async def create_model_labels_async(
        self,
        model_id: str,
        request: main_models.CreateModelLabelsRequest,
    ) -> main_models.CreateModelLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_model_labels_with_options_async(model_id, request, headers, runtime)

    def create_model_version_with_options(
        self,
        model_id: str,
        request: main_models.CreateModelVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.approval_status):
            body['ApprovalStatus'] = request.approval_status
        if not DaraCore.is_null(request.compression_spec):
            body['CompressionSpec'] = request.compression_spec
        if not DaraCore.is_null(request.distillation_spec):
            body['DistillationSpec'] = request.distillation_spec
        if not DaraCore.is_null(request.evaluation_spec):
            body['EvaluationSpec'] = request.evaluation_spec
        if not DaraCore.is_null(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.format_type):
            body['FormatType'] = request.format_type
        if not DaraCore.is_null(request.framework_type):
            body['FrameworkType'] = request.framework_type
        if not DaraCore.is_null(request.inference_spec):
            body['InferenceSpec'] = request.inference_spec
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.metrics):
            body['Metrics'] = request.metrics
        if not DaraCore.is_null(request.options):
            body['Options'] = request.options
        if not DaraCore.is_null(request.source_id):
            body['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.training_spec):
            body['TrainingSpec'] = request.training_spec
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        if not DaraCore.is_null(request.version_description):
            body['VersionDescription'] = request.version_description
        if not DaraCore.is_null(request.version_name):
            body['VersionName'] = request.version_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModelVersion',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_version_with_options_async(
        self,
        model_id: str,
        request: main_models.CreateModelVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.approval_status):
            body['ApprovalStatus'] = request.approval_status
        if not DaraCore.is_null(request.compression_spec):
            body['CompressionSpec'] = request.compression_spec
        if not DaraCore.is_null(request.distillation_spec):
            body['DistillationSpec'] = request.distillation_spec
        if not DaraCore.is_null(request.evaluation_spec):
            body['EvaluationSpec'] = request.evaluation_spec
        if not DaraCore.is_null(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.format_type):
            body['FormatType'] = request.format_type
        if not DaraCore.is_null(request.framework_type):
            body['FrameworkType'] = request.framework_type
        if not DaraCore.is_null(request.inference_spec):
            body['InferenceSpec'] = request.inference_spec
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.metrics):
            body['Metrics'] = request.metrics
        if not DaraCore.is_null(request.options):
            body['Options'] = request.options
        if not DaraCore.is_null(request.source_id):
            body['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.training_spec):
            body['TrainingSpec'] = request.training_spec
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        if not DaraCore.is_null(request.version_description):
            body['VersionDescription'] = request.version_description
        if not DaraCore.is_null(request.version_name):
            body['VersionName'] = request.version_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModelVersion',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model_version(
        self,
        model_id: str,
        request: main_models.CreateModelVersionRequest,
    ) -> main_models.CreateModelVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_model_version_with_options(model_id, request, headers, runtime)

    async def create_model_version_async(
        self,
        model_id: str,
        request: main_models.CreateModelVersionRequest,
    ) -> main_models.CreateModelVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_model_version_with_options_async(model_id, request, headers, runtime)

    def create_model_version_labels_with_options(
        self,
        model_id: str,
        version_name: str,
        request: main_models.CreateModelVersionLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelVersionLabelsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModelVersionLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}/versions/{DaraURL.percent_encode(version_name)}/labels',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelVersionLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_version_labels_with_options_async(
        self,
        model_id: str,
        version_name: str,
        request: main_models.CreateModelVersionLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelVersionLabelsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModelVersionLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}/versions/{DaraURL.percent_encode(version_name)}/labels',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelVersionLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model_version_labels(
        self,
        model_id: str,
        version_name: str,
        request: main_models.CreateModelVersionLabelsRequest,
    ) -> main_models.CreateModelVersionLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_model_version_labels_with_options(model_id, version_name, request, headers, runtime)

    async def create_model_version_labels_async(
        self,
        model_id: str,
        version_name: str,
        request: main_models.CreateModelVersionLabelsRequest,
    ) -> main_models.CreateModelVersionLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_model_version_labels_with_options_async(model_id, version_name, request, headers, runtime)

    def create_product_orders_with_options(
        self,
        request: main_models.CreateProductOrdersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateProductOrdersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_pay):
            body['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.products):
            body['Products'] = request.products
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProductOrders',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/productorders',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProductOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_product_orders_with_options_async(
        self,
        request: main_models.CreateProductOrdersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateProductOrdersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_pay):
            body['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.products):
            body['Products'] = request.products
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProductOrders',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/productorders',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProductOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_product_orders(
        self,
        request: main_models.CreateProductOrdersRequest,
    ) -> main_models.CreateProductOrdersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_product_orders_with_options(request, headers, runtime)

    async def create_product_orders_async(
        self,
        request: main_models.CreateProductOrdersRequest,
    ) -> main_models.CreateProductOrdersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_product_orders_with_options_async(request, headers, runtime)

    def create_run_with_options(
        self,
        request: main_models.CreateRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRunResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.experiment_id):
            body['ExperimentId'] = request.experiment_id
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.params):
            body['Params'] = request.params
        if not DaraCore.is_null(request.source_id):
            body['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRun',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/runs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_run_with_options_async(
        self,
        request: main_models.CreateRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRunResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.experiment_id):
            body['ExperimentId'] = request.experiment_id
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.params):
            body['Params'] = request.params
        if not DaraCore.is_null(request.source_id):
            body['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRun',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/runs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_run(
        self,
        request: main_models.CreateRunRequest,
    ) -> main_models.CreateRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_run_with_options(request, headers, runtime)

    async def create_run_async(
        self,
        request: main_models.CreateRunRequest,
    ) -> main_models.CreateRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_run_with_options_async(request, headers, runtime)

    def create_workspace_with_options(
        self,
        request: main_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkspaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.env_types):
            body['EnvTypes'] = request.env_types
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.workspace_name):
            body['WorkspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkspace',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workspace_with_options_async(
        self,
        request: main_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkspaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.env_types):
            body['EnvTypes'] = request.env_types
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.workspace_name):
            body['WorkspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkspace',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workspace(
        self,
        request: main_models.CreateWorkspaceRequest,
    ) -> main_models.CreateWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_workspace_with_options(request, headers, runtime)

    async def create_workspace_async(
        self,
        request: main_models.CreateWorkspaceRequest,
    ) -> main_models.CreateWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_workspace_with_options_async(request, headers, runtime)

    def create_workspace_resource_with_options(
        self,
        workspace_id: str,
        request: main_models.CreateWorkspaceResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkspaceResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.option):
            body['Option'] = request.option
        if not DaraCore.is_null(request.resources):
            body['Resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkspaceResource',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/resources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkspaceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workspace_resource_with_options_async(
        self,
        workspace_id: str,
        request: main_models.CreateWorkspaceResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkspaceResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.option):
            body['Option'] = request.option
        if not DaraCore.is_null(request.resources):
            body['Resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkspaceResource',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/resources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkspaceResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workspace_resource(
        self,
        workspace_id: str,
        request: main_models.CreateWorkspaceResourceRequest,
    ) -> main_models.CreateWorkspaceResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_workspace_resource_with_options(workspace_id, request, headers, runtime)

    async def create_workspace_resource_async(
        self,
        workspace_id: str,
        request: main_models.CreateWorkspaceResourceRequest,
    ) -> main_models.CreateWorkspaceResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_workspace_resource_with_options_async(workspace_id, request, headers, runtime)

    def delete_code_source_with_options(
        self,
        code_source_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCodeSourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteCodeSource',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/codesources/{DaraURL.percent_encode(code_source_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCodeSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_code_source_with_options_async(
        self,
        code_source_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCodeSourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteCodeSource',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/codesources/{DaraURL.percent_encode(code_source_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCodeSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_code_source(
        self,
        code_source_id: str,
    ) -> main_models.DeleteCodeSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_code_source_with_options(code_source_id, headers, runtime)

    async def delete_code_source_async(
        self,
        code_source_id: str,
    ) -> main_models.DeleteCodeSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_code_source_with_options_async(code_source_id, headers, runtime)

    def delete_config_with_options(
        self,
        workspace_id: str,
        config_key: str,
        request: main_models.DeleteConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_name):
            query['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConfig',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/configs/{DaraURL.percent_encode(config_key)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_config_with_options_async(
        self,
        workspace_id: str,
        config_key: str,
        request: main_models.DeleteConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_name):
            query['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConfig',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/configs/{DaraURL.percent_encode(config_key)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_config(
        self,
        workspace_id: str,
        config_key: str,
        request: main_models.DeleteConfigRequest,
    ) -> main_models.DeleteConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_config_with_options(workspace_id, config_key, request, headers, runtime)

    async def delete_config_async(
        self,
        workspace_id: str,
        config_key: str,
        request: main_models.DeleteConfigRequest,
    ) -> main_models.DeleteConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_config_with_options_async(workspace_id, config_key, request, headers, runtime)

    def delete_connection_with_options(
        self,
        connection_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConnectionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConnection',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/connections/{DaraURL.percent_encode(connection_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_connection_with_options_async(
        self,
        connection_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConnectionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConnection',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/connections/{DaraURL.percent_encode(connection_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_connection(
        self,
        connection_id: str,
    ) -> main_models.DeleteConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_connection_with_options(connection_id, headers, runtime)

    async def delete_connection_async(
        self,
        connection_id: str,
    ) -> main_models.DeleteConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_connection_with_options_async(connection_id, headers, runtime)

    def delete_dataset_with_options(
        self,
        dataset_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataset',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_with_options_async(
        self,
        dataset_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataset',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset(
        self,
        dataset_id: str,
    ) -> main_models.DeleteDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_dataset_with_options(dataset_id, headers, runtime)

    async def delete_dataset_async(
        self,
        dataset_id: str,
    ) -> main_models.DeleteDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_dataset_with_options_async(dataset_id, headers, runtime)

    def delete_dataset_file_metas_with_options(
        self,
        dataset_id: str,
        request: main_models.DeleteDatasetFileMetasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetFileMetasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_file_meta_ids):
            query['DatasetFileMetaIds'] = request.dataset_file_meta_ids
        if not DaraCore.is_null(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatasetFileMetas',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetfilemetas',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetFileMetasResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_file_metas_with_options_async(
        self,
        dataset_id: str,
        request: main_models.DeleteDatasetFileMetasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetFileMetasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_file_meta_ids):
            query['DatasetFileMetaIds'] = request.dataset_file_meta_ids
        if not DaraCore.is_null(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatasetFileMetas',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetfilemetas',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetFileMetasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset_file_metas(
        self,
        dataset_id: str,
        request: main_models.DeleteDatasetFileMetasRequest,
    ) -> main_models.DeleteDatasetFileMetasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_dataset_file_metas_with_options(dataset_id, request, headers, runtime)

    async def delete_dataset_file_metas_async(
        self,
        dataset_id: str,
        request: main_models.DeleteDatasetFileMetasRequest,
    ) -> main_models.DeleteDatasetFileMetasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_dataset_file_metas_with_options_async(dataset_id, request, headers, runtime)

    def delete_dataset_job_with_options(
        self,
        dataset_id: str,
        dataset_job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatasetJob',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobs/{DaraURL.percent_encode(dataset_job_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_job_with_options_async(
        self,
        dataset_id: str,
        dataset_job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatasetJob',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobs/{DaraURL.percent_encode(dataset_job_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset_job(
        self,
        dataset_id: str,
        dataset_job_id: str,
    ) -> main_models.DeleteDatasetJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_dataset_job_with_options(dataset_id, dataset_job_id, headers, runtime)

    async def delete_dataset_job_async(
        self,
        dataset_id: str,
        dataset_job_id: str,
    ) -> main_models.DeleteDatasetJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_dataset_job_with_options_async(dataset_id, dataset_job_id, headers, runtime)

    def delete_dataset_job_config_with_options(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: main_models.DeleteDatasetJobConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetJobConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatasetJobConfig',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobconfigs/{DaraURL.percent_encode(dataset_job_config_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_job_config_with_options_async(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: main_models.DeleteDatasetJobConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetJobConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatasetJobConfig',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobconfigs/{DaraURL.percent_encode(dataset_job_config_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetJobConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset_job_config(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: main_models.DeleteDatasetJobConfigRequest,
    ) -> main_models.DeleteDatasetJobConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_dataset_job_config_with_options(dataset_id, dataset_job_config_id, request, headers, runtime)

    async def delete_dataset_job_config_async(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: main_models.DeleteDatasetJobConfigRequest,
    ) -> main_models.DeleteDatasetJobConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_dataset_job_config_with_options_async(dataset_id, dataset_job_config_id, request, headers, runtime)

    def delete_dataset_labels_with_options(
        self,
        dataset_id: str,
        request: main_models.DeleteDatasetLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.label_keys):
            query['LabelKeys'] = request.label_keys
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatasetLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/labels',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_labels_with_options_async(
        self,
        dataset_id: str,
        request: main_models.DeleteDatasetLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.label_keys):
            query['LabelKeys'] = request.label_keys
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatasetLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/labels',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset_labels(
        self,
        dataset_id: str,
        request: main_models.DeleteDatasetLabelsRequest,
    ) -> main_models.DeleteDatasetLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_dataset_labels_with_options(dataset_id, request, headers, runtime)

    async def delete_dataset_labels_async(
        self,
        dataset_id: str,
        request: main_models.DeleteDatasetLabelsRequest,
    ) -> main_models.DeleteDatasetLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_dataset_labels_with_options_async(dataset_id, request, headers, runtime)

    def delete_dataset_version_with_options(
        self,
        dataset_id: str,
        version_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatasetVersion',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/versions/{DaraURL.percent_encode(version_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_version_with_options_async(
        self,
        dataset_id: str,
        version_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatasetVersion',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/versions/{DaraURL.percent_encode(version_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset_version(
        self,
        dataset_id: str,
        version_name: str,
    ) -> main_models.DeleteDatasetVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_dataset_version_with_options(dataset_id, version_name, headers, runtime)

    async def delete_dataset_version_async(
        self,
        dataset_id: str,
        version_name: str,
    ) -> main_models.DeleteDatasetVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_dataset_version_with_options_async(dataset_id, version_name, headers, runtime)

    def delete_dataset_version_labels_with_options(
        self,
        dataset_id: str,
        version_name: str,
        request: main_models.DeleteDatasetVersionLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetVersionLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keys):
            query['Keys'] = request.keys
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatasetVersionLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/versions/{DaraURL.percent_encode(version_name)}/labels',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetVersionLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_version_labels_with_options_async(
        self,
        dataset_id: str,
        version_name: str,
        request: main_models.DeleteDatasetVersionLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetVersionLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keys):
            query['Keys'] = request.keys
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatasetVersionLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/versions/{DaraURL.percent_encode(version_name)}/labels',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetVersionLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset_version_labels(
        self,
        dataset_id: str,
        version_name: str,
        request: main_models.DeleteDatasetVersionLabelsRequest,
    ) -> main_models.DeleteDatasetVersionLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_dataset_version_labels_with_options(dataset_id, version_name, request, headers, runtime)

    async def delete_dataset_version_labels_async(
        self,
        dataset_id: str,
        version_name: str,
        request: main_models.DeleteDatasetVersionLabelsRequest,
    ) -> main_models.DeleteDatasetVersionLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_dataset_version_labels_with_options_async(dataset_id, version_name, request, headers, runtime)

    def delete_experiment_with_options(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExperimentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteExperiment',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_experiment_with_options_async(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExperimentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteExperiment',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_experiment(
        self,
        experiment_id: str,
    ) -> main_models.DeleteExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_experiment_with_options(experiment_id, headers, runtime)

    async def delete_experiment_async(
        self,
        experiment_id: str,
    ) -> main_models.DeleteExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_experiment_with_options_async(experiment_id, headers, runtime)

    def delete_experiment_label_with_options(
        self,
        experiment_id: str,
        key: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExperimentLabelResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteExperimentLabel',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}/labels/{DaraURL.percent_encode(key)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExperimentLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_experiment_label_with_options_async(
        self,
        experiment_id: str,
        key: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExperimentLabelResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteExperimentLabel',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}/labels/{DaraURL.percent_encode(key)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExperimentLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_experiment_label(
        self,
        experiment_id: str,
        key: str,
    ) -> main_models.DeleteExperimentLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_experiment_label_with_options(experiment_id, key, headers, runtime)

    async def delete_experiment_label_async(
        self,
        experiment_id: str,
        key: str,
    ) -> main_models.DeleteExperimentLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_experiment_label_with_options_async(experiment_id, key, headers, runtime)

    def delete_members_with_options(
        self,
        workspace_id: str,
        request: main_models.DeleteMembersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.member_ids):
            query['MemberIds'] = request.member_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMembers',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/members',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_members_with_options_async(
        self,
        workspace_id: str,
        request: main_models.DeleteMembersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.member_ids):
            query['MemberIds'] = request.member_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMembers',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/members',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_members(
        self,
        workspace_id: str,
        request: main_models.DeleteMembersRequest,
    ) -> main_models.DeleteMembersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_members_with_options(workspace_id, request, headers, runtime)

    async def delete_members_async(
        self,
        workspace_id: str,
        request: main_models.DeleteMembersRequest,
    ) -> main_models.DeleteMembersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_members_with_options_async(workspace_id, request, headers, runtime)

    def delete_model_with_options(
        self,
        model_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteModel',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_with_options_async(
        self,
        model_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteModel',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model(
        self,
        model_id: str,
    ) -> main_models.DeleteModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_model_with_options(model_id, headers, runtime)

    async def delete_model_async(
        self,
        model_id: str,
    ) -> main_models.DeleteModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_model_with_options_async(model_id, headers, runtime)

    def delete_model_labels_with_options(
        self,
        model_id: str,
        request: main_models.DeleteModelLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.label_keys):
            query['LabelKeys'] = request.label_keys
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModelLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}/labels',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_labels_with_options_async(
        self,
        model_id: str,
        request: main_models.DeleteModelLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.label_keys):
            query['LabelKeys'] = request.label_keys
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModelLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}/labels',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model_labels(
        self,
        model_id: str,
        request: main_models.DeleteModelLabelsRequest,
    ) -> main_models.DeleteModelLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_model_labels_with_options(model_id, request, headers, runtime)

    async def delete_model_labels_async(
        self,
        model_id: str,
        request: main_models.DeleteModelLabelsRequest,
    ) -> main_models.DeleteModelLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_model_labels_with_options_async(model_id, request, headers, runtime)

    def delete_model_version_with_options(
        self,
        model_id: str,
        version_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteModelVersion',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}/versions/{DaraURL.percent_encode(version_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_version_with_options_async(
        self,
        model_id: str,
        version_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteModelVersion',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}/versions/{DaraURL.percent_encode(version_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model_version(
        self,
        model_id: str,
        version_name: str,
    ) -> main_models.DeleteModelVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_model_version_with_options(model_id, version_name, headers, runtime)

    async def delete_model_version_async(
        self,
        model_id: str,
        version_name: str,
    ) -> main_models.DeleteModelVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_model_version_with_options_async(model_id, version_name, headers, runtime)

    def delete_model_version_labels_with_options(
        self,
        model_id: str,
        version_name: str,
        request: main_models.DeleteModelVersionLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelVersionLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.label_keys):
            query['LabelKeys'] = request.label_keys
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModelVersionLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}/versions/{DaraURL.percent_encode(version_name)}/labels',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelVersionLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_version_labels_with_options_async(
        self,
        model_id: str,
        version_name: str,
        request: main_models.DeleteModelVersionLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelVersionLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.label_keys):
            query['LabelKeys'] = request.label_keys
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModelVersionLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}/versions/{DaraURL.percent_encode(version_name)}/labels',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelVersionLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model_version_labels(
        self,
        model_id: str,
        version_name: str,
        request: main_models.DeleteModelVersionLabelsRequest,
    ) -> main_models.DeleteModelVersionLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_model_version_labels_with_options(model_id, version_name, request, headers, runtime)

    async def delete_model_version_labels_async(
        self,
        model_id: str,
        version_name: str,
        request: main_models.DeleteModelVersionLabelsRequest,
    ) -> main_models.DeleteModelVersionLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_model_version_labels_with_options_async(model_id, version_name, request, headers, runtime)

    def delete_run_with_options(
        self,
        run_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRunResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteRun',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/runs/{DaraURL.percent_encode(run_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_run_with_options_async(
        self,
        run_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRunResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteRun',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/runs/{DaraURL.percent_encode(run_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_run(
        self,
        run_id: str,
    ) -> main_models.DeleteRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_run_with_options(run_id, headers, runtime)

    async def delete_run_async(
        self,
        run_id: str,
    ) -> main_models.DeleteRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_run_with_options_async(run_id, headers, runtime)

    def delete_run_label_with_options(
        self,
        run_id: str,
        key: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRunLabelResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteRunLabel',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/runs/{DaraURL.percent_encode(run_id)}/labels/{DaraURL.percent_encode(key)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRunLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_run_label_with_options_async(
        self,
        run_id: str,
        key: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRunLabelResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteRunLabel',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/runs/{DaraURL.percent_encode(run_id)}/labels/{DaraURL.percent_encode(key)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRunLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_run_label(
        self,
        run_id: str,
        key: str,
    ) -> main_models.DeleteRunLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_run_label_with_options(run_id, key, headers, runtime)

    async def delete_run_label_async(
        self,
        run_id: str,
        key: str,
    ) -> main_models.DeleteRunLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_run_label_with_options_async(run_id, key, headers, runtime)

    def delete_user_config_with_options(
        self,
        category_name: str,
        request: main_models.DeleteUserConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_key):
            query['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserConfig',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/userconfigs/{DaraURL.percent_encode(category_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_config_with_options_async(
        self,
        category_name: str,
        request: main_models.DeleteUserConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_key):
            query['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserConfig',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/userconfigs/{DaraURL.percent_encode(category_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_config(
        self,
        category_name: str,
        request: main_models.DeleteUserConfigRequest,
    ) -> main_models.DeleteUserConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_user_config_with_options(category_name, request, headers, runtime)

    async def delete_user_config_async(
        self,
        category_name: str,
        request: main_models.DeleteUserConfigRequest,
    ) -> main_models.DeleteUserConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_user_config_with_options_async(category_name, request, headers, runtime)

    def delete_workspace_with_options(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkspaceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkspace',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workspace_with_options_async(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkspaceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkspace',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workspace(
        self,
        workspace_id: str,
    ) -> main_models.DeleteWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_workspace_with_options(workspace_id, headers, runtime)

    async def delete_workspace_async(
        self,
        workspace_id: str,
    ) -> main_models.DeleteWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_workspace_with_options_async(workspace_id, headers, runtime)

    def delete_workspace_resource_with_options(
        self,
        workspace_id: str,
        request: main_models.DeleteWorkspaceResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkspaceResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkspaceResource',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/resources',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkspaceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workspace_resource_with_options_async(
        self,
        workspace_id: str,
        request: main_models.DeleteWorkspaceResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkspaceResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkspaceResource',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/resources',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkspaceResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workspace_resource(
        self,
        workspace_id: str,
        request: main_models.DeleteWorkspaceResourceRequest,
    ) -> main_models.DeleteWorkspaceResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_workspace_resource_with_options(workspace_id, request, headers, runtime)

    async def delete_workspace_resource_async(
        self,
        workspace_id: str,
        request: main_models.DeleteWorkspaceResourceRequest,
    ) -> main_models.DeleteWorkspaceResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_workspace_resource_with_options_async(workspace_id, request, headers, runtime)

    def get_code_source_with_options(
        self,
        code_source_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCodeSourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCodeSource',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/codesources/{DaraURL.percent_encode(code_source_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCodeSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_code_source_with_options_async(
        self,
        code_source_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCodeSourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCodeSource',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/codesources/{DaraURL.percent_encode(code_source_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCodeSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_code_source(
        self,
        code_source_id: str,
    ) -> main_models.GetCodeSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_code_source_with_options(code_source_id, headers, runtime)

    async def get_code_source_async(
        self,
        code_source_id: str,
    ) -> main_models.GetCodeSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_code_source_with_options_async(code_source_id, headers, runtime)

    def get_config_with_options(
        self,
        workspace_id: str,
        request: main_models.GetConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_name):
            query['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.config_key):
            query['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConfig',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_config_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_name):
            query['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.config_key):
            query['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConfig',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_config(
        self,
        workspace_id: str,
        request: main_models.GetConfigRequest,
    ) -> main_models.GetConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_config_with_options(workspace_id, request, headers, runtime)

    async def get_config_async(
        self,
        workspace_id: str,
        request: main_models.GetConfigRequest,
    ) -> main_models.GetConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_config_with_options_async(workspace_id, request, headers, runtime)

    def get_connection_with_options(
        self,
        connection_id: str,
        request: main_models.GetConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypt_option):
            query['EncryptOption'] = request.encrypt_option
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConnection',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/connections/{DaraURL.percent_encode(connection_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_connection_with_options_async(
        self,
        connection_id: str,
        request: main_models.GetConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypt_option):
            query['EncryptOption'] = request.encrypt_option
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConnection',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/connections/{DaraURL.percent_encode(connection_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_connection(
        self,
        connection_id: str,
        request: main_models.GetConnectionRequest,
    ) -> main_models.GetConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_connection_with_options(connection_id, request, headers, runtime)

    async def get_connection_async(
        self,
        connection_id: str,
        request: main_models.GetConnectionRequest,
    ) -> main_models.GetConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_connection_with_options_async(connection_id, request, headers, runtime)

    def get_dataset_with_options(
        self,
        dataset_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDataset',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_with_options_async(
        self,
        dataset_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDataset',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset(
        self,
        dataset_id: str,
    ) -> main_models.GetDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_dataset_with_options(dataset_id, headers, runtime)

    async def get_dataset_async(
        self,
        dataset_id: str,
    ) -> main_models.GetDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_dataset_with_options_async(dataset_id, headers, runtime)

    def get_dataset_file_meta_with_options(
        self,
        dataset_id: str,
        dataset_file_meta_id: str,
        request: main_models.GetDatasetFileMetaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetFileMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatasetFileMeta',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetfilemetas/{DaraURL.percent_encode(dataset_file_meta_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_file_meta_with_options_async(
        self,
        dataset_id: str,
        dataset_file_meta_id: str,
        request: main_models.GetDatasetFileMetaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetFileMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatasetFileMeta',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetfilemetas/{DaraURL.percent_encode(dataset_file_meta_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset_file_meta(
        self,
        dataset_id: str,
        dataset_file_meta_id: str,
        request: main_models.GetDatasetFileMetaRequest,
    ) -> main_models.GetDatasetFileMetaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_dataset_file_meta_with_options(dataset_id, dataset_file_meta_id, request, headers, runtime)

    async def get_dataset_file_meta_async(
        self,
        dataset_id: str,
        dataset_file_meta_id: str,
        request: main_models.GetDatasetFileMetaRequest,
    ) -> main_models.GetDatasetFileMetaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_dataset_file_meta_with_options_async(dataset_id, dataset_file_meta_id, request, headers, runtime)

    def get_dataset_file_metas_statistics_with_options(
        self,
        dataset_id: str,
        request: main_models.GetDatasetFileMetasStatisticsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetFileMetasStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregate_by):
            query['AggregateBy'] = request.aggregate_by
        if not DaraCore.is_null(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatasetFileMetasStatistics',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/statistics/datasets/{DaraURL.percent_encode(dataset_id)}/datasetfilemetas',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetFileMetasStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_file_metas_statistics_with_options_async(
        self,
        dataset_id: str,
        request: main_models.GetDatasetFileMetasStatisticsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetFileMetasStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregate_by):
            query['AggregateBy'] = request.aggregate_by
        if not DaraCore.is_null(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatasetFileMetasStatistics',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/statistics/datasets/{DaraURL.percent_encode(dataset_id)}/datasetfilemetas',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetFileMetasStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset_file_metas_statistics(
        self,
        dataset_id: str,
        request: main_models.GetDatasetFileMetasStatisticsRequest,
    ) -> main_models.GetDatasetFileMetasStatisticsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_dataset_file_metas_statistics_with_options(dataset_id, request, headers, runtime)

    async def get_dataset_file_metas_statistics_async(
        self,
        dataset_id: str,
        request: main_models.GetDatasetFileMetasStatisticsRequest,
    ) -> main_models.GetDatasetFileMetasStatisticsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_dataset_file_metas_statistics_with_options_async(dataset_id, request, headers, runtime)

    def get_dataset_job_with_options(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: main_models.GetDatasetJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatasetJob',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobs/{DaraURL.percent_encode(dataset_job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_job_with_options_async(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: main_models.GetDatasetJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatasetJob',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobs/{DaraURL.percent_encode(dataset_job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset_job(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: main_models.GetDatasetJobRequest,
    ) -> main_models.GetDatasetJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_dataset_job_with_options(dataset_id, dataset_job_id, request, headers, runtime)

    async def get_dataset_job_async(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: main_models.GetDatasetJobRequest,
    ) -> main_models.GetDatasetJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_dataset_job_with_options_async(dataset_id, dataset_job_id, request, headers, runtime)

    def get_dataset_job_config_with_options(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: main_models.GetDatasetJobConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetJobConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatasetJobConfig',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobconfigs/{DaraURL.percent_encode(dataset_job_config_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_job_config_with_options_async(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: main_models.GetDatasetJobConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetJobConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatasetJobConfig',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobconfigs/{DaraURL.percent_encode(dataset_job_config_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetJobConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset_job_config(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: main_models.GetDatasetJobConfigRequest,
    ) -> main_models.GetDatasetJobConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_dataset_job_config_with_options(dataset_id, dataset_job_config_id, request, headers, runtime)

    async def get_dataset_job_config_async(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: main_models.GetDatasetJobConfigRequest,
    ) -> main_models.GetDatasetJobConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_dataset_job_config_with_options_async(dataset_id, dataset_job_config_id, request, headers, runtime)

    def get_dataset_version_with_options(
        self,
        dataset_id: str,
        version_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDatasetVersion',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/versions/{DaraURL.percent_encode(version_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_version_with_options_async(
        self,
        dataset_id: str,
        version_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDatasetVersion',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/versions/{DaraURL.percent_encode(version_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset_version(
        self,
        dataset_id: str,
        version_name: str,
    ) -> main_models.GetDatasetVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_dataset_version_with_options(dataset_id, version_name, headers, runtime)

    async def get_dataset_version_async(
        self,
        dataset_id: str,
        version_name: str,
    ) -> main_models.GetDatasetVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_dataset_version_with_options_async(dataset_id, version_name, headers, runtime)

    def get_default_workspace_with_options(
        self,
        request: main_models.GetDefaultWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDefaultWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDefaultWorkspace',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/defaultWorkspaces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDefaultWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_default_workspace_with_options_async(
        self,
        request: main_models.GetDefaultWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDefaultWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDefaultWorkspace',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/defaultWorkspaces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDefaultWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_default_workspace(
        self,
        request: main_models.GetDefaultWorkspaceRequest,
    ) -> main_models.GetDefaultWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_default_workspace_with_options(request, headers, runtime)

    async def get_default_workspace_async(
        self,
        request: main_models.GetDefaultWorkspaceRequest,
    ) -> main_models.GetDefaultWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_default_workspace_with_options_async(request, headers, runtime)

    def get_experiment_with_options(
        self,
        experiment_id: str,
        request: main_models.GetExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetExperimentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExperiment',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_experiment_with_options_async(
        self,
        experiment_id: str,
        request: main_models.GetExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetExperimentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExperiment',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_experiment(
        self,
        experiment_id: str,
        request: main_models.GetExperimentRequest,
    ) -> main_models.GetExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_experiment_with_options(experiment_id, request, headers, runtime)

    async def get_experiment_async(
        self,
        experiment_id: str,
        request: main_models.GetExperimentRequest,
    ) -> main_models.GetExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_experiment_with_options_async(experiment_id, request, headers, runtime)

    def get_image_with_options(
        self,
        image_id: str,
        request: main_models.GetImageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImage',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/images/{DaraURL.percent_encode(image_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_with_options_async(
        self,
        image_id: str,
        request: main_models.GetImageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImage',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/images/{DaraURL.percent_encode(image_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image(
        self,
        image_id: str,
        request: main_models.GetImageRequest,
    ) -> main_models.GetImageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_image_with_options(image_id, request, headers, runtime)

    async def get_image_async(
        self,
        image_id: str,
        request: main_models.GetImageRequest,
    ) -> main_models.GetImageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_image_with_options_async(image_id, request, headers, runtime)

    def get_member_with_options(
        self,
        workspace_id: str,
        request: main_models.GetMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.member_id):
            query['MemberId'] = request.member_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMember',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/member',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_member_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.member_id):
            query['MemberId'] = request.member_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMember',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/member',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_member(
        self,
        workspace_id: str,
        request: main_models.GetMemberRequest,
    ) -> main_models.GetMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_member_with_options(workspace_id, request, headers, runtime)

    async def get_member_async(
        self,
        workspace_id: str,
        request: main_models.GetMemberRequest,
    ) -> main_models.GetMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_member_with_options_async(workspace_id, request, headers, runtime)

    def get_model_with_options(
        self,
        model_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModel',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_with_options_async(
        self,
        model_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModel',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model(
        self,
        model_id: str,
    ) -> main_models.GetModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_model_with_options(model_id, headers, runtime)

    async def get_model_async(
        self,
        model_id: str,
    ) -> main_models.GetModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_model_with_options_async(model_id, headers, runtime)

    def get_model_version_with_options(
        self,
        model_id: str,
        version_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModelVersion',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}/versions/{DaraURL.percent_encode(version_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_version_with_options_async(
        self,
        model_id: str,
        version_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModelVersion',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}/versions/{DaraURL.percent_encode(version_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_version(
        self,
        model_id: str,
        version_name: str,
    ) -> main_models.GetModelVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_model_version_with_options(model_id, version_name, headers, runtime)

    async def get_model_version_async(
        self,
        model_id: str,
        version_name: str,
    ) -> main_models.GetModelVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_model_version_with_options_async(model_id, version_name, headers, runtime)

    def get_permission_with_options(
        self,
        workspace_id: str,
        permission_code: str,
        tmp_req: main_models.GetPermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPermissionResponse:
        tmp_req.validate()
        request = main_models.GetPermissionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.labels):
            request.labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        query = {}
        if not DaraCore.is_null(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.creator):
            query['Creator'] = request.creator
        if not DaraCore.is_null(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPermission',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/permissions/{DaraURL.percent_encode(permission_code)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_permission_with_options_async(
        self,
        workspace_id: str,
        permission_code: str,
        tmp_req: main_models.GetPermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPermissionResponse:
        tmp_req.validate()
        request = main_models.GetPermissionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.labels):
            request.labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        query = {}
        if not DaraCore.is_null(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.creator):
            query['Creator'] = request.creator
        if not DaraCore.is_null(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPermission',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/permissions/{DaraURL.percent_encode(permission_code)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_permission(
        self,
        workspace_id: str,
        permission_code: str,
        request: main_models.GetPermissionRequest,
    ) -> main_models.GetPermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_permission_with_options(workspace_id, permission_code, request, headers, runtime)

    async def get_permission_async(
        self,
        workspace_id: str,
        permission_code: str,
        request: main_models.GetPermissionRequest,
    ) -> main_models.GetPermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_permission_with_options_async(workspace_id, permission_code, request, headers, runtime)

    def get_run_with_options(
        self,
        run_id: str,
        request: main_models.GetRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRunResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRun',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/runs/{DaraURL.percent_encode(run_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_run_with_options_async(
        self,
        run_id: str,
        request: main_models.GetRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRunResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRun',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/runs/{DaraURL.percent_encode(run_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_run(
        self,
        run_id: str,
        request: main_models.GetRunRequest,
    ) -> main_models.GetRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_run_with_options(run_id, request, headers, runtime)

    async def get_run_async(
        self,
        run_id: str,
        request: main_models.GetRunRequest,
    ) -> main_models.GetRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_run_with_options_async(run_id, request, headers, runtime)

    def get_workspace_with_options(
        self,
        workspace_id: str,
        request: main_models.GetWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkspace',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workspace_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkspace',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workspace(
        self,
        workspace_id: str,
        request: main_models.GetWorkspaceRequest,
    ) -> main_models.GetWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_workspace_with_options(workspace_id, request, headers, runtime)

    async def get_workspace_async(
        self,
        workspace_id: str,
        request: main_models.GetWorkspaceRequest,
    ) -> main_models.GetWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_workspace_with_options_async(workspace_id, request, headers, runtime)

    def list_code_sources_with_options(
        self,
        request: main_models.ListCodeSourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCodeSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCodeSources',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/codesources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCodeSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_code_sources_with_options_async(
        self,
        request: main_models.ListCodeSourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCodeSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCodeSources',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/codesources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCodeSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_code_sources(
        self,
        request: main_models.ListCodeSourcesRequest,
    ) -> main_models.ListCodeSourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_code_sources_with_options(request, headers, runtime)

    async def list_code_sources_async(
        self,
        request: main_models.ListCodeSourcesRequest,
    ) -> main_models.ListCodeSourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_code_sources_with_options_async(request, headers, runtime)

    def list_configs_with_options(
        self,
        workspace_id: str,
        request: main_models.ListConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_name):
            query['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.config_keys):
            query['ConfigKeys'] = request.config_keys
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConfigs',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/configs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_configs_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_name):
            query['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.config_keys):
            query['ConfigKeys'] = request.config_keys
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConfigs',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/configs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_configs(
        self,
        workspace_id: str,
        request: main_models.ListConfigsRequest,
    ) -> main_models.ListConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_configs_with_options(workspace_id, request, headers, runtime)

    async def list_configs_async(
        self,
        workspace_id: str,
        request: main_models.ListConfigsRequest,
    ) -> main_models.ListConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_configs_with_options_async(workspace_id, request, headers, runtime)

    def list_connections_with_options(
        self,
        tmp_req: main_models.ListConnectionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConnectionsResponse:
        tmp_req.validate()
        request = main_models.ListConnectionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.connection_ids):
            request.connection_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.connection_ids, 'ConnectionIds', 'simple')
        if not DaraCore.is_null(tmp_req.connection_types):
            request.connection_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.connection_types, 'ConnectionTypes', 'simple')
        if not DaraCore.is_null(tmp_req.model_types):
            request.model_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.model_types, 'ModelTypes', 'simple')
        query = {}
        if not DaraCore.is_null(request.connection_ids_shrink):
            query['ConnectionIds'] = request.connection_ids_shrink
        if not DaraCore.is_null(request.connection_name):
            query['ConnectionName'] = request.connection_name
        if not DaraCore.is_null(request.connection_types_shrink):
            query['ConnectionTypes'] = request.connection_types_shrink
        if not DaraCore.is_null(request.creator):
            query['Creator'] = request.creator
        if not DaraCore.is_null(request.encrypt_option):
            query['EncryptOption'] = request.encrypt_option
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.model_types_shrink):
            query['ModelTypes'] = request.model_types_shrink
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.tool_call):
            query['ToolCall'] = request.tool_call
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConnections',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/connections',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_connections_with_options_async(
        self,
        tmp_req: main_models.ListConnectionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConnectionsResponse:
        tmp_req.validate()
        request = main_models.ListConnectionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.connection_ids):
            request.connection_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.connection_ids, 'ConnectionIds', 'simple')
        if not DaraCore.is_null(tmp_req.connection_types):
            request.connection_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.connection_types, 'ConnectionTypes', 'simple')
        if not DaraCore.is_null(tmp_req.model_types):
            request.model_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.model_types, 'ModelTypes', 'simple')
        query = {}
        if not DaraCore.is_null(request.connection_ids_shrink):
            query['ConnectionIds'] = request.connection_ids_shrink
        if not DaraCore.is_null(request.connection_name):
            query['ConnectionName'] = request.connection_name
        if not DaraCore.is_null(request.connection_types_shrink):
            query['ConnectionTypes'] = request.connection_types_shrink
        if not DaraCore.is_null(request.creator):
            query['Creator'] = request.creator
        if not DaraCore.is_null(request.encrypt_option):
            query['EncryptOption'] = request.encrypt_option
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.model_types_shrink):
            query['ModelTypes'] = request.model_types_shrink
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.tool_call):
            query['ToolCall'] = request.tool_call
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConnections',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/connections',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConnectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_connections(
        self,
        request: main_models.ListConnectionsRequest,
    ) -> main_models.ListConnectionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_connections_with_options(request, headers, runtime)

    async def list_connections_async(
        self,
        request: main_models.ListConnectionsRequest,
    ) -> main_models.ListConnectionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_connections_with_options_async(request, headers, runtime)

    def list_dataset_file_metas_with_options(
        self,
        dataset_id: str,
        tmp_req: main_models.ListDatasetFileMetasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetFileMetasResponse:
        tmp_req.validate()
        request = main_models.ListDatasetFileMetasShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.query_content_type_include_any):
            request.query_content_type_include_any_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_content_type_include_any, 'QueryContentTypeIncludeAny', 'simple')
        if not DaraCore.is_null(tmp_req.query_file_type_include_any):
            request.query_file_type_include_any_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_file_type_include_any, 'QueryFileTypeIncludeAny', 'simple')
        if not DaraCore.is_null(tmp_req.query_tags_exclude):
            request.query_tags_exclude_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_tags_exclude, 'QueryTagsExclude', 'simple')
        if not DaraCore.is_null(tmp_req.query_tags_include_all):
            request.query_tags_include_all_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_tags_include_all, 'QueryTagsIncludeAll', 'simple')
        if not DaraCore.is_null(tmp_req.query_tags_include_any):
            request.query_tags_include_any_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_tags_include_any, 'QueryTagsIncludeAny', 'simple')
        query = {}
        if not DaraCore.is_null(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.end_file_update_time):
            query['EndFileUpdateTime'] = request.end_file_update_time
        if not DaraCore.is_null(request.end_tag_update_time):
            query['EndTagUpdateTime'] = request.end_tag_update_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_content_type_include_any_shrink):
            query['QueryContentTypeIncludeAny'] = request.query_content_type_include_any_shrink
        if not DaraCore.is_null(request.query_expression):
            query['QueryExpression'] = request.query_expression
        if not DaraCore.is_null(request.query_file_dir):
            query['QueryFileDir'] = request.query_file_dir
        if not DaraCore.is_null(request.query_file_name):
            query['QueryFileName'] = request.query_file_name
        if not DaraCore.is_null(request.query_file_type_include_any_shrink):
            query['QueryFileTypeIncludeAny'] = request.query_file_type_include_any_shrink
        if not DaraCore.is_null(request.query_image):
            query['QueryImage'] = request.query_image
        if not DaraCore.is_null(request.query_tags_exclude_shrink):
            query['QueryTagsExclude'] = request.query_tags_exclude_shrink
        if not DaraCore.is_null(request.query_tags_include_all_shrink):
            query['QueryTagsIncludeAll'] = request.query_tags_include_all_shrink
        if not DaraCore.is_null(request.query_tags_include_any_shrink):
            query['QueryTagsIncludeAny'] = request.query_tags_include_any_shrink
        if not DaraCore.is_null(request.query_text):
            query['QueryText'] = request.query_text
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.query_video):
            query['QueryVideo'] = request.query_video
        if not DaraCore.is_null(request.score_threshold):
            query['ScoreThreshold'] = request.score_threshold
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_file_update_time):
            query['StartFileUpdateTime'] = request.start_file_update_time
        if not DaraCore.is_null(request.start_tag_update_time):
            query['StartTagUpdateTime'] = request.start_tag_update_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.thumbnail_mode):
            query['ThumbnailMode'] = request.thumbnail_mode
        if not DaraCore.is_null(request.top_k):
            query['TopK'] = request.top_k
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasetFileMetas',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetfilemetas',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetFileMetasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dataset_file_metas_with_options_async(
        self,
        dataset_id: str,
        tmp_req: main_models.ListDatasetFileMetasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetFileMetasResponse:
        tmp_req.validate()
        request = main_models.ListDatasetFileMetasShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.query_content_type_include_any):
            request.query_content_type_include_any_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_content_type_include_any, 'QueryContentTypeIncludeAny', 'simple')
        if not DaraCore.is_null(tmp_req.query_file_type_include_any):
            request.query_file_type_include_any_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_file_type_include_any, 'QueryFileTypeIncludeAny', 'simple')
        if not DaraCore.is_null(tmp_req.query_tags_exclude):
            request.query_tags_exclude_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_tags_exclude, 'QueryTagsExclude', 'simple')
        if not DaraCore.is_null(tmp_req.query_tags_include_all):
            request.query_tags_include_all_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_tags_include_all, 'QueryTagsIncludeAll', 'simple')
        if not DaraCore.is_null(tmp_req.query_tags_include_any):
            request.query_tags_include_any_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_tags_include_any, 'QueryTagsIncludeAny', 'simple')
        query = {}
        if not DaraCore.is_null(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.end_file_update_time):
            query['EndFileUpdateTime'] = request.end_file_update_time
        if not DaraCore.is_null(request.end_tag_update_time):
            query['EndTagUpdateTime'] = request.end_tag_update_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_content_type_include_any_shrink):
            query['QueryContentTypeIncludeAny'] = request.query_content_type_include_any_shrink
        if not DaraCore.is_null(request.query_expression):
            query['QueryExpression'] = request.query_expression
        if not DaraCore.is_null(request.query_file_dir):
            query['QueryFileDir'] = request.query_file_dir
        if not DaraCore.is_null(request.query_file_name):
            query['QueryFileName'] = request.query_file_name
        if not DaraCore.is_null(request.query_file_type_include_any_shrink):
            query['QueryFileTypeIncludeAny'] = request.query_file_type_include_any_shrink
        if not DaraCore.is_null(request.query_image):
            query['QueryImage'] = request.query_image
        if not DaraCore.is_null(request.query_tags_exclude_shrink):
            query['QueryTagsExclude'] = request.query_tags_exclude_shrink
        if not DaraCore.is_null(request.query_tags_include_all_shrink):
            query['QueryTagsIncludeAll'] = request.query_tags_include_all_shrink
        if not DaraCore.is_null(request.query_tags_include_any_shrink):
            query['QueryTagsIncludeAny'] = request.query_tags_include_any_shrink
        if not DaraCore.is_null(request.query_text):
            query['QueryText'] = request.query_text
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.query_video):
            query['QueryVideo'] = request.query_video
        if not DaraCore.is_null(request.score_threshold):
            query['ScoreThreshold'] = request.score_threshold
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_file_update_time):
            query['StartFileUpdateTime'] = request.start_file_update_time
        if not DaraCore.is_null(request.start_tag_update_time):
            query['StartTagUpdateTime'] = request.start_tag_update_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.thumbnail_mode):
            query['ThumbnailMode'] = request.thumbnail_mode
        if not DaraCore.is_null(request.top_k):
            query['TopK'] = request.top_k
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasetFileMetas',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetfilemetas',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetFileMetasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dataset_file_metas(
        self,
        dataset_id: str,
        request: main_models.ListDatasetFileMetasRequest,
    ) -> main_models.ListDatasetFileMetasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_dataset_file_metas_with_options(dataset_id, request, headers, runtime)

    async def list_dataset_file_metas_async(
        self,
        dataset_id: str,
        request: main_models.ListDatasetFileMetasRequest,
    ) -> main_models.ListDatasetFileMetasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_dataset_file_metas_with_options_async(dataset_id, request, headers, runtime)

    def list_dataset_job_configs_with_options(
        self,
        dataset_id: str,
        request: main_models.ListDatasetJobConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetJobConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_type):
            query['ConfigType'] = request.config_type
        if not DaraCore.is_null(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasetJobConfigs',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobconfigs/',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetJobConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dataset_job_configs_with_options_async(
        self,
        dataset_id: str,
        request: main_models.ListDatasetJobConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetJobConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_type):
            query['ConfigType'] = request.config_type
        if not DaraCore.is_null(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasetJobConfigs',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobconfigs/',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetJobConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dataset_job_configs(
        self,
        dataset_id: str,
        request: main_models.ListDatasetJobConfigsRequest,
    ) -> main_models.ListDatasetJobConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_dataset_job_configs_with_options(dataset_id, request, headers, runtime)

    async def list_dataset_job_configs_async(
        self,
        dataset_id: str,
        request: main_models.ListDatasetJobConfigsRequest,
    ) -> main_models.ListDatasetJobConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_dataset_job_configs_with_options_async(dataset_id, request, headers, runtime)

    def list_dataset_jobs_with_options(
        self,
        dataset_id: str,
        request: main_models.ListDatasetJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.job_action):
            query['JobAction'] = request.job_action
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasetJobs',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dataset_jobs_with_options_async(
        self,
        dataset_id: str,
        request: main_models.ListDatasetJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.job_action):
            query['JobAction'] = request.job_action
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasetJobs',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dataset_jobs(
        self,
        dataset_id: str,
        request: main_models.ListDatasetJobsRequest,
    ) -> main_models.ListDatasetJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_dataset_jobs_with_options(dataset_id, request, headers, runtime)

    async def list_dataset_jobs_async(
        self,
        dataset_id: str,
        request: main_models.ListDatasetJobsRequest,
    ) -> main_models.ListDatasetJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_dataset_jobs_with_options_async(dataset_id, request, headers, runtime)

    def list_dataset_versions_with_options(
        self,
        dataset_id: str,
        request: main_models.ListDatasetVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.label_keys):
            query['LabelKeys'] = request.label_keys
        if not DaraCore.is_null(request.label_values):
            query['LabelValues'] = request.label_values
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.properties):
            query['Properties'] = request.properties
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_types):
            query['SourceTypes'] = request.source_types
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasetVersions',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dataset_versions_with_options_async(
        self,
        dataset_id: str,
        request: main_models.ListDatasetVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.label_keys):
            query['LabelKeys'] = request.label_keys
        if not DaraCore.is_null(request.label_values):
            query['LabelValues'] = request.label_values
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.properties):
            query['Properties'] = request.properties
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_types):
            query['SourceTypes'] = request.source_types
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasetVersions',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dataset_versions(
        self,
        dataset_id: str,
        request: main_models.ListDatasetVersionsRequest,
    ) -> main_models.ListDatasetVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_dataset_versions_with_options(dataset_id, request, headers, runtime)

    async def list_dataset_versions_async(
        self,
        dataset_id: str,
        request: main_models.ListDatasetVersionsRequest,
    ) -> main_models.ListDatasetVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_dataset_versions_with_options_async(dataset_id, request, headers, runtime)

    def list_datasets_with_options(
        self,
        request: main_models.ListDatasetsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.data_source_types):
            query['DataSourceTypes'] = request.data_source_types
        if not DaraCore.is_null(request.data_types):
            query['DataTypes'] = request.data_types
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.label):
            query['Label'] = request.label
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.properties):
            query['Properties'] = request.properties
        if not DaraCore.is_null(request.provider):
            query['Provider'] = request.provider
        if not DaraCore.is_null(request.share_scope):
            query['ShareScope'] = request.share_scope
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.source_dataset_id):
            query['SourceDatasetId'] = request.source_dataset_id
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_types):
            query['SourceTypes'] = request.source_types
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasets',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_datasets_with_options_async(
        self,
        request: main_models.ListDatasetsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.data_source_types):
            query['DataSourceTypes'] = request.data_source_types
        if not DaraCore.is_null(request.data_types):
            query['DataTypes'] = request.data_types
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.label):
            query['Label'] = request.label
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.properties):
            query['Properties'] = request.properties
        if not DaraCore.is_null(request.provider):
            query['Provider'] = request.provider
        if not DaraCore.is_null(request.share_scope):
            query['ShareScope'] = request.share_scope
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.source_dataset_id):
            query['SourceDatasetId'] = request.source_dataset_id
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_types):
            query['SourceTypes'] = request.source_types
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasets',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_datasets(
        self,
        request: main_models.ListDatasetsRequest,
    ) -> main_models.ListDatasetsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_datasets_with_options(request, headers, runtime)

    async def list_datasets_async(
        self,
        request: main_models.ListDatasetsRequest,
    ) -> main_models.ListDatasetsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_datasets_with_options_async(request, headers, runtime)

    def list_experiment_with_options(
        self,
        tmp_req: main_models.ListExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExperimentResponse:
        tmp_req.validate()
        request = main_models.ListExperimentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.options):
            request.options_shrink = Utils.array_to_string_with_specified_style(tmp_req.options, 'Options', 'json')
        query = {}
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.options_shrink):
            query['Options'] = request.options_shrink
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.page_token):
            query['PageToken'] = request.page_token
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExperiment',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_experiment_with_options_async(
        self,
        tmp_req: main_models.ListExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExperimentResponse:
        tmp_req.validate()
        request = main_models.ListExperimentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.options):
            request.options_shrink = Utils.array_to_string_with_specified_style(tmp_req.options, 'Options', 'json')
        query = {}
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.options_shrink):
            query['Options'] = request.options_shrink
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.page_token):
            query['PageToken'] = request.page_token
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExperiment',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_experiment(
        self,
        request: main_models.ListExperimentRequest,
    ) -> main_models.ListExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_experiment_with_options(request, headers, runtime)

    async def list_experiment_async(
        self,
        request: main_models.ListExperimentRequest,
    ) -> main_models.ListExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_experiment_with_options_async(request, headers, runtime)

    def list_features_with_options(
        self,
        request: main_models.ListFeaturesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFeaturesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.names):
            query['Names'] = request.names
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFeatures',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/features',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_features_with_options_async(
        self,
        request: main_models.ListFeaturesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFeaturesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.names):
            query['Names'] = request.names
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFeatures',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/features',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_features(
        self,
        request: main_models.ListFeaturesRequest,
    ) -> main_models.ListFeaturesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_features_with_options(request, headers, runtime)

    async def list_features_async(
        self,
        request: main_models.ListFeaturesRequest,
    ) -> main_models.ListFeaturesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_features_with_options_async(request, headers, runtime)

    def list_image_labels_with_options(
        self,
        request: main_models.ListImageLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListImageLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.label_filter):
            query['LabelFilter'] = request.label_filter
        if not DaraCore.is_null(request.label_keys):
            query['LabelKeys'] = request.label_keys
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListImageLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/image/labels',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListImageLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_image_labels_with_options_async(
        self,
        request: main_models.ListImageLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListImageLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.label_filter):
            query['LabelFilter'] = request.label_filter
        if not DaraCore.is_null(request.label_keys):
            query['LabelKeys'] = request.label_keys
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListImageLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/image/labels',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListImageLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_image_labels(
        self,
        request: main_models.ListImageLabelsRequest,
    ) -> main_models.ListImageLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_image_labels_with_options(request, headers, runtime)

    async def list_image_labels_async(
        self,
        request: main_models.ListImageLabelsRequest,
    ) -> main_models.ListImageLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_image_labels_with_options_async(request, headers, runtime)

    def list_images_with_options(
        self,
        request: main_models.ListImagesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListImagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListImages',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/images',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_images_with_options_async(
        self,
        request: main_models.ListImagesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListImagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListImages',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/images',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_images(
        self,
        request: main_models.ListImagesRequest,
    ) -> main_models.ListImagesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_images_with_options(request, headers, runtime)

    async def list_images_async(
        self,
        request: main_models.ListImagesRequest,
    ) -> main_models.ListImagesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_images_with_options_async(request, headers, runtime)

    def list_members_with_options(
        self,
        workspace_id: str,
        request: main_models.ListMembersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.member_name):
            query['MemberName'] = request.member_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.roles):
            query['Roles'] = request.roles
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMembers',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/members',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_members_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListMembersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.member_name):
            query['MemberName'] = request.member_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.roles):
            query['Roles'] = request.roles
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMembers',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/members',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_members(
        self,
        workspace_id: str,
        request: main_models.ListMembersRequest,
    ) -> main_models.ListMembersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_members_with_options(workspace_id, request, headers, runtime)

    async def list_members_async(
        self,
        workspace_id: str,
        request: main_models.ListMembersRequest,
    ) -> main_models.ListMembersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_members_with_options_async(workspace_id, request, headers, runtime)

    def list_model_versions_with_options(
        self,
        model_id: str,
        request: main_models.ListModelVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.approval_status):
            query['ApprovalStatus'] = request.approval_status
        if not DaraCore.is_null(request.format_type):
            query['FormatType'] = request.format_type
        if not DaraCore.is_null(request.framework_type):
            query['FrameworkType'] = request.framework_type
        if not DaraCore.is_null(request.label):
            query['Label'] = request.label
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelVersions',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_versions_with_options_async(
        self,
        model_id: str,
        request: main_models.ListModelVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.approval_status):
            query['ApprovalStatus'] = request.approval_status
        if not DaraCore.is_null(request.format_type):
            query['FormatType'] = request.format_type
        if not DaraCore.is_null(request.framework_type):
            query['FrameworkType'] = request.framework_type
        if not DaraCore.is_null(request.label):
            query['Label'] = request.label
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelVersions',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_versions(
        self,
        model_id: str,
        request: main_models.ListModelVersionsRequest,
    ) -> main_models.ListModelVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_model_versions_with_options(model_id, request, headers, runtime)

    async def list_model_versions_async(
        self,
        model_id: str,
        request: main_models.ListModelVersionsRequest,
    ) -> main_models.ListModelVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_model_versions_with_options_async(model_id, request, headers, runtime)

    def list_models_with_options(
        self,
        tmp_req: main_models.ListModelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelsResponse:
        tmp_req.validate()
        request = main_models.ListModelsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.conditions):
            request.conditions_shrink = Utils.array_to_string_with_specified_style(tmp_req.conditions, 'Conditions', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.collections):
            query['Collections'] = request.collections
        if not DaraCore.is_null(request.conditions_shrink):
            query['Conditions'] = request.conditions_shrink
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.label):
            query['Label'] = request.label
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.model_type):
            query['ModelType'] = request.model_type
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.origin):
            query['Origin'] = request.origin
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.provider):
            query['Provider'] = request.provider
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not DaraCore.is_null(request.task):
            query['Task'] = request.task
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_models_with_options_async(
        self,
        tmp_req: main_models.ListModelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelsResponse:
        tmp_req.validate()
        request = main_models.ListModelsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.conditions):
            request.conditions_shrink = Utils.array_to_string_with_specified_style(tmp_req.conditions, 'Conditions', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.collections):
            query['Collections'] = request.collections
        if not DaraCore.is_null(request.conditions_shrink):
            query['Conditions'] = request.conditions_shrink
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.label):
            query['Label'] = request.label
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.model_type):
            query['ModelType'] = request.model_type
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.origin):
            query['Origin'] = request.origin
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.provider):
            query['Provider'] = request.provider
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not DaraCore.is_null(request.task):
            query['Task'] = request.task
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_models(
        self,
        request: main_models.ListModelsRequest,
    ) -> main_models.ListModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_models_with_options(request, headers, runtime)

    async def list_models_async(
        self,
        request: main_models.ListModelsRequest,
    ) -> main_models.ListModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_models_with_options_async(request, headers, runtime)

    def list_permissions_with_options(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPermissionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListPermissions',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/permissions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_permissions_with_options_async(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPermissionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListPermissions',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/permissions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_permissions(
        self,
        workspace_id: str,
    ) -> main_models.ListPermissionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_permissions_with_options(workspace_id, headers, runtime)

    async def list_permissions_async(
        self,
        workspace_id: str,
    ) -> main_models.ListPermissionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_permissions_with_options_async(workspace_id, headers, runtime)

    def list_products_with_options(
        self,
        request: main_models.ListProductsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_codes):
            query['ProductCodes'] = request.product_codes
        if not DaraCore.is_null(request.service_codes):
            query['ServiceCodes'] = request.service_codes
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProducts',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/products',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_products_with_options_async(
        self,
        request: main_models.ListProductsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_codes):
            query['ProductCodes'] = request.product_codes
        if not DaraCore.is_null(request.service_codes):
            query['ServiceCodes'] = request.service_codes
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProducts',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/products',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_products(
        self,
        request: main_models.ListProductsRequest,
    ) -> main_models.ListProductsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_products_with_options(request, headers, runtime)

    async def list_products_async(
        self,
        request: main_models.ListProductsRequest,
    ) -> main_models.ListProductsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_products_with_options_async(request, headers, runtime)

    def list_quotas_with_options(
        self,
        request: main_models.ListQuotasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotas',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quotas_with_options_async(
        self,
        request: main_models.ListQuotasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotas',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quotas(
        self,
        request: main_models.ListQuotasRequest,
    ) -> main_models.ListQuotasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_quotas_with_options(request, headers, runtime)

    async def list_quotas_async(
        self,
        request: main_models.ListQuotasRequest,
    ) -> main_models.ListQuotasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_quotas_with_options_async(request, headers, runtime)

    def list_resources_with_options(
        self,
        request: main_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_types):
            query['ProductTypes'] = request.product_types
        if not DaraCore.is_null(request.quota_ids):
            query['QuotaIds'] = request.quota_ids
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.verbose_fields):
            query['VerboseFields'] = request.verbose_fields
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResources',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_with_options_async(
        self,
        request: main_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_types):
            query['ProductTypes'] = request.product_types
        if not DaraCore.is_null(request.quota_ids):
            query['QuotaIds'] = request.quota_ids
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.verbose_fields):
            query['VerboseFields'] = request.verbose_fields
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResources',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources(
        self,
        request: main_models.ListResourcesRequest,
    ) -> main_models.ListResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_resources_with_options(request, headers, runtime)

    async def list_resources_async(
        self,
        request: main_models.ListResourcesRequest,
    ) -> main_models.ListResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_resources_with_options_async(request, headers, runtime)

    def list_run_metrics_with_options(
        self,
        run_id: str,
        request: main_models.ListRunMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRunMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['PageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRunMetrics',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/runs/{DaraURL.percent_encode(run_id)}/metrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRunMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_run_metrics_with_options_async(
        self,
        run_id: str,
        request: main_models.ListRunMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRunMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['PageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRunMetrics',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/runs/{DaraURL.percent_encode(run_id)}/metrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRunMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_run_metrics(
        self,
        run_id: str,
        request: main_models.ListRunMetricsRequest,
    ) -> main_models.ListRunMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_run_metrics_with_options(run_id, request, headers, runtime)

    async def list_run_metrics_async(
        self,
        run_id: str,
        request: main_models.ListRunMetricsRequest,
    ) -> main_models.ListRunMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_run_metrics_with_options_async(run_id, request, headers, runtime)

    def list_runs_with_options(
        self,
        request: main_models.ListRunsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRunsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not DaraCore.is_null(request.gmt_create_time):
            query['GmtCreateTime'] = request.gmt_create_time
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.page_token):
            query['PageToken'] = request.page_token
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRuns',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/runs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRunsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_runs_with_options_async(
        self,
        request: main_models.ListRunsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRunsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not DaraCore.is_null(request.gmt_create_time):
            query['GmtCreateTime'] = request.gmt_create_time
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.page_token):
            query['PageToken'] = request.page_token
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRuns',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/runs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRunsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_runs(
        self,
        request: main_models.ListRunsRequest,
    ) -> main_models.ListRunsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_runs_with_options(request, headers, runtime)

    async def list_runs_async(
        self,
        request: main_models.ListRunsRequest,
    ) -> main_models.ListRunsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_runs_with_options_async(request, headers, runtime)

    def list_user_configs_with_options(
        self,
        request: main_models.ListUserConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUserConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_names):
            query['CategoryNames'] = request.category_names
        if not DaraCore.is_null(request.config_keys):
            query['ConfigKeys'] = request.config_keys
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserConfigs',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/userconfigs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_configs_with_options_async(
        self,
        request: main_models.ListUserConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUserConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_names):
            query['CategoryNames'] = request.category_names
        if not DaraCore.is_null(request.config_keys):
            query['ConfigKeys'] = request.config_keys
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserConfigs',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/userconfigs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_configs(
        self,
        request: main_models.ListUserConfigsRequest,
    ) -> main_models.ListUserConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_user_configs_with_options(request, headers, runtime)

    async def list_user_configs_async(
        self,
        request: main_models.ListUserConfigsRequest,
    ) -> main_models.ListUserConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_user_configs_with_options_async(request, headers, runtime)

    def list_workspace_users_with_options(
        self,
        workspace_id: str,
        request: main_models.ListWorkspaceUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspaceUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaceUsers',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/users',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspaceUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspace_users_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListWorkspaceUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspaceUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaceUsers',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/users',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspaceUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspace_users(
        self,
        workspace_id: str,
        request: main_models.ListWorkspaceUsersRequest,
    ) -> main_models.ListWorkspaceUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_workspace_users_with_options(workspace_id, request, headers, runtime)

    async def list_workspace_users_async(
        self,
        workspace_id: str,
        request: main_models.ListWorkspaceUsersRequest,
    ) -> main_models.ListWorkspaceUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_workspace_users_with_options_async(workspace_id, request, headers, runtime)

    def list_workspaces_with_options(
        self,
        request: main_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fields):
            query['Fields'] = request.fields
        if not DaraCore.is_null(request.module_list):
            query['ModuleList'] = request.module_list
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        if not DaraCore.is_null(request.workspace_name):
            query['WorkspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaces',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspaces_with_options_async(
        self,
        request: main_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fields):
            query['Fields'] = request.fields
        if not DaraCore.is_null(request.module_list):
            query['ModuleList'] = request.module_list
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        if not DaraCore.is_null(request.workspace_name):
            query['WorkspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaces',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspaces(
        self,
        request: main_models.ListWorkspacesRequest,
    ) -> main_models.ListWorkspacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_workspaces_with_options(request, headers, runtime)

    async def list_workspaces_async(
        self,
        request: main_models.ListWorkspacesRequest,
    ) -> main_models.ListWorkspacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_workspaces_with_options_async(request, headers, runtime)

    def log_run_metrics_with_options(
        self,
        run_id: str,
        request: main_models.LogRunMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.LogRunMetricsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.metrics):
            body['Metrics'] = request.metrics
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LogRunMetrics',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/runs/{DaraURL.percent_encode(run_id)}/metrics/action/log',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LogRunMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def log_run_metrics_with_options_async(
        self,
        run_id: str,
        request: main_models.LogRunMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.LogRunMetricsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.metrics):
            body['Metrics'] = request.metrics
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LogRunMetrics',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/runs/{DaraURL.percent_encode(run_id)}/metrics/action/log',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LogRunMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def log_run_metrics(
        self,
        run_id: str,
        request: main_models.LogRunMetricsRequest,
    ) -> main_models.LogRunMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.log_run_metrics_with_options(run_id, request, headers, runtime)

    async def log_run_metrics_async(
        self,
        run_id: str,
        request: main_models.LogRunMetricsRequest,
    ) -> main_models.LogRunMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.log_run_metrics_with_options_async(run_id, request, headers, runtime)

    def publish_code_source_with_options(
        self,
        code_source_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishCodeSourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'PublishCodeSource',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/codesources/{DaraURL.percent_encode(code_source_id)}/publish',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishCodeSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_code_source_with_options_async(
        self,
        code_source_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishCodeSourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'PublishCodeSource',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/codesources/{DaraURL.percent_encode(code_source_id)}/publish',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishCodeSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_code_source(
        self,
        code_source_id: str,
    ) -> main_models.PublishCodeSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.publish_code_source_with_options(code_source_id, headers, runtime)

    async def publish_code_source_async(
        self,
        code_source_id: str,
    ) -> main_models.PublishCodeSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.publish_code_source_with_options_async(code_source_id, headers, runtime)

    def publish_dataset_with_options(
        self,
        dataset_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishDatasetResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'PublishDataset',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/publish',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_dataset_with_options_async(
        self,
        dataset_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishDatasetResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'PublishDataset',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/publish',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_dataset(
        self,
        dataset_id: str,
    ) -> main_models.PublishDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.publish_dataset_with_options(dataset_id, headers, runtime)

    async def publish_dataset_async(
        self,
        dataset_id: str,
    ) -> main_models.PublishDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.publish_dataset_with_options_async(dataset_id, headers, runtime)

    def publish_image_with_options(
        self,
        image_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishImageResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'PublishImage',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/images/{DaraURL.percent_encode(image_id)}/publish',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_image_with_options_async(
        self,
        image_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishImageResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'PublishImage',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/images/{DaraURL.percent_encode(image_id)}/publish',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_image(
        self,
        image_id: str,
    ) -> main_models.PublishImageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.publish_image_with_options(image_id, headers, runtime)

    async def publish_image_async(
        self,
        image_id: str,
    ) -> main_models.PublishImageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.publish_image_with_options_async(image_id, headers, runtime)

    def remove_image_with_options(
        self,
        image_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveImageResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveImage',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/images/{DaraURL.percent_encode(image_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_image_with_options_async(
        self,
        image_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveImageResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveImage',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/images/{DaraURL.percent_encode(image_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_image(
        self,
        image_id: str,
    ) -> main_models.RemoveImageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_image_with_options(image_id, headers, runtime)

    async def remove_image_async(
        self,
        image_id: str,
    ) -> main_models.RemoveImageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_image_with_options_async(image_id, headers, runtime)

    def remove_image_labels_with_options(
        self,
        image_id: str,
        label_key: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveImageLabelsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveImageLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/images/{DaraURL.percent_encode(image_id)}/labels/{DaraURL.percent_encode(label_key)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveImageLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_image_labels_with_options_async(
        self,
        image_id: str,
        label_key: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveImageLabelsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveImageLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/images/{DaraURL.percent_encode(image_id)}/labels/{DaraURL.percent_encode(label_key)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveImageLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_image_labels(
        self,
        image_id: str,
        label_key: str,
    ) -> main_models.RemoveImageLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_image_labels_with_options(image_id, label_key, headers, runtime)

    async def remove_image_labels_async(
        self,
        image_id: str,
        label_key: str,
    ) -> main_models.RemoveImageLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_image_labels_with_options_async(image_id, label_key, headers, runtime)

    def remove_member_role_with_options(
        self,
        workspace_id: str,
        member_id: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveMemberRoleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveMemberRole',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/members/{DaraURL.percent_encode(member_id)}/roles/{DaraURL.percent_encode(role_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveMemberRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_member_role_with_options_async(
        self,
        workspace_id: str,
        member_id: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveMemberRoleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveMemberRole',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/members/{DaraURL.percent_encode(member_id)}/roles/{DaraURL.percent_encode(role_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveMemberRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_member_role(
        self,
        workspace_id: str,
        member_id: str,
        role_name: str,
    ) -> main_models.RemoveMemberRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_member_role_with_options(workspace_id, member_id, role_name, headers, runtime)

    async def remove_member_role_async(
        self,
        workspace_id: str,
        member_id: str,
        role_name: str,
    ) -> main_models.RemoveMemberRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_member_role_with_options_async(workspace_id, member_id, role_name, headers, runtime)

    def set_experiment_labels_with_options(
        self,
        experiment_id: str,
        request: main_models.SetExperimentLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SetExperimentLabelsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetExperimentLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}/labels',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetExperimentLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_experiment_labels_with_options_async(
        self,
        experiment_id: str,
        request: main_models.SetExperimentLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SetExperimentLabelsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetExperimentLabels',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}/labels',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetExperimentLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_experiment_labels(
        self,
        experiment_id: str,
        request: main_models.SetExperimentLabelsRequest,
    ) -> main_models.SetExperimentLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.set_experiment_labels_with_options(experiment_id, request, headers, runtime)

    async def set_experiment_labels_async(
        self,
        experiment_id: str,
        request: main_models.SetExperimentLabelsRequest,
    ) -> main_models.SetExperimentLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.set_experiment_labels_with_options_async(experiment_id, request, headers, runtime)

    def set_user_configs_with_options(
        self,
        request: main_models.SetUserConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SetUserConfigsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.configs):
            body['Configs'] = request.configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetUserConfigs',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/userconfigs',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetUserConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_user_configs_with_options_async(
        self,
        request: main_models.SetUserConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SetUserConfigsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.configs):
            body['Configs'] = request.configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetUserConfigs',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/userconfigs',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetUserConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_user_configs(
        self,
        request: main_models.SetUserConfigsRequest,
    ) -> main_models.SetUserConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.set_user_configs_with_options(request, headers, runtime)

    async def set_user_configs_async(
        self,
        request: main_models.SetUserConfigsRequest,
    ) -> main_models.SetUserConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.set_user_configs_with_options_async(request, headers, runtime)

    def stop_dataset_job_with_options(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: main_models.StopDatasetJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopDatasetJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopDatasetJob',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobs/{DaraURL.percent_encode(dataset_job_id)}/action/stop',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDatasetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_dataset_job_with_options_async(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: main_models.StopDatasetJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopDatasetJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopDatasetJob',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobs/{DaraURL.percent_encode(dataset_job_id)}/action/stop',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDatasetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_dataset_job(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: main_models.StopDatasetJobRequest,
    ) -> main_models.StopDatasetJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_dataset_job_with_options(dataset_id, dataset_job_id, request, headers, runtime)

    async def stop_dataset_job_async(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: main_models.StopDatasetJobRequest,
    ) -> main_models.StopDatasetJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_dataset_job_with_options_async(dataset_id, dataset_job_id, request, headers, runtime)

    def update_code_source_with_options(
        self,
        code_source_id: str,
        request: main_models.UpdateCodeSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCodeSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code_branch):
            body['CodeBranch'] = request.code_branch
        if not DaraCore.is_null(request.code_commit):
            body['CodeCommit'] = request.code_commit
        if not DaraCore.is_null(request.code_repo):
            body['CodeRepo'] = request.code_repo
        if not DaraCore.is_null(request.code_repo_access_token):
            body['CodeRepoAccessToken'] = request.code_repo_access_token
        if not DaraCore.is_null(request.code_repo_user_name):
            body['CodeRepoUserName'] = request.code_repo_user_name
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.mount_path):
            body['MountPath'] = request.mount_path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCodeSource',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/codesources/{DaraURL.percent_encode(code_source_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCodeSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_code_source_with_options_async(
        self,
        code_source_id: str,
        request: main_models.UpdateCodeSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCodeSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code_branch):
            body['CodeBranch'] = request.code_branch
        if not DaraCore.is_null(request.code_commit):
            body['CodeCommit'] = request.code_commit
        if not DaraCore.is_null(request.code_repo):
            body['CodeRepo'] = request.code_repo
        if not DaraCore.is_null(request.code_repo_access_token):
            body['CodeRepoAccessToken'] = request.code_repo_access_token
        if not DaraCore.is_null(request.code_repo_user_name):
            body['CodeRepoUserName'] = request.code_repo_user_name
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.mount_path):
            body['MountPath'] = request.mount_path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCodeSource',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/codesources/{DaraURL.percent_encode(code_source_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCodeSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_code_source(
        self,
        code_source_id: str,
        request: main_models.UpdateCodeSourceRequest,
    ) -> main_models.UpdateCodeSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_code_source_with_options(code_source_id, request, headers, runtime)

    async def update_code_source_async(
        self,
        code_source_id: str,
        request: main_models.UpdateCodeSourceRequest,
    ) -> main_models.UpdateCodeSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_code_source_with_options_async(code_source_id, request, headers, runtime)

    def update_config_with_options(
        self,
        workspace_id: str,
        request: main_models.UpdateConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_name):
            body['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.config_key):
            body['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.config_value):
            body['ConfigValue'] = request.config_value
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfig',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/config',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_config_with_options_async(
        self,
        workspace_id: str,
        request: main_models.UpdateConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_name):
            body['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.config_key):
            body['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.config_value):
            body['ConfigValue'] = request.config_value
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfig',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/config',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_config(
        self,
        workspace_id: str,
        request: main_models.UpdateConfigRequest,
    ) -> main_models.UpdateConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_config_with_options(workspace_id, request, headers, runtime)

    async def update_config_async(
        self,
        workspace_id: str,
        request: main_models.UpdateConfigRequest,
    ) -> main_models.UpdateConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_config_with_options_async(workspace_id, request, headers, runtime)

    def update_configs_with_options(
        self,
        workspace_id: str,
        request: main_models.UpdateConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.configs):
            body['Configs'] = request.configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfigs',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/configs',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_configs_with_options_async(
        self,
        workspace_id: str,
        request: main_models.UpdateConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.configs):
            body['Configs'] = request.configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfigs',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/configs',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_configs(
        self,
        workspace_id: str,
        request: main_models.UpdateConfigsRequest,
    ) -> main_models.UpdateConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_configs_with_options(workspace_id, request, headers, runtime)

    async def update_configs_async(
        self,
        workspace_id: str,
        request: main_models.UpdateConfigsRequest,
    ) -> main_models.UpdateConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_configs_with_options_async(workspace_id, request, headers, runtime)

    def update_connection_with_options(
        self,
        connection_id: str,
        request: main_models.UpdateConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConnectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.configs):
            body['Configs'] = request.configs
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.models):
            body['Models'] = request.models
        if not DaraCore.is_null(request.secrets):
            body['Secrets'] = request.secrets
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConnection',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/connections/{DaraURL.percent_encode(connection_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_connection_with_options_async(
        self,
        connection_id: str,
        request: main_models.UpdateConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConnectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.configs):
            body['Configs'] = request.configs
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.models):
            body['Models'] = request.models
        if not DaraCore.is_null(request.secrets):
            body['Secrets'] = request.secrets
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConnection',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/connections/{DaraURL.percent_encode(connection_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_connection(
        self,
        connection_id: str,
        request: main_models.UpdateConnectionRequest,
    ) -> main_models.UpdateConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_connection_with_options(connection_id, request, headers, runtime)

    async def update_connection_async(
        self,
        connection_id: str,
        request: main_models.UpdateConnectionRequest,
    ) -> main_models.UpdateConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_connection_with_options_async(connection_id, request, headers, runtime)

    def update_dataset_with_options(
        self,
        dataset_id: str,
        request: main_models.UpdateDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.edition):
            body['Edition'] = request.edition
        if not DaraCore.is_null(request.mount_access_read_write_role_id_list):
            body['MountAccessReadWriteRoleIdList'] = request.mount_access_read_write_role_id_list
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.options):
            body['Options'] = request.options
        if not DaraCore.is_null(request.sharing_config):
            body['SharingConfig'] = request.sharing_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataset',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_with_options_async(
        self,
        dataset_id: str,
        request: main_models.UpdateDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.edition):
            body['Edition'] = request.edition
        if not DaraCore.is_null(request.mount_access_read_write_role_id_list):
            body['MountAccessReadWriteRoleIdList'] = request.mount_access_read_write_role_id_list
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.options):
            body['Options'] = request.options
        if not DaraCore.is_null(request.sharing_config):
            body['SharingConfig'] = request.sharing_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataset',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset(
        self,
        dataset_id: str,
        request: main_models.UpdateDatasetRequest,
    ) -> main_models.UpdateDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_dataset_with_options(dataset_id, request, headers, runtime)

    async def update_dataset_async(
        self,
        dataset_id: str,
        request: main_models.UpdateDatasetRequest,
    ) -> main_models.UpdateDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_dataset_with_options_async(dataset_id, request, headers, runtime)

    def update_dataset_file_metas_with_options(
        self,
        dataset_id: str,
        request: main_models.UpdateDatasetFileMetasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetFileMetasResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_file_metas):
            body['DatasetFileMetas'] = request.dataset_file_metas
        if not DaraCore.is_null(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.tag_job_id):
            body['TagJobId'] = request.tag_job_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDatasetFileMetas',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetfilemetas',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetFileMetasResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_file_metas_with_options_async(
        self,
        dataset_id: str,
        request: main_models.UpdateDatasetFileMetasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetFileMetasResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_file_metas):
            body['DatasetFileMetas'] = request.dataset_file_metas
        if not DaraCore.is_null(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.tag_job_id):
            body['TagJobId'] = request.tag_job_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDatasetFileMetas',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetfilemetas',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetFileMetasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset_file_metas(
        self,
        dataset_id: str,
        request: main_models.UpdateDatasetFileMetasRequest,
    ) -> main_models.UpdateDatasetFileMetasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_dataset_file_metas_with_options(dataset_id, request, headers, runtime)

    async def update_dataset_file_metas_async(
        self,
        dataset_id: str,
        request: main_models.UpdateDatasetFileMetasRequest,
    ) -> main_models.UpdateDatasetFileMetasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_dataset_file_metas_with_options_async(dataset_id, request, headers, runtime)

    def update_dataset_job_with_options(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: main_models.UpdateDatasetJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDatasetJob',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobs/{DaraURL.percent_encode(dataset_job_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_job_with_options_async(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: main_models.UpdateDatasetJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDatasetJob',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobs/{DaraURL.percent_encode(dataset_job_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset_job(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: main_models.UpdateDatasetJobRequest,
    ) -> main_models.UpdateDatasetJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_dataset_job_with_options(dataset_id, dataset_job_id, request, headers, runtime)

    async def update_dataset_job_async(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: main_models.UpdateDatasetJobRequest,
    ) -> main_models.UpdateDatasetJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_dataset_job_with_options_async(dataset_id, dataset_job_id, request, headers, runtime)

    def update_dataset_job_config_with_options(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: main_models.UpdateDatasetJobConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetJobConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.config_type):
            body['ConfigType'] = request.config_type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDatasetJobConfig',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobconfigs/{DaraURL.percent_encode(dataset_job_config_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_job_config_with_options_async(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: main_models.UpdateDatasetJobConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetJobConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.config_type):
            body['ConfigType'] = request.config_type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDatasetJobConfig',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/datasetjobconfigs/{DaraURL.percent_encode(dataset_job_config_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetJobConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset_job_config(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: main_models.UpdateDatasetJobConfigRequest,
    ) -> main_models.UpdateDatasetJobConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_dataset_job_config_with_options(dataset_id, dataset_job_config_id, request, headers, runtime)

    async def update_dataset_job_config_async(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: main_models.UpdateDatasetJobConfigRequest,
    ) -> main_models.UpdateDatasetJobConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_dataset_job_config_with_options_async(dataset_id, dataset_job_config_id, request, headers, runtime)

    def update_dataset_version_with_options(
        self,
        dataset_id: str,
        version_name: str,
        request: main_models.UpdateDatasetVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_count):
            body['DataCount'] = request.data_count
        if not DaraCore.is_null(request.data_size):
            body['DataSize'] = request.data_size
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.options):
            body['Options'] = request.options
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDatasetVersion',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/versions/{DaraURL.percent_encode(version_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_version_with_options_async(
        self,
        dataset_id: str,
        version_name: str,
        request: main_models.UpdateDatasetVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_count):
            body['DataCount'] = request.data_count
        if not DaraCore.is_null(request.data_size):
            body['DataSize'] = request.data_size
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.options):
            body['Options'] = request.options
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDatasetVersion',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/versions/{DaraURL.percent_encode(version_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset_version(
        self,
        dataset_id: str,
        version_name: str,
        request: main_models.UpdateDatasetVersionRequest,
    ) -> main_models.UpdateDatasetVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_dataset_version_with_options(dataset_id, version_name, request, headers, runtime)

    async def update_dataset_version_async(
        self,
        dataset_id: str,
        version_name: str,
        request: main_models.UpdateDatasetVersionRequest,
    ) -> main_models.UpdateDatasetVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_dataset_version_with_options_async(dataset_id, version_name, request, headers, runtime)

    def update_default_workspace_with_options(
        self,
        request: main_models.UpdateDefaultWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDefaultWorkspaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDefaultWorkspace',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/defaultWorkspaces',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDefaultWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_default_workspace_with_options_async(
        self,
        request: main_models.UpdateDefaultWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDefaultWorkspaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDefaultWorkspace',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/defaultWorkspaces',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDefaultWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_default_workspace(
        self,
        request: main_models.UpdateDefaultWorkspaceRequest,
    ) -> main_models.UpdateDefaultWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_default_workspace_with_options(request, headers, runtime)

    async def update_default_workspace_async(
        self,
        request: main_models.UpdateDefaultWorkspaceRequest,
    ) -> main_models.UpdateDefaultWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_default_workspace_with_options_async(request, headers, runtime)

    def update_experiment_with_options(
        self,
        experiment_id: str,
        request: main_models.UpdateExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExperimentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExperiment',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_experiment_with_options_async(
        self,
        experiment_id: str,
        request: main_models.UpdateExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExperimentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExperiment',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_experiment(
        self,
        experiment_id: str,
        request: main_models.UpdateExperimentRequest,
    ) -> main_models.UpdateExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_experiment_with_options(experiment_id, request, headers, runtime)

    async def update_experiment_async(
        self,
        experiment_id: str,
        request: main_models.UpdateExperimentRequest,
    ) -> main_models.UpdateExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_experiment_with_options_async(experiment_id, request, headers, runtime)

    def update_model_with_options(
        self,
        model_id: str,
        request: main_models.UpdateModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.domain):
            body['Domain'] = request.domain
        if not DaraCore.is_null(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.model_description):
            body['ModelDescription'] = request.model_description
        if not DaraCore.is_null(request.model_doc):
            body['ModelDoc'] = request.model_doc
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.model_type):
            body['ModelType'] = request.model_type
        if not DaraCore.is_null(request.order_number):
            body['OrderNumber'] = request.order_number
        if not DaraCore.is_null(request.origin):
            body['Origin'] = request.origin
        if not DaraCore.is_null(request.parameter_size):
            body['ParameterSize'] = request.parameter_size
        if not DaraCore.is_null(request.task):
            body['Task'] = request.task
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModel',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_with_options_async(
        self,
        model_id: str,
        request: main_models.UpdateModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.domain):
            body['Domain'] = request.domain
        if not DaraCore.is_null(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.model_description):
            body['ModelDescription'] = request.model_description
        if not DaraCore.is_null(request.model_doc):
            body['ModelDoc'] = request.model_doc
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.model_type):
            body['ModelType'] = request.model_type
        if not DaraCore.is_null(request.order_number):
            body['OrderNumber'] = request.order_number
        if not DaraCore.is_null(request.origin):
            body['Origin'] = request.origin
        if not DaraCore.is_null(request.parameter_size):
            body['ParameterSize'] = request.parameter_size
        if not DaraCore.is_null(request.task):
            body['Task'] = request.task
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModel',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model(
        self,
        model_id: str,
        request: main_models.UpdateModelRequest,
    ) -> main_models.UpdateModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_model_with_options(model_id, request, headers, runtime)

    async def update_model_async(
        self,
        model_id: str,
        request: main_models.UpdateModelRequest,
    ) -> main_models.UpdateModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_model_with_options_async(model_id, request, headers, runtime)

    def update_model_version_with_options(
        self,
        model_id: str,
        version_name: str,
        request: main_models.UpdateModelVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.approval_status):
            body['ApprovalStatus'] = request.approval_status
        if not DaraCore.is_null(request.compression_spec):
            body['CompressionSpec'] = request.compression_spec
        if not DaraCore.is_null(request.distillation_spec):
            body['DistillationSpec'] = request.distillation_spec
        if not DaraCore.is_null(request.evaluation_spec):
            body['EvaluationSpec'] = request.evaluation_spec
        if not DaraCore.is_null(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.inference_spec):
            body['InferenceSpec'] = request.inference_spec
        if not DaraCore.is_null(request.metrics):
            body['Metrics'] = request.metrics
        if not DaraCore.is_null(request.options):
            body['Options'] = request.options
        if not DaraCore.is_null(request.source_id):
            body['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.training_spec):
            body['TrainingSpec'] = request.training_spec
        if not DaraCore.is_null(request.version_description):
            body['VersionDescription'] = request.version_description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModelVersion',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}/versions/{DaraURL.percent_encode(version_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_version_with_options_async(
        self,
        model_id: str,
        version_name: str,
        request: main_models.UpdateModelVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.approval_status):
            body['ApprovalStatus'] = request.approval_status
        if not DaraCore.is_null(request.compression_spec):
            body['CompressionSpec'] = request.compression_spec
        if not DaraCore.is_null(request.distillation_spec):
            body['DistillationSpec'] = request.distillation_spec
        if not DaraCore.is_null(request.evaluation_spec):
            body['EvaluationSpec'] = request.evaluation_spec
        if not DaraCore.is_null(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.inference_spec):
            body['InferenceSpec'] = request.inference_spec
        if not DaraCore.is_null(request.metrics):
            body['Metrics'] = request.metrics
        if not DaraCore.is_null(request.options):
            body['Options'] = request.options
        if not DaraCore.is_null(request.source_id):
            body['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.training_spec):
            body['TrainingSpec'] = request.training_spec
        if not DaraCore.is_null(request.version_description):
            body['VersionDescription'] = request.version_description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModelVersion',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/models/{DaraURL.percent_encode(model_id)}/versions/{DaraURL.percent_encode(version_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model_version(
        self,
        model_id: str,
        version_name: str,
        request: main_models.UpdateModelVersionRequest,
    ) -> main_models.UpdateModelVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_model_version_with_options(model_id, version_name, request, headers, runtime)

    async def update_model_version_async(
        self,
        model_id: str,
        version_name: str,
        request: main_models.UpdateModelVersionRequest,
    ) -> main_models.UpdateModelVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_model_version_with_options_async(model_id, version_name, request, headers, runtime)

    def update_run_with_options(
        self,
        run_id: str,
        request: main_models.UpdateRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRunResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.params):
            body['Params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRun',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/runs/{DaraURL.percent_encode(run_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_run_with_options_async(
        self,
        run_id: str,
        request: main_models.UpdateRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRunResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.params):
            body['Params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRun',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/runs/{DaraURL.percent_encode(run_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_run(
        self,
        run_id: str,
        request: main_models.UpdateRunRequest,
    ) -> main_models.UpdateRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_run_with_options(run_id, request, headers, runtime)

    async def update_run_async(
        self,
        run_id: str,
        request: main_models.UpdateRunRequest,
    ) -> main_models.UpdateRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_run_with_options_async(run_id, request, headers, runtime)

    def update_workspace_with_options(
        self,
        workspace_id: str,
        request: main_models.UpdateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkspaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkspace',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workspace_with_options_async(
        self,
        workspace_id: str,
        request: main_models.UpdateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkspaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkspace',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workspace(
        self,
        workspace_id: str,
        request: main_models.UpdateWorkspaceRequest,
    ) -> main_models.UpdateWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_workspace_with_options(workspace_id, request, headers, runtime)

    async def update_workspace_async(
        self,
        workspace_id: str,
        request: main_models.UpdateWorkspaceRequest,
    ) -> main_models.UpdateWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_workspace_with_options_async(workspace_id, request, headers, runtime)

    def update_workspace_resource_with_options(
        self,
        workspace_id: str,
        request: main_models.UpdateWorkspaceResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkspaceResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_name):
            body['GroupName'] = request.group_name
        if not DaraCore.is_null(request.is_default):
            body['IsDefault'] = request.is_default
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkspaceResource',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/resources',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkspaceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workspace_resource_with_options_async(
        self,
        workspace_id: str,
        request: main_models.UpdateWorkspaceResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkspaceResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_name):
            body['GroupName'] = request.group_name
        if not DaraCore.is_null(request.is_default):
            body['IsDefault'] = request.is_default
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.spec):
            body['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkspaceResource',
            version = '2021-02-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/resources',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkspaceResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workspace_resource(
        self,
        workspace_id: str,
        request: main_models.UpdateWorkspaceResourceRequest,
    ) -> main_models.UpdateWorkspaceResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_workspace_resource_with_options(workspace_id, request, headers, runtime)

    async def update_workspace_resource_async(
        self,
        workspace_id: str,
        request: main_models.UpdateWorkspaceResourceRequest,
    ) -> main_models.UpdateWorkspaceResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_workspace_resource_with_options_async(workspace_id, request, headers, runtime)
