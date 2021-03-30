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
        query = {}
        query['RegionId'] = request.region_id
        query['FileSystemId'] = request.file_system_id
        query['ClientIP'] = request.client_ip
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddClientToBlackList',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.AddClientToBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_client_to_black_list_with_options_async(
        self,
        request: nas20170626_models.AddClientToBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.AddClientToBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['FileSystemId'] = request.file_system_id
        query['ClientIP'] = request.client_ip
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddClientToBlackList',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.AddClientToBlackListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddTags',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.AddTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_tags_with_options_async(
        self,
        request: nas20170626_models.AddTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.AddTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddTags',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.AddTagsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        query['FileSystemIds'] = request.file_system_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ApplyAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ApplyAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_auto_snapshot_policy_with_options_async(
        self,
        request: nas20170626_models.ApplyAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ApplyAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        query['FileSystemIds'] = request.file_system_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ApplyAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ApplyAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemIds'] = request.file_system_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CancelAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_auto_snapshot_policy_with_options_async(
        self,
        request: nas20170626_models.CancelAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemIds'] = request.file_system_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CancelAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['Path'] = request.path
        query['UserType'] = request.user_type
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CancelDirQuota',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelDirQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_dir_quota_with_options_async(
        self,
        request: nas20170626_models.CancelDirQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelDirQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['Path'] = request.path
        query['UserType'] = request.user_type
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CancelDirQuota',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelDirQuotaResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CancelLifecycleRetrieveJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelLifecycleRetrieveJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_lifecycle_retrieve_job_with_options_async(
        self,
        request: nas20170626_models.CancelLifecycleRetrieveJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelLifecycleRetrieveJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CancelLifecycleRetrieveJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelLifecycleRetrieveJobResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_access_group_with_options(
        self,
        request: nas20170626_models.CreateAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateAccessGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessGroupName'] = request.access_group_name
        query['AccessGroupType'] = request.access_group_type
        query['Description'] = request.description
        query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccessGroup',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAccessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_group_with_options_async(
        self,
        request: nas20170626_models.CreateAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateAccessGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessGroupName'] = request.access_group_name
        query['AccessGroupType'] = request.access_group_type
        query['Description'] = request.description
        query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccessGroup',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAccessGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AccessGroupName'] = request.access_group_name
        query['SourceCidrIp'] = request.source_cidr_ip
        query['RWAccessType'] = request.rwaccess_type
        query['UserAccessType'] = request.user_access_type
        query['Priority'] = request.priority
        query['FileSystemType'] = request.file_system_type
        query['Ipv6SourceCidrIp'] = request.ipv_6source_cidr_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccessRule',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_rule_with_options_async(
        self,
        request: nas20170626_models.CreateAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateAccessRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessGroupName'] = request.access_group_name
        query['SourceCidrIp'] = request.source_cidr_ip
        query['RWAccessType'] = request.rwaccess_type
        query['UserAccessType'] = request.user_access_type
        query['Priority'] = request.priority
        query['FileSystemType'] = request.file_system_type
        query['Ipv6SourceCidrIp'] = request.ipv_6source_cidr_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccessRule',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RepeatWeekdays'] = request.repeat_weekdays
        query['TimePoints'] = request.time_points
        query['RetentionDays'] = request.retention_days
        query['AutoSnapshotPolicyName'] = request.auto_snapshot_policy_name
        query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_auto_snapshot_policy_with_options_async(
        self,
        request: nas20170626_models.CreateAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RepeatWeekdays'] = request.repeat_weekdays
        query['TimePoints'] = request.time_points
        query['RetentionDays'] = request.retention_days
        query['AutoSnapshotPolicyName'] = request.auto_snapshot_policy_name
        query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemType'] = request.file_system_type
        query['ChargeType'] = request.charge_type
        query['Duration'] = request.duration
        query['Capacity'] = request.capacity
        query['Bandwidth'] = request.bandwidth
        query['StorageType'] = request.storage_type
        query['ZoneId'] = request.zone_id
        query['ProtocolType'] = request.protocol_type
        query['EncryptType'] = request.encrypt_type
        query['SnapshotId'] = request.snapshot_id
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['Description'] = request.description
        query['ClientToken'] = request.client_token
        query['KmsKeyId'] = request.kms_key_id
        query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_file_system_with_options_async(
        self,
        request: nas20170626_models.CreateFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateFileSystemResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemType'] = request.file_system_type
        query['ChargeType'] = request.charge_type
        query['Duration'] = request.duration
        query['Capacity'] = request.capacity
        query['Bandwidth'] = request.bandwidth
        query['StorageType'] = request.storage_type
        query['ZoneId'] = request.zone_id
        query['ProtocolType'] = request.protocol_type
        query['EncryptType'] = request.encrypt_type
        query['SnapshotId'] = request.snapshot_id
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['Description'] = request.description
        query['ClientToken'] = request.client_token
        query['KmsKeyId'] = request.kms_key_id
        query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['URI'] = request.uri
        query['BindDN'] = request.bind_dn
        query['SearchBase'] = request.search_base
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateLDAPConfig',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLDAPConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ldapconfig_with_options_async(
        self,
        request: nas20170626_models.CreateLDAPConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateLDAPConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['URI'] = request.uri
        query['BindDN'] = request.bind_dn
        query['SearchBase'] = request.search_base
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateLDAPConfig',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLDAPConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['LifecyclePolicyName'] = request.lifecycle_policy_name
        query['Path'] = request.path
        query['LifecycleRuleName'] = request.lifecycle_rule_name
        query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateLifecyclePolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLifecyclePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_lifecycle_policy_with_options_async(
        self,
        request: nas20170626_models.CreateLifecyclePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateLifecyclePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['LifecyclePolicyName'] = request.lifecycle_policy_name
        query['Path'] = request.path
        query['LifecycleRuleName'] = request.lifecycle_rule_name
        query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateLifecyclePolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLifecyclePolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['Paths'] = request.paths
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateLifecycleRetrieveJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLifecycleRetrieveJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_lifecycle_retrieve_job_with_options_async(
        self,
        request: nas20170626_models.CreateLifecycleRetrieveJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateLifecycleRetrieveJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['Paths'] = request.paths
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateLifecycleRetrieveJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLifecycleRetrieveJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['AccessGroupName'] = request.access_group_name
        query['NetworkType'] = request.network_type
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['SecurityGroupId'] = request.security_group_id
        query['EnableIpv6'] = request.enable_ipv_6
        query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mount_target_with_options_async(
        self,
        request: nas20170626_models.CreateMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateMountTargetResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['AccessGroupName'] = request.access_group_name
        query['NetworkType'] = request.network_type
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['SecurityGroupId'] = request.security_group_id
        query['EnableIpv6'] = request.enable_ipv_6
        query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_snapshot_with_options(
        self,
        request: nas20170626_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['SnapshotName'] = request.snapshot_name
        query['Description'] = request.description
        query['RetentionDays'] = request.retention_days
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_snapshot_with_options_async(
        self,
        request: nas20170626_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['SnapshotName'] = request.snapshot_name
        query['Description'] = request.description
        query['RetentionDays'] = request.retention_days
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AccessGroupName'] = request.access_group_name
        query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAccessGroup',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAccessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_group_with_options_async(
        self,
        request: nas20170626_models.DeleteAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteAccessGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessGroupName'] = request.access_group_name
        query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAccessGroup',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAccessGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AccessGroupName'] = request.access_group_name
        query['AccessRuleId'] = request.access_rule_id
        query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAccessRule',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_rule_with_options_async(
        self,
        request: nas20170626_models.DeleteAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteAccessRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessGroupName'] = request.access_group_name
        query['AccessRuleId'] = request.access_rule_id
        query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAccessRule',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_auto_snapshot_policy_with_options_async(
        self,
        request: nas20170626_models.DeleteAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_file_system_with_options_async(
        self,
        request: nas20170626_models.DeleteFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteFileSystemResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteLDAPConfig',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteLDAPConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ldapconfig_with_options_async(
        self,
        request: nas20170626_models.DeleteLDAPConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteLDAPConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteLDAPConfig',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteLDAPConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['LifecyclePolicyName'] = request.lifecycle_policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteLifecyclePolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteLifecyclePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_lifecycle_policy_with_options_async(
        self,
        request: nas20170626_models.DeleteLifecyclePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteLifecyclePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['LifecyclePolicyName'] = request.lifecycle_policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteLifecyclePolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteLifecyclePolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['MountTargetDomain'] = request.mount_target_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mount_target_with_options_async(
        self,
        request: nas20170626_models.DeleteMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteMountTargetResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['MountTargetDomain'] = request.mount_target_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_snapshot_with_options_async(
        self,
        request: nas20170626_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AccessGroupName'] = request.access_group_name
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['UseUTCDateTime'] = request.use_utcdate_time
        query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAccessGroups',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAccessGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_groups_with_options_async(
        self,
        request: nas20170626_models.DescribeAccessGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAccessGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessGroupName'] = request.access_group_name
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['UseUTCDateTime'] = request.use_utcdate_time
        query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAccessGroups',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAccessGroupsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AccessGroupName'] = request.access_group_name
        query['AccessRuleId'] = request.access_rule_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAccessRules',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAccessRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_rules_with_options_async(
        self,
        request: nas20170626_models.DescribeAccessRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAccessRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessGroupName'] = request.access_group_name
        query['AccessRuleId'] = request.access_rule_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAccessRules',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAccessRulesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAutoSnapshotPolicies',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAutoSnapshotPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_snapshot_policies_with_options_async(
        self,
        request: nas20170626_models.DescribeAutoSnapshotPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAutoSnapshotPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAutoSnapshotPolicies',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAutoSnapshotPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemIds'] = request.file_system_ids
        query['AutoSnapshotPolicyIds'] = request.auto_snapshot_policy_ids
        query['FileSystemType'] = request.file_system_type
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAutoSnapshotTasks',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAutoSnapshotTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_snapshot_tasks_with_options_async(
        self,
        request: nas20170626_models.DescribeAutoSnapshotTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAutoSnapshotTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemIds'] = request.file_system_ids
        query['AutoSnapshotPolicyIds'] = request.auto_snapshot_policy_ids
        query['FileSystemType'] = request.file_system_type
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAutoSnapshotTasks',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAutoSnapshotTasksResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['FileSystemId'] = request.file_system_id
        query['ClientIP'] = request.client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBlackListClients',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeBlackListClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_black_list_clients_with_options_async(
        self,
        request: nas20170626_models.DescribeBlackListClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeBlackListClientsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['FileSystemId'] = request.file_system_id
        query['ClientIP'] = request.client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBlackListClients',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeBlackListClientsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['Path'] = request.path
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDirQuotas',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeDirQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dir_quotas_with_options_async(
        self,
        request: nas20170626_models.DescribeDirQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeDirQuotasResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['Path'] = request.path
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDirQuotas',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeDirQuotasResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['FileSystemType'] = request.file_system_type
        query['VpcId'] = request.vpc_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFileSystems',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeFileSystemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_file_systems_with_options_async(
        self,
        request: nas20170626_models.DescribeFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeFileSystemsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['FileSystemType'] = request.file_system_type
        query['VpcId'] = request.vpc_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFileSystems',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeFileSystemsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFileSystemStatistics',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeFileSystemStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_file_system_statistics_with_options_async(
        self,
        request: nas20170626_models.DescribeFileSystemStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeFileSystemStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFileSystemStatistics',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeFileSystemStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLDAPConfig',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeLDAPConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ldapconfig_with_options_async(
        self,
        request: nas20170626_models.DescribeLDAPConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeLDAPConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLDAPConfig',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeLDAPConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLifecyclePolicies',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeLifecyclePoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lifecycle_policies_with_options_async(
        self,
        request: nas20170626_models.DescribeLifecyclePoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeLifecyclePoliciesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLifecyclePolicies',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeLifecyclePoliciesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLogAnalysis',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeLogAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_analysis_with_options_async(
        self,
        request: nas20170626_models.DescribeLogAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeLogAnalysisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLogAnalysis',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeLogAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['PageSize'] = request.page_size
        query['FileSystemId'] = request.file_system_id
        query['ClientIP'] = request.client_ip
        query['MountTargetDomain'] = request.mount_target_domain
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMountedClients',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeMountedClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mounted_clients_with_options_async(
        self,
        request: nas20170626_models.DescribeMountedClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeMountedClientsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['PageSize'] = request.page_size
        query['FileSystemId'] = request.file_system_id
        query['ClientIP'] = request.client_ip
        query['MountTargetDomain'] = request.mount_target_domain
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMountedClients',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeMountedClientsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['MountTargetDomain'] = request.mount_target_domain
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['DualStackMountTargetDomain'] = request.dual_stack_mount_target_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMountTargets',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeMountTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mount_targets_with_options_async(
        self,
        request: nas20170626_models.DescribeMountTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeMountTargetsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['MountTargetDomain'] = request.mount_target_domain
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['DualStackMountTargetDomain'] = request.dual_stack_mount_target_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMountTargets',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeMountTargetsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: nas20170626_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemType'] = request.file_system_type
        query['FileSystemId'] = request.file_system_id
        query['SnapshotIds'] = request.snapshot_ids
        query['SnapshotName'] = request.snapshot_name
        query['SnapshotType'] = request.snapshot_type
        query['Status'] = request.status
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSnapshots',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_snapshots_with_options_async(
        self,
        request: nas20170626_models.DescribeSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeSnapshotsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemType'] = request.file_system_type
        query['FileSystemId'] = request.file_system_id
        query['SnapshotIds'] = request.snapshot_ids
        query['SnapshotName'] = request.snapshot_name
        query['SnapshotType'] = request.snapshot_type
        query['Status'] = request.status
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSnapshots',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['PageSize'] = request.page_size
        query['UseUTCDateTime'] = request.use_utcdate_time
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeStoragePackages',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeStoragePackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_storage_packages_with_options_async(
        self,
        request: nas20170626_models.DescribeStoragePackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeStoragePackagesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['PageSize'] = request.page_size
        query['UseUTCDateTime'] = request.use_utcdate_time
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeStoragePackages',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeStoragePackagesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: nas20170626_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeTagsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: nas20170626_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_directory_or_file_properties_with_options(
        self,
        request: nas20170626_models.GetDirectoryOrFilePropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.GetDirectoryOrFilePropertiesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDirectoryOrFileProperties',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.GetDirectoryOrFilePropertiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_directory_or_file_properties_with_options_async(
        self,
        request: nas20170626_models.GetDirectoryOrFilePropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.GetDirectoryOrFilePropertiesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDirectoryOrFileProperties',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.GetDirectoryOrFilePropertiesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_directories_and_files_with_options(
        self,
        request: nas20170626_models.ListDirectoriesAndFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListDirectoriesAndFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['Path'] = request.path
        query['NextToken'] = request.next_token
        query['StorageType'] = request.storage_type
        query['DirectoryOnly'] = request.directory_only
        query['MaxResults'] = request.max_results
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListDirectoriesAndFiles',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListDirectoriesAndFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_directories_and_files_with_options_async(
        self,
        request: nas20170626_models.ListDirectoriesAndFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListDirectoriesAndFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['Path'] = request.path
        query['NextToken'] = request.next_token
        query['StorageType'] = request.storage_type
        query['DirectoryOnly'] = request.directory_only
        query['MaxResults'] = request.max_results
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListDirectoriesAndFiles',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListDirectoriesAndFilesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['FileSystemId'] = request.file_system_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListLifecycleRetrieveJobs',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListLifecycleRetrieveJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_lifecycle_retrieve_jobs_with_options_async(
        self,
        request: nas20170626_models.ListLifecycleRetrieveJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListLifecycleRetrieveJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['FileSystemId'] = request.file_system_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListLifecycleRetrieveJobs',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListLifecycleRetrieveJobsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_tag_resources_with_options(
        self,
        request: nas20170626_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceType'] = request.resource_type
        query['NextToken'] = request.next_token
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: nas20170626_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceType'] = request.resource_type
        query['NextToken'] = request.next_token
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AccessGroupName'] = request.access_group_name
        query['Description'] = request.description
        query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyAccessGroup',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAccessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_access_group_with_options_async(
        self,
        request: nas20170626_models.ModifyAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyAccessGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessGroupName'] = request.access_group_name
        query['Description'] = request.description
        query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyAccessGroup',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAccessGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AccessGroupName'] = request.access_group_name
        query['AccessRuleId'] = request.access_rule_id
        query['SourceCidrIp'] = request.source_cidr_ip
        query['RWAccessType'] = request.rwaccess_type
        query['UserAccessType'] = request.user_access_type
        query['Priority'] = request.priority
        query['FileSystemType'] = request.file_system_type
        query['Ipv6SourceCidrIp'] = request.ipv_6source_cidr_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyAccessRule',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_access_rule_with_options_async(
        self,
        request: nas20170626_models.ModifyAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyAccessRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessGroupName'] = request.access_group_name
        query['AccessRuleId'] = request.access_rule_id
        query['SourceCidrIp'] = request.source_cidr_ip
        query['RWAccessType'] = request.rwaccess_type
        query['UserAccessType'] = request.user_access_type
        query['Priority'] = request.priority
        query['FileSystemType'] = request.file_system_type
        query['Ipv6SourceCidrIp'] = request.ipv_6source_cidr_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyAccessRule',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        query['AutoSnapshotPolicyName'] = request.auto_snapshot_policy_name
        query['RepeatWeekdays'] = request.repeat_weekdays
        query['RetentionDays'] = request.retention_days
        query['TimePoints'] = request.time_points
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_auto_snapshot_policy_with_options_async(
        self,
        request: nas20170626_models.ModifyAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        query['AutoSnapshotPolicyName'] = request.auto_snapshot_policy_name
        query['RepeatWeekdays'] = request.repeat_weekdays
        query['RetentionDays'] = request.retention_days
        query['TimePoints'] = request.time_points
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_file_system_with_options_async(
        self,
        request: nas20170626_models.ModifyFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyFileSystemResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['URI'] = request.uri
        query['BindDN'] = request.bind_dn
        query['SearchBase'] = request.search_base
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyLDAPConfig',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyLDAPConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ldapconfig_with_options_async(
        self,
        request: nas20170626_models.ModifyLDAPConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyLDAPConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['URI'] = request.uri
        query['BindDN'] = request.bind_dn
        query['SearchBase'] = request.search_base
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyLDAPConfig',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyLDAPConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['LifecyclePolicyName'] = request.lifecycle_policy_name
        query['Path'] = request.path
        query['LifecycleRuleName'] = request.lifecycle_rule_name
        query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyLifecyclePolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyLifecyclePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_lifecycle_policy_with_options_async(
        self,
        request: nas20170626_models.ModifyLifecyclePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyLifecyclePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['LifecyclePolicyName'] = request.lifecycle_policy_name
        query['Path'] = request.path
        query['LifecycleRuleName'] = request.lifecycle_rule_name
        query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyLifecyclePolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyLifecyclePolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['MountTargetDomain'] = request.mount_target_domain
        query['AccessGroupName'] = request.access_group_name
        query['Status'] = request.status
        query['DualStackMountTargetDomain'] = request.dual_stack_mount_target_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_mount_target_with_options_async(
        self,
        request: nas20170626_models.ModifyMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyMountTargetResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['MountTargetDomain'] = request.mount_target_domain
        query['AccessGroupName'] = request.access_group_name
        query['Status'] = request.status
        query['DualStackMountTargetDomain'] = request.dual_stack_mount_target_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='OpenNASService',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.OpenNASServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_nasservice_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.OpenNASServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenNASService',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.OpenNASServiceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['FileSystemId'] = request.file_system_id
        query['ClientIP'] = request.client_ip
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveClientFromBlackList',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.RemoveClientFromBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_client_from_black_list_with_options_async(
        self,
        request: nas20170626_models.RemoveClientFromBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.RemoveClientFromBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['FileSystemId'] = request.file_system_id
        query['ClientIP'] = request.client_ip
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveClientFromBlackList',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.RemoveClientFromBlackListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveTags',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.RemoveTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_tags_with_options_async(
        self,
        request: nas20170626_models.RemoveTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.RemoveTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveTags',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.RemoveTagsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ResetFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_file_system_with_options_async(
        self,
        request: nas20170626_models.ResetFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ResetFileSystemResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ResetFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RetryLifecycleRetrieveJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.RetryLifecycleRetrieveJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_lifecycle_retrieve_job_with_options_async(
        self,
        request: nas20170626_models.RetryLifecycleRetrieveJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.RetryLifecycleRetrieveJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RetryLifecycleRetrieveJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.RetryLifecycleRetrieveJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['Path'] = request.path
        query['QuotaType'] = request.quota_type
        query['UserType'] = request.user_type
        query['UserId'] = request.user_id
        query['SizeLimit'] = request.size_limit
        query['FileCountLimit'] = request.file_count_limit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDirQuota',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.SetDirQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dir_quota_with_options_async(
        self,
        request: nas20170626_models.SetDirQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.SetDirQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['Path'] = request.path
        query['QuotaType'] = request.quota_type
        query['UserType'] = request.user_type
        query['UserId'] = request.user_id
        query['SizeLimit'] = request.size_limit
        query['FileCountLimit'] = request.file_count_limit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDirQuota',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.SetDirQuotaResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceType'] = request.resource_type
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: nas20170626_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceType'] = request.resource_type
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceType'] = request.resource_type
        query['All'] = request.all
        query['ResourceId'] = request.resource_id
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: nas20170626_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceType'] = request.resource_type
        query['All'] = request.all
        query['ResourceId'] = request.resource_id
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def upgrade_file_system_with_options(
        self,
        request: nas20170626_models.UpgradeFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.UpgradeFileSystemResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['Capacity'] = request.capacity
        query['DryRun'] = request.dry_run
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpgradeFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.UpgradeFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_file_system_with_options_async(
        self,
        request: nas20170626_models.UpgradeFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.UpgradeFileSystemResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileSystemId'] = request.file_system_id
        query['Capacity'] = request.capacity
        query['DryRun'] = request.dry_run
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpgradeFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.UpgradeFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
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
