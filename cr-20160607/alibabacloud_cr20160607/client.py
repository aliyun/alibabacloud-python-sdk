# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cr20160607 import models as cr_20160607_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cr', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_repo_build(
        self,
        repo_namespace: str,
        repo_name: str,
        build_id: str,
    ) -> cr_20160607_models.CancelRepoBuildResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_repo_build_with_options(repo_namespace, repo_name, build_id, headers, runtime)

    async def cancel_repo_build_async(
        self,
        repo_namespace: str,
        repo_name: str,
        build_id: str,
    ) -> cr_20160607_models.CancelRepoBuildResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_repo_build_with_options_async(repo_namespace, repo_name, build_id, headers, runtime)

    def cancel_repo_build_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        build_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.CancelRepoBuildResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.CancelRepoBuildResponse().from_map(
            self.do_roarequest('CancelRepoBuild', '2016-06-07', 'HTTPS', 'POST', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/build/{{BuildId}}/cancel', 'none', req, runtime)
        )

    async def cancel_repo_build_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        build_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.CancelRepoBuildResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.CancelRepoBuildResponse().from_map(
            await self.do_roarequest_async('CancelRepoBuild', '2016-06-07', 'HTTPS', 'POST', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/build/{{BuildId}}/cancel', 'none', req, runtime)
        )

    def create_namespace(self) -> cr_20160607_models.CreateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_namespace_with_options(headers, runtime)

    async def create_namespace_async(self) -> cr_20160607_models.CreateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_namespace_with_options_async(headers, runtime)

    def create_namespace_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.CreateNamespaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.CreateNamespaceResponse().from_map(
            self.do_roarequest('CreateNamespace', '2016-06-07', 'HTTPS', 'PUT', 'AK', f'/namespace', 'none', req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.CreateNamespaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.CreateNamespaceResponse().from_map(
            await self.do_roarequest_async('CreateNamespace', '2016-06-07', 'HTTPS', 'PUT', 'AK', f'/namespace', 'none', req, runtime)
        )

    def create_repo(self) -> cr_20160607_models.CreateRepoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_repo_with_options(headers, runtime)

    async def create_repo_async(self) -> cr_20160607_models.CreateRepoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_repo_with_options_async(headers, runtime)

    def create_repo_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.CreateRepoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.CreateRepoResponse().from_map(
            self.do_roarequest('CreateRepo', '2016-06-07', 'HTTPS', 'PUT', 'AK', f'/repos', 'none', req, runtime)
        )

    async def create_repo_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.CreateRepoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.CreateRepoResponse().from_map(
            await self.do_roarequest_async('CreateRepo', '2016-06-07', 'HTTPS', 'PUT', 'AK', f'/repos', 'none', req, runtime)
        )

    def create_repo_build_rule(
        self,
        repo_namespace: str,
        repo_name: str,
    ) -> cr_20160607_models.CreateRepoBuildRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_repo_build_rule_with_options(repo_namespace, repo_name, headers, runtime)

    async def create_repo_build_rule_async(
        self,
        repo_namespace: str,
        repo_name: str,
    ) -> cr_20160607_models.CreateRepoBuildRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_repo_build_rule_with_options_async(repo_namespace, repo_name, headers, runtime)

    def create_repo_build_rule_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.CreateRepoBuildRuleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.CreateRepoBuildRuleResponse().from_map(
            self.do_roarequest('CreateRepoBuildRule', '2016-06-07', 'HTTPS', 'PUT', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/rules', 'none', req, runtime)
        )

    async def create_repo_build_rule_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.CreateRepoBuildRuleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.CreateRepoBuildRuleResponse().from_map(
            await self.do_roarequest_async('CreateRepoBuildRule', '2016-06-07', 'HTTPS', 'PUT', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/rules', 'none', req, runtime)
        )

    def create_repo_webhook(
        self,
        repo_namespace: str,
        repo_name: str,
    ) -> cr_20160607_models.CreateRepoWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_repo_webhook_with_options(repo_namespace, repo_name, headers, runtime)

    async def create_repo_webhook_async(
        self,
        repo_namespace: str,
        repo_name: str,
    ) -> cr_20160607_models.CreateRepoWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_repo_webhook_with_options_async(repo_namespace, repo_name, headers, runtime)

    def create_repo_webhook_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.CreateRepoWebhookResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.CreateRepoWebhookResponse().from_map(
            self.do_roarequest('CreateRepoWebhook', '2016-06-07', 'HTTPS', 'PUT', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/webhooks', 'none', req, runtime)
        )

    async def create_repo_webhook_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.CreateRepoWebhookResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.CreateRepoWebhookResponse().from_map(
            await self.do_roarequest_async('CreateRepoWebhook', '2016-06-07', 'HTTPS', 'PUT', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/webhooks', 'none', req, runtime)
        )

    def create_user_info(self) -> cr_20160607_models.CreateUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_user_info_with_options(headers, runtime)

    async def create_user_info_async(self) -> cr_20160607_models.CreateUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_user_info_with_options_async(headers, runtime)

    def create_user_info_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.CreateUserInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.CreateUserInfoResponse().from_map(
            self.do_roarequest('CreateUserInfo', '2016-06-07', 'HTTPS', 'PUT', 'AK', f'/users', 'none', req, runtime)
        )

    async def create_user_info_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.CreateUserInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.CreateUserInfoResponse().from_map(
            await self.do_roarequest_async('CreateUserInfo', '2016-06-07', 'HTTPS', 'PUT', 'AK', f'/users', 'none', req, runtime)
        )

    def delete_image(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
    ) -> cr_20160607_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_image_with_options(repo_namespace, repo_name, tag, headers, runtime)

    async def delete_image_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
    ) -> cr_20160607_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_image_with_options_async(repo_namespace, repo_name, tag, headers, runtime)

    def delete_image_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.DeleteImageResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.DeleteImageResponse().from_map(
            self.do_roarequest('DeleteImage', '2016-06-07', 'HTTPS', 'DELETE', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/tags/{{Tag}}', 'none', req, runtime)
        )

    async def delete_image_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.DeleteImageResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.DeleteImageResponse().from_map(
            await self.do_roarequest_async('DeleteImage', '2016-06-07', 'HTTPS', 'DELETE', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/tags/{{Tag}}', 'none', req, runtime)
        )

    def delete_namespace(
        self,
        namespace: str,
    ) -> cr_20160607_models.DeleteNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_namespace_with_options(namespace, headers, runtime)

    async def delete_namespace_async(
        self,
        namespace: str,
    ) -> cr_20160607_models.DeleteNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_namespace_with_options_async(namespace, headers, runtime)

    def delete_namespace_with_options(
        self,
        namespace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.DeleteNamespaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.DeleteNamespaceResponse().from_map(
            self.do_roarequest('DeleteNamespace', '2016-06-07', 'HTTPS', 'DELETE', 'AK', f'/namespace/{namespace}', 'none', req, runtime)
        )

    async def delete_namespace_with_options_async(
        self,
        namespace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.DeleteNamespaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.DeleteNamespaceResponse().from_map(
            await self.do_roarequest_async('DeleteNamespace', '2016-06-07', 'HTTPS', 'DELETE', 'AK', f'/namespace/{namespace}', 'none', req, runtime)
        )

    def delete_repo(
        self,
        repo_namespace: str,
        repo_name: str,
    ) -> cr_20160607_models.DeleteRepoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repo_with_options(repo_namespace, repo_name, headers, runtime)

    async def delete_repo_async(
        self,
        repo_namespace: str,
        repo_name: str,
    ) -> cr_20160607_models.DeleteRepoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_repo_with_options_async(repo_namespace, repo_name, headers, runtime)

    def delete_repo_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.DeleteRepoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.DeleteRepoResponse().from_map(
            self.do_roarequest('DeleteRepo', '2016-06-07', 'HTTPS', 'DELETE', 'AK', f'/repos/{repo_namespace}/{{RepoName}}', 'none', req, runtime)
        )

    async def delete_repo_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.DeleteRepoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.DeleteRepoResponse().from_map(
            await self.do_roarequest_async('DeleteRepo', '2016-06-07', 'HTTPS', 'DELETE', 'AK', f'/repos/{repo_namespace}/{{RepoName}}', 'none', req, runtime)
        )

    def delete_repo_build_rule(
        self,
        repo_namespace: str,
        repo_name: str,
        build_rule_id: str,
    ) -> cr_20160607_models.DeleteRepoBuildRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repo_build_rule_with_options(repo_namespace, repo_name, build_rule_id, headers, runtime)

    async def delete_repo_build_rule_async(
        self,
        repo_namespace: str,
        repo_name: str,
        build_rule_id: str,
    ) -> cr_20160607_models.DeleteRepoBuildRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_repo_build_rule_with_options_async(repo_namespace, repo_name, build_rule_id, headers, runtime)

    def delete_repo_build_rule_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        build_rule_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.DeleteRepoBuildRuleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.DeleteRepoBuildRuleResponse().from_map(
            self.do_roarequest('DeleteRepoBuildRule', '2016-06-07', 'HTTPS', 'DELETE', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/rules/{{BuildRuleId}}', 'none', req, runtime)
        )

    async def delete_repo_build_rule_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        build_rule_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.DeleteRepoBuildRuleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.DeleteRepoBuildRuleResponse().from_map(
            await self.do_roarequest_async('DeleteRepoBuildRule', '2016-06-07', 'HTTPS', 'DELETE', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/rules/{{BuildRuleId}}', 'none', req, runtime)
        )

    def delete_repo_webhook(
        self,
        repo_namespace: str,
        repo_name: str,
        webhook_id: str,
    ) -> cr_20160607_models.DeleteRepoWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repo_webhook_with_options(repo_namespace, repo_name, webhook_id, headers, runtime)

    async def delete_repo_webhook_async(
        self,
        repo_namespace: str,
        repo_name: str,
        webhook_id: str,
    ) -> cr_20160607_models.DeleteRepoWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_repo_webhook_with_options_async(repo_namespace, repo_name, webhook_id, headers, runtime)

    def delete_repo_webhook_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        webhook_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.DeleteRepoWebhookResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.DeleteRepoWebhookResponse().from_map(
            self.do_roarequest('DeleteRepoWebhook', '2016-06-07', 'HTTPS', 'DELETE', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/webhooks/{{WebhookId}}', 'none', req, runtime)
        )

    async def delete_repo_webhook_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        webhook_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.DeleteRepoWebhookResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.DeleteRepoWebhookResponse().from_map(
            await self.do_roarequest_async('DeleteRepoWebhook', '2016-06-07', 'HTTPS', 'DELETE', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/webhooks/{{WebhookId}}', 'none', req, runtime)
        )

    def get_authorization_token(self) -> cr_20160607_models.GetAuthorizationTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_authorization_token_with_options(headers, runtime)

    async def get_authorization_token_async(self) -> cr_20160607_models.GetAuthorizationTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_authorization_token_with_options_async(headers, runtime)

    def get_authorization_token_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetAuthorizationTokenResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetAuthorizationTokenResponse().from_map(
            self.do_roarequest('GetAuthorizationToken', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/tokens', 'none', req, runtime)
        )

    async def get_authorization_token_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetAuthorizationTokenResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetAuthorizationTokenResponse().from_map(
            await self.do_roarequest_async('GetAuthorizationToken', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/tokens', 'none', req, runtime)
        )

    def get_image_layer(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
    ) -> cr_20160607_models.GetImageLayerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_image_layer_with_options(repo_namespace, repo_name, tag, headers, runtime)

    async def get_image_layer_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
    ) -> cr_20160607_models.GetImageLayerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_image_layer_with_options_async(repo_namespace, repo_name, tag, headers, runtime)

    def get_image_layer_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetImageLayerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetImageLayerResponse().from_map(
            self.do_roarequest('GetImageLayer', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/tags/{{Tag}}/layers', 'none', req, runtime)
        )

    async def get_image_layer_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetImageLayerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetImageLayerResponse().from_map(
            await self.do_roarequest_async('GetImageLayer', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/tags/{{Tag}}/layers', 'none', req, runtime)
        )

    def get_image_manifest(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        request: cr_20160607_models.GetImageManifestRequest,
    ) -> cr_20160607_models.GetImageManifestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_image_manifest_with_options(repo_namespace, repo_name, tag, request, headers, runtime)

    async def get_image_manifest_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        request: cr_20160607_models.GetImageManifestRequest,
    ) -> cr_20160607_models.GetImageManifestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_image_manifest_with_options_async(repo_namespace, repo_name, tag, request, headers, runtime)

    def get_image_manifest_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        request: cr_20160607_models.GetImageManifestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetImageManifestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cr_20160607_models.GetImageManifestResponse().from_map(
            self.do_roarequest('GetImageManifest', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/tags/{{Tag}}/manifest', 'none', req, runtime)
        )

    async def get_image_manifest_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        request: cr_20160607_models.GetImageManifestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetImageManifestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cr_20160607_models.GetImageManifestResponse().from_map(
            await self.do_roarequest_async('GetImageManifest', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/tags/{{Tag}}/manifest', 'none', req, runtime)
        )

    def get_namespace(
        self,
        namespace: str,
    ) -> cr_20160607_models.GetNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_namespace_with_options(namespace, headers, runtime)

    async def get_namespace_async(
        self,
        namespace: str,
    ) -> cr_20160607_models.GetNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_namespace_with_options_async(namespace, headers, runtime)

    def get_namespace_with_options(
        self,
        namespace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetNamespaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetNamespaceResponse().from_map(
            self.do_roarequest('GetNamespace', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/namespace/{namespace}', 'none', req, runtime)
        )

    async def get_namespace_with_options_async(
        self,
        namespace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetNamespaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetNamespaceResponse().from_map(
            await self.do_roarequest_async('GetNamespace', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/namespace/{namespace}', 'none', req, runtime)
        )

    def get_namespace_list(
        self,
        request: cr_20160607_models.GetNamespaceListRequest,
    ) -> cr_20160607_models.GetNamespaceListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_namespace_list_with_options(request, headers, runtime)

    async def get_namespace_list_async(
        self,
        request: cr_20160607_models.GetNamespaceListRequest,
    ) -> cr_20160607_models.GetNamespaceListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_namespace_list_with_options_async(request, headers, runtime)

    def get_namespace_list_with_options(
        self,
        request: cr_20160607_models.GetNamespaceListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetNamespaceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.authorize):
            query['Authorize'] = request.authorize
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cr_20160607_models.GetNamespaceListResponse().from_map(
            self.do_roarequest('GetNamespaceList', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/namespace', 'none', req, runtime)
        )

    async def get_namespace_list_with_options_async(
        self,
        request: cr_20160607_models.GetNamespaceListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetNamespaceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.authorize):
            query['Authorize'] = request.authorize
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cr_20160607_models.GetNamespaceListResponse().from_map(
            await self.do_roarequest_async('GetNamespaceList', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/namespace', 'none', req, runtime)
        )

    def get_region(
        self,
        request: cr_20160607_models.GetRegionRequest,
    ) -> cr_20160607_models.GetRegionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_region_with_options(request, headers, runtime)

    async def get_region_async(
        self,
        request: cr_20160607_models.GetRegionRequest,
    ) -> cr_20160607_models.GetRegionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_region_with_options_async(request, headers, runtime)

    def get_region_with_options(
        self,
        request: cr_20160607_models.GetRegionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRegionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cr_20160607_models.GetRegionResponse().from_map(
            self.do_roarequest('GetRegion', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/regions', 'none', req, runtime)
        )

    async def get_region_with_options_async(
        self,
        request: cr_20160607_models.GetRegionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRegionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cr_20160607_models.GetRegionResponse().from_map(
            await self.do_roarequest_async('GetRegion', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/regions', 'none', req, runtime)
        )

    def get_region_list(self) -> cr_20160607_models.GetRegionListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_region_list_with_options(headers, runtime)

    async def get_region_list_async(self) -> cr_20160607_models.GetRegionListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_region_list_with_options_async(headers, runtime)

    def get_region_list_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRegionListResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetRegionListResponse().from_map(
            self.do_roarequest('GetRegionList', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/regions', 'none', req, runtime)
        )

    async def get_region_list_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRegionListResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetRegionListResponse().from_map(
            await self.do_roarequest_async('GetRegionList', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/regions', 'none', req, runtime)
        )

    def get_repo(
        self,
        repo_namespace: str,
        repo_name: str,
    ) -> cr_20160607_models.GetRepoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_with_options(repo_namespace, repo_name, headers, runtime)

    async def get_repo_async(
        self,
        repo_namespace: str,
        repo_name: str,
    ) -> cr_20160607_models.GetRepoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repo_with_options_async(repo_namespace, repo_name, headers, runtime)

    def get_repo_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetRepoResponse().from_map(
            self.do_roarequest('GetRepo', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}', 'none', req, runtime)
        )

    async def get_repo_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetRepoResponse().from_map(
            await self.do_roarequest_async('GetRepo', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}', 'none', req, runtime)
        )

    def get_repo_build_list(
        self,
        repo_namespace: str,
        repo_name: str,
        request: cr_20160607_models.GetRepoBuildListRequest,
    ) -> cr_20160607_models.GetRepoBuildListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_build_list_with_options(repo_namespace, repo_name, request, headers, runtime)

    async def get_repo_build_list_async(
        self,
        repo_namespace: str,
        repo_name: str,
        request: cr_20160607_models.GetRepoBuildListRequest,
    ) -> cr_20160607_models.GetRepoBuildListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repo_build_list_with_options_async(repo_namespace, repo_name, request, headers, runtime)

    def get_repo_build_list_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        request: cr_20160607_models.GetRepoBuildListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoBuildListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cr_20160607_models.GetRepoBuildListResponse().from_map(
            self.do_roarequest('GetRepoBuildList', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/build', 'none', req, runtime)
        )

    async def get_repo_build_list_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        request: cr_20160607_models.GetRepoBuildListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoBuildListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cr_20160607_models.GetRepoBuildListResponse().from_map(
            await self.do_roarequest_async('GetRepoBuildList', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/build', 'none', req, runtime)
        )

    def get_repo_build_rule_list(
        self,
        repo_namespace: str,
        repo_name: str,
    ) -> cr_20160607_models.GetRepoBuildRuleListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_build_rule_list_with_options(repo_namespace, repo_name, headers, runtime)

    async def get_repo_build_rule_list_async(
        self,
        repo_namespace: str,
        repo_name: str,
    ) -> cr_20160607_models.GetRepoBuildRuleListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repo_build_rule_list_with_options_async(repo_namespace, repo_name, headers, runtime)

    def get_repo_build_rule_list_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoBuildRuleListResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetRepoBuildRuleListResponse().from_map(
            self.do_roarequest('GetRepoBuildRuleList', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/rules', 'none', req, runtime)
        )

    async def get_repo_build_rule_list_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoBuildRuleListResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetRepoBuildRuleListResponse().from_map(
            await self.do_roarequest_async('GetRepoBuildRuleList', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/rules', 'none', req, runtime)
        )

    def get_repo_build_status(
        self,
        repo_namespace: str,
        repo_name: str,
        build_id: str,
    ) -> cr_20160607_models.GetRepoBuildStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_build_status_with_options(repo_namespace, repo_name, build_id, headers, runtime)

    async def get_repo_build_status_async(
        self,
        repo_namespace: str,
        repo_name: str,
        build_id: str,
    ) -> cr_20160607_models.GetRepoBuildStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repo_build_status_with_options_async(repo_namespace, repo_name, build_id, headers, runtime)

    def get_repo_build_status_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        build_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoBuildStatusResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetRepoBuildStatusResponse().from_map(
            self.do_roarequest('GetRepoBuildStatus', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/build/{{BuildId}}/status', 'none', req, runtime)
        )

    async def get_repo_build_status_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        build_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoBuildStatusResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetRepoBuildStatusResponse().from_map(
            await self.do_roarequest_async('GetRepoBuildStatus', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/build/{{BuildId}}/status', 'none', req, runtime)
        )

    def get_repo_list(
        self,
        request: cr_20160607_models.GetRepoListRequest,
    ) -> cr_20160607_models.GetRepoListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_list_with_options(request, headers, runtime)

    async def get_repo_list_async(
        self,
        request: cr_20160607_models.GetRepoListRequest,
    ) -> cr_20160607_models.GetRepoListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repo_list_with_options_async(request, headers, runtime)

    def get_repo_list_with_options(
        self,
        request: cr_20160607_models.GetRepoListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cr_20160607_models.GetRepoListResponse().from_map(
            self.do_roarequest('GetRepoList', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos', 'none', req, runtime)
        )

    async def get_repo_list_with_options_async(
        self,
        request: cr_20160607_models.GetRepoListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cr_20160607_models.GetRepoListResponse().from_map(
            await self.do_roarequest_async('GetRepoList', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos', 'none', req, runtime)
        )

    def get_repo_list_by_namespace(
        self,
        repo_namespace: str,
        request: cr_20160607_models.GetRepoListByNamespaceRequest,
    ) -> cr_20160607_models.GetRepoListByNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_list_by_namespace_with_options(repo_namespace, request, headers, runtime)

    async def get_repo_list_by_namespace_async(
        self,
        repo_namespace: str,
        request: cr_20160607_models.GetRepoListByNamespaceRequest,
    ) -> cr_20160607_models.GetRepoListByNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repo_list_by_namespace_with_options_async(repo_namespace, request, headers, runtime)

    def get_repo_list_by_namespace_with_options(
        self,
        repo_namespace: str,
        request: cr_20160607_models.GetRepoListByNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoListByNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cr_20160607_models.GetRepoListByNamespaceResponse().from_map(
            self.do_roarequest('GetRepoListByNamespace', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}', 'none', req, runtime)
        )

    async def get_repo_list_by_namespace_with_options_async(
        self,
        repo_namespace: str,
        request: cr_20160607_models.GetRepoListByNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoListByNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cr_20160607_models.GetRepoListByNamespaceResponse().from_map(
            await self.do_roarequest_async('GetRepoListByNamespace', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}', 'none', req, runtime)
        )

    def get_repo_tag(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
    ) -> cr_20160607_models.GetRepoTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_tag_with_options(repo_namespace, repo_name, tag, headers, runtime)

    async def get_repo_tag_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
    ) -> cr_20160607_models.GetRepoTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repo_tag_with_options_async(repo_namespace, repo_name, tag, headers, runtime)

    def get_repo_tag_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoTagResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetRepoTagResponse().from_map(
            self.do_roarequest('GetRepoTag', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/tags/{{Tag}}', 'json', req, runtime)
        )

    async def get_repo_tag_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoTagResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetRepoTagResponse().from_map(
            await self.do_roarequest_async('GetRepoTag', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/tags/{{Tag}}', 'json', req, runtime)
        )

    def get_repo_tags(
        self,
        repo_namespace: str,
        repo_name: str,
        request: cr_20160607_models.GetRepoTagsRequest,
    ) -> cr_20160607_models.GetRepoTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_tags_with_options(repo_namespace, repo_name, request, headers, runtime)

    async def get_repo_tags_async(
        self,
        repo_namespace: str,
        repo_name: str,
        request: cr_20160607_models.GetRepoTagsRequest,
    ) -> cr_20160607_models.GetRepoTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repo_tags_with_options_async(repo_namespace, repo_name, request, headers, runtime)

    def get_repo_tags_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        request: cr_20160607_models.GetRepoTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cr_20160607_models.GetRepoTagsResponse().from_map(
            self.do_roarequest('GetRepoTags', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/tags', 'none', req, runtime)
        )

    async def get_repo_tags_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        request: cr_20160607_models.GetRepoTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cr_20160607_models.GetRepoTagsResponse().from_map(
            await self.do_roarequest_async('GetRepoTags', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/tags', 'none', req, runtime)
        )

    def get_repo_tag_scan_list(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        request: cr_20160607_models.GetRepoTagScanListRequest,
    ) -> cr_20160607_models.GetRepoTagScanListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_tag_scan_list_with_options(repo_namespace, repo_name, tag, request, headers, runtime)

    async def get_repo_tag_scan_list_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        request: cr_20160607_models.GetRepoTagScanListRequest,
    ) -> cr_20160607_models.GetRepoTagScanListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repo_tag_scan_list_with_options_async(repo_namespace, repo_name, tag, request, headers, runtime)

    def get_repo_tag_scan_list_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        request: cr_20160607_models.GetRepoTagScanListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoTagScanListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cr_20160607_models.GetRepoTagScanListResponse().from_map(
            self.do_roarequest('GetRepoTagScanList', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/tags/{{Tag}}/scanResult', 'none', req, runtime)
        )

    async def get_repo_tag_scan_list_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        request: cr_20160607_models.GetRepoTagScanListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoTagScanListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cr_20160607_models.GetRepoTagScanListResponse().from_map(
            await self.do_roarequest_async('GetRepoTagScanList', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/tags/{{Tag}}/scanResult', 'none', req, runtime)
        )

    def get_repo_tag_scan_status(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
    ) -> cr_20160607_models.GetRepoTagScanStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_tag_scan_status_with_options(repo_namespace, repo_name, tag, headers, runtime)

    async def get_repo_tag_scan_status_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
    ) -> cr_20160607_models.GetRepoTagScanStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repo_tag_scan_status_with_options_async(repo_namespace, repo_name, tag, headers, runtime)

    def get_repo_tag_scan_status_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoTagScanStatusResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetRepoTagScanStatusResponse().from_map(
            self.do_roarequest('GetRepoTagScanStatus', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/tags/{{Tag}}/scanStatus', 'none', req, runtime)
        )

    async def get_repo_tag_scan_status_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoTagScanStatusResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetRepoTagScanStatusResponse().from_map(
            await self.do_roarequest_async('GetRepoTagScanStatus', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/tags/{{Tag}}/scanStatus', 'none', req, runtime)
        )

    def get_repo_tag_scan_summary(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
    ) -> cr_20160607_models.GetRepoTagScanSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_tag_scan_summary_with_options(repo_namespace, repo_name, tag, headers, runtime)

    async def get_repo_tag_scan_summary_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
    ) -> cr_20160607_models.GetRepoTagScanSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repo_tag_scan_summary_with_options_async(repo_namespace, repo_name, tag, headers, runtime)

    def get_repo_tag_scan_summary_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoTagScanSummaryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetRepoTagScanSummaryResponse().from_map(
            self.do_roarequest('GetRepoTagScanSummary', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/tags/{{Tag}}/scanCount', 'none', req, runtime)
        )

    async def get_repo_tag_scan_summary_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoTagScanSummaryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetRepoTagScanSummaryResponse().from_map(
            await self.do_roarequest_async('GetRepoTagScanSummary', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/tags/{{Tag}}/scanCount', 'none', req, runtime)
        )

    def get_repo_webhook(
        self,
        repo_namespace: str,
        repo_name: str,
    ) -> cr_20160607_models.GetRepoWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_webhook_with_options(repo_namespace, repo_name, headers, runtime)

    async def get_repo_webhook_async(
        self,
        repo_namespace: str,
        repo_name: str,
    ) -> cr_20160607_models.GetRepoWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repo_webhook_with_options_async(repo_namespace, repo_name, headers, runtime)

    def get_repo_webhook_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoWebhookResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetRepoWebhookResponse().from_map(
            self.do_roarequest('GetRepoWebhook', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/webhooks', 'none', req, runtime)
        )

    async def get_repo_webhook_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoWebhookResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.GetRepoWebhookResponse().from_map(
            await self.do_roarequest_async('GetRepoWebhook', '2016-06-07', 'HTTPS', 'GET', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/webhooks', 'none', req, runtime)
        )

    def start_image_scan(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
    ) -> cr_20160607_models.StartImageScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_image_scan_with_options(repo_namespace, repo_name, tag, headers, runtime)

    async def start_image_scan_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
    ) -> cr_20160607_models.StartImageScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_image_scan_with_options_async(repo_namespace, repo_name, tag, headers, runtime)

    def start_image_scan_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.StartImageScanResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.StartImageScanResponse().from_map(
            self.do_roarequest('StartImageScan', '2016-06-07', 'HTTPS', 'PUT', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/tags/{{Tag}}/scan', 'none', req, runtime)
        )

    async def start_image_scan_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.StartImageScanResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.StartImageScanResponse().from_map(
            await self.do_roarequest_async('StartImageScan', '2016-06-07', 'HTTPS', 'PUT', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/tags/{{Tag}}/scan', 'none', req, runtime)
        )

    def start_repo_build_by_rule(
        self,
        repo_namespace: str,
        repo_name: str,
        build_rule_id: str,
    ) -> cr_20160607_models.StartRepoBuildByRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_repo_build_by_rule_with_options(repo_namespace, repo_name, build_rule_id, headers, runtime)

    async def start_repo_build_by_rule_async(
        self,
        repo_namespace: str,
        repo_name: str,
        build_rule_id: str,
    ) -> cr_20160607_models.StartRepoBuildByRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_repo_build_by_rule_with_options_async(repo_namespace, repo_name, build_rule_id, headers, runtime)

    def start_repo_build_by_rule_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        build_rule_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.StartRepoBuildByRuleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.StartRepoBuildByRuleResponse().from_map(
            self.do_roarequest('StartRepoBuildByRule', '2016-06-07', 'HTTPS', 'PUT', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/rules/{{BuildRuleId}}/build', 'none', req, runtime)
        )

    async def start_repo_build_by_rule_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        build_rule_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.StartRepoBuildByRuleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.StartRepoBuildByRuleResponse().from_map(
            await self.do_roarequest_async('StartRepoBuildByRule', '2016-06-07', 'HTTPS', 'PUT', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/rules/{{BuildRuleId}}/build', 'none', req, runtime)
        )

    def update_namespace(
        self,
        namespace: str,
    ) -> cr_20160607_models.UpdateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_namespace_with_options(namespace, headers, runtime)

    async def update_namespace_async(
        self,
        namespace: str,
    ) -> cr_20160607_models.UpdateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_namespace_with_options_async(namespace, headers, runtime)

    def update_namespace_with_options(
        self,
        namespace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.UpdateNamespaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.UpdateNamespaceResponse().from_map(
            self.do_roarequest('UpdateNamespace', '2016-06-07', 'HTTPS', 'POST', 'AK', f'/namespace/{namespace}', 'none', req, runtime)
        )

    async def update_namespace_with_options_async(
        self,
        namespace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.UpdateNamespaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.UpdateNamespaceResponse().from_map(
            await self.do_roarequest_async('UpdateNamespace', '2016-06-07', 'HTTPS', 'POST', 'AK', f'/namespace/{namespace}', 'none', req, runtime)
        )

    def update_repo(
        self,
        repo_namespace: str,
        repo_name: str,
    ) -> cr_20160607_models.UpdateRepoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_repo_with_options(repo_namespace, repo_name, headers, runtime)

    async def update_repo_async(
        self,
        repo_namespace: str,
        repo_name: str,
    ) -> cr_20160607_models.UpdateRepoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_repo_with_options_async(repo_namespace, repo_name, headers, runtime)

    def update_repo_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.UpdateRepoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.UpdateRepoResponse().from_map(
            self.do_roarequest('UpdateRepo', '2016-06-07', 'HTTPS', 'POST', 'AK', f'/repos/{repo_namespace}/{{RepoName}}', 'none', req, runtime)
        )

    async def update_repo_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.UpdateRepoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.UpdateRepoResponse().from_map(
            await self.do_roarequest_async('UpdateRepo', '2016-06-07', 'HTTPS', 'POST', 'AK', f'/repos/{repo_namespace}/{{RepoName}}', 'none', req, runtime)
        )

    def update_repo_build_rule(
        self,
        repo_namespace: str,
        repo_name: str,
        build_rule_id: str,
    ) -> cr_20160607_models.UpdateRepoBuildRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_repo_build_rule_with_options(repo_namespace, repo_name, build_rule_id, headers, runtime)

    async def update_repo_build_rule_async(
        self,
        repo_namespace: str,
        repo_name: str,
        build_rule_id: str,
    ) -> cr_20160607_models.UpdateRepoBuildRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_repo_build_rule_with_options_async(repo_namespace, repo_name, build_rule_id, headers, runtime)

    def update_repo_build_rule_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        build_rule_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.UpdateRepoBuildRuleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.UpdateRepoBuildRuleResponse().from_map(
            self.do_roarequest('UpdateRepoBuildRule', '2016-06-07', 'HTTPS', 'POST', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/rules/{{BuildRuleId}}', 'none', req, runtime)
        )

    async def update_repo_build_rule_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        build_rule_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.UpdateRepoBuildRuleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.UpdateRepoBuildRuleResponse().from_map(
            await self.do_roarequest_async('UpdateRepoBuildRule', '2016-06-07', 'HTTPS', 'POST', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/rules/{{BuildRuleId}}', 'none', req, runtime)
        )

    def update_repo_webhook(
        self,
        repo_namespace: str,
        repo_name: str,
        webhook_id: str,
    ) -> cr_20160607_models.UpdateRepoWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_repo_webhook_with_options(repo_namespace, repo_name, webhook_id, headers, runtime)

    async def update_repo_webhook_async(
        self,
        repo_namespace: str,
        repo_name: str,
        webhook_id: str,
    ) -> cr_20160607_models.UpdateRepoWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_repo_webhook_with_options_async(repo_namespace, repo_name, webhook_id, headers, runtime)

    def update_repo_webhook_with_options(
        self,
        repo_namespace: str,
        repo_name: str,
        webhook_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.UpdateRepoWebhookResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.UpdateRepoWebhookResponse().from_map(
            self.do_roarequest('UpdateRepoWebhook', '2016-06-07', 'HTTPS', 'POST', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/webhooks/{{WebhookId}}', 'none', req, runtime)
        )

    async def update_repo_webhook_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        webhook_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.UpdateRepoWebhookResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.UpdateRepoWebhookResponse().from_map(
            await self.do_roarequest_async('UpdateRepoWebhook', '2016-06-07', 'HTTPS', 'POST', 'AK', f'/repos/{repo_namespace}/{{RepoName}}/webhooks/{{WebhookId}}', 'none', req, runtime)
        )

    def update_user_info(self) -> cr_20160607_models.UpdateUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_user_info_with_options(headers, runtime)

    async def update_user_info_async(self) -> cr_20160607_models.UpdateUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_user_info_with_options_async(headers, runtime)

    def update_user_info_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.UpdateUserInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.UpdateUserInfoResponse().from_map(
            self.do_roarequest('UpdateUserInfo', '2016-06-07', 'HTTPS', 'POST', 'AK', f'/users', 'none', req, runtime)
        )

    async def update_user_info_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.UpdateUserInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cr_20160607_models.UpdateUserInfoResponse().from_map(
            await self.do_roarequest_async('UpdateUserInfo', '2016-06-07', 'HTTPS', 'POST', 'AK', f'/users', 'none', req, runtime)
        )
