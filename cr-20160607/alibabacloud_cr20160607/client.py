# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        build_id = OpenApiUtilClient.get_encode_param(build_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelRepoBuild',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/build/{build_id}/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.CancelRepoBuildResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_repo_build_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        build_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.CancelRepoBuildResponse:
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        build_id = OpenApiUtilClient.get_encode_param(build_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelRepoBuild',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/build/{build_id}/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.CancelRepoBuildResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/namespace',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.CreateNamespaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/namespace',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.CreateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateRepo',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.CreateRepoResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repo_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.CreateRepoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateRepo',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.CreateRepoResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateRepoBuildRule',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/rules',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.CreateRepoBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repo_build_rule_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.CreateRepoBuildRuleResponse:
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateRepoBuildRule',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/rules',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.CreateRepoBuildRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateRepoWebhook',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/webhooks',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.CreateRepoWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repo_webhook_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.CreateRepoWebhookResponse:
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateRepoWebhook',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/webhooks',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.CreateRepoWebhookResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateUserInfo',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/users',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.CreateUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_info_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.CreateUserInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateUserInfo',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/users',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.CreateUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteImage',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/tags/{tag}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.DeleteImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_image_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.DeleteImageResponse:
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteImage',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/tags/{tag}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.DeleteImageResponse(),
            await self.call_api_async(params, req, runtime)
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
        namespace = OpenApiUtilClient.get_encode_param(namespace)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteNamespace',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/namespace/{namespace}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.DeleteNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_namespace_with_options_async(
        self,
        namespace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.DeleteNamespaceResponse:
        namespace = OpenApiUtilClient.get_encode_param(namespace)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteNamespace',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/namespace/{namespace}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.DeleteNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRepo',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.DeleteRepoResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repo_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.DeleteRepoResponse:
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRepo',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.DeleteRepoResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        build_rule_id = OpenApiUtilClient.get_encode_param(build_rule_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRepoBuildRule',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/rules/{build_rule_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.DeleteRepoBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repo_build_rule_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        build_rule_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.DeleteRepoBuildRuleResponse:
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        build_rule_id = OpenApiUtilClient.get_encode_param(build_rule_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRepoBuildRule',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/rules/{build_rule_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.DeleteRepoBuildRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        webhook_id = OpenApiUtilClient.get_encode_param(webhook_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRepoWebhook',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/webhooks/{webhook_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.DeleteRepoWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repo_webhook_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        webhook_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.DeleteRepoWebhookResponse:
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        webhook_id = OpenApiUtilClient.get_encode_param(webhook_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRepoWebhook',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/webhooks/{webhook_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.DeleteRepoWebhookResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetAuthorizationToken',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/tokens',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetAuthorizationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_authorization_token_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetAuthorizationTokenResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAuthorizationToken',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/tokens',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetAuthorizationTokenResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetImageLayer',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/tags/{tag}/layers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetImageLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_layer_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetImageLayerResponse:
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetImageLayer',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/tags/{tag}/layers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetImageLayerResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        query = {}
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageManifest',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/tags/{tag}/manifest',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetImageManifestResponse(),
            self.call_api(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        query = {}
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageManifest',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/tags/{tag}/manifest',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetImageManifestResponse(),
            await self.call_api_async(params, req, runtime)
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
        namespace = OpenApiUtilClient.get_encode_param(namespace)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetNamespace',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/namespace/{namespace}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_namespace_with_options_async(
        self,
        namespace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetNamespaceResponse:
        namespace = OpenApiUtilClient.get_encode_param(namespace)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetNamespace',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/namespace/{namespace}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.authorize):
            query['Authorize'] = request.authorize
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNamespaceList',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/namespace',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetNamespaceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_namespace_list_with_options_async(
        self,
        request: cr_20160607_models.GetNamespaceListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetNamespaceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorize):
            query['Authorize'] = request.authorize
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNamespaceList',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/namespace',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetNamespaceListResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetRegion',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRegionResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetRegion',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRegionResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetRegionList',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRegionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_region_list_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRegionListResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRegionList',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRegionListResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepo',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoResponse:
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepo',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoBuildList',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/build',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoBuildListResponse(),
            self.call_api(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoBuildList',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/build',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoBuildListResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepoBuildRuleList',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/rules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoBuildRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_build_rule_list_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoBuildRuleListResponse:
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepoBuildRuleList',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/rules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoBuildRuleListResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        build_id = OpenApiUtilClient.get_encode_param(build_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepoBuildStatus',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/build/{build_id}/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoBuildStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_build_status_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        build_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoBuildStatusResponse:
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        build_id = OpenApiUtilClient.get_encode_param(build_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepoBuildStatus',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/build/{build_id}/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoBuildStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoList',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_list_with_options_async(
        self,
        request: cr_20160607_models.GetRepoListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoList',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoListResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoListByNamespace',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoListByNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_list_by_namespace_with_options_async(
        self,
        repo_namespace: str,
        request: cr_20160607_models.GetRepoListByNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoListByNamespaceResponse:
        UtilClient.validate_model(request)
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoListByNamespace',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoListByNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepoTag',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/tags/{tag}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_tag_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoTagResponse:
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepoTag',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/tags/{tag}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoTagResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
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
        params = open_api_models.Params(
            action='GetRepoTagScanList',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/tags/{tag}/scanResult',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoTagScanListResponse(),
            self.call_api(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
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
        params = open_api_models.Params(
            action='GetRepoTagScanList',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/tags/{tag}/scanResult',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoTagScanListResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepoTagScanStatus',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/tags/{tag}/scanStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoTagScanStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_tag_scan_status_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoTagScanStatusResponse:
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepoTagScanStatus',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/tags/{tag}/scanStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoTagScanStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepoTagScanSummary',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/tags/{tag}/scanCount',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoTagScanSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_tag_scan_summary_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoTagScanSummaryResponse:
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepoTagScanSummary',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/tags/{tag}/scanCount',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoTagScanSummaryResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoTags',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoTagsResponse(),
            self.call_api(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoTags',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoTagsResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepoWebhook',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/webhooks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_webhook_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetRepoWebhookResponse:
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepoWebhook',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/webhooks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_quota(
        self,
        resource_name: str,
    ) -> cr_20160607_models.GetResourceQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_quota_with_options(resource_name, headers, runtime)

    async def get_resource_quota_async(
        self,
        resource_name: str,
    ) -> cr_20160607_models.GetResourceQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resource_quota_with_options_async(resource_name, headers, runtime)

    def get_resource_quota_with_options(
        self,
        resource_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetResourceQuotaResponse:
        resource_name = OpenApiUtilClient.get_encode_param(resource_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetResourceQuota',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/resource/{resource_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetResourceQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_quota_with_options_async(
        self,
        resource_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.GetResourceQuotaResponse:
        resource_name = OpenApiUtilClient.get_encode_param(resource_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetResourceQuota',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/resource/{resource_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetResourceQuotaResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartImageScan',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/tags/{tag}/scan',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.StartImageScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_image_scan_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        tag: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.StartImageScanResponse:
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartImageScan',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/tags/{tag}/scan',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.StartImageScanResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        build_rule_id = OpenApiUtilClient.get_encode_param(build_rule_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartRepoBuildByRule',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/rules/{build_rule_id}/build',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.StartRepoBuildByRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_repo_build_by_rule_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        build_rule_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.StartRepoBuildByRuleResponse:
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        build_rule_id = OpenApiUtilClient.get_encode_param(build_rule_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartRepoBuildByRule',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/rules/{build_rule_id}/build',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.StartRepoBuildByRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        namespace = OpenApiUtilClient.get_encode_param(namespace)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateNamespace',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/namespace/{namespace}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.UpdateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_namespace_with_options_async(
        self,
        namespace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.UpdateNamespaceResponse:
        namespace = OpenApiUtilClient.get_encode_param(namespace)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateNamespace',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/namespace/{namespace}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.UpdateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateRepo',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.UpdateRepoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_repo_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.UpdateRepoResponse:
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateRepo',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.UpdateRepoResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        build_rule_id = OpenApiUtilClient.get_encode_param(build_rule_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateRepoBuildRule',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/rules/{build_rule_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.UpdateRepoBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_repo_build_rule_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        build_rule_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.UpdateRepoBuildRuleResponse:
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        build_rule_id = OpenApiUtilClient.get_encode_param(build_rule_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateRepoBuildRule',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/rules/{build_rule_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.UpdateRepoBuildRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        webhook_id = OpenApiUtilClient.get_encode_param(webhook_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateRepoWebhook',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/webhooks/{webhook_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.UpdateRepoWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_repo_webhook_with_options_async(
        self,
        repo_namespace: str,
        repo_name: str,
        webhook_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.UpdateRepoWebhookResponse:
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        webhook_id = OpenApiUtilClient.get_encode_param(webhook_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateRepoWebhook',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/repos/{repo_namespace}/{repo_name}/webhooks/{webhook_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.UpdateRepoWebhookResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateUserInfo',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/users',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.UpdateUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_info_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cr_20160607_models.UpdateUserInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateUserInfo',
            version='2016-06-07',
            protocol='HTTPS',
            pathname=f'/users',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.UpdateUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )
