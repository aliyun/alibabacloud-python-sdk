# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_gateway_pop.client import Client as GatewayClientClient
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
        self._product_id = 'Tag'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
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
        """
        @summary 绑定策略
        
        @description If you use the Tag Policy feature in single-account mode, you can call this API operation to attach a tag policy to the current logon account. If you use the Tag Policy feature in multi-account mode, you can call this API operation to attach a tag policy to the Root folder, a folder other than the Root folder, or a member in a resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to attach the tag policy with an ID of `p-de62a0bf400e4b69***` to the current logon account. In this example, the Tag Policy feature in single-account mode is used.
        
        @param request: AttachPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachPolicyResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.AttachPolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.AttachPolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def attach_policy_with_options_async(
        self,
        request: tag_20180828_models.AttachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.AttachPolicyResponse:
        """
        @summary 绑定策略
        
        @description If you use the Tag Policy feature in single-account mode, you can call this API operation to attach a tag policy to the current logon account. If you use the Tag Policy feature in multi-account mode, you can call this API operation to attach a tag policy to the Root folder, a folder other than the Root folder, or a member in a resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to attach the tag policy with an ID of `p-de62a0bf400e4b69***` to the current logon account. In this example, the Tag Policy feature in single-account mode is used.
        
        @param request: AttachPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachPolicyResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.AttachPolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.AttachPolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def attach_policy(
        self,
        request: tag_20180828_models.AttachPolicyRequest,
    ) -> tag_20180828_models.AttachPolicyResponse:
        """
        @summary 绑定策略
        
        @description If you use the Tag Policy feature in single-account mode, you can call this API operation to attach a tag policy to the current logon account. If you use the Tag Policy feature in multi-account mode, you can call this API operation to attach a tag policy to the Root folder, a folder other than the Root folder, or a member in a resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to attach the tag policy with an ID of `p-de62a0bf400e4b69***` to the current logon account. In this example, the Tag Policy feature in single-account mode is used.
        
        @param request: AttachPolicyRequest
        @return: AttachPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_policy_with_options(request, runtime)

    async def attach_policy_async(
        self,
        request: tag_20180828_models.AttachPolicyRequest,
    ) -> tag_20180828_models.AttachPolicyResponse:
        """
        @summary 绑定策略
        
        @description If you use the Tag Policy feature in single-account mode, you can call this API operation to attach a tag policy to the current logon account. If you use the Tag Policy feature in multi-account mode, you can call this API operation to attach a tag policy to the Root folder, a folder other than the Root folder, or a member in a resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to attach the tag policy with an ID of `p-de62a0bf400e4b69***` to the current logon account. In this example, the Tag Policy feature in single-account mode is used.
        
        @param request: AttachPolicyRequest
        @return: AttachPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_policy_with_options_async(request, runtime)

    def check_created_by_enabled_with_options(
        self,
        request: tag_20180828_models.CheckCreatedByEnabledRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.CheckCreatedByEnabledResponse:
        """
        @summary 校验CreatedBy开通状态
        
        @param request: CheckCreatedByEnabledRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCreatedByEnabledResponse
        """
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCreatedByEnabled',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.CheckCreatedByEnabledResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.CheckCreatedByEnabledResponse(),
                self.execute(params, req, runtime)
            )

    async def check_created_by_enabled_with_options_async(
        self,
        request: tag_20180828_models.CheckCreatedByEnabledRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.CheckCreatedByEnabledResponse:
        """
        @summary 校验CreatedBy开通状态
        
        @param request: CheckCreatedByEnabledRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCreatedByEnabledResponse
        """
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCreatedByEnabled',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.CheckCreatedByEnabledResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.CheckCreatedByEnabledResponse(),
                await self.execute_async(params, req, runtime)
            )

    def check_created_by_enabled(
        self,
        request: tag_20180828_models.CheckCreatedByEnabledRequest,
    ) -> tag_20180828_models.CheckCreatedByEnabledResponse:
        """
        @summary 校验CreatedBy开通状态
        
        @param request: CheckCreatedByEnabledRequest
        @return: CheckCreatedByEnabledResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_created_by_enabled_with_options(request, runtime)

    async def check_created_by_enabled_async(
        self,
        request: tag_20180828_models.CheckCreatedByEnabledRequest,
    ) -> tag_20180828_models.CheckCreatedByEnabledResponse:
        """
        @summary 校验CreatedBy开通状态
        
        @param request: CheckCreatedByEnabledRequest
        @return: CheckCreatedByEnabledResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_created_by_enabled_with_options_async(request, runtime)

    def close_created_by_with_options(
        self,
        request: tag_20180828_models.CloseCreatedByRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.CloseCreatedByResponse:
        """
        @summary 关闭CreatedBy服务
        
        @param request: CloseCreatedByRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseCreatedByResponse
        """
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseCreatedBy',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.CloseCreatedByResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.CloseCreatedByResponse(),
                self.execute(params, req, runtime)
            )

    async def close_created_by_with_options_async(
        self,
        request: tag_20180828_models.CloseCreatedByRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.CloseCreatedByResponse:
        """
        @summary 关闭CreatedBy服务
        
        @param request: CloseCreatedByRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseCreatedByResponse
        """
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseCreatedBy',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.CloseCreatedByResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.CloseCreatedByResponse(),
                await self.execute_async(params, req, runtime)
            )

    def close_created_by(
        self,
        request: tag_20180828_models.CloseCreatedByRequest,
    ) -> tag_20180828_models.CloseCreatedByResponse:
        """
        @summary 关闭CreatedBy服务
        
        @param request: CloseCreatedByRequest
        @return: CloseCreatedByResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.close_created_by_with_options(request, runtime)

    async def close_created_by_async(
        self,
        request: tag_20180828_models.CloseCreatedByRequest,
    ) -> tag_20180828_models.CloseCreatedByResponse:
        """
        @summary 关闭CreatedBy服务
        
        @param request: CloseCreatedByRequest
        @return: CloseCreatedByResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.close_created_by_with_options_async(request, runtime)

    def create_policy_with_options(
        self,
        request: tag_20180828_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.CreatePolicyResponse:
        """
        @summary Creates a tag policy.
        
        @description ###
        This topic provides an example on how to call the API operation to create a tag policy named `test`. In this example, the Tag Policy feature in multi-account mode is used. The tag policy defines that resources to which the `CostCenter:Beijing` or `CostCenter:Shanghai` tag is added are compliant and other resources are not compliant.
        
        @param request: CreatePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.CreatePolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.CreatePolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def create_policy_with_options_async(
        self,
        request: tag_20180828_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.CreatePolicyResponse:
        """
        @summary Creates a tag policy.
        
        @description ###
        This topic provides an example on how to call the API operation to create a tag policy named `test`. In this example, the Tag Policy feature in multi-account mode is used. The tag policy defines that resources to which the `CostCenter:Beijing` or `CostCenter:Shanghai` tag is added are compliant and other resources are not compliant.
        
        @param request: CreatePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.CreatePolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.CreatePolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_policy(
        self,
        request: tag_20180828_models.CreatePolicyRequest,
    ) -> tag_20180828_models.CreatePolicyResponse:
        """
        @summary Creates a tag policy.
        
        @description ###
        This topic provides an example on how to call the API operation to create a tag policy named `test`. In this example, the Tag Policy feature in multi-account mode is used. The tag policy defines that resources to which the `CostCenter:Beijing` or `CostCenter:Shanghai` tag is added are compliant and other resources are not compliant.
        
        @param request: CreatePolicyRequest
        @return: CreatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_policy_with_options(request, runtime)

    async def create_policy_async(
        self,
        request: tag_20180828_models.CreatePolicyRequest,
    ) -> tag_20180828_models.CreatePolicyResponse:
        """
        @summary Creates a tag policy.
        
        @description ###
        This topic provides an example on how to call the API operation to create a tag policy named `test`. In this example, the Tag Policy feature in multi-account mode is used. The tag policy defines that resources to which the `CostCenter:Beijing` or `CostCenter:Shanghai` tag is added are compliant and other resources are not compliant.
        
        @param request: CreatePolicyRequest
        @return: CreatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_with_options_async(request, runtime)

    def create_tags_with_options(
        self,
        request: tag_20180828_models.CreateTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.CreateTagsResponse:
        """
        @summary Creates preset tags.
        
        @description ###
        A preset tag is a tag that you create in advance and is available for the resources in all regions. You can create preset tags in the stage of tag planning and add them to specific resources in the stage of tag implementation. When you create a preset tag, you can specify only the tag key. You can specify a tag value in the future.
        This topic provides an example on how to call the API operation to create a preset tag whose tag key is `Environment` to indicate the business environment.
        
        @param request: CreateTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTagsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.CreateTagsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.CreateTagsResponse(),
                self.execute(params, req, runtime)
            )

    async def create_tags_with_options_async(
        self,
        request: tag_20180828_models.CreateTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.CreateTagsResponse:
        """
        @summary Creates preset tags.
        
        @description ###
        A preset tag is a tag that you create in advance and is available for the resources in all regions. You can create preset tags in the stage of tag planning and add them to specific resources in the stage of tag implementation. When you create a preset tag, you can specify only the tag key. You can specify a tag value in the future.
        This topic provides an example on how to call the API operation to create a preset tag whose tag key is `Environment` to indicate the business environment.
        
        @param request: CreateTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTagsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.CreateTagsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.CreateTagsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_tags(
        self,
        request: tag_20180828_models.CreateTagsRequest,
    ) -> tag_20180828_models.CreateTagsResponse:
        """
        @summary Creates preset tags.
        
        @description ###
        A preset tag is a tag that you create in advance and is available for the resources in all regions. You can create preset tags in the stage of tag planning and add them to specific resources in the stage of tag implementation. When you create a preset tag, you can specify only the tag key. You can specify a tag value in the future.
        This topic provides an example on how to call the API operation to create a preset tag whose tag key is `Environment` to indicate the business environment.
        
        @param request: CreateTagsRequest
        @return: CreateTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_tags_with_options(request, runtime)

    async def create_tags_async(
        self,
        request: tag_20180828_models.CreateTagsRequest,
    ) -> tag_20180828_models.CreateTagsResponse:
        """
        @summary Creates preset tags.
        
        @description ###
        A preset tag is a tag that you create in advance and is available for the resources in all regions. You can create preset tags in the stage of tag planning and add them to specific resources in the stage of tag implementation. When you create a preset tag, you can specify only the tag key. You can specify a tag value in the future.
        This topic provides an example on how to call the API operation to create a preset tag whose tag key is `Environment` to indicate the business environment.
        
        @param request: CreateTagsRequest
        @return: CreateTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_tags_with_options_async(request, runtime)

    def delete_policy_with_options(
        self,
        request: tag_20180828_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.DeletePolicyResponse:
        """
        @summary 删除策略
        
        @description Before you delete a tag policy, make sure that the tag policy is detached from all objects to which the tag policy is attached. For more information about how to detach a tag policy, see [DetachPolicy](https://help.aliyun.com/document_detail/429724.html).
        This topic provides an example on how to call the API operation to delete the tag policy with an ID of `p-557cb141331f41c7***`.
        
        @param request: DeletePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.DeletePolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.DeletePolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_policy_with_options_async(
        self,
        request: tag_20180828_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.DeletePolicyResponse:
        """
        @summary 删除策略
        
        @description Before you delete a tag policy, make sure that the tag policy is detached from all objects to which the tag policy is attached. For more information about how to detach a tag policy, see [DetachPolicy](https://help.aliyun.com/document_detail/429724.html).
        This topic provides an example on how to call the API operation to delete the tag policy with an ID of `p-557cb141331f41c7***`.
        
        @param request: DeletePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.DeletePolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.DeletePolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_policy(
        self,
        request: tag_20180828_models.DeletePolicyRequest,
    ) -> tag_20180828_models.DeletePolicyResponse:
        """
        @summary 删除策略
        
        @description Before you delete a tag policy, make sure that the tag policy is detached from all objects to which the tag policy is attached. For more information about how to detach a tag policy, see [DetachPolicy](https://help.aliyun.com/document_detail/429724.html).
        This topic provides an example on how to call the API operation to delete the tag policy with an ID of `p-557cb141331f41c7***`.
        
        @param request: DeletePolicyRequest
        @return: DeletePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_with_options(request, runtime)

    async def delete_policy_async(
        self,
        request: tag_20180828_models.DeletePolicyRequest,
    ) -> tag_20180828_models.DeletePolicyResponse:
        """
        @summary 删除策略
        
        @description Before you delete a tag policy, make sure that the tag policy is detached from all objects to which the tag policy is attached. For more information about how to detach a tag policy, see [DetachPolicy](https://help.aliyun.com/document_detail/429724.html).
        This topic provides an example on how to call the API operation to delete the tag policy with an ID of `p-557cb141331f41c7***`.
        
        @param request: DeletePolicyRequest
        @return: DeletePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_with_options_async(request, runtime)

    def delete_tag_with_options(
        self,
        request: tag_20180828_models.DeleteTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.DeleteTagResponse:
        """
        @summary Deletes a preset tag.
        
        @description This topic provides an example on how to call the API operation to delete the preset tag whose tag key is `Environment` and tag value is `test`.
        
        @param request: DeleteTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTagResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.DeleteTagResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.DeleteTagResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_tag_with_options_async(
        self,
        request: tag_20180828_models.DeleteTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.DeleteTagResponse:
        """
        @summary Deletes a preset tag.
        
        @description This topic provides an example on how to call the API operation to delete the preset tag whose tag key is `Environment` and tag value is `test`.
        
        @param request: DeleteTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTagResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.DeleteTagResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.DeleteTagResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_tag(
        self,
        request: tag_20180828_models.DeleteTagRequest,
    ) -> tag_20180828_models.DeleteTagResponse:
        """
        @summary Deletes a preset tag.
        
        @description This topic provides an example on how to call the API operation to delete the preset tag whose tag key is `Environment` and tag value is `test`.
        
        @param request: DeleteTagRequest
        @return: DeleteTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_with_options(request, runtime)

    async def delete_tag_async(
        self,
        request: tag_20180828_models.DeleteTagRequest,
    ) -> tag_20180828_models.DeleteTagResponse:
        """
        @summary Deletes a preset tag.
        
        @description This topic provides an example on how to call the API operation to delete the preset tag whose tag key is `Environment` and tag value is `test`.
        
        @param request: DeleteTagRequest
        @return: DeleteTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_tag_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: tag_20180828_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.DescribeRegionsResponse:
        """
        @summary Queries the regions where the Tag service is available.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.DescribeRegionsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.DescribeRegionsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_regions_with_options_async(
        self,
        request: tag_20180828_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.DescribeRegionsResponse:
        """
        @summary Queries the regions where the Tag service is available.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.DescribeRegionsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.DescribeRegionsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_regions(
        self,
        request: tag_20180828_models.DescribeRegionsRequest,
    ) -> tag_20180828_models.DescribeRegionsResponse:
        """
        @summary Queries the regions where the Tag service is available.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: tag_20180828_models.DescribeRegionsRequest,
    ) -> tag_20180828_models.DescribeRegionsResponse:
        """
        @summary Queries the regions where the Tag service is available.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def detach_policy_with_options(
        self,
        request: tag_20180828_models.DetachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.DetachPolicyResponse:
        """
        @summary 解除策略绑定
        
        @description If you use the Tag Policy feature in single-account mode, you can call this API operation to detach a tag policy from the current logon account. If you use the Tag Policy feature in multi-account mode, you can call this API operation to detach a tag policy from the Root folder, a folder other than the Root folder, or a member in a resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to detach the tag policy with an ID of `p-a3381efe2fe34a75***` from the current logon account. In this example, the Tag Policy feature in single-account mode is used.
        
        @param request: DetachPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachPolicyResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.DetachPolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.DetachPolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def detach_policy_with_options_async(
        self,
        request: tag_20180828_models.DetachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.DetachPolicyResponse:
        """
        @summary 解除策略绑定
        
        @description If you use the Tag Policy feature in single-account mode, you can call this API operation to detach a tag policy from the current logon account. If you use the Tag Policy feature in multi-account mode, you can call this API operation to detach a tag policy from the Root folder, a folder other than the Root folder, or a member in a resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to detach the tag policy with an ID of `p-a3381efe2fe34a75***` from the current logon account. In this example, the Tag Policy feature in single-account mode is used.
        
        @param request: DetachPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachPolicyResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.DetachPolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.DetachPolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def detach_policy(
        self,
        request: tag_20180828_models.DetachPolicyRequest,
    ) -> tag_20180828_models.DetachPolicyResponse:
        """
        @summary 解除策略绑定
        
        @description If you use the Tag Policy feature in single-account mode, you can call this API operation to detach a tag policy from the current logon account. If you use the Tag Policy feature in multi-account mode, you can call this API operation to detach a tag policy from the Root folder, a folder other than the Root folder, or a member in a resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to detach the tag policy with an ID of `p-a3381efe2fe34a75***` from the current logon account. In this example, the Tag Policy feature in single-account mode is used.
        
        @param request: DetachPolicyRequest
        @return: DetachPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_policy_with_options(request, runtime)

    async def detach_policy_async(
        self,
        request: tag_20180828_models.DetachPolicyRequest,
    ) -> tag_20180828_models.DetachPolicyResponse:
        """
        @summary 解除策略绑定
        
        @description If you use the Tag Policy feature in single-account mode, you can call this API operation to detach a tag policy from the current logon account. If you use the Tag Policy feature in multi-account mode, you can call this API operation to detach a tag policy from the Root folder, a folder other than the Root folder, or a member in a resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to detach the tag policy with an ID of `p-a3381efe2fe34a75***` from the current logon account. In this example, the Tag Policy feature in single-account mode is used.
        
        @param request: DetachPolicyRequest
        @return: DetachPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_policy_with_options_async(request, runtime)

    def disable_policy_type_with_options(
        self,
        request: tag_20180828_models.DisablePolicyTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.DisablePolicyTypeResponse:
        """
        @summary 关闭策略
        
        @param request: DisablePolicyTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisablePolicyTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.open_type):
            query['OpenType'] = request.open_type
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.DisablePolicyTypeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.DisablePolicyTypeResponse(),
                self.execute(params, req, runtime)
            )

    async def disable_policy_type_with_options_async(
        self,
        request: tag_20180828_models.DisablePolicyTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.DisablePolicyTypeResponse:
        """
        @summary 关闭策略
        
        @param request: DisablePolicyTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisablePolicyTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.open_type):
            query['OpenType'] = request.open_type
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.DisablePolicyTypeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.DisablePolicyTypeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def disable_policy_type(
        self,
        request: tag_20180828_models.DisablePolicyTypeRequest,
    ) -> tag_20180828_models.DisablePolicyTypeResponse:
        """
        @summary 关闭策略
        
        @param request: DisablePolicyTypeRequest
        @return: DisablePolicyTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_policy_type_with_options(request, runtime)

    async def disable_policy_type_async(
        self,
        request: tag_20180828_models.DisablePolicyTypeRequest,
    ) -> tag_20180828_models.DisablePolicyTypeResponse:
        """
        @summary 关闭策略
        
        @param request: DisablePolicyTypeRequest
        @return: DisablePolicyTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_policy_type_with_options_async(request, runtime)

    def enable_policy_type_with_options(
        self,
        request: tag_20180828_models.EnablePolicyTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.EnablePolicyTypeResponse:
        """
        @summary 开通策略
        
        @param request: EnablePolicyTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnablePolicyTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.open_type):
            query['OpenType'] = request.open_type
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.EnablePolicyTypeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.EnablePolicyTypeResponse(),
                self.execute(params, req, runtime)
            )

    async def enable_policy_type_with_options_async(
        self,
        request: tag_20180828_models.EnablePolicyTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.EnablePolicyTypeResponse:
        """
        @summary 开通策略
        
        @param request: EnablePolicyTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnablePolicyTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.open_type):
            query['OpenType'] = request.open_type
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.EnablePolicyTypeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.EnablePolicyTypeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def enable_policy_type(
        self,
        request: tag_20180828_models.EnablePolicyTypeRequest,
    ) -> tag_20180828_models.EnablePolicyTypeResponse:
        """
        @summary 开通策略
        
        @param request: EnablePolicyTypeRequest
        @return: EnablePolicyTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_policy_type_with_options(request, runtime)

    async def enable_policy_type_async(
        self,
        request: tag_20180828_models.EnablePolicyTypeRequest,
    ) -> tag_20180828_models.EnablePolicyTypeResponse:
        """
        @summary 开通策略
        
        @param request: EnablePolicyTypeRequest
        @return: EnablePolicyTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_policy_type_with_options_async(request, runtime)

    def generate_config_rule_report_with_options(
        self,
        request: tag_20180828_models.GenerateConfigRuleReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.GenerateConfigRuleReportResponse:
        """
        @summary 生成规则检测报告
        
        @description If you use the Tag Policy feature in single-account mode, you can call this API operation to generate a resource non-compliance report for the current logon account. If you use the Tag Policy feature in multi-account mode, you can call this API operation to generate a resource non-compliance report for the Root folder, a folder other than the Root folder, or a member in a resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call this API operation to generate a resource non-compliance report for the current logon account. In this example, the Tag Policy feature in single-account mode is used.
        
        @param request: GenerateConfigRuleReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateConfigRuleReportResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.GenerateConfigRuleReportResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.GenerateConfigRuleReportResponse(),
                self.execute(params, req, runtime)
            )

    async def generate_config_rule_report_with_options_async(
        self,
        request: tag_20180828_models.GenerateConfigRuleReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.GenerateConfigRuleReportResponse:
        """
        @summary 生成规则检测报告
        
        @description If you use the Tag Policy feature in single-account mode, you can call this API operation to generate a resource non-compliance report for the current logon account. If you use the Tag Policy feature in multi-account mode, you can call this API operation to generate a resource non-compliance report for the Root folder, a folder other than the Root folder, or a member in a resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call this API operation to generate a resource non-compliance report for the current logon account. In this example, the Tag Policy feature in single-account mode is used.
        
        @param request: GenerateConfigRuleReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateConfigRuleReportResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.GenerateConfigRuleReportResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.GenerateConfigRuleReportResponse(),
                await self.execute_async(params, req, runtime)
            )

    def generate_config_rule_report(
        self,
        request: tag_20180828_models.GenerateConfigRuleReportRequest,
    ) -> tag_20180828_models.GenerateConfigRuleReportResponse:
        """
        @summary 生成规则检测报告
        
        @description If you use the Tag Policy feature in single-account mode, you can call this API operation to generate a resource non-compliance report for the current logon account. If you use the Tag Policy feature in multi-account mode, you can call this API operation to generate a resource non-compliance report for the Root folder, a folder other than the Root folder, or a member in a resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call this API operation to generate a resource non-compliance report for the current logon account. In this example, the Tag Policy feature in single-account mode is used.
        
        @param request: GenerateConfigRuleReportRequest
        @return: GenerateConfigRuleReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_config_rule_report_with_options(request, runtime)

    async def generate_config_rule_report_async(
        self,
        request: tag_20180828_models.GenerateConfigRuleReportRequest,
    ) -> tag_20180828_models.GenerateConfigRuleReportResponse:
        """
        @summary 生成规则检测报告
        
        @description If you use the Tag Policy feature in single-account mode, you can call this API operation to generate a resource non-compliance report for the current logon account. If you use the Tag Policy feature in multi-account mode, you can call this API operation to generate a resource non-compliance report for the Root folder, a folder other than the Root folder, or a member in a resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call this API operation to generate a resource non-compliance report for the current logon account. In this example, the Tag Policy feature in single-account mode is used.
        
        @param request: GenerateConfigRuleReportRequest
        @return: GenerateConfigRuleReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_config_rule_report_with_options_async(request, runtime)

    def get_config_rule_report_with_options(
        self,
        request: tag_20180828_models.GetConfigRuleReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.GetConfigRuleReportResponse:
        """
        @summary Queries the basic information of the resource non-compliance report that is last generated.
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query the basic information of the resource non-compliance report that is last generated for the account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query the basic information of the resource non-compliance report that is last generated for an object in the resource directory. The object can be the Root folder, a folder other than the Root folder, or a member. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call this API operation to query the basic information of the resource non-compliance report that is last generated for the current logon account. In this example, the Tag Policy feature in single-account mode is used. The response shows that the ID of the report is `crp-ao0786618088006c***`.
        
        @param request: GetConfigRuleReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConfigRuleReportResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.GetConfigRuleReportResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.GetConfigRuleReportResponse(),
                self.execute(params, req, runtime)
            )

    async def get_config_rule_report_with_options_async(
        self,
        request: tag_20180828_models.GetConfigRuleReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.GetConfigRuleReportResponse:
        """
        @summary Queries the basic information of the resource non-compliance report that is last generated.
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query the basic information of the resource non-compliance report that is last generated for the account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query the basic information of the resource non-compliance report that is last generated for an object in the resource directory. The object can be the Root folder, a folder other than the Root folder, or a member. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call this API operation to query the basic information of the resource non-compliance report that is last generated for the current logon account. In this example, the Tag Policy feature in single-account mode is used. The response shows that the ID of the report is `crp-ao0786618088006c***`.
        
        @param request: GetConfigRuleReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConfigRuleReportResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.GetConfigRuleReportResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.GetConfigRuleReportResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_config_rule_report(
        self,
        request: tag_20180828_models.GetConfigRuleReportRequest,
    ) -> tag_20180828_models.GetConfigRuleReportResponse:
        """
        @summary Queries the basic information of the resource non-compliance report that is last generated.
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query the basic information of the resource non-compliance report that is last generated for the account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query the basic information of the resource non-compliance report that is last generated for an object in the resource directory. The object can be the Root folder, a folder other than the Root folder, or a member. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call this API operation to query the basic information of the resource non-compliance report that is last generated for the current logon account. In this example, the Tag Policy feature in single-account mode is used. The response shows that the ID of the report is `crp-ao0786618088006c***`.
        
        @param request: GetConfigRuleReportRequest
        @return: GetConfigRuleReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_config_rule_report_with_options(request, runtime)

    async def get_config_rule_report_async(
        self,
        request: tag_20180828_models.GetConfigRuleReportRequest,
    ) -> tag_20180828_models.GetConfigRuleReportResponse:
        """
        @summary Queries the basic information of the resource non-compliance report that is last generated.
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query the basic information of the resource non-compliance report that is last generated for the account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query the basic information of the resource non-compliance report that is last generated for an object in the resource directory. The object can be the Root folder, a folder other than the Root folder, or a member. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call this API operation to query the basic information of the resource non-compliance report that is last generated for the current logon account. In this example, the Tag Policy feature in single-account mode is used. The response shows that the ID of the report is `crp-ao0786618088006c***`.
        
        @param request: GetConfigRuleReportRequest
        @return: GetConfigRuleReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_config_rule_report_with_options_async(request, runtime)

    def get_effective_policy_with_options(
        self,
        request: tag_20180828_models.GetEffectivePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.GetEffectivePolicyResponse:
        """
        @summary 查询有效策略
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query the effective tag policy for the account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query the effective tag policy for the Root folder, a folder other than the Root folder, or a member in the resource directory. You can also use a member of a resource directory to call this API operation to query the effective tag policy for the member. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        An effective tag policy is obtained based on tag policy inheritance. For more information, see [Inheritance of a tag policy and calculation of an effective tag policy](https://help.aliyun.com/document_detail/417435.html).
        This topic provides an example on how to call the API operation to query the effective tag policy for the current logon account. In this example, the Tag Policy feature in single-account mode is used.
        
        @param request: GetEffectivePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEffectivePolicyResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.GetEffectivePolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.GetEffectivePolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def get_effective_policy_with_options_async(
        self,
        request: tag_20180828_models.GetEffectivePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.GetEffectivePolicyResponse:
        """
        @summary 查询有效策略
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query the effective tag policy for the account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query the effective tag policy for the Root folder, a folder other than the Root folder, or a member in the resource directory. You can also use a member of a resource directory to call this API operation to query the effective tag policy for the member. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        An effective tag policy is obtained based on tag policy inheritance. For more information, see [Inheritance of a tag policy and calculation of an effective tag policy](https://help.aliyun.com/document_detail/417435.html).
        This topic provides an example on how to call the API operation to query the effective tag policy for the current logon account. In this example, the Tag Policy feature in single-account mode is used.
        
        @param request: GetEffectivePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEffectivePolicyResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.GetEffectivePolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.GetEffectivePolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_effective_policy(
        self,
        request: tag_20180828_models.GetEffectivePolicyRequest,
    ) -> tag_20180828_models.GetEffectivePolicyResponse:
        """
        @summary 查询有效策略
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query the effective tag policy for the account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query the effective tag policy for the Root folder, a folder other than the Root folder, or a member in the resource directory. You can also use a member of a resource directory to call this API operation to query the effective tag policy for the member. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        An effective tag policy is obtained based on tag policy inheritance. For more information, see [Inheritance of a tag policy and calculation of an effective tag policy](https://help.aliyun.com/document_detail/417435.html).
        This topic provides an example on how to call the API operation to query the effective tag policy for the current logon account. In this example, the Tag Policy feature in single-account mode is used.
        
        @param request: GetEffectivePolicyRequest
        @return: GetEffectivePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_effective_policy_with_options(request, runtime)

    async def get_effective_policy_async(
        self,
        request: tag_20180828_models.GetEffectivePolicyRequest,
    ) -> tag_20180828_models.GetEffectivePolicyResponse:
        """
        @summary 查询有效策略
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query the effective tag policy for the account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query the effective tag policy for the Root folder, a folder other than the Root folder, or a member in the resource directory. You can also use a member of a resource directory to call this API operation to query the effective tag policy for the member. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        An effective tag policy is obtained based on tag policy inheritance. For more information, see [Inheritance of a tag policy and calculation of an effective tag policy](https://help.aliyun.com/document_detail/417435.html).
        This topic provides an example on how to call the API operation to query the effective tag policy for the current logon account. In this example, the Tag Policy feature in single-account mode is used.
        
        @param request: GetEffectivePolicyRequest
        @return: GetEffectivePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_effective_policy_with_options_async(request, runtime)

    def get_policy_with_options(
        self,
        request: tag_20180828_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.GetPolicyResponse:
        """
        @summary 查询策略
        
        @description This topic provides an example on how to call the API operation to query the details of the tag policy with an ID of `p-557cb141331f41c7***`.
        
        @param request: GetPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.GetPolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.GetPolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def get_policy_with_options_async(
        self,
        request: tag_20180828_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.GetPolicyResponse:
        """
        @summary 查询策略
        
        @description This topic provides an example on how to call the API operation to query the details of the tag policy with an ID of `p-557cb141331f41c7***`.
        
        @param request: GetPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.GetPolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.GetPolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_policy(
        self,
        request: tag_20180828_models.GetPolicyRequest,
    ) -> tag_20180828_models.GetPolicyResponse:
        """
        @summary 查询策略
        
        @description This topic provides an example on how to call the API operation to query the details of the tag policy with an ID of `p-557cb141331f41c7***`.
        
        @param request: GetPolicyRequest
        @return: GetPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_policy_with_options(request, runtime)

    async def get_policy_async(
        self,
        request: tag_20180828_models.GetPolicyRequest,
    ) -> tag_20180828_models.GetPolicyResponse:
        """
        @summary 查询策略
        
        @description This topic provides an example on how to call the API operation to query the details of the tag policy with an ID of `p-557cb141331f41c7***`.
        
        @param request: GetPolicyRequest
        @return: GetPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_with_options_async(request, runtime)

    def get_policy_enable_status_with_options(
        self,
        request: tag_20180828_models.GetPolicyEnableStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.GetPolicyEnableStatusResponse:
        """
        @summary Queries the status of the Tag Policy feature.
        
        @description This topic provides an example on how to call the API operation to query the status of the Tag Policy feature for the current logon account. The response shows that the Tag Policy feature in multi-account mode is enabled for the current logon account.
        
        @param request: GetPolicyEnableStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyEnableStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.open_type):
            query['OpenType'] = request.open_type
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.GetPolicyEnableStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.GetPolicyEnableStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def get_policy_enable_status_with_options_async(
        self,
        request: tag_20180828_models.GetPolicyEnableStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.GetPolicyEnableStatusResponse:
        """
        @summary Queries the status of the Tag Policy feature.
        
        @description This topic provides an example on how to call the API operation to query the status of the Tag Policy feature for the current logon account. The response shows that the Tag Policy feature in multi-account mode is enabled for the current logon account.
        
        @param request: GetPolicyEnableStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyEnableStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.open_type):
            query['OpenType'] = request.open_type
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.GetPolicyEnableStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.GetPolicyEnableStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_policy_enable_status(
        self,
        request: tag_20180828_models.GetPolicyEnableStatusRequest,
    ) -> tag_20180828_models.GetPolicyEnableStatusResponse:
        """
        @summary Queries the status of the Tag Policy feature.
        
        @description This topic provides an example on how to call the API operation to query the status of the Tag Policy feature for the current logon account. The response shows that the Tag Policy feature in multi-account mode is enabled for the current logon account.
        
        @param request: GetPolicyEnableStatusRequest
        @return: GetPolicyEnableStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_policy_enable_status_with_options(request, runtime)

    async def get_policy_enable_status_async(
        self,
        request: tag_20180828_models.GetPolicyEnableStatusRequest,
    ) -> tag_20180828_models.GetPolicyEnableStatusResponse:
        """
        @summary Queries the status of the Tag Policy feature.
        
        @description This topic provides an example on how to call the API operation to query the status of the Tag Policy feature for the current logon account. The response shows that the Tag Policy feature in multi-account mode is enabled for the current logon account.
        
        @param request: GetPolicyEnableStatusRequest
        @return: GetPolicyEnableStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_enable_status_with_options_async(request, runtime)

    def list_config_rules_for_target_with_options(
        self,
        request: tag_20180828_models.ListConfigRulesForTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListConfigRulesForTargetResponse:
        """
        @summary Queries a list of tag detection tasks for an object.
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query the tag detection tasks for the account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query the tag detection tasks for the Root folder, a folder other than the Root folder, or a member in the resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to query the tag detection tasks for the current logon account. In this example, the Tag Policy feature in single-account mode is used. The response shows that only one tag detection task exists.
        
        @param request: ListConfigRulesForTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConfigRulesForTargetResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.ListConfigRulesForTargetResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.ListConfigRulesForTargetResponse(),
                self.execute(params, req, runtime)
            )

    async def list_config_rules_for_target_with_options_async(
        self,
        request: tag_20180828_models.ListConfigRulesForTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListConfigRulesForTargetResponse:
        """
        @summary Queries a list of tag detection tasks for an object.
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query the tag detection tasks for the account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query the tag detection tasks for the Root folder, a folder other than the Root folder, or a member in the resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to query the tag detection tasks for the current logon account. In this example, the Tag Policy feature in single-account mode is used. The response shows that only one tag detection task exists.
        
        @param request: ListConfigRulesForTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConfigRulesForTargetResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.ListConfigRulesForTargetResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.ListConfigRulesForTargetResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_config_rules_for_target(
        self,
        request: tag_20180828_models.ListConfigRulesForTargetRequest,
    ) -> tag_20180828_models.ListConfigRulesForTargetResponse:
        """
        @summary Queries a list of tag detection tasks for an object.
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query the tag detection tasks for the account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query the tag detection tasks for the Root folder, a folder other than the Root folder, or a member in the resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to query the tag detection tasks for the current logon account. In this example, the Tag Policy feature in single-account mode is used. The response shows that only one tag detection task exists.
        
        @param request: ListConfigRulesForTargetRequest
        @return: ListConfigRulesForTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_config_rules_for_target_with_options(request, runtime)

    async def list_config_rules_for_target_async(
        self,
        request: tag_20180828_models.ListConfigRulesForTargetRequest,
    ) -> tag_20180828_models.ListConfigRulesForTargetResponse:
        """
        @summary Queries a list of tag detection tasks for an object.
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query the tag detection tasks for the account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query the tag detection tasks for the Root folder, a folder other than the Root folder, or a member in the resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to query the tag detection tasks for the current logon account. In this example, the Tag Policy feature in single-account mode is used. The response shows that only one tag detection task exists.
        
        @param request: ListConfigRulesForTargetRequest
        @return: ListConfigRulesForTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_config_rules_for_target_with_options_async(request, runtime)

    def list_policies_with_options(
        self,
        request: tag_20180828_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListPoliciesResponse:
        """
        @summary Queries tag policies.
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query all tag policies that are created for the account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query all tag policies that are created for the resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to query all tag policies that are created for the current logon account. In this example, the Tag Policy feature in single-account mode is used. The response shows that two tag policies are created.
        
        @param request: ListPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPoliciesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.ListPoliciesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.ListPoliciesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_policies_with_options_async(
        self,
        request: tag_20180828_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListPoliciesResponse:
        """
        @summary Queries tag policies.
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query all tag policies that are created for the account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query all tag policies that are created for the resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to query all tag policies that are created for the current logon account. In this example, the Tag Policy feature in single-account mode is used. The response shows that two tag policies are created.
        
        @param request: ListPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPoliciesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.ListPoliciesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.ListPoliciesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_policies(
        self,
        request: tag_20180828_models.ListPoliciesRequest,
    ) -> tag_20180828_models.ListPoliciesResponse:
        """
        @summary Queries tag policies.
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query all tag policies that are created for the account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query all tag policies that are created for the resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to query all tag policies that are created for the current logon account. In this example, the Tag Policy feature in single-account mode is used. The response shows that two tag policies are created.
        
        @param request: ListPoliciesRequest
        @return: ListPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_policies_with_options(request, runtime)

    async def list_policies_async(
        self,
        request: tag_20180828_models.ListPoliciesRequest,
    ) -> tag_20180828_models.ListPoliciesResponse:
        """
        @summary Queries tag policies.
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query all tag policies that are created for the account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query all tag policies that are created for the resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to query all tag policies that are created for the current logon account. In this example, the Tag Policy feature in single-account mode is used. The response shows that two tag policies are created.
        
        @param request: ListPoliciesRequest
        @return: ListPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_policies_with_options_async(request, runtime)

    def list_policies_for_target_with_options(
        self,
        request: tag_20180828_models.ListPoliciesForTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListPoliciesForTargetResponse:
        """
        @summary Queries the tag policies that are attached to an object.
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query the tag policies that are attached to the account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query the tag policies that are attached to the Root folder, a folder other than the Root folder, or a member in the resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to query the tag policies that are attached to the current logon account. In this example, the Tag Policy feature in single-account mode is used. The response shows that only one tag policy is attached to the current logon account.
        
        @param request: ListPoliciesForTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPoliciesForTargetResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.ListPoliciesForTargetResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.ListPoliciesForTargetResponse(),
                self.execute(params, req, runtime)
            )

    async def list_policies_for_target_with_options_async(
        self,
        request: tag_20180828_models.ListPoliciesForTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListPoliciesForTargetResponse:
        """
        @summary Queries the tag policies that are attached to an object.
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query the tag policies that are attached to the account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query the tag policies that are attached to the Root folder, a folder other than the Root folder, or a member in the resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to query the tag policies that are attached to the current logon account. In this example, the Tag Policy feature in single-account mode is used. The response shows that only one tag policy is attached to the current logon account.
        
        @param request: ListPoliciesForTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPoliciesForTargetResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.ListPoliciesForTargetResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.ListPoliciesForTargetResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_policies_for_target(
        self,
        request: tag_20180828_models.ListPoliciesForTargetRequest,
    ) -> tag_20180828_models.ListPoliciesForTargetResponse:
        """
        @summary Queries the tag policies that are attached to an object.
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query the tag policies that are attached to the account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query the tag policies that are attached to the Root folder, a folder other than the Root folder, or a member in the resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to query the tag policies that are attached to the current logon account. In this example, the Tag Policy feature in single-account mode is used. The response shows that only one tag policy is attached to the current logon account.
        
        @param request: ListPoliciesForTargetRequest
        @return: ListPoliciesForTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_policies_for_target_with_options(request, runtime)

    async def list_policies_for_target_async(
        self,
        request: tag_20180828_models.ListPoliciesForTargetRequest,
    ) -> tag_20180828_models.ListPoliciesForTargetResponse:
        """
        @summary Queries the tag policies that are attached to an object.
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query the tag policies that are attached to the account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query the tag policies that are attached to the Root folder, a folder other than the Root folder, or a member in the resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to query the tag policies that are attached to the current logon account. In this example, the Tag Policy feature in single-account mode is used. The response shows that only one tag policy is attached to the current logon account.
        
        @param request: ListPoliciesForTargetRequest
        @return: ListPoliciesForTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_policies_for_target_with_options_async(request, runtime)

    def list_resources_by_tag_with_options(
        self,
        request: tag_20180828_models.ListResourcesByTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListResourcesByTagResponse:
        """
        @summary Queries resources to which a specified tag is added or resources to which a specified tag is not added.
        
        @description This topic provides an example on how to call the API operation in the China (Shenzhen) region to query virtual private clouds (VPCs) to which the tag key `k1` is added. The response shows that the tag key is added to two VPCs.
        
        @param request: ListResourcesByTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcesByTagResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.ListResourcesByTagResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.ListResourcesByTagResponse(),
                self.execute(params, req, runtime)
            )

    async def list_resources_by_tag_with_options_async(
        self,
        request: tag_20180828_models.ListResourcesByTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListResourcesByTagResponse:
        """
        @summary Queries resources to which a specified tag is added or resources to which a specified tag is not added.
        
        @description This topic provides an example on how to call the API operation in the China (Shenzhen) region to query virtual private clouds (VPCs) to which the tag key `k1` is added. The response shows that the tag key is added to two VPCs.
        
        @param request: ListResourcesByTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcesByTagResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.ListResourcesByTagResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.ListResourcesByTagResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_resources_by_tag(
        self,
        request: tag_20180828_models.ListResourcesByTagRequest,
    ) -> tag_20180828_models.ListResourcesByTagResponse:
        """
        @summary Queries resources to which a specified tag is added or resources to which a specified tag is not added.
        
        @description This topic provides an example on how to call the API operation in the China (Shenzhen) region to query virtual private clouds (VPCs) to which the tag key `k1` is added. The response shows that the tag key is added to two VPCs.
        
        @param request: ListResourcesByTagRequest
        @return: ListResourcesByTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resources_by_tag_with_options(request, runtime)

    async def list_resources_by_tag_async(
        self,
        request: tag_20180828_models.ListResourcesByTagRequest,
    ) -> tag_20180828_models.ListResourcesByTagResponse:
        """
        @summary Queries resources to which a specified tag is added or resources to which a specified tag is not added.
        
        @description This topic provides an example on how to call the API operation in the China (Shenzhen) region to query virtual private clouds (VPCs) to which the tag key `k1` is added. The response shows that the tag key is added to two VPCs.
        
        @param request: ListResourcesByTagRequest
        @return: ListResourcesByTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resources_by_tag_with_options_async(request, runtime)

    def list_support_resource_types_with_options(
        self,
        request: tag_20180828_models.ListSupportResourceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListSupportResourceTypesResponse:
        """
        @summary Queries the resource types supported by tags and tag-related capability items.
        
        @description ### [](#)Call examples
        Query a list of resource types supported by TagResources or UntagResources. For more information, see [Example](https://api.alibabacloud.com/api/Tag/2018-08-28/ListSupportResourceTypes?tab=DEBUG\\&params=%7B%22RegionId%22:%22cn-hangzhou%22,%22SupportCode%22:%22TAG_CONSOLE_SUPPORT%22%7D).
        Query a list of resource types supported by ListTagResources or ListResourcesByTag. For more information, see [Example](https://api.alibabacloud.com/api/Tag/2018-08-28/ListSupportResourceTypes?tab=DEBUG\\&params=%7B%22RegionId%22:%22cn-hangzhou%22%7D).
        Query a list of resource types that support createdby tags. For more information, see [Example](https://api.alibabacloud.com/api/Tag/2018-08-28/ListSupportResourceTypes?tab=DEBUG\\&params=%7B%22RegionId%22:%22cn-hangzhou%22,%22SupportCode%22:%22CREATED_BY_TAG_CONSOLE_SUPPORT%22%7D).
        
        @param request: ListSupportResourceTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSupportResourceTypesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.ListSupportResourceTypesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.ListSupportResourceTypesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_support_resource_types_with_options_async(
        self,
        request: tag_20180828_models.ListSupportResourceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListSupportResourceTypesResponse:
        """
        @summary Queries the resource types supported by tags and tag-related capability items.
        
        @description ### [](#)Call examples
        Query a list of resource types supported by TagResources or UntagResources. For more information, see [Example](https://api.alibabacloud.com/api/Tag/2018-08-28/ListSupportResourceTypes?tab=DEBUG\\&params=%7B%22RegionId%22:%22cn-hangzhou%22,%22SupportCode%22:%22TAG_CONSOLE_SUPPORT%22%7D).
        Query a list of resource types supported by ListTagResources or ListResourcesByTag. For more information, see [Example](https://api.alibabacloud.com/api/Tag/2018-08-28/ListSupportResourceTypes?tab=DEBUG\\&params=%7B%22RegionId%22:%22cn-hangzhou%22%7D).
        Query a list of resource types that support createdby tags. For more information, see [Example](https://api.alibabacloud.com/api/Tag/2018-08-28/ListSupportResourceTypes?tab=DEBUG\\&params=%7B%22RegionId%22:%22cn-hangzhou%22,%22SupportCode%22:%22CREATED_BY_TAG_CONSOLE_SUPPORT%22%7D).
        
        @param request: ListSupportResourceTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSupportResourceTypesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.ListSupportResourceTypesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.ListSupportResourceTypesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_support_resource_types(
        self,
        request: tag_20180828_models.ListSupportResourceTypesRequest,
    ) -> tag_20180828_models.ListSupportResourceTypesResponse:
        """
        @summary Queries the resource types supported by tags and tag-related capability items.
        
        @description ### [](#)Call examples
        Query a list of resource types supported by TagResources or UntagResources. For more information, see [Example](https://api.alibabacloud.com/api/Tag/2018-08-28/ListSupportResourceTypes?tab=DEBUG\\&params=%7B%22RegionId%22:%22cn-hangzhou%22,%22SupportCode%22:%22TAG_CONSOLE_SUPPORT%22%7D).
        Query a list of resource types supported by ListTagResources or ListResourcesByTag. For more information, see [Example](https://api.alibabacloud.com/api/Tag/2018-08-28/ListSupportResourceTypes?tab=DEBUG\\&params=%7B%22RegionId%22:%22cn-hangzhou%22%7D).
        Query a list of resource types that support createdby tags. For more information, see [Example](https://api.alibabacloud.com/api/Tag/2018-08-28/ListSupportResourceTypes?tab=DEBUG\\&params=%7B%22RegionId%22:%22cn-hangzhou%22,%22SupportCode%22:%22CREATED_BY_TAG_CONSOLE_SUPPORT%22%7D).
        
        @param request: ListSupportResourceTypesRequest
        @return: ListSupportResourceTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_support_resource_types_with_options(request, runtime)

    async def list_support_resource_types_async(
        self,
        request: tag_20180828_models.ListSupportResourceTypesRequest,
    ) -> tag_20180828_models.ListSupportResourceTypesResponse:
        """
        @summary Queries the resource types supported by tags and tag-related capability items.
        
        @description ### [](#)Call examples
        Query a list of resource types supported by TagResources or UntagResources. For more information, see [Example](https://api.alibabacloud.com/api/Tag/2018-08-28/ListSupportResourceTypes?tab=DEBUG\\&params=%7B%22RegionId%22:%22cn-hangzhou%22,%22SupportCode%22:%22TAG_CONSOLE_SUPPORT%22%7D).
        Query a list of resource types supported by ListTagResources or ListResourcesByTag. For more information, see [Example](https://api.alibabacloud.com/api/Tag/2018-08-28/ListSupportResourceTypes?tab=DEBUG\\&params=%7B%22RegionId%22:%22cn-hangzhou%22%7D).
        Query a list of resource types that support createdby tags. For more information, see [Example](https://api.alibabacloud.com/api/Tag/2018-08-28/ListSupportResourceTypes?tab=DEBUG\\&params=%7B%22RegionId%22:%22cn-hangzhou%22,%22SupportCode%22:%22CREATED_BY_TAG_CONSOLE_SUPPORT%22%7D).
        
        @param request: ListSupportResourceTypesRequest
        @return: ListSupportResourceTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_support_resource_types_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: tag_20180828_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTagKeysResponse:
        """
        @summary Queries tag keys.
        
        @description This topic provides an example on how to call the API operation to query the tag keys in the `cn-hangzhou` region. The response shows that the following tag keys exist: `team`, `k1`, and `k2`.
        
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.ListTagKeysResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.ListTagKeysResponse(),
                self.execute(params, req, runtime)
            )

    async def list_tag_keys_with_options_async(
        self,
        request: tag_20180828_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTagKeysResponse:
        """
        @summary Queries tag keys.
        
        @description This topic provides an example on how to call the API operation to query the tag keys in the `cn-hangzhou` region. The response shows that the following tag keys exist: `team`, `k1`, and `k2`.
        
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.ListTagKeysResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.ListTagKeysResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_tag_keys(
        self,
        request: tag_20180828_models.ListTagKeysRequest,
    ) -> tag_20180828_models.ListTagKeysResponse:
        """
        @summary Queries tag keys.
        
        @description This topic provides an example on how to call the API operation to query the tag keys in the `cn-hangzhou` region. The response shows that the following tag keys exist: `team`, `k1`, and `k2`.
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: tag_20180828_models.ListTagKeysRequest,
    ) -> tag_20180828_models.ListTagKeysResponse:
        """
        @summary Queries tag keys.
        
        @description This topic provides an example on how to call the API operation to query the tag keys in the `cn-hangzhou` region. The response shows that the following tag keys exist: `team`, `k1`, and `k2`.
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: tag_20180828_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to the resources of various Alibaba Cloud services.
        
        @description For information about the Alibaba Cloud services that support tags, see [Services that work with Tag](https://help.aliyun.com/document_detail/171455.html).
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.ListTagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.ListTagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_tag_resources_with_options_async(
        self,
        request: tag_20180828_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to the resources of various Alibaba Cloud services.
        
        @description For information about the Alibaba Cloud services that support tags, see [Services that work with Tag](https://help.aliyun.com/document_detail/171455.html).
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.ListTagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.ListTagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_tag_resources(
        self,
        request: tag_20180828_models.ListTagResourcesRequest,
    ) -> tag_20180828_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to the resources of various Alibaba Cloud services.
        
        @description For information about the Alibaba Cloud services that support tags, see [Services that work with Tag](https://help.aliyun.com/document_detail/171455.html).
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: tag_20180828_models.ListTagResourcesRequest,
    ) -> tag_20180828_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to the resources of various Alibaba Cloud services.
        
        @description For information about the Alibaba Cloud services that support tags, see [Services that work with Tag](https://help.aliyun.com/document_detail/171455.html).
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: tag_20180828_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTagValuesResponse:
        """
        @summary Queries the tag values of a tag key.
        
        @description This topic provides an example on how to call the API operation to query the values of the tag key `k1` in the `cn-hangzhou` region. The response shows that the value of the tag key `k1` is `v1`.
        
        @param request: ListTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagValuesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.ListTagValuesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.ListTagValuesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_tag_values_with_options_async(
        self,
        request: tag_20180828_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTagValuesResponse:
        """
        @summary Queries the tag values of a tag key.
        
        @description This topic provides an example on how to call the API operation to query the values of the tag key `k1` in the `cn-hangzhou` region. The response shows that the value of the tag key `k1` is `v1`.
        
        @param request: ListTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagValuesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.ListTagValuesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.ListTagValuesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_tag_values(
        self,
        request: tag_20180828_models.ListTagValuesRequest,
    ) -> tag_20180828_models.ListTagValuesResponse:
        """
        @summary Queries the tag values of a tag key.
        
        @description This topic provides an example on how to call the API operation to query the values of the tag key `k1` in the `cn-hangzhou` region. The response shows that the value of the tag key `k1` is `v1`.
        
        @param request: ListTagValuesRequest
        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: tag_20180828_models.ListTagValuesRequest,
    ) -> tag_20180828_models.ListTagValuesResponse:
        """
        @summary Queries the tag values of a tag key.
        
        @description This topic provides an example on how to call the API operation to query the values of the tag key `k1` in the `cn-hangzhou` region. The response shows that the value of the tag key `k1` is `v1`.
        
        @param request: ListTagValuesRequest
        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def list_targets_for_policy_with_options(
        self,
        request: tag_20180828_models.ListTargetsForPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTargetsForPolicyResponse:
        """
        @summary Queries the objects to which a tag policy is attached.
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query the object to which a tag policy is attached. The object is the current logon account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query the objects to which a tag policy is attached. The objects include the Root folder, folders other than the Root folder, and members in the resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to query the objects to which the tag policy with an ID of `p-de62a0bf400e4b69***` is attached. In this example, the Tag Policy feature in multi-account mode is used. The response shows that the tag policy is attached to two members in the related resource directory.
        
        @param request: ListTargetsForPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTargetsForPolicyResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.ListTargetsForPolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.ListTargetsForPolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def list_targets_for_policy_with_options_async(
        self,
        request: tag_20180828_models.ListTargetsForPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTargetsForPolicyResponse:
        """
        @summary Queries the objects to which a tag policy is attached.
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query the object to which a tag policy is attached. The object is the current logon account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query the objects to which a tag policy is attached. The objects include the Root folder, folders other than the Root folder, and members in the resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to query the objects to which the tag policy with an ID of `p-de62a0bf400e4b69***` is attached. In this example, the Tag Policy feature in multi-account mode is used. The response shows that the tag policy is attached to two members in the related resource directory.
        
        @param request: ListTargetsForPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTargetsForPolicyResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.ListTargetsForPolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.ListTargetsForPolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_targets_for_policy(
        self,
        request: tag_20180828_models.ListTargetsForPolicyRequest,
    ) -> tag_20180828_models.ListTargetsForPolicyResponse:
        """
        @summary Queries the objects to which a tag policy is attached.
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query the object to which a tag policy is attached. The object is the current logon account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query the objects to which a tag policy is attached. The objects include the Root folder, folders other than the Root folder, and members in the resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to query the objects to which the tag policy with an ID of `p-de62a0bf400e4b69***` is attached. In this example, the Tag Policy feature in multi-account mode is used. The response shows that the tag policy is attached to two members in the related resource directory.
        
        @param request: ListTargetsForPolicyRequest
        @return: ListTargetsForPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_targets_for_policy_with_options(request, runtime)

    async def list_targets_for_policy_async(
        self,
        request: tag_20180828_models.ListTargetsForPolicyRequest,
    ) -> tag_20180828_models.ListTargetsForPolicyResponse:
        """
        @summary Queries the objects to which a tag policy is attached.
        
        @description If you use the Tag Policy feature in single-account mode, you can use the current logon account to call this API operation to query the object to which a tag policy is attached. The object is the current logon account. If you use the Tag Policy feature in multi-account mode, you can use the management account of a resource directory to call this API operation to query the objects to which a tag policy is attached. The objects include the Root folder, folders other than the Root folder, and members in the resource directory. For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        This topic provides an example on how to call the API operation to query the objects to which the tag policy with an ID of `p-de62a0bf400e4b69***` is attached. In this example, the Tag Policy feature in multi-account mode is used. The response shows that the tag policy is attached to two members in the related resource directory.
        
        @param request: ListTargetsForPolicyRequest
        @return: ListTargetsForPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_targets_for_policy_with_options_async(request, runtime)

    def modify_policy_with_options(
        self,
        request: tag_20180828_models.ModifyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ModifyPolicyResponse:
        """
        @summary 修改策略
        
        @description This topic provides an example on how to call the API operation to change the name of a tag policy to `test`.
        
        @param request: ModifyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPolicyResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.ModifyPolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.ModifyPolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_policy_with_options_async(
        self,
        request: tag_20180828_models.ModifyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ModifyPolicyResponse:
        """
        @summary 修改策略
        
        @description This topic provides an example on how to call the API operation to change the name of a tag policy to `test`.
        
        @param request: ModifyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPolicyResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.ModifyPolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.ModifyPolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_policy(
        self,
        request: tag_20180828_models.ModifyPolicyRequest,
    ) -> tag_20180828_models.ModifyPolicyResponse:
        """
        @summary 修改策略
        
        @description This topic provides an example on how to call the API operation to change the name of a tag policy to `test`.
        
        @param request: ModifyPolicyRequest
        @return: ModifyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_policy_with_options(request, runtime)

    async def modify_policy_async(
        self,
        request: tag_20180828_models.ModifyPolicyRequest,
    ) -> tag_20180828_models.ModifyPolicyResponse:
        """
        @summary 修改策略
        
        @description This topic provides an example on how to call the API operation to change the name of a tag policy to `test`.
        
        @param request: ModifyPolicyRequest
        @return: ModifyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_policy_with_options_async(request, runtime)

    def open_created_by_with_options(
        self,
        request: tag_20180828_models.OpenCreatedByRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.OpenCreatedByResponse:
        """
        @summary Enables createdby tags.
        
        @description createdby tags can help you analyze costs and bills and manage the costs of cloud resources in an efficient manner. You can identify the creators of resources based on the createdby tags added to the resources. createdby tags are system tags that are provided by Alibaba Cloud and automatically added to resources. The key of createdby tags is `acs:tag:createdby`.
        
        @param request: OpenCreatedByRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenCreatedByResponse
        """
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenCreatedBy',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.OpenCreatedByResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.OpenCreatedByResponse(),
                self.execute(params, req, runtime)
            )

    async def open_created_by_with_options_async(
        self,
        request: tag_20180828_models.OpenCreatedByRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.OpenCreatedByResponse:
        """
        @summary Enables createdby tags.
        
        @description createdby tags can help you analyze costs and bills and manage the costs of cloud resources in an efficient manner. You can identify the creators of resources based on the createdby tags added to the resources. createdby tags are system tags that are provided by Alibaba Cloud and automatically added to resources. The key of createdby tags is `acs:tag:createdby`.
        
        @param request: OpenCreatedByRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenCreatedByResponse
        """
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenCreatedBy',
            version='2018-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.OpenCreatedByResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.OpenCreatedByResponse(),
                await self.execute_async(params, req, runtime)
            )

    def open_created_by(
        self,
        request: tag_20180828_models.OpenCreatedByRequest,
    ) -> tag_20180828_models.OpenCreatedByResponse:
        """
        @summary Enables createdby tags.
        
        @description createdby tags can help you analyze costs and bills and manage the costs of cloud resources in an efficient manner. You can identify the creators of resources based on the createdby tags added to the resources. createdby tags are system tags that are provided by Alibaba Cloud and automatically added to resources. The key of createdby tags is `acs:tag:createdby`.
        
        @param request: OpenCreatedByRequest
        @return: OpenCreatedByResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_created_by_with_options(request, runtime)

    async def open_created_by_async(
        self,
        request: tag_20180828_models.OpenCreatedByRequest,
    ) -> tag_20180828_models.OpenCreatedByResponse:
        """
        @summary Enables createdby tags.
        
        @description createdby tags can help you analyze costs and bills and manage the costs of cloud resources in an efficient manner. You can identify the creators of resources based on the createdby tags added to the resources. createdby tags are system tags that are provided by Alibaba Cloud and automatically added to resources. The key of createdby tags is `acs:tag:createdby`.
        
        @param request: OpenCreatedByRequest
        @return: OpenCreatedByResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_created_by_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: tag_20180828_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.TagResourcesResponse:
        """
        @summary Adds tags to the resources of various Alibaba Cloud services.
        
        @description Tags are used to identify resources. Tags allow you to categorize, search for, and aggregate resources that have the same characteristics from different dimensions. This facilitates resource management. For more information, see [Tag overview](https://help.aliyun.com/document_detail/156983.html).
        For information about the Alibaba Cloud services that support tags, see [Services that work with Tag](https://help.aliyun.com/document_detail/171455.html).
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.TagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.TagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def tag_resources_with_options_async(
        self,
        request: tag_20180828_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.TagResourcesResponse:
        """
        @summary Adds tags to the resources of various Alibaba Cloud services.
        
        @description Tags are used to identify resources. Tags allow you to categorize, search for, and aggregate resources that have the same characteristics from different dimensions. This facilitates resource management. For more information, see [Tag overview](https://help.aliyun.com/document_detail/156983.html).
        For information about the Alibaba Cloud services that support tags, see [Services that work with Tag](https://help.aliyun.com/document_detail/171455.html).
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.TagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.TagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def tag_resources(
        self,
        request: tag_20180828_models.TagResourcesRequest,
    ) -> tag_20180828_models.TagResourcesResponse:
        """
        @summary Adds tags to the resources of various Alibaba Cloud services.
        
        @description Tags are used to identify resources. Tags allow you to categorize, search for, and aggregate resources that have the same characteristics from different dimensions. This facilitates resource management. For more information, see [Tag overview](https://help.aliyun.com/document_detail/156983.html).
        For information about the Alibaba Cloud services that support tags, see [Services that work with Tag](https://help.aliyun.com/document_detail/171455.html).
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: tag_20180828_models.TagResourcesRequest,
    ) -> tag_20180828_models.TagResourcesResponse:
        """
        @summary Adds tags to the resources of various Alibaba Cloud services.
        
        @description Tags are used to identify resources. Tags allow you to categorize, search for, and aggregate resources that have the same characteristics from different dimensions. This facilitates resource management. For more information, see [Tag overview](https://help.aliyun.com/document_detail/156983.html).
        For information about the Alibaba Cloud services that support tags, see [Services that work with Tag](https://help.aliyun.com/document_detail/171455.html).
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: tag_20180828_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.UntagResourcesResponse:
        """
        @summary Removes tags from the resources of various Alibaba Cloud services.
        
        @description After you remove a tag, the tag is automatically deleted within 24 hours if it is not added to other resources.
        For information about the Alibaba Cloud services that support tags, see [Services that work with Tag](https://help.aliyun.com/document_detail/171455.html).
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.UntagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.UntagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def untag_resources_with_options_async(
        self,
        request: tag_20180828_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.UntagResourcesResponse:
        """
        @summary Removes tags from the resources of various Alibaba Cloud services.
        
        @description After you remove a tag, the tag is automatically deleted within 24 hours if it is not added to other resources.
        For information about the Alibaba Cloud services that support tags, see [Services that work with Tag](https://help.aliyun.com/document_detail/171455.html).
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                tag_20180828_models.UntagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                tag_20180828_models.UntagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def untag_resources(
        self,
        request: tag_20180828_models.UntagResourcesRequest,
    ) -> tag_20180828_models.UntagResourcesResponse:
        """
        @summary Removes tags from the resources of various Alibaba Cloud services.
        
        @description After you remove a tag, the tag is automatically deleted within 24 hours if it is not added to other resources.
        For information about the Alibaba Cloud services that support tags, see [Services that work with Tag](https://help.aliyun.com/document_detail/171455.html).
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: tag_20180828_models.UntagResourcesRequest,
    ) -> tag_20180828_models.UntagResourcesResponse:
        """
        @summary Removes tags from the resources of various Alibaba Cloud services.
        
        @description After you remove a tag, the tag is automatically deleted within 24 hours if it is not added to other resources.
        For information about the Alibaba Cloud services that support tags, see [Services that work with Tag](https://help.aliyun.com/document_detail/171455.html).
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
