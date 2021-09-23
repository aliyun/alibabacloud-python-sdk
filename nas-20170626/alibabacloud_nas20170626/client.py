# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_nas20170626 import models as nas20170626_models
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
        self._endpoint_map = {
            'cn-chengdu': 'nas.aliyuncs.com',
            'me-east-1': 'nas.ap-northeast-1.aliyuncs.com',
            'cn-hangzhou-finance': 'nas.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('nas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_client_to_black_list_with_options(
        self,
        request: nas20170626_models.AddClientToBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.AddClientToBlackListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.AddClientToBlackListResponse(),
            self.do_rpcrequest('AddClientToBlackList', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_client_to_black_list_with_options_async(
        self,
        request: nas20170626_models.AddClientToBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.AddClientToBlackListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.AddClientToBlackListResponse(),
            await self.do_rpcrequest_async('AddClientToBlackList', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_client_to_black_list(
        self,
        request: nas20170626_models.AddClientToBlackListRequest,
    ) -> nas20170626_models.AddClientToBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_client_to_black_list_with_options(request, runtime)

    async def add_client_to_black_list_async(
        self,
        request: nas20170626_models.AddClientToBlackListRequest,
    ) -> nas20170626_models.AddClientToBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_client_to_black_list_with_options_async(request, runtime)

    def add_tags_with_options(
        self,
        request: nas20170626_models.AddTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.AddTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.AddTagsResponse(),
            self.do_rpcrequest('AddTags', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_tags_with_options_async(
        self,
        request: nas20170626_models.AddTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.AddTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.AddTagsResponse(),
            await self.do_rpcrequest_async('AddTags', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_tags(
        self,
        request: nas20170626_models.AddTagsRequest,
    ) -> nas20170626_models.AddTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_tags_with_options(request, runtime)

    async def add_tags_async(
        self,
        request: nas20170626_models.AddTagsRequest,
    ) -> nas20170626_models.AddTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_tags_with_options_async(request, runtime)

    def apply_auto_snapshot_policy_with_options(
        self,
        request: nas20170626_models.ApplyAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ApplyAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ApplyAutoSnapshotPolicyResponse(),
            self.do_rpcrequest('ApplyAutoSnapshotPolicy', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def apply_auto_snapshot_policy_with_options_async(
        self,
        request: nas20170626_models.ApplyAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ApplyAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ApplyAutoSnapshotPolicyResponse(),
            await self.do_rpcrequest_async('ApplyAutoSnapshotPolicy', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_auto_snapshot_policy(
        self,
        request: nas20170626_models.ApplyAutoSnapshotPolicyRequest,
    ) -> nas20170626_models.ApplyAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_auto_snapshot_policy_with_options(request, runtime)

    async def apply_auto_snapshot_policy_async(
        self,
        request: nas20170626_models.ApplyAutoSnapshotPolicyRequest,
    ) -> nas20170626_models.ApplyAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_auto_snapshot_policy_with_options_async(request, runtime)

    def cancel_auto_snapshot_policy_with_options(
        self,
        request: nas20170626_models.CancelAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CancelAutoSnapshotPolicyResponse(),
            self.do_rpcrequest('CancelAutoSnapshotPolicy', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_auto_snapshot_policy_with_options_async(
        self,
        request: nas20170626_models.CancelAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CancelAutoSnapshotPolicyResponse(),
            await self.do_rpcrequest_async('CancelAutoSnapshotPolicy', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_auto_snapshot_policy(
        self,
        request: nas20170626_models.CancelAutoSnapshotPolicyRequest,
    ) -> nas20170626_models.CancelAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_auto_snapshot_policy_with_options(request, runtime)

    async def cancel_auto_snapshot_policy_async(
        self,
        request: nas20170626_models.CancelAutoSnapshotPolicyRequest,
    ) -> nas20170626_models.CancelAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_auto_snapshot_policy_with_options_async(request, runtime)

    def cancel_dir_quota_with_options(
        self,
        request: nas20170626_models.CancelDirQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelDirQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CancelDirQuotaResponse(),
            self.do_rpcrequest('CancelDirQuota', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_dir_quota_with_options_async(
        self,
        request: nas20170626_models.CancelDirQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelDirQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CancelDirQuotaResponse(),
            await self.do_rpcrequest_async('CancelDirQuota', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_dir_quota(
        self,
        request: nas20170626_models.CancelDirQuotaRequest,
    ) -> nas20170626_models.CancelDirQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_dir_quota_with_options(request, runtime)

    async def cancel_dir_quota_async(
        self,
        request: nas20170626_models.CancelDirQuotaRequest,
    ) -> nas20170626_models.CancelDirQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_dir_quota_with_options_async(request, runtime)

    def cancel_lifecycle_retrieve_job_with_options(
        self,
        request: nas20170626_models.CancelLifecycleRetrieveJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelLifecycleRetrieveJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CancelLifecycleRetrieveJobResponse(),
            self.do_rpcrequest('CancelLifecycleRetrieveJob', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_lifecycle_retrieve_job_with_options_async(
        self,
        request: nas20170626_models.CancelLifecycleRetrieveJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelLifecycleRetrieveJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CancelLifecycleRetrieveJobResponse(),
            await self.do_rpcrequest_async('CancelLifecycleRetrieveJob', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_lifecycle_retrieve_job(
        self,
        request: nas20170626_models.CancelLifecycleRetrieveJobRequest,
    ) -> nas20170626_models.CancelLifecycleRetrieveJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_lifecycle_retrieve_job_with_options(request, runtime)

    async def cancel_lifecycle_retrieve_job_async(
        self,
        request: nas20170626_models.CancelLifecycleRetrieveJobRequest,
    ) -> nas20170626_models.CancelLifecycleRetrieveJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_lifecycle_retrieve_job_with_options_async(request, runtime)

    def cancel_recycle_bin_job_with_options(
        self,
        request: nas20170626_models.CancelRecycleBinJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelRecycleBinJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            nas20170626_models.CancelRecycleBinJobResponse(),
            self.do_rpcrequest('CancelRecycleBinJob', '2017-06-26', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def cancel_recycle_bin_job_with_options_async(
        self,
        request: nas20170626_models.CancelRecycleBinJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelRecycleBinJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            nas20170626_models.CancelRecycleBinJobResponse(),
            await self.do_rpcrequest_async('CancelRecycleBinJob', '2017-06-26', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def cancel_recycle_bin_job(
        self,
        request: nas20170626_models.CancelRecycleBinJobRequest,
    ) -> nas20170626_models.CancelRecycleBinJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_recycle_bin_job_with_options(request, runtime)

    async def cancel_recycle_bin_job_async(
        self,
        request: nas20170626_models.CancelRecycleBinJobRequest,
    ) -> nas20170626_models.CancelRecycleBinJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_recycle_bin_job_with_options_async(request, runtime)

    def create_access_group_with_options(
        self,
        request: nas20170626_models.CreateAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateAccessGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAccessGroupResponse(),
            self.do_rpcrequest('CreateAccessGroup', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_access_group_with_options_async(
        self,
        request: nas20170626_models.CreateAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateAccessGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAccessGroupResponse(),
            await self.do_rpcrequest_async('CreateAccessGroup', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_access_group(
        self,
        request: nas20170626_models.CreateAccessGroupRequest,
    ) -> nas20170626_models.CreateAccessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_access_group_with_options(request, runtime)

    async def create_access_group_async(
        self,
        request: nas20170626_models.CreateAccessGroupRequest,
    ) -> nas20170626_models.CreateAccessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_access_group_with_options_async(request, runtime)

    def create_access_rule_with_options(
        self,
        request: nas20170626_models.CreateAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateAccessRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAccessRuleResponse(),
            self.do_rpcrequest('CreateAccessRule', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_access_rule_with_options_async(
        self,
        request: nas20170626_models.CreateAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateAccessRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAccessRuleResponse(),
            await self.do_rpcrequest_async('CreateAccessRule', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_access_rule(
        self,
        request: nas20170626_models.CreateAccessRuleRequest,
    ) -> nas20170626_models.CreateAccessRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_access_rule_with_options(request, runtime)

    async def create_access_rule_async(
        self,
        request: nas20170626_models.CreateAccessRuleRequest,
    ) -> nas20170626_models.CreateAccessRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_access_rule_with_options_async(request, runtime)

    def create_auto_snapshot_policy_with_options(
        self,
        request: nas20170626_models.CreateAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAutoSnapshotPolicyResponse(),
            self.do_rpcrequest('CreateAutoSnapshotPolicy', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_auto_snapshot_policy_with_options_async(
        self,
        request: nas20170626_models.CreateAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAutoSnapshotPolicyResponse(),
            await self.do_rpcrequest_async('CreateAutoSnapshotPolicy', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_auto_snapshot_policy(
        self,
        request: nas20170626_models.CreateAutoSnapshotPolicyRequest,
    ) -> nas20170626_models.CreateAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_auto_snapshot_policy_with_options(request, runtime)

    async def create_auto_snapshot_policy_async(
        self,
        request: nas20170626_models.CreateAutoSnapshotPolicyRequest,
    ) -> nas20170626_models.CreateAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_auto_snapshot_policy_with_options_async(request, runtime)

    def create_file_system_with_options(
        self,
        request: nas20170626_models.CreateFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateFileSystemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CreateFileSystemResponse(),
            self.do_rpcrequest('CreateFileSystem', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_file_system_with_options_async(
        self,
        request: nas20170626_models.CreateFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateFileSystemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CreateFileSystemResponse(),
            await self.do_rpcrequest_async('CreateFileSystem', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_file_system(
        self,
        request: nas20170626_models.CreateFileSystemRequest,
    ) -> nas20170626_models.CreateFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_file_system_with_options(request, runtime)

    async def create_file_system_async(
        self,
        request: nas20170626_models.CreateFileSystemRequest,
    ) -> nas20170626_models.CreateFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_file_system_with_options_async(request, runtime)

    def create_ldapconfig_with_options(
        self,
        request: nas20170626_models.CreateLDAPConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateLDAPConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLDAPConfigResponse(),
            self.do_rpcrequest('CreateLDAPConfig', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ldapconfig_with_options_async(
        self,
        request: nas20170626_models.CreateLDAPConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateLDAPConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLDAPConfigResponse(),
            await self.do_rpcrequest_async('CreateLDAPConfig', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ldapconfig(
        self,
        request: nas20170626_models.CreateLDAPConfigRequest,
    ) -> nas20170626_models.CreateLDAPConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ldapconfig_with_options(request, runtime)

    async def create_ldapconfig_async(
        self,
        request: nas20170626_models.CreateLDAPConfigRequest,
    ) -> nas20170626_models.CreateLDAPConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ldapconfig_with_options_async(request, runtime)

    def create_lifecycle_policy_with_options(
        self,
        request: nas20170626_models.CreateLifecyclePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateLifecyclePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLifecyclePolicyResponse(),
            self.do_rpcrequest('CreateLifecyclePolicy', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_lifecycle_policy_with_options_async(
        self,
        request: nas20170626_models.CreateLifecyclePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateLifecyclePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLifecyclePolicyResponse(),
            await self.do_rpcrequest_async('CreateLifecyclePolicy', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_lifecycle_policy(
        self,
        request: nas20170626_models.CreateLifecyclePolicyRequest,
    ) -> nas20170626_models.CreateLifecyclePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_lifecycle_policy_with_options(request, runtime)

    async def create_lifecycle_policy_async(
        self,
        request: nas20170626_models.CreateLifecyclePolicyRequest,
    ) -> nas20170626_models.CreateLifecyclePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_lifecycle_policy_with_options_async(request, runtime)

    def create_lifecycle_retrieve_job_with_options(
        self,
        request: nas20170626_models.CreateLifecycleRetrieveJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateLifecycleRetrieveJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLifecycleRetrieveJobResponse(),
            self.do_rpcrequest('CreateLifecycleRetrieveJob', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_lifecycle_retrieve_job_with_options_async(
        self,
        request: nas20170626_models.CreateLifecycleRetrieveJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateLifecycleRetrieveJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLifecycleRetrieveJobResponse(),
            await self.do_rpcrequest_async('CreateLifecycleRetrieveJob', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_lifecycle_retrieve_job(
        self,
        request: nas20170626_models.CreateLifecycleRetrieveJobRequest,
    ) -> nas20170626_models.CreateLifecycleRetrieveJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_lifecycle_retrieve_job_with_options(request, runtime)

    async def create_lifecycle_retrieve_job_async(
        self,
        request: nas20170626_models.CreateLifecycleRetrieveJobRequest,
    ) -> nas20170626_models.CreateLifecycleRetrieveJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_lifecycle_retrieve_job_with_options_async(request, runtime)

    def create_mount_target_with_options(
        self,
        request: nas20170626_models.CreateMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateMountTargetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CreateMountTargetResponse(),
            self.do_rpcrequest('CreateMountTarget', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_mount_target_with_options_async(
        self,
        request: nas20170626_models.CreateMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateMountTargetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CreateMountTargetResponse(),
            await self.do_rpcrequest_async('CreateMountTarget', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_mount_target(
        self,
        request: nas20170626_models.CreateMountTargetRequest,
    ) -> nas20170626_models.CreateMountTargetResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_mount_target_with_options(request, runtime)

    async def create_mount_target_async(
        self,
        request: nas20170626_models.CreateMountTargetRequest,
    ) -> nas20170626_models.CreateMountTargetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_mount_target_with_options_async(request, runtime)

    def create_recycle_bin_delete_job_with_options(
        self,
        request: nas20170626_models.CreateRecycleBinDeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateRecycleBinDeleteJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            nas20170626_models.CreateRecycleBinDeleteJobResponse(),
            self.do_rpcrequest('CreateRecycleBinDeleteJob', '2017-06-26', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def create_recycle_bin_delete_job_with_options_async(
        self,
        request: nas20170626_models.CreateRecycleBinDeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateRecycleBinDeleteJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            nas20170626_models.CreateRecycleBinDeleteJobResponse(),
            await self.do_rpcrequest_async('CreateRecycleBinDeleteJob', '2017-06-26', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def create_recycle_bin_delete_job(
        self,
        request: nas20170626_models.CreateRecycleBinDeleteJobRequest,
    ) -> nas20170626_models.CreateRecycleBinDeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_recycle_bin_delete_job_with_options(request, runtime)

    async def create_recycle_bin_delete_job_async(
        self,
        request: nas20170626_models.CreateRecycleBinDeleteJobRequest,
    ) -> nas20170626_models.CreateRecycleBinDeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_recycle_bin_delete_job_with_options_async(request, runtime)

    def create_recycle_bin_restore_job_with_options(
        self,
        request: nas20170626_models.CreateRecycleBinRestoreJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateRecycleBinRestoreJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            nas20170626_models.CreateRecycleBinRestoreJobResponse(),
            self.do_rpcrequest('CreateRecycleBinRestoreJob', '2017-06-26', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def create_recycle_bin_restore_job_with_options_async(
        self,
        request: nas20170626_models.CreateRecycleBinRestoreJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateRecycleBinRestoreJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            nas20170626_models.CreateRecycleBinRestoreJobResponse(),
            await self.do_rpcrequest_async('CreateRecycleBinRestoreJob', '2017-06-26', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def create_recycle_bin_restore_job(
        self,
        request: nas20170626_models.CreateRecycleBinRestoreJobRequest,
    ) -> nas20170626_models.CreateRecycleBinRestoreJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_recycle_bin_restore_job_with_options(request, runtime)

    async def create_recycle_bin_restore_job_async(
        self,
        request: nas20170626_models.CreateRecycleBinRestoreJobRequest,
    ) -> nas20170626_models.CreateRecycleBinRestoreJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_recycle_bin_restore_job_with_options_async(request, runtime)

    def create_snapshot_with_options(
        self,
        request: nas20170626_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CreateSnapshotResponse(),
            self.do_rpcrequest('CreateSnapshot', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_snapshot_with_options_async(
        self,
        request: nas20170626_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.CreateSnapshotResponse(),
            await self.do_rpcrequest_async('CreateSnapshot', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_snapshot(
        self,
        request: nas20170626_models.CreateSnapshotRequest,
    ) -> nas20170626_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

    async def create_snapshot_async(
        self,
        request: nas20170626_models.CreateSnapshotRequest,
    ) -> nas20170626_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_snapshot_with_options_async(request, runtime)

    def delete_access_group_with_options(
        self,
        request: nas20170626_models.DeleteAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteAccessGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAccessGroupResponse(),
            self.do_rpcrequest('DeleteAccessGroup', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_access_group_with_options_async(
        self,
        request: nas20170626_models.DeleteAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteAccessGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAccessGroupResponse(),
            await self.do_rpcrequest_async('DeleteAccessGroup', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_access_group(
        self,
        request: nas20170626_models.DeleteAccessGroupRequest,
    ) -> nas20170626_models.DeleteAccessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_access_group_with_options(request, runtime)

    async def delete_access_group_async(
        self,
        request: nas20170626_models.DeleteAccessGroupRequest,
    ) -> nas20170626_models.DeleteAccessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_access_group_with_options_async(request, runtime)

    def delete_access_rule_with_options(
        self,
        request: nas20170626_models.DeleteAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteAccessRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAccessRuleResponse(),
            self.do_rpcrequest('DeleteAccessRule', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_access_rule_with_options_async(
        self,
        request: nas20170626_models.DeleteAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteAccessRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAccessRuleResponse(),
            await self.do_rpcrequest_async('DeleteAccessRule', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_access_rule(
        self,
        request: nas20170626_models.DeleteAccessRuleRequest,
    ) -> nas20170626_models.DeleteAccessRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_access_rule_with_options(request, runtime)

    async def delete_access_rule_async(
        self,
        request: nas20170626_models.DeleteAccessRuleRequest,
    ) -> nas20170626_models.DeleteAccessRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_access_rule_with_options_async(request, runtime)

    def delete_auto_snapshot_policy_with_options(
        self,
        request: nas20170626_models.DeleteAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAutoSnapshotPolicyResponse(),
            self.do_rpcrequest('DeleteAutoSnapshotPolicy', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_auto_snapshot_policy_with_options_async(
        self,
        request: nas20170626_models.DeleteAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAutoSnapshotPolicyResponse(),
            await self.do_rpcrequest_async('DeleteAutoSnapshotPolicy', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_auto_snapshot_policy(
        self,
        request: nas20170626_models.DeleteAutoSnapshotPolicyRequest,
    ) -> nas20170626_models.DeleteAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_snapshot_policy_with_options(request, runtime)

    async def delete_auto_snapshot_policy_async(
        self,
        request: nas20170626_models.DeleteAutoSnapshotPolicyRequest,
    ) -> nas20170626_models.DeleteAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_auto_snapshot_policy_with_options_async(request, runtime)

    def delete_file_system_with_options(
        self,
        request: nas20170626_models.DeleteFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteFileSystemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteFileSystemResponse(),
            self.do_rpcrequest('DeleteFileSystem', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_file_system_with_options_async(
        self,
        request: nas20170626_models.DeleteFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteFileSystemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteFileSystemResponse(),
            await self.do_rpcrequest_async('DeleteFileSystem', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_file_system(
        self,
        request: nas20170626_models.DeleteFileSystemRequest,
    ) -> nas20170626_models.DeleteFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_file_system_with_options(request, runtime)

    async def delete_file_system_async(
        self,
        request: nas20170626_models.DeleteFileSystemRequest,
    ) -> nas20170626_models.DeleteFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_file_system_with_options_async(request, runtime)

    def delete_ldapconfig_with_options(
        self,
        request: nas20170626_models.DeleteLDAPConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteLDAPConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteLDAPConfigResponse(),
            self.do_rpcrequest('DeleteLDAPConfig', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ldapconfig_with_options_async(
        self,
        request: nas20170626_models.DeleteLDAPConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteLDAPConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteLDAPConfigResponse(),
            await self.do_rpcrequest_async('DeleteLDAPConfig', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ldapconfig(
        self,
        request: nas20170626_models.DeleteLDAPConfigRequest,
    ) -> nas20170626_models.DeleteLDAPConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ldapconfig_with_options(request, runtime)

    async def delete_ldapconfig_async(
        self,
        request: nas20170626_models.DeleteLDAPConfigRequest,
    ) -> nas20170626_models.DeleteLDAPConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ldapconfig_with_options_async(request, runtime)

    def delete_lifecycle_policy_with_options(
        self,
        request: nas20170626_models.DeleteLifecyclePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteLifecyclePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteLifecyclePolicyResponse(),
            self.do_rpcrequest('DeleteLifecyclePolicy', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_lifecycle_policy_with_options_async(
        self,
        request: nas20170626_models.DeleteLifecyclePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteLifecyclePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteLifecyclePolicyResponse(),
            await self.do_rpcrequest_async('DeleteLifecyclePolicy', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_lifecycle_policy(
        self,
        request: nas20170626_models.DeleteLifecyclePolicyRequest,
    ) -> nas20170626_models.DeleteLifecyclePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_lifecycle_policy_with_options(request, runtime)

    async def delete_lifecycle_policy_async(
        self,
        request: nas20170626_models.DeleteLifecyclePolicyRequest,
    ) -> nas20170626_models.DeleteLifecyclePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_lifecycle_policy_with_options_async(request, runtime)

    def delete_mount_target_with_options(
        self,
        request: nas20170626_models.DeleteMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteMountTargetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteMountTargetResponse(),
            self.do_rpcrequest('DeleteMountTarget', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_mount_target_with_options_async(
        self,
        request: nas20170626_models.DeleteMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteMountTargetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteMountTargetResponse(),
            await self.do_rpcrequest_async('DeleteMountTarget', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_mount_target(
        self,
        request: nas20170626_models.DeleteMountTargetRequest,
    ) -> nas20170626_models.DeleteMountTargetResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_mount_target_with_options(request, runtime)

    async def delete_mount_target_async(
        self,
        request: nas20170626_models.DeleteMountTargetRequest,
    ) -> nas20170626_models.DeleteMountTargetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_mount_target_with_options_async(request, runtime)

    def delete_snapshot_with_options(
        self,
        request: nas20170626_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteSnapshotResponse(),
            self.do_rpcrequest('DeleteSnapshot', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_snapshot_with_options_async(
        self,
        request: nas20170626_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteSnapshotResponse(),
            await self.do_rpcrequest_async('DeleteSnapshot', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_snapshot(
        self,
        request: nas20170626_models.DeleteSnapshotRequest,
    ) -> nas20170626_models.DeleteSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    async def delete_snapshot_async(
        self,
        request: nas20170626_models.DeleteSnapshotRequest,
    ) -> nas20170626_models.DeleteSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_snapshot_with_options_async(request, runtime)

    def describe_access_groups_with_options(
        self,
        request: nas20170626_models.DescribeAccessGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAccessGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAccessGroupsResponse(),
            self.do_rpcrequest('DescribeAccessGroups', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_access_groups_with_options_async(
        self,
        request: nas20170626_models.DescribeAccessGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAccessGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAccessGroupsResponse(),
            await self.do_rpcrequest_async('DescribeAccessGroups', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_access_groups(
        self,
        request: nas20170626_models.DescribeAccessGroupsRequest,
    ) -> nas20170626_models.DescribeAccessGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_access_groups_with_options(request, runtime)

    async def describe_access_groups_async(
        self,
        request: nas20170626_models.DescribeAccessGroupsRequest,
    ) -> nas20170626_models.DescribeAccessGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_access_groups_with_options_async(request, runtime)

    def describe_access_rules_with_options(
        self,
        request: nas20170626_models.DescribeAccessRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAccessRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAccessRulesResponse(),
            self.do_rpcrequest('DescribeAccessRules', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_access_rules_with_options_async(
        self,
        request: nas20170626_models.DescribeAccessRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAccessRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAccessRulesResponse(),
            await self.do_rpcrequest_async('DescribeAccessRules', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_access_rules(
        self,
        request: nas20170626_models.DescribeAccessRulesRequest,
    ) -> nas20170626_models.DescribeAccessRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_access_rules_with_options(request, runtime)

    async def describe_access_rules_async(
        self,
        request: nas20170626_models.DescribeAccessRulesRequest,
    ) -> nas20170626_models.DescribeAccessRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_access_rules_with_options_async(request, runtime)

    def describe_auto_snapshot_policies_with_options(
        self,
        request: nas20170626_models.DescribeAutoSnapshotPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAutoSnapshotPoliciesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAutoSnapshotPoliciesResponse(),
            self.do_rpcrequest('DescribeAutoSnapshotPolicies', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_auto_snapshot_policies_with_options_async(
        self,
        request: nas20170626_models.DescribeAutoSnapshotPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAutoSnapshotPoliciesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAutoSnapshotPoliciesResponse(),
            await self.do_rpcrequest_async('DescribeAutoSnapshotPolicies', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_snapshot_policies(
        self,
        request: nas20170626_models.DescribeAutoSnapshotPoliciesRequest,
    ) -> nas20170626_models.DescribeAutoSnapshotPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_snapshot_policies_with_options(request, runtime)

    async def describe_auto_snapshot_policies_async(
        self,
        request: nas20170626_models.DescribeAutoSnapshotPoliciesRequest,
    ) -> nas20170626_models.DescribeAutoSnapshotPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_snapshot_policies_with_options_async(request, runtime)

    def describe_auto_snapshot_tasks_with_options(
        self,
        request: nas20170626_models.DescribeAutoSnapshotTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAutoSnapshotTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAutoSnapshotTasksResponse(),
            self.do_rpcrequest('DescribeAutoSnapshotTasks', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_auto_snapshot_tasks_with_options_async(
        self,
        request: nas20170626_models.DescribeAutoSnapshotTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAutoSnapshotTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAutoSnapshotTasksResponse(),
            await self.do_rpcrequest_async('DescribeAutoSnapshotTasks', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_snapshot_tasks(
        self,
        request: nas20170626_models.DescribeAutoSnapshotTasksRequest,
    ) -> nas20170626_models.DescribeAutoSnapshotTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_snapshot_tasks_with_options(request, runtime)

    async def describe_auto_snapshot_tasks_async(
        self,
        request: nas20170626_models.DescribeAutoSnapshotTasksRequest,
    ) -> nas20170626_models.DescribeAutoSnapshotTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_snapshot_tasks_with_options_async(request, runtime)

    def describe_black_list_clients_with_options(
        self,
        request: nas20170626_models.DescribeBlackListClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeBlackListClientsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeBlackListClientsResponse(),
            self.do_rpcrequest('DescribeBlackListClients', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_black_list_clients_with_options_async(
        self,
        request: nas20170626_models.DescribeBlackListClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeBlackListClientsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeBlackListClientsResponse(),
            await self.do_rpcrequest_async('DescribeBlackListClients', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_black_list_clients(
        self,
        request: nas20170626_models.DescribeBlackListClientsRequest,
    ) -> nas20170626_models.DescribeBlackListClientsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_black_list_clients_with_options(request, runtime)

    async def describe_black_list_clients_async(
        self,
        request: nas20170626_models.DescribeBlackListClientsRequest,
    ) -> nas20170626_models.DescribeBlackListClientsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_black_list_clients_with_options_async(request, runtime)

    def describe_dir_quotas_with_options(
        self,
        request: nas20170626_models.DescribeDirQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeDirQuotasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeDirQuotasResponse(),
            self.do_rpcrequest('DescribeDirQuotas', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dir_quotas_with_options_async(
        self,
        request: nas20170626_models.DescribeDirQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeDirQuotasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeDirQuotasResponse(),
            await self.do_rpcrequest_async('DescribeDirQuotas', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dir_quotas(
        self,
        request: nas20170626_models.DescribeDirQuotasRequest,
    ) -> nas20170626_models.DescribeDirQuotasResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dir_quotas_with_options(request, runtime)

    async def describe_dir_quotas_async(
        self,
        request: nas20170626_models.DescribeDirQuotasRequest,
    ) -> nas20170626_models.DescribeDirQuotasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dir_quotas_with_options_async(request, runtime)

    def describe_file_systems_with_options(
        self,
        request: nas20170626_models.DescribeFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeFileSystemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeFileSystemsResponse(),
            self.do_rpcrequest('DescribeFileSystems', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_file_systems_with_options_async(
        self,
        request: nas20170626_models.DescribeFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeFileSystemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeFileSystemsResponse(),
            await self.do_rpcrequest_async('DescribeFileSystems', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_file_systems(
        self,
        request: nas20170626_models.DescribeFileSystemsRequest,
    ) -> nas20170626_models.DescribeFileSystemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_file_systems_with_options(request, runtime)

    async def describe_file_systems_async(
        self,
        request: nas20170626_models.DescribeFileSystemsRequest,
    ) -> nas20170626_models.DescribeFileSystemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_file_systems_with_options_async(request, runtime)

    def describe_file_system_statistics_with_options(
        self,
        request: nas20170626_models.DescribeFileSystemStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeFileSystemStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeFileSystemStatisticsResponse(),
            self.do_rpcrequest('DescribeFileSystemStatistics', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_file_system_statistics_with_options_async(
        self,
        request: nas20170626_models.DescribeFileSystemStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeFileSystemStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeFileSystemStatisticsResponse(),
            await self.do_rpcrequest_async('DescribeFileSystemStatistics', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_file_system_statistics(
        self,
        request: nas20170626_models.DescribeFileSystemStatisticsRequest,
    ) -> nas20170626_models.DescribeFileSystemStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_file_system_statistics_with_options(request, runtime)

    async def describe_file_system_statistics_async(
        self,
        request: nas20170626_models.DescribeFileSystemStatisticsRequest,
    ) -> nas20170626_models.DescribeFileSystemStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_file_system_statistics_with_options_async(request, runtime)

    def describe_ldapconfig_with_options(
        self,
        request: nas20170626_models.DescribeLDAPConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeLDAPConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeLDAPConfigResponse(),
            self.do_rpcrequest('DescribeLDAPConfig', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ldapconfig_with_options_async(
        self,
        request: nas20170626_models.DescribeLDAPConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeLDAPConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeLDAPConfigResponse(),
            await self.do_rpcrequest_async('DescribeLDAPConfig', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ldapconfig(
        self,
        request: nas20170626_models.DescribeLDAPConfigRequest,
    ) -> nas20170626_models.DescribeLDAPConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ldapconfig_with_options(request, runtime)

    async def describe_ldapconfig_async(
        self,
        request: nas20170626_models.DescribeLDAPConfigRequest,
    ) -> nas20170626_models.DescribeLDAPConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ldapconfig_with_options_async(request, runtime)

    def describe_lifecycle_policies_with_options(
        self,
        request: nas20170626_models.DescribeLifecyclePoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeLifecyclePoliciesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeLifecyclePoliciesResponse(),
            self.do_rpcrequest('DescribeLifecyclePolicies', '2017-06-26', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_lifecycle_policies_with_options_async(
        self,
        request: nas20170626_models.DescribeLifecyclePoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeLifecyclePoliciesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeLifecyclePoliciesResponse(),
            await self.do_rpcrequest_async('DescribeLifecyclePolicies', '2017-06-26', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_lifecycle_policies(
        self,
        request: nas20170626_models.DescribeLifecyclePoliciesRequest,
    ) -> nas20170626_models.DescribeLifecyclePoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_lifecycle_policies_with_options(request, runtime)

    async def describe_lifecycle_policies_async(
        self,
        request: nas20170626_models.DescribeLifecyclePoliciesRequest,
    ) -> nas20170626_models.DescribeLifecyclePoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_lifecycle_policies_with_options_async(request, runtime)

    def describe_log_analysis_with_options(
        self,
        request: nas20170626_models.DescribeLogAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeLogAnalysisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeLogAnalysisResponse(),
            self.do_rpcrequest('DescribeLogAnalysis', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_log_analysis_with_options_async(
        self,
        request: nas20170626_models.DescribeLogAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeLogAnalysisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeLogAnalysisResponse(),
            await self.do_rpcrequest_async('DescribeLogAnalysis', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_log_analysis(
        self,
        request: nas20170626_models.DescribeLogAnalysisRequest,
    ) -> nas20170626_models.DescribeLogAnalysisResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_log_analysis_with_options(request, runtime)

    async def describe_log_analysis_async(
        self,
        request: nas20170626_models.DescribeLogAnalysisRequest,
    ) -> nas20170626_models.DescribeLogAnalysisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_analysis_with_options_async(request, runtime)

    def describe_mounted_clients_with_options(
        self,
        request: nas20170626_models.DescribeMountedClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeMountedClientsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeMountedClientsResponse(),
            self.do_rpcrequest('DescribeMountedClients', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_mounted_clients_with_options_async(
        self,
        request: nas20170626_models.DescribeMountedClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeMountedClientsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeMountedClientsResponse(),
            await self.do_rpcrequest_async('DescribeMountedClients', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_mounted_clients(
        self,
        request: nas20170626_models.DescribeMountedClientsRequest,
    ) -> nas20170626_models.DescribeMountedClientsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mounted_clients_with_options(request, runtime)

    async def describe_mounted_clients_async(
        self,
        request: nas20170626_models.DescribeMountedClientsRequest,
    ) -> nas20170626_models.DescribeMountedClientsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mounted_clients_with_options_async(request, runtime)

    def describe_mount_targets_with_options(
        self,
        request: nas20170626_models.DescribeMountTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeMountTargetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeMountTargetsResponse(),
            self.do_rpcrequest('DescribeMountTargets', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_mount_targets_with_options_async(
        self,
        request: nas20170626_models.DescribeMountTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeMountTargetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeMountTargetsResponse(),
            await self.do_rpcrequest_async('DescribeMountTargets', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_mount_targets(
        self,
        request: nas20170626_models.DescribeMountTargetsRequest,
    ) -> nas20170626_models.DescribeMountTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mount_targets_with_options(request, runtime)

    async def describe_mount_targets_async(
        self,
        request: nas20170626_models.DescribeMountTargetsRequest,
    ) -> nas20170626_models.DescribeMountTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mount_targets_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: nas20170626_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: nas20170626_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeRegionsResponse(),
            await self.do_rpcrequest_async('DescribeRegions', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: nas20170626_models.DescribeRegionsRequest,
    ) -> nas20170626_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: nas20170626_models.DescribeRegionsRequest,
    ) -> nas20170626_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_snapshots_with_options(
        self,
        request: nas20170626_models.DescribeSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeSnapshotsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeSnapshotsResponse(),
            self.do_rpcrequest('DescribeSnapshots', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_snapshots_with_options_async(
        self,
        request: nas20170626_models.DescribeSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeSnapshotsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeSnapshotsResponse(),
            await self.do_rpcrequest_async('DescribeSnapshots', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_snapshots(
        self,
        request: nas20170626_models.DescribeSnapshotsRequest,
    ) -> nas20170626_models.DescribeSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshots_with_options(request, runtime)

    async def describe_snapshots_async(
        self,
        request: nas20170626_models.DescribeSnapshotsRequest,
    ) -> nas20170626_models.DescribeSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_snapshots_with_options_async(request, runtime)

    def describe_storage_packages_with_options(
        self,
        request: nas20170626_models.DescribeStoragePackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeStoragePackagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeStoragePackagesResponse(),
            self.do_rpcrequest('DescribeStoragePackages', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_storage_packages_with_options_async(
        self,
        request: nas20170626_models.DescribeStoragePackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeStoragePackagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeStoragePackagesResponse(),
            await self.do_rpcrequest_async('DescribeStoragePackages', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_storage_packages(
        self,
        request: nas20170626_models.DescribeStoragePackagesRequest,
    ) -> nas20170626_models.DescribeStoragePackagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_packages_with_options(request, runtime)

    async def describe_storage_packages_async(
        self,
        request: nas20170626_models.DescribeStoragePackagesRequest,
    ) -> nas20170626_models.DescribeStoragePackagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_storage_packages_with_options_async(request, runtime)

    def describe_tags_with_options(
        self,
        request: nas20170626_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeTagsResponse(),
            self.do_rpcrequest('DescribeTags', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: nas20170626_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeTagsResponse(),
            await self.do_rpcrequest_async('DescribeTags', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tags(
        self,
        request: nas20170626_models.DescribeTagsRequest,
    ) -> nas20170626_models.DescribeTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    async def describe_tags_async(
        self,
        request: nas20170626_models.DescribeTagsRequest,
    ) -> nas20170626_models.DescribeTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tags_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: nas20170626_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeZonesResponse(),
            self.do_rpcrequest('DescribeZones', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: nas20170626_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeZonesResponse(),
            await self.do_rpcrequest_async('DescribeZones', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_zones(
        self,
        request: nas20170626_models.DescribeZonesRequest,
    ) -> nas20170626_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: nas20170626_models.DescribeZonesRequest,
    ) -> nas20170626_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def disable_and_clean_recycle_bin_with_options(
        self,
        request: nas20170626_models.DisableAndCleanRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DisableAndCleanRecycleBinResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            nas20170626_models.DisableAndCleanRecycleBinResponse(),
            self.do_rpcrequest('DisableAndCleanRecycleBin', '2017-06-26', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def disable_and_clean_recycle_bin_with_options_async(
        self,
        request: nas20170626_models.DisableAndCleanRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DisableAndCleanRecycleBinResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            nas20170626_models.DisableAndCleanRecycleBinResponse(),
            await self.do_rpcrequest_async('DisableAndCleanRecycleBin', '2017-06-26', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def disable_and_clean_recycle_bin(
        self,
        request: nas20170626_models.DisableAndCleanRecycleBinRequest,
    ) -> nas20170626_models.DisableAndCleanRecycleBinResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_and_clean_recycle_bin_with_options(request, runtime)

    async def disable_and_clean_recycle_bin_async(
        self,
        request: nas20170626_models.DisableAndCleanRecycleBinRequest,
    ) -> nas20170626_models.DisableAndCleanRecycleBinResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_and_clean_recycle_bin_with_options_async(request, runtime)

    def enable_recycle_bin_with_options(
        self,
        request: nas20170626_models.EnableRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.EnableRecycleBinResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.EnableRecycleBinResponse(),
            self.do_rpcrequest('EnableRecycleBin', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_recycle_bin_with_options_async(
        self,
        request: nas20170626_models.EnableRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.EnableRecycleBinResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.EnableRecycleBinResponse(),
            await self.do_rpcrequest_async('EnableRecycleBin', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_recycle_bin(
        self,
        request: nas20170626_models.EnableRecycleBinRequest,
    ) -> nas20170626_models.EnableRecycleBinResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_recycle_bin_with_options(request, runtime)

    async def enable_recycle_bin_async(
        self,
        request: nas20170626_models.EnableRecycleBinRequest,
    ) -> nas20170626_models.EnableRecycleBinResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_recycle_bin_with_options_async(request, runtime)

    def get_directory_or_file_properties_with_options(
        self,
        request: nas20170626_models.GetDirectoryOrFilePropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.GetDirectoryOrFilePropertiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.GetDirectoryOrFilePropertiesResponse(),
            self.do_rpcrequest('GetDirectoryOrFileProperties', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_directory_or_file_properties_with_options_async(
        self,
        request: nas20170626_models.GetDirectoryOrFilePropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.GetDirectoryOrFilePropertiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.GetDirectoryOrFilePropertiesResponse(),
            await self.do_rpcrequest_async('GetDirectoryOrFileProperties', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_directory_or_file_properties(
        self,
        request: nas20170626_models.GetDirectoryOrFilePropertiesRequest,
    ) -> nas20170626_models.GetDirectoryOrFilePropertiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_directory_or_file_properties_with_options(request, runtime)

    async def get_directory_or_file_properties_async(
        self,
        request: nas20170626_models.GetDirectoryOrFilePropertiesRequest,
    ) -> nas20170626_models.GetDirectoryOrFilePropertiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_directory_or_file_properties_with_options_async(request, runtime)

    def get_recycle_bin_attribute_with_options(
        self,
        request: nas20170626_models.GetRecycleBinAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.GetRecycleBinAttributeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            nas20170626_models.GetRecycleBinAttributeResponse(),
            self.do_rpcrequest('GetRecycleBinAttribute', '2017-06-26', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_recycle_bin_attribute_with_options_async(
        self,
        request: nas20170626_models.GetRecycleBinAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.GetRecycleBinAttributeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            nas20170626_models.GetRecycleBinAttributeResponse(),
            await self.do_rpcrequest_async('GetRecycleBinAttribute', '2017-06-26', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_recycle_bin_attribute(
        self,
        request: nas20170626_models.GetRecycleBinAttributeRequest,
    ) -> nas20170626_models.GetRecycleBinAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_recycle_bin_attribute_with_options(request, runtime)

    async def get_recycle_bin_attribute_async(
        self,
        request: nas20170626_models.GetRecycleBinAttributeRequest,
    ) -> nas20170626_models.GetRecycleBinAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_recycle_bin_attribute_with_options_async(request, runtime)

    def list_directories_and_files_with_options(
        self,
        request: nas20170626_models.ListDirectoriesAndFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListDirectoriesAndFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ListDirectoriesAndFilesResponse(),
            self.do_rpcrequest('ListDirectoriesAndFiles', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_directories_and_files_with_options_async(
        self,
        request: nas20170626_models.ListDirectoriesAndFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListDirectoriesAndFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ListDirectoriesAndFilesResponse(),
            await self.do_rpcrequest_async('ListDirectoriesAndFiles', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_directories_and_files(
        self,
        request: nas20170626_models.ListDirectoriesAndFilesRequest,
    ) -> nas20170626_models.ListDirectoriesAndFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_directories_and_files_with_options(request, runtime)

    async def list_directories_and_files_async(
        self,
        request: nas20170626_models.ListDirectoriesAndFilesRequest,
    ) -> nas20170626_models.ListDirectoriesAndFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_directories_and_files_with_options_async(request, runtime)

    def list_lifecycle_retrieve_jobs_with_options(
        self,
        request: nas20170626_models.ListLifecycleRetrieveJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListLifecycleRetrieveJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ListLifecycleRetrieveJobsResponse(),
            self.do_rpcrequest('ListLifecycleRetrieveJobs', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_lifecycle_retrieve_jobs_with_options_async(
        self,
        request: nas20170626_models.ListLifecycleRetrieveJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListLifecycleRetrieveJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ListLifecycleRetrieveJobsResponse(),
            await self.do_rpcrequest_async('ListLifecycleRetrieveJobs', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_lifecycle_retrieve_jobs(
        self,
        request: nas20170626_models.ListLifecycleRetrieveJobsRequest,
    ) -> nas20170626_models.ListLifecycleRetrieveJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_lifecycle_retrieve_jobs_with_options(request, runtime)

    async def list_lifecycle_retrieve_jobs_async(
        self,
        request: nas20170626_models.ListLifecycleRetrieveJobsRequest,
    ) -> nas20170626_models.ListLifecycleRetrieveJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_lifecycle_retrieve_jobs_with_options_async(request, runtime)

    def list_recently_recycled_directories_with_options(
        self,
        request: nas20170626_models.ListRecentlyRecycledDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListRecentlyRecycledDirectoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            nas20170626_models.ListRecentlyRecycledDirectoriesResponse(),
            self.do_rpcrequest('ListRecentlyRecycledDirectories', '2017-06-26', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_recently_recycled_directories_with_options_async(
        self,
        request: nas20170626_models.ListRecentlyRecycledDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListRecentlyRecycledDirectoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            nas20170626_models.ListRecentlyRecycledDirectoriesResponse(),
            await self.do_rpcrequest_async('ListRecentlyRecycledDirectories', '2017-06-26', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_recently_recycled_directories(
        self,
        request: nas20170626_models.ListRecentlyRecycledDirectoriesRequest,
    ) -> nas20170626_models.ListRecentlyRecycledDirectoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_recently_recycled_directories_with_options(request, runtime)

    async def list_recently_recycled_directories_async(
        self,
        request: nas20170626_models.ListRecentlyRecycledDirectoriesRequest,
    ) -> nas20170626_models.ListRecentlyRecycledDirectoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_recently_recycled_directories_with_options_async(request, runtime)

    def list_recycle_bin_jobs_with_options(
        self,
        request: nas20170626_models.ListRecycleBinJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListRecycleBinJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            nas20170626_models.ListRecycleBinJobsResponse(),
            self.do_rpcrequest('ListRecycleBinJobs', '2017-06-26', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_recycle_bin_jobs_with_options_async(
        self,
        request: nas20170626_models.ListRecycleBinJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListRecycleBinJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            nas20170626_models.ListRecycleBinJobsResponse(),
            await self.do_rpcrequest_async('ListRecycleBinJobs', '2017-06-26', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_recycle_bin_jobs(
        self,
        request: nas20170626_models.ListRecycleBinJobsRequest,
    ) -> nas20170626_models.ListRecycleBinJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_recycle_bin_jobs_with_options(request, runtime)

    async def list_recycle_bin_jobs_async(
        self,
        request: nas20170626_models.ListRecycleBinJobsRequest,
    ) -> nas20170626_models.ListRecycleBinJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_recycle_bin_jobs_with_options_async(request, runtime)

    def list_recycled_directories_and_files_with_options(
        self,
        request: nas20170626_models.ListRecycledDirectoriesAndFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListRecycledDirectoriesAndFilesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            nas20170626_models.ListRecycledDirectoriesAndFilesResponse(),
            self.do_rpcrequest('ListRecycledDirectoriesAndFiles', '2017-06-26', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_recycled_directories_and_files_with_options_async(
        self,
        request: nas20170626_models.ListRecycledDirectoriesAndFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListRecycledDirectoriesAndFilesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            nas20170626_models.ListRecycledDirectoriesAndFilesResponse(),
            await self.do_rpcrequest_async('ListRecycledDirectoriesAndFiles', '2017-06-26', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_recycled_directories_and_files(
        self,
        request: nas20170626_models.ListRecycledDirectoriesAndFilesRequest,
    ) -> nas20170626_models.ListRecycledDirectoriesAndFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_recycled_directories_and_files_with_options(request, runtime)

    async def list_recycled_directories_and_files_async(
        self,
        request: nas20170626_models.ListRecycledDirectoriesAndFilesRequest,
    ) -> nas20170626_models.ListRecycledDirectoriesAndFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_recycled_directories_and_files_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: nas20170626_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: nas20170626_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ListTagResourcesResponse(),
            await self.do_rpcrequest_async('ListTagResources', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: nas20170626_models.ListTagResourcesRequest,
    ) -> nas20170626_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: nas20170626_models.ListTagResourcesRequest,
    ) -> nas20170626_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_access_group_with_options(
        self,
        request: nas20170626_models.ModifyAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyAccessGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAccessGroupResponse(),
            self.do_rpcrequest('ModifyAccessGroup', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_access_group_with_options_async(
        self,
        request: nas20170626_models.ModifyAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyAccessGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAccessGroupResponse(),
            await self.do_rpcrequest_async('ModifyAccessGroup', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_access_group(
        self,
        request: nas20170626_models.ModifyAccessGroupRequest,
    ) -> nas20170626_models.ModifyAccessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_access_group_with_options(request, runtime)

    async def modify_access_group_async(
        self,
        request: nas20170626_models.ModifyAccessGroupRequest,
    ) -> nas20170626_models.ModifyAccessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_access_group_with_options_async(request, runtime)

    def modify_access_rule_with_options(
        self,
        request: nas20170626_models.ModifyAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyAccessRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAccessRuleResponse(),
            self.do_rpcrequest('ModifyAccessRule', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_access_rule_with_options_async(
        self,
        request: nas20170626_models.ModifyAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyAccessRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAccessRuleResponse(),
            await self.do_rpcrequest_async('ModifyAccessRule', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_access_rule(
        self,
        request: nas20170626_models.ModifyAccessRuleRequest,
    ) -> nas20170626_models.ModifyAccessRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_access_rule_with_options(request, runtime)

    async def modify_access_rule_async(
        self,
        request: nas20170626_models.ModifyAccessRuleRequest,
    ) -> nas20170626_models.ModifyAccessRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_access_rule_with_options_async(request, runtime)

    def modify_auto_snapshot_policy_with_options(
        self,
        request: nas20170626_models.ModifyAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAutoSnapshotPolicyResponse(),
            self.do_rpcrequest('ModifyAutoSnapshotPolicy', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_auto_snapshot_policy_with_options_async(
        self,
        request: nas20170626_models.ModifyAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAutoSnapshotPolicyResponse(),
            await self.do_rpcrequest_async('ModifyAutoSnapshotPolicy', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_auto_snapshot_policy(
        self,
        request: nas20170626_models.ModifyAutoSnapshotPolicyRequest,
    ) -> nas20170626_models.ModifyAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_snapshot_policy_with_options(request, runtime)

    async def modify_auto_snapshot_policy_async(
        self,
        request: nas20170626_models.ModifyAutoSnapshotPolicyRequest,
    ) -> nas20170626_models.ModifyAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_auto_snapshot_policy_with_options_async(request, runtime)

    def modify_file_system_with_options(
        self,
        request: nas20170626_models.ModifyFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyFileSystemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyFileSystemResponse(),
            self.do_rpcrequest('ModifyFileSystem', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_file_system_with_options_async(
        self,
        request: nas20170626_models.ModifyFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyFileSystemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyFileSystemResponse(),
            await self.do_rpcrequest_async('ModifyFileSystem', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_file_system(
        self,
        request: nas20170626_models.ModifyFileSystemRequest,
    ) -> nas20170626_models.ModifyFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_file_system_with_options(request, runtime)

    async def modify_file_system_async(
        self,
        request: nas20170626_models.ModifyFileSystemRequest,
    ) -> nas20170626_models.ModifyFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_file_system_with_options_async(request, runtime)

    def modify_ldapconfig_with_options(
        self,
        request: nas20170626_models.ModifyLDAPConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyLDAPConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyLDAPConfigResponse(),
            self.do_rpcrequest('ModifyLDAPConfig', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ldapconfig_with_options_async(
        self,
        request: nas20170626_models.ModifyLDAPConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyLDAPConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyLDAPConfigResponse(),
            await self.do_rpcrequest_async('ModifyLDAPConfig', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ldapconfig(
        self,
        request: nas20170626_models.ModifyLDAPConfigRequest,
    ) -> nas20170626_models.ModifyLDAPConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ldapconfig_with_options(request, runtime)

    async def modify_ldapconfig_async(
        self,
        request: nas20170626_models.ModifyLDAPConfigRequest,
    ) -> nas20170626_models.ModifyLDAPConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ldapconfig_with_options_async(request, runtime)

    def modify_lifecycle_policy_with_options(
        self,
        request: nas20170626_models.ModifyLifecyclePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyLifecyclePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyLifecyclePolicyResponse(),
            self.do_rpcrequest('ModifyLifecyclePolicy', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_lifecycle_policy_with_options_async(
        self,
        request: nas20170626_models.ModifyLifecyclePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyLifecyclePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyLifecyclePolicyResponse(),
            await self.do_rpcrequest_async('ModifyLifecyclePolicy', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_lifecycle_policy(
        self,
        request: nas20170626_models.ModifyLifecyclePolicyRequest,
    ) -> nas20170626_models.ModifyLifecyclePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_lifecycle_policy_with_options(request, runtime)

    async def modify_lifecycle_policy_async(
        self,
        request: nas20170626_models.ModifyLifecyclePolicyRequest,
    ) -> nas20170626_models.ModifyLifecyclePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_lifecycle_policy_with_options_async(request, runtime)

    def modify_mount_target_with_options(
        self,
        request: nas20170626_models.ModifyMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyMountTargetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyMountTargetResponse(),
            self.do_rpcrequest('ModifyMountTarget', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_mount_target_with_options_async(
        self,
        request: nas20170626_models.ModifyMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyMountTargetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyMountTargetResponse(),
            await self.do_rpcrequest_async('ModifyMountTarget', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_mount_target(
        self,
        request: nas20170626_models.ModifyMountTargetRequest,
    ) -> nas20170626_models.ModifyMountTargetResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_mount_target_with_options(request, runtime)

    async def modify_mount_target_async(
        self,
        request: nas20170626_models.ModifyMountTargetRequest,
    ) -> nas20170626_models.ModifyMountTargetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_mount_target_with_options_async(request, runtime)

    def open_nasservice_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.OpenNASServiceResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            nas20170626_models.OpenNASServiceResponse(),
            self.do_rpcrequest('OpenNASService', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_nasservice_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.OpenNASServiceResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            nas20170626_models.OpenNASServiceResponse(),
            await self.do_rpcrequest_async('OpenNASService', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_nasservice(self) -> nas20170626_models.OpenNASServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_nasservice_with_options(runtime)

    async def open_nasservice_async(self) -> nas20170626_models.OpenNASServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_nasservice_with_options_async(runtime)

    def remove_client_from_black_list_with_options(
        self,
        request: nas20170626_models.RemoveClientFromBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.RemoveClientFromBlackListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.RemoveClientFromBlackListResponse(),
            self.do_rpcrequest('RemoveClientFromBlackList', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_client_from_black_list_with_options_async(
        self,
        request: nas20170626_models.RemoveClientFromBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.RemoveClientFromBlackListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.RemoveClientFromBlackListResponse(),
            await self.do_rpcrequest_async('RemoveClientFromBlackList', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_client_from_black_list(
        self,
        request: nas20170626_models.RemoveClientFromBlackListRequest,
    ) -> nas20170626_models.RemoveClientFromBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_client_from_black_list_with_options(request, runtime)

    async def remove_client_from_black_list_async(
        self,
        request: nas20170626_models.RemoveClientFromBlackListRequest,
    ) -> nas20170626_models.RemoveClientFromBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_client_from_black_list_with_options_async(request, runtime)

    def remove_tags_with_options(
        self,
        request: nas20170626_models.RemoveTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.RemoveTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.RemoveTagsResponse(),
            self.do_rpcrequest('RemoveTags', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_tags_with_options_async(
        self,
        request: nas20170626_models.RemoveTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.RemoveTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.RemoveTagsResponse(),
            await self.do_rpcrequest_async('RemoveTags', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_tags(
        self,
        request: nas20170626_models.RemoveTagsRequest,
    ) -> nas20170626_models.RemoveTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_tags_with_options(request, runtime)

    async def remove_tags_async(
        self,
        request: nas20170626_models.RemoveTagsRequest,
    ) -> nas20170626_models.RemoveTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_tags_with_options_async(request, runtime)

    def reset_file_system_with_options(
        self,
        request: nas20170626_models.ResetFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ResetFileSystemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ResetFileSystemResponse(),
            self.do_rpcrequest('ResetFileSystem', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_file_system_with_options_async(
        self,
        request: nas20170626_models.ResetFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ResetFileSystemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.ResetFileSystemResponse(),
            await self.do_rpcrequest_async('ResetFileSystem', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_file_system(
        self,
        request: nas20170626_models.ResetFileSystemRequest,
    ) -> nas20170626_models.ResetFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_file_system_with_options(request, runtime)

    async def reset_file_system_async(
        self,
        request: nas20170626_models.ResetFileSystemRequest,
    ) -> nas20170626_models.ResetFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_file_system_with_options_async(request, runtime)

    def retry_lifecycle_retrieve_job_with_options(
        self,
        request: nas20170626_models.RetryLifecycleRetrieveJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.RetryLifecycleRetrieveJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.RetryLifecycleRetrieveJobResponse(),
            self.do_rpcrequest('RetryLifecycleRetrieveJob', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def retry_lifecycle_retrieve_job_with_options_async(
        self,
        request: nas20170626_models.RetryLifecycleRetrieveJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.RetryLifecycleRetrieveJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.RetryLifecycleRetrieveJobResponse(),
            await self.do_rpcrequest_async('RetryLifecycleRetrieveJob', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def retry_lifecycle_retrieve_job(
        self,
        request: nas20170626_models.RetryLifecycleRetrieveJobRequest,
    ) -> nas20170626_models.RetryLifecycleRetrieveJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.retry_lifecycle_retrieve_job_with_options(request, runtime)

    async def retry_lifecycle_retrieve_job_async(
        self,
        request: nas20170626_models.RetryLifecycleRetrieveJobRequest,
    ) -> nas20170626_models.RetryLifecycleRetrieveJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retry_lifecycle_retrieve_job_with_options_async(request, runtime)

    def set_dir_quota_with_options(
        self,
        request: nas20170626_models.SetDirQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.SetDirQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.SetDirQuotaResponse(),
            self.do_rpcrequest('SetDirQuota', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_dir_quota_with_options_async(
        self,
        request: nas20170626_models.SetDirQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.SetDirQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.SetDirQuotaResponse(),
            await self.do_rpcrequest_async('SetDirQuota', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_dir_quota(
        self,
        request: nas20170626_models.SetDirQuotaRequest,
    ) -> nas20170626_models.SetDirQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_dir_quota_with_options(request, runtime)

    async def set_dir_quota_async(
        self,
        request: nas20170626_models.SetDirQuotaRequest,
    ) -> nas20170626_models.SetDirQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_dir_quota_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: nas20170626_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: nas20170626_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.TagResourcesResponse(),
            await self.do_rpcrequest_async('TagResources', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: nas20170626_models.TagResourcesRequest,
    ) -> nas20170626_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: nas20170626_models.TagResourcesRequest,
    ) -> nas20170626_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: nas20170626_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: nas20170626_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.UntagResourcesResponse(),
            await self.do_rpcrequest_async('UntagResources', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: nas20170626_models.UntagResourcesRequest,
    ) -> nas20170626_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: nas20170626_models.UntagResourcesRequest,
    ) -> nas20170626_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_recycle_bin_attribute_with_options(
        self,
        request: nas20170626_models.UpdateRecycleBinAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.UpdateRecycleBinAttributeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            nas20170626_models.UpdateRecycleBinAttributeResponse(),
            self.do_rpcrequest('UpdateRecycleBinAttribute', '2017-06-26', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def update_recycle_bin_attribute_with_options_async(
        self,
        request: nas20170626_models.UpdateRecycleBinAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.UpdateRecycleBinAttributeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            nas20170626_models.UpdateRecycleBinAttributeResponse(),
            await self.do_rpcrequest_async('UpdateRecycleBinAttribute', '2017-06-26', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def update_recycle_bin_attribute(
        self,
        request: nas20170626_models.UpdateRecycleBinAttributeRequest,
    ) -> nas20170626_models.UpdateRecycleBinAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_recycle_bin_attribute_with_options(request, runtime)

    async def update_recycle_bin_attribute_async(
        self,
        request: nas20170626_models.UpdateRecycleBinAttributeRequest,
    ) -> nas20170626_models.UpdateRecycleBinAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_recycle_bin_attribute_with_options_async(request, runtime)

    def upgrade_file_system_with_options(
        self,
        request: nas20170626_models.UpgradeFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.UpgradeFileSystemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.UpgradeFileSystemResponse(),
            self.do_rpcrequest('UpgradeFileSystem', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_file_system_with_options_async(
        self,
        request: nas20170626_models.UpgradeFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.UpgradeFileSystemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nas20170626_models.UpgradeFileSystemResponse(),
            await self.do_rpcrequest_async('UpgradeFileSystem', '2017-06-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_file_system(
        self,
        request: nas20170626_models.UpgradeFileSystemRequest,
    ) -> nas20170626_models.UpgradeFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_file_system_with_options(request, runtime)

    async def upgrade_file_system_async(
        self,
        request: nas20170626_models.UpgradeFileSystemRequest,
    ) -> nas20170626_models.UpgradeFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_file_system_with_options_async(request, runtime)
