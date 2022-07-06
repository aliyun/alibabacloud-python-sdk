# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tag20180828 import models as tag_20180828_models
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
            'cn-qingdao': 'tag.aliyuncs.com',
            'cn-beijing': 'tag.aliyuncs.com',
            'cn-hangzhou': 'tag.aliyuncs.com',
            'cn-shanghai': 'tag.aliyuncs.com',
            'cn-shenzhen': 'tag.aliyuncs.com',
            'cn-hongkong': 'tag.aliyuncs.com',
            'ap-southeast-1': 'tag.aliyuncs.com',
            'us-west-1': 'tag.aliyuncs.com',
            'us-east-1': 'tag.aliyuncs.com',
            'cn-hangzhou-finance': 'tag.aliyuncs.com',
            'cn-shanghai-finance-1': 'tag.aliyuncs.com',
            'ap-northeast-2-pop': 'tag.aliyuncs.com',
            'cn-beijing-finance-pop': 'tag.aliyuncs.com',
            'cn-beijing-gov-1': 'tag.aliyuncs.com',
            'cn-beijing-nu16-b01': 'tag.aliyuncs.com',
            'cn-edge-1': 'tag.aliyuncs.com',
            'cn-fujian': 'tag.aliyuncs.com',
            'cn-haidian-cm12-c01': 'tag.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'tag.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'tag.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'tag.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'tag.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'tag.aliyuncs.com',
            'cn-hangzhou-test-306': 'tag.aliyuncs.com',
            'cn-hongkong-finance-pop': 'tag.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'tag.aliyuncs.com',
            'cn-shanghai-et15-b01': 'tag.aliyuncs.com',
            'cn-shanghai-et2-b01': 'tag.aliyuncs.com',
            'cn-shanghai-inner': 'tag.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'tag.aliyuncs.com',
            'cn-shenzhen-inner': 'tag.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'tag.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'tag.aliyuncs.com',
            'cn-wuhan': 'tag.aliyuncs.com',
            'cn-yushanfang': 'tag.aliyuncs.com',
            'cn-zhangbei': 'tag.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'tag.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'tag.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'tag.aliyuncs.com',
            'eu-west-1-oxs': 'tag.cn-shenzhen-cloudstone.aliyuncs.com',
            'rus-west-1-pop': 'tag.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('tag', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def attach_policy_with_options(
        self,
        request: tag_20180828_models.AttachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.AttachPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachPolicy',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.AttachPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_policy_with_options_async(
        self,
        request: tag_20180828_models.AttachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.AttachPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachPolicy',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.AttachPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_policy(
        self,
        request: tag_20180828_models.AttachPolicyRequest,
    ) -> tag_20180828_models.AttachPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_policy_with_options(request, runtime)

    async def attach_policy_async(
        self,
        request: tag_20180828_models.AttachPolicyRequest,
    ) -> tag_20180828_models.AttachPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_policy_with_options_async(request, runtime)

    def create_policy_with_options(
        self,
        request: tag_20180828_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.CreatePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy_content):
            query['PolicyContent'] = request.policy_content
        if not UtilClient.is_unset(request.policy_desc):
            query['PolicyDesc'] = request.policy_desc
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicy',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.CreatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_with_options_async(
        self,
        request: tag_20180828_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.CreatePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy_content):
            query['PolicyContent'] = request.policy_content
        if not UtilClient.is_unset(request.policy_desc):
            query['PolicyDesc'] = request.policy_desc
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicy',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.CreatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy(
        self,
        request: tag_20180828_models.CreatePolicyRequest,
    ) -> tag_20180828_models.CreatePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_policy_with_options(request, runtime)

    async def create_policy_async(
        self,
        request: tag_20180828_models.CreatePolicyRequest,
    ) -> tag_20180828_models.CreatePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_with_options_async(request, runtime)

    def create_tags_with_options(
        self,
        request: tag_20180828_models.CreateTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.CreateTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.tag_key_value_param_list):
            query['TagKeyValueParamList'] = request.tag_key_value_param_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTags',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.CreateTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tags_with_options_async(
        self,
        request: tag_20180828_models.CreateTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.CreateTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.tag_key_value_param_list):
            query['TagKeyValueParamList'] = request.tag_key_value_param_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTags',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.CreateTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tags(
        self,
        request: tag_20180828_models.CreateTagsRequest,
    ) -> tag_20180828_models.CreateTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_tags_with_options(request, runtime)

    async def create_tags_async(
        self,
        request: tag_20180828_models.CreateTagsRequest,
    ) -> tag_20180828_models.CreateTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_tags_with_options_async(request, runtime)

    def delete_policy_with_options(
        self,
        request: tag_20180828_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.DeletePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicy',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.DeletePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_with_options_async(
        self,
        request: tag_20180828_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.DeletePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicy',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.DeletePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy(
        self,
        request: tag_20180828_models.DeletePolicyRequest,
    ) -> tag_20180828_models.DeletePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_with_options(request, runtime)

    async def delete_policy_async(
        self,
        request: tag_20180828_models.DeletePolicyRequest,
    ) -> tag_20180828_models.DeletePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_with_options_async(request, runtime)

    def delete_tag_with_options(
        self,
        request: tag_20180828_models.DeleteTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.DeleteTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTag',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.DeleteTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tag_with_options_async(
        self,
        request: tag_20180828_models.DeleteTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.DeleteTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTag',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.DeleteTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tag(
        self,
        request: tag_20180828_models.DeleteTagRequest,
    ) -> tag_20180828_models.DeleteTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_with_options(request, runtime)

    async def delete_tag_async(
        self,
        request: tag_20180828_models.DeleteTagRequest,
    ) -> tag_20180828_models.DeleteTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_tag_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: tag_20180828_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: tag_20180828_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: tag_20180828_models.DescribeRegionsRequest,
    ) -> tag_20180828_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: tag_20180828_models.DescribeRegionsRequest,
    ) -> tag_20180828_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def detach_policy_with_options(
        self,
        request: tag_20180828_models.DetachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.DetachPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachPolicy',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.DetachPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_policy_with_options_async(
        self,
        request: tag_20180828_models.DetachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.DetachPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachPolicy',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.DetachPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_policy(
        self,
        request: tag_20180828_models.DetachPolicyRequest,
    ) -> tag_20180828_models.DetachPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_policy_with_options(request, runtime)

    async def detach_policy_async(
        self,
        request: tag_20180828_models.DetachPolicyRequest,
    ) -> tag_20180828_models.DetachPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_policy_with_options_async(request, runtime)

    def disable_policy_type_with_options(
        self,
        request: tag_20180828_models.DisablePolicyTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.DisablePolicyTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisablePolicyType',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.DisablePolicyTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_policy_type_with_options_async(
        self,
        request: tag_20180828_models.DisablePolicyTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.DisablePolicyTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisablePolicyType',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.DisablePolicyTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_policy_type(
        self,
        request: tag_20180828_models.DisablePolicyTypeRequest,
    ) -> tag_20180828_models.DisablePolicyTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_policy_type_with_options(request, runtime)

    async def disable_policy_type_async(
        self,
        request: tag_20180828_models.DisablePolicyTypeRequest,
    ) -> tag_20180828_models.DisablePolicyTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_policy_type_with_options_async(request, runtime)

    def enable_policy_type_with_options(
        self,
        request: tag_20180828_models.EnablePolicyTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.EnablePolicyTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnablePolicyType',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.EnablePolicyTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_policy_type_with_options_async(
        self,
        request: tag_20180828_models.EnablePolicyTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.EnablePolicyTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnablePolicyType',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.EnablePolicyTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_policy_type(
        self,
        request: tag_20180828_models.EnablePolicyTypeRequest,
    ) -> tag_20180828_models.EnablePolicyTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_policy_type_with_options(request, runtime)

    async def enable_policy_type_async(
        self,
        request: tag_20180828_models.EnablePolicyTypeRequest,
    ) -> tag_20180828_models.EnablePolicyTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_policy_type_with_options_async(request, runtime)

    def generate_config_rule_report_with_options(
        self,
        request: tag_20180828_models.GenerateConfigRuleReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.GenerateConfigRuleReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateConfigRuleReport',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.GenerateConfigRuleReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_config_rule_report_with_options_async(
        self,
        request: tag_20180828_models.GenerateConfigRuleReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.GenerateConfigRuleReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateConfigRuleReport',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.GenerateConfigRuleReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_config_rule_report(
        self,
        request: tag_20180828_models.GenerateConfigRuleReportRequest,
    ) -> tag_20180828_models.GenerateConfigRuleReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_config_rule_report_with_options(request, runtime)

    async def generate_config_rule_report_async(
        self,
        request: tag_20180828_models.GenerateConfigRuleReportRequest,
    ) -> tag_20180828_models.GenerateConfigRuleReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_config_rule_report_with_options_async(request, runtime)

    def get_config_rule_report_with_options(
        self,
        request: tag_20180828_models.GetConfigRuleReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.GetConfigRuleReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConfigRuleReport',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.GetConfigRuleReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_config_rule_report_with_options_async(
        self,
        request: tag_20180828_models.GetConfigRuleReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.GetConfigRuleReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConfigRuleReport',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.GetConfigRuleReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_config_rule_report(
        self,
        request: tag_20180828_models.GetConfigRuleReportRequest,
    ) -> tag_20180828_models.GetConfigRuleReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_config_rule_report_with_options(request, runtime)

    async def get_config_rule_report_async(
        self,
        request: tag_20180828_models.GetConfigRuleReportRequest,
    ) -> tag_20180828_models.GetConfigRuleReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_config_rule_report_with_options_async(request, runtime)

    def get_effective_policy_with_options(
        self,
        request: tag_20180828_models.GetEffectivePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.GetEffectivePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEffectivePolicy',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.GetEffectivePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_effective_policy_with_options_async(
        self,
        request: tag_20180828_models.GetEffectivePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.GetEffectivePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEffectivePolicy',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.GetEffectivePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_effective_policy(
        self,
        request: tag_20180828_models.GetEffectivePolicyRequest,
    ) -> tag_20180828_models.GetEffectivePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_effective_policy_with_options(request, runtime)

    async def get_effective_policy_async(
        self,
        request: tag_20180828_models.GetEffectivePolicyRequest,
    ) -> tag_20180828_models.GetEffectivePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_effective_policy_with_options_async(request, runtime)

    def get_policy_with_options(
        self,
        request: tag_20180828_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.GetPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicy',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.GetPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_with_options_async(
        self,
        request: tag_20180828_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.GetPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicy',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.GetPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy(
        self,
        request: tag_20180828_models.GetPolicyRequest,
    ) -> tag_20180828_models.GetPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_policy_with_options(request, runtime)

    async def get_policy_async(
        self,
        request: tag_20180828_models.GetPolicyRequest,
    ) -> tag_20180828_models.GetPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_with_options_async(request, runtime)

    def get_policy_enable_status_with_options(
        self,
        request: tag_20180828_models.GetPolicyEnableStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.GetPolicyEnableStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicyEnableStatus',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.GetPolicyEnableStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_enable_status_with_options_async(
        self,
        request: tag_20180828_models.GetPolicyEnableStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.GetPolicyEnableStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicyEnableStatus',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.GetPolicyEnableStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy_enable_status(
        self,
        request: tag_20180828_models.GetPolicyEnableStatusRequest,
    ) -> tag_20180828_models.GetPolicyEnableStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_policy_enable_status_with_options(request, runtime)

    async def get_policy_enable_status_async(
        self,
        request: tag_20180828_models.GetPolicyEnableStatusRequest,
    ) -> tag_20180828_models.GetPolicyEnableStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_enable_status_with_options_async(request, runtime)

    def list_config_rules_for_target_with_options(
        self,
        request: tag_20180828_models.ListConfigRulesForTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListConfigRulesForTargetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigRulesForTarget',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.ListConfigRulesForTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_rules_for_target_with_options_async(
        self,
        request: tag_20180828_models.ListConfigRulesForTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListConfigRulesForTargetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigRulesForTarget',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.ListConfigRulesForTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_rules_for_target(
        self,
        request: tag_20180828_models.ListConfigRulesForTargetRequest,
    ) -> tag_20180828_models.ListConfigRulesForTargetResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_config_rules_for_target_with_options(request, runtime)

    async def list_config_rules_for_target_async(
        self,
        request: tag_20180828_models.ListConfigRulesForTargetRequest,
    ) -> tag_20180828_models.ListConfigRulesForTargetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_config_rules_for_target_with_options_async(request, runtime)

    def list_policies_with_options(
        self,
        request: tag_20180828_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy_ids):
            query['PolicyIds'] = request.policy_ids
        if not UtilClient.is_unset(request.policy_names):
            query['PolicyNames'] = request.policy_names
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicies',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.ListPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_with_options_async(
        self,
        request: tag_20180828_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy_ids):
            query['PolicyIds'] = request.policy_ids
        if not UtilClient.is_unset(request.policy_names):
            query['PolicyNames'] = request.policy_names
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicies',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.ListPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies(
        self,
        request: tag_20180828_models.ListPoliciesRequest,
    ) -> tag_20180828_models.ListPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_policies_with_options(request, runtime)

    async def list_policies_async(
        self,
        request: tag_20180828_models.ListPoliciesRequest,
    ) -> tag_20180828_models.ListPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_policies_with_options_async(request, runtime)

    def list_policies_for_target_with_options(
        self,
        request: tag_20180828_models.ListPoliciesForTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListPoliciesForTargetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPoliciesForTarget',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.ListPoliciesForTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_for_target_with_options_async(
        self,
        request: tag_20180828_models.ListPoliciesForTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListPoliciesForTargetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPoliciesForTarget',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.ListPoliciesForTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies_for_target(
        self,
        request: tag_20180828_models.ListPoliciesForTargetRequest,
    ) -> tag_20180828_models.ListPoliciesForTargetResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_policies_for_target_with_options(request, runtime)

    async def list_policies_for_target_async(
        self,
        request: tag_20180828_models.ListPoliciesForTargetRequest,
    ) -> tag_20180828_models.ListPoliciesForTargetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_policies_for_target_with_options_async(request, runtime)

    def list_resources_by_tag_with_options(
        self,
        request: tag_20180828_models.ListResourcesByTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListResourcesByTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fuzzy_type):
            query['FuzzyType'] = request.fuzzy_type
        if not UtilClient.is_unset(request.include_all_tags):
            query['IncludeAllTags'] = request.include_all_tags
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourcesByTag',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.ListResourcesByTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_by_tag_with_options_async(
        self,
        request: tag_20180828_models.ListResourcesByTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListResourcesByTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fuzzy_type):
            query['FuzzyType'] = request.fuzzy_type
        if not UtilClient.is_unset(request.include_all_tags):
            query['IncludeAllTags'] = request.include_all_tags
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourcesByTag',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.ListResourcesByTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources_by_tag(
        self,
        request: tag_20180828_models.ListResourcesByTagRequest,
    ) -> tag_20180828_models.ListResourcesByTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resources_by_tag_with_options(request, runtime)

    async def list_resources_by_tag_async(
        self,
        request: tag_20180828_models.ListResourcesByTagRequest,
    ) -> tag_20180828_models.ListResourcesByTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resources_by_tag_with_options_async(request, runtime)

    def list_support_resource_types_with_options(
        self,
        request: tag_20180828_models.ListSupportResourceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListSupportResourceTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_tye):
            query['ResourceTye'] = request.resource_tye
        if not UtilClient.is_unset(request.show_items):
            query['ShowItems'] = request.show_items
        if not UtilClient.is_unset(request.support_code):
            query['SupportCode'] = request.support_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSupportResourceTypes',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.ListSupportResourceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_support_resource_types_with_options_async(
        self,
        request: tag_20180828_models.ListSupportResourceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListSupportResourceTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_tye):
            query['ResourceTye'] = request.resource_tye
        if not UtilClient.is_unset(request.show_items):
            query['ShowItems'] = request.show_items
        if not UtilClient.is_unset(request.support_code):
            query['SupportCode'] = request.support_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSupportResourceTypes',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.ListSupportResourceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_support_resource_types(
        self,
        request: tag_20180828_models.ListSupportResourceTypesRequest,
    ) -> tag_20180828_models.ListSupportResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_support_resource_types_with_options(request, runtime)

    async def list_support_resource_types_async(
        self,
        request: tag_20180828_models.ListSupportResourceTypesRequest,
    ) -> tag_20180828_models.ListSupportResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_support_resource_types_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: tag_20180828_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.fuzzy_type):
            query['FuzzyType'] = request.fuzzy_type
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: tag_20180828_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.fuzzy_type):
            query['FuzzyType'] = request.fuzzy_type
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: tag_20180828_models.ListTagKeysRequest,
    ) -> tag_20180828_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: tag_20180828_models.ListTagKeysRequest,
    ) -> tag_20180828_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: tag_20180828_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_arn):
            query['ResourceARN'] = request.resource_arn
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: tag_20180828_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_arn):
            query['ResourceARN'] = request.resource_arn
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: tag_20180828_models.ListTagResourcesRequest,
    ) -> tag_20180828_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: tag_20180828_models.ListTagResourcesRequest,
    ) -> tag_20180828_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: tag_20180828_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fuzzy_type):
            query['FuzzyType'] = request.fuzzy_type
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: tag_20180828_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fuzzy_type):
            query['FuzzyType'] = request.fuzzy_type
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: tag_20180828_models.ListTagValuesRequest,
    ) -> tag_20180828_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: tag_20180828_models.ListTagValuesRequest,
    ) -> tag_20180828_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def list_targets_for_policy_with_options(
        self,
        request: tag_20180828_models.ListTargetsForPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTargetsForPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTargetsForPolicy',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.ListTargetsForPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_targets_for_policy_with_options_async(
        self,
        request: tag_20180828_models.ListTargetsForPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTargetsForPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTargetsForPolicy',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.ListTargetsForPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_targets_for_policy(
        self,
        request: tag_20180828_models.ListTargetsForPolicyRequest,
    ) -> tag_20180828_models.ListTargetsForPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_targets_for_policy_with_options(request, runtime)

    async def list_targets_for_policy_async(
        self,
        request: tag_20180828_models.ListTargetsForPolicyRequest,
    ) -> tag_20180828_models.ListTargetsForPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_targets_for_policy_with_options_async(request, runtime)

    def modify_policy_with_options(
        self,
        request: tag_20180828_models.ModifyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ModifyPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy_content):
            query['PolicyContent'] = request.policy_content
        if not UtilClient.is_unset(request.policy_desc):
            query['PolicyDesc'] = request.policy_desc
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPolicy',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.ModifyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_policy_with_options_async(
        self,
        request: tag_20180828_models.ModifyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ModifyPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy_content):
            query['PolicyContent'] = request.policy_content
        if not UtilClient.is_unset(request.policy_desc):
            query['PolicyDesc'] = request.policy_desc
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPolicy',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.ModifyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_policy(
        self,
        request: tag_20180828_models.ModifyPolicyRequest,
    ) -> tag_20180828_models.ModifyPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_policy_with_options(request, runtime)

    async def modify_policy_async(
        self,
        request: tag_20180828_models.ModifyPolicyRequest,
    ) -> tag_20180828_models.ModifyPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_policy_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: tag_20180828_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_arn):
            query['ResourceARN'] = request.resource_arn
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: tag_20180828_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_arn):
            query['ResourceARN'] = request.resource_arn
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: tag_20180828_models.TagResourcesRequest,
    ) -> tag_20180828_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: tag_20180828_models.TagResourcesRequest,
    ) -> tag_20180828_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: tag_20180828_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_arn):
            query['ResourceARN'] = request.resource_arn
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: tag_20180828_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_arn):
            query['ResourceARN'] = request.resource_arn
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tag_20180828_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: tag_20180828_models.UntagResourcesRequest,
    ) -> tag_20180828_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: tag_20180828_models.UntagResourcesRequest,
    ) -> tag_20180828_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
