# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sts20150401 import models as sts_20150401_models
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
        self._signature_algorithm = 'v2'
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-2-pop': 'sts.aliyuncs.com',
            'cn-beijing-finance-1': 'sts.aliyuncs.com',
            'cn-beijing-finance-pop': 'sts.aliyuncs.com',
            'cn-beijing-gov-1': 'sts.aliyuncs.com',
            'cn-beijing-nu16-b01': 'sts.aliyuncs.com',
            'cn-edge-1': 'sts.aliyuncs.com',
            'cn-fujian': 'sts.aliyuncs.com',
            'cn-haidian-cm12-c01': 'sts.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'sts.aliyuncs.com',
            'cn-hangzhou-finance': 'sts.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'sts.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'sts.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'sts.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'sts.aliyuncs.com',
            'cn-hangzhou-test-306': 'sts.aliyuncs.com',
            'cn-hongkong-finance-pop': 'sts.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'sts.aliyuncs.com',
            'cn-north-2-gov-1': 'sts-vpc.cn-north-2-gov-1.aliyuncs.com',
            'cn-qingdao-nebula': 'sts.aliyuncs.com',
            'cn-shanghai-et15-b01': 'sts.aliyuncs.com',
            'cn-shanghai-et2-b01': 'sts.aliyuncs.com',
            'cn-shanghai-inner': 'sts.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'sts.aliyuncs.com',
            'cn-shenzhen-finance-1': 'sts-vpc.cn-shenzhen-finance-1.aliyuncs.com',
            'cn-shenzhen-inner': 'sts.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'sts.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'sts.aliyuncs.com',
            'cn-wuhan': 'sts.aliyuncs.com',
            'cn-yushanfang': 'sts.aliyuncs.com',
            'cn-zhangbei': 'sts.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'sts.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'sts.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'sts.aliyuncs.com',
            'eu-west-1-oxs': 'sts.aliyuncs.com',
            'rus-west-1-pop': 'sts.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('sts', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def assume_role_with_options(
        self,
        request: sts_20150401_models.AssumeRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sts_20150401_models.AssumeRoleResponse:
        """
        ### Prerequisites
        You cannot use an Alibaba Cloud account to call this operation. The requester of this operation can only be a RAM user or RAM role. Make sure that the AliyunSTSAssumeRoleAccess policy is attached to the requester. After this policy is attached to the requester, the requester has the management permissions on STS.
        If you do not attach the AliyunSTSAssumeRoleAccess policy to the requester, the following error message is returned:
        `You are not authorized to do this action. You should be authorized by RAM.`
        You can refer to the following information to troubleshoot the error:
        *   Cause of the error: The policy that is required to assume a RAM role is not attached to the requester. To resolve this issue, attach the AliyunSTSAssumeRoleAccess policy or a custom policy to the requester. For more information, see [Can I specify the RAM role that a RAM user can assume?](~~39744~~) and [Grant permissions to a RAM user](~~116146~~).
        *   Cause of the error: The requester is not authorized to assume the RAM role. To resolve this issue, add the requester to the Principal element in the trust policy of the RAM role For more information, see [Edit the trust policy of a RAM role](~~116819~~).
        ### Best practices
        An STS token is valid for a period of time after it is issued, and the number of STS tokens that can be issued within an interval is also limited. Therefore, we recommend that you configure a proper validity period for an STS token and repeatedly use the token within this period. This prevents frequent issuing of STS tokens from adversely affecting your services if a large number of requests are sent. For more information about the limit, see [Is the number of STS API requests limited?](~~39744~~) You can configure the `DurationSeconds` parameter to specify a validity period for an STS token.
        When you upload or download Object Storage Service (OSS) objects on mobile devices, a large number of STS API requests are sent. In this case, repeated use of an STS token may not meet your business requirements. To avoid the limit on STS API requests from affecting access to OSS, you can **add a signature to the URL of an OSS object**. For more information, see [Add signatures to URLs](~~31952~~) and [Obtain signature information from the server and upload data to OSS](~~31926~~).
        
        @param request: AssumeRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssumeRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration_seconds):
            query['DurationSeconds'] = request.duration_seconds
        if not UtilClient.is_unset(request.external_id):
            query['ExternalId'] = request.external_id
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.role_session_name):
            query['RoleSessionName'] = request.role_session_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssumeRole',
            version='2015-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sts_20150401_models.AssumeRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def assume_role_with_options_async(
        self,
        request: sts_20150401_models.AssumeRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sts_20150401_models.AssumeRoleResponse:
        """
        ### Prerequisites
        You cannot use an Alibaba Cloud account to call this operation. The requester of this operation can only be a RAM user or RAM role. Make sure that the AliyunSTSAssumeRoleAccess policy is attached to the requester. After this policy is attached to the requester, the requester has the management permissions on STS.
        If you do not attach the AliyunSTSAssumeRoleAccess policy to the requester, the following error message is returned:
        `You are not authorized to do this action. You should be authorized by RAM.`
        You can refer to the following information to troubleshoot the error:
        *   Cause of the error: The policy that is required to assume a RAM role is not attached to the requester. To resolve this issue, attach the AliyunSTSAssumeRoleAccess policy or a custom policy to the requester. For more information, see [Can I specify the RAM role that a RAM user can assume?](~~39744~~) and [Grant permissions to a RAM user](~~116146~~).
        *   Cause of the error: The requester is not authorized to assume the RAM role. To resolve this issue, add the requester to the Principal element in the trust policy of the RAM role For more information, see [Edit the trust policy of a RAM role](~~116819~~).
        ### Best practices
        An STS token is valid for a period of time after it is issued, and the number of STS tokens that can be issued within an interval is also limited. Therefore, we recommend that you configure a proper validity period for an STS token and repeatedly use the token within this period. This prevents frequent issuing of STS tokens from adversely affecting your services if a large number of requests are sent. For more information about the limit, see [Is the number of STS API requests limited?](~~39744~~) You can configure the `DurationSeconds` parameter to specify a validity period for an STS token.
        When you upload or download Object Storage Service (OSS) objects on mobile devices, a large number of STS API requests are sent. In this case, repeated use of an STS token may not meet your business requirements. To avoid the limit on STS API requests from affecting access to OSS, you can **add a signature to the URL of an OSS object**. For more information, see [Add signatures to URLs](~~31952~~) and [Obtain signature information from the server and upload data to OSS](~~31926~~).
        
        @param request: AssumeRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssumeRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration_seconds):
            query['DurationSeconds'] = request.duration_seconds
        if not UtilClient.is_unset(request.external_id):
            query['ExternalId'] = request.external_id
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.role_session_name):
            query['RoleSessionName'] = request.role_session_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssumeRole',
            version='2015-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sts_20150401_models.AssumeRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assume_role(
        self,
        request: sts_20150401_models.AssumeRoleRequest,
    ) -> sts_20150401_models.AssumeRoleResponse:
        """
        ### Prerequisites
        You cannot use an Alibaba Cloud account to call this operation. The requester of this operation can only be a RAM user or RAM role. Make sure that the AliyunSTSAssumeRoleAccess policy is attached to the requester. After this policy is attached to the requester, the requester has the management permissions on STS.
        If you do not attach the AliyunSTSAssumeRoleAccess policy to the requester, the following error message is returned:
        `You are not authorized to do this action. You should be authorized by RAM.`
        You can refer to the following information to troubleshoot the error:
        *   Cause of the error: The policy that is required to assume a RAM role is not attached to the requester. To resolve this issue, attach the AliyunSTSAssumeRoleAccess policy or a custom policy to the requester. For more information, see [Can I specify the RAM role that a RAM user can assume?](~~39744~~) and [Grant permissions to a RAM user](~~116146~~).
        *   Cause of the error: The requester is not authorized to assume the RAM role. To resolve this issue, add the requester to the Principal element in the trust policy of the RAM role For more information, see [Edit the trust policy of a RAM role](~~116819~~).
        ### Best practices
        An STS token is valid for a period of time after it is issued, and the number of STS tokens that can be issued within an interval is also limited. Therefore, we recommend that you configure a proper validity period for an STS token and repeatedly use the token within this period. This prevents frequent issuing of STS tokens from adversely affecting your services if a large number of requests are sent. For more information about the limit, see [Is the number of STS API requests limited?](~~39744~~) You can configure the `DurationSeconds` parameter to specify a validity period for an STS token.
        When you upload or download Object Storage Service (OSS) objects on mobile devices, a large number of STS API requests are sent. In this case, repeated use of an STS token may not meet your business requirements. To avoid the limit on STS API requests from affecting access to OSS, you can **add a signature to the URL of an OSS object**. For more information, see [Add signatures to URLs](~~31952~~) and [Obtain signature information from the server and upload data to OSS](~~31926~~).
        
        @param request: AssumeRoleRequest
        @return: AssumeRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.assume_role_with_options(request, runtime)

    async def assume_role_async(
        self,
        request: sts_20150401_models.AssumeRoleRequest,
    ) -> sts_20150401_models.AssumeRoleResponse:
        """
        ### Prerequisites
        You cannot use an Alibaba Cloud account to call this operation. The requester of this operation can only be a RAM user or RAM role. Make sure that the AliyunSTSAssumeRoleAccess policy is attached to the requester. After this policy is attached to the requester, the requester has the management permissions on STS.
        If you do not attach the AliyunSTSAssumeRoleAccess policy to the requester, the following error message is returned:
        `You are not authorized to do this action. You should be authorized by RAM.`
        You can refer to the following information to troubleshoot the error:
        *   Cause of the error: The policy that is required to assume a RAM role is not attached to the requester. To resolve this issue, attach the AliyunSTSAssumeRoleAccess policy or a custom policy to the requester. For more information, see [Can I specify the RAM role that a RAM user can assume?](~~39744~~) and [Grant permissions to a RAM user](~~116146~~).
        *   Cause of the error: The requester is not authorized to assume the RAM role. To resolve this issue, add the requester to the Principal element in the trust policy of the RAM role For more information, see [Edit the trust policy of a RAM role](~~116819~~).
        ### Best practices
        An STS token is valid for a period of time after it is issued, and the number of STS tokens that can be issued within an interval is also limited. Therefore, we recommend that you configure a proper validity period for an STS token and repeatedly use the token within this period. This prevents frequent issuing of STS tokens from adversely affecting your services if a large number of requests are sent. For more information about the limit, see [Is the number of STS API requests limited?](~~39744~~) You can configure the `DurationSeconds` parameter to specify a validity period for an STS token.
        When you upload or download Object Storage Service (OSS) objects on mobile devices, a large number of STS API requests are sent. In this case, repeated use of an STS token may not meet your business requirements. To avoid the limit on STS API requests from affecting access to OSS, you can **add a signature to the URL of an OSS object**. For more information, see [Add signatures to URLs](~~31952~~) and [Obtain signature information from the server and upload data to OSS](~~31926~~).
        
        @param request: AssumeRoleRequest
        @return: AssumeRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.assume_role_with_options_async(request, runtime)

    def assume_role_with_oidcwith_options(
        self,
        request: sts_20150401_models.AssumeRoleWithOIDCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sts_20150401_models.AssumeRoleWithOIDCResponse:
        """
        ### Prerequisites
        - An OIDC token is obtained from an external identity provider (IdP).
        - An OIDC IdP is created in the RAM console. For more information, see [Create an OIDC IdP](~~327123~~) or [CreateOIDCProvider](~~327135~~).
        - A RAM role whose trusted entity is an OIDC IdP is created in the RAM console. For more information, see [Create a RAM role for a trusted IdP](~~116805~~) or [CreateRole](~~28710~~).
        
        @param request: AssumeRoleWithOIDCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssumeRoleWithOIDCResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration_seconds):
            query['DurationSeconds'] = request.duration_seconds
        if not UtilClient.is_unset(request.oidcprovider_arn):
            query['OIDCProviderArn'] = request.oidcprovider_arn
        if not UtilClient.is_unset(request.oidctoken):
            query['OIDCToken'] = request.oidctoken
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.role_session_name):
            query['RoleSessionName'] = request.role_session_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssumeRoleWithOIDC',
            version='2015-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sts_20150401_models.AssumeRoleWithOIDCResponse(),
            self.call_api(params, req, runtime)
        )

    async def assume_role_with_oidcwith_options_async(
        self,
        request: sts_20150401_models.AssumeRoleWithOIDCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sts_20150401_models.AssumeRoleWithOIDCResponse:
        """
        ### Prerequisites
        - An OIDC token is obtained from an external identity provider (IdP).
        - An OIDC IdP is created in the RAM console. For more information, see [Create an OIDC IdP](~~327123~~) or [CreateOIDCProvider](~~327135~~).
        - A RAM role whose trusted entity is an OIDC IdP is created in the RAM console. For more information, see [Create a RAM role for a trusted IdP](~~116805~~) or [CreateRole](~~28710~~).
        
        @param request: AssumeRoleWithOIDCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssumeRoleWithOIDCResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration_seconds):
            query['DurationSeconds'] = request.duration_seconds
        if not UtilClient.is_unset(request.oidcprovider_arn):
            query['OIDCProviderArn'] = request.oidcprovider_arn
        if not UtilClient.is_unset(request.oidctoken):
            query['OIDCToken'] = request.oidctoken
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.role_session_name):
            query['RoleSessionName'] = request.role_session_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssumeRoleWithOIDC',
            version='2015-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sts_20150401_models.AssumeRoleWithOIDCResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assume_role_with_oidc(
        self,
        request: sts_20150401_models.AssumeRoleWithOIDCRequest,
    ) -> sts_20150401_models.AssumeRoleWithOIDCResponse:
        """
        ### Prerequisites
        - An OIDC token is obtained from an external identity provider (IdP).
        - An OIDC IdP is created in the RAM console. For more information, see [Create an OIDC IdP](~~327123~~) or [CreateOIDCProvider](~~327135~~).
        - A RAM role whose trusted entity is an OIDC IdP is created in the RAM console. For more information, see [Create a RAM role for a trusted IdP](~~116805~~) or [CreateRole](~~28710~~).
        
        @param request: AssumeRoleWithOIDCRequest
        @return: AssumeRoleWithOIDCResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.assume_role_with_oidcwith_options(request, runtime)

    async def assume_role_with_oidc_async(
        self,
        request: sts_20150401_models.AssumeRoleWithOIDCRequest,
    ) -> sts_20150401_models.AssumeRoleWithOIDCResponse:
        """
        ### Prerequisites
        - An OIDC token is obtained from an external identity provider (IdP).
        - An OIDC IdP is created in the RAM console. For more information, see [Create an OIDC IdP](~~327123~~) or [CreateOIDCProvider](~~327135~~).
        - A RAM role whose trusted entity is an OIDC IdP is created in the RAM console. For more information, see [Create a RAM role for a trusted IdP](~~116805~~) or [CreateRole](~~28710~~).
        
        @param request: AssumeRoleWithOIDCRequest
        @return: AssumeRoleWithOIDCResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.assume_role_with_oidcwith_options_async(request, runtime)

    def assume_role_with_samlwith_options(
        self,
        request: sts_20150401_models.AssumeRoleWithSAMLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sts_20150401_models.AssumeRoleWithSAMLResponse:
        """
        ### Prerequisites
        - A SAML response is obtained from an external identity provider (IdP).
        - A SAML IdP is created in the RAM console. For more information, see [Create a SAML IdP](~~116083~~) or [CreateSAMLProvider](~~186846~~).
        - A RAM role whose trusted entity is a SAML IdP is created in the RAM console. For more information, see [Create a RAM role for a trusted IdP](~~116805~~) or [CreateRole](~~28710~~).
        
        @param request: AssumeRoleWithSAMLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssumeRoleWithSAMLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration_seconds):
            query['DurationSeconds'] = request.duration_seconds
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.samlassertion):
            query['SAMLAssertion'] = request.samlassertion
        if not UtilClient.is_unset(request.samlprovider_arn):
            query['SAMLProviderArn'] = request.samlprovider_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssumeRoleWithSAML',
            version='2015-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sts_20150401_models.AssumeRoleWithSAMLResponse(),
            self.call_api(params, req, runtime)
        )

    async def assume_role_with_samlwith_options_async(
        self,
        request: sts_20150401_models.AssumeRoleWithSAMLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sts_20150401_models.AssumeRoleWithSAMLResponse:
        """
        ### Prerequisites
        - A SAML response is obtained from an external identity provider (IdP).
        - A SAML IdP is created in the RAM console. For more information, see [Create a SAML IdP](~~116083~~) or [CreateSAMLProvider](~~186846~~).
        - A RAM role whose trusted entity is a SAML IdP is created in the RAM console. For more information, see [Create a RAM role for a trusted IdP](~~116805~~) or [CreateRole](~~28710~~).
        
        @param request: AssumeRoleWithSAMLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssumeRoleWithSAMLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration_seconds):
            query['DurationSeconds'] = request.duration_seconds
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.samlassertion):
            query['SAMLAssertion'] = request.samlassertion
        if not UtilClient.is_unset(request.samlprovider_arn):
            query['SAMLProviderArn'] = request.samlprovider_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssumeRoleWithSAML',
            version='2015-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sts_20150401_models.AssumeRoleWithSAMLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assume_role_with_saml(
        self,
        request: sts_20150401_models.AssumeRoleWithSAMLRequest,
    ) -> sts_20150401_models.AssumeRoleWithSAMLResponse:
        """
        ### Prerequisites
        - A SAML response is obtained from an external identity provider (IdP).
        - A SAML IdP is created in the RAM console. For more information, see [Create a SAML IdP](~~116083~~) or [CreateSAMLProvider](~~186846~~).
        - A RAM role whose trusted entity is a SAML IdP is created in the RAM console. For more information, see [Create a RAM role for a trusted IdP](~~116805~~) or [CreateRole](~~28710~~).
        
        @param request: AssumeRoleWithSAMLRequest
        @return: AssumeRoleWithSAMLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.assume_role_with_samlwith_options(request, runtime)

    async def assume_role_with_saml_async(
        self,
        request: sts_20150401_models.AssumeRoleWithSAMLRequest,
    ) -> sts_20150401_models.AssumeRoleWithSAMLResponse:
        """
        ### Prerequisites
        - A SAML response is obtained from an external identity provider (IdP).
        - A SAML IdP is created in the RAM console. For more information, see [Create a SAML IdP](~~116083~~) or [CreateSAMLProvider](~~186846~~).
        - A RAM role whose trusted entity is a SAML IdP is created in the RAM console. For more information, see [Create a RAM role for a trusted IdP](~~116805~~) or [CreateRole](~~28710~~).
        
        @param request: AssumeRoleWithSAMLRequest
        @return: AssumeRoleWithSAMLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.assume_role_with_samlwith_options_async(request, runtime)

    def get_caller_identity_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sts_20150401_models.GetCallerIdentityResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCallerIdentity',
            version='2015-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sts_20150401_models.GetCallerIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_caller_identity_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sts_20150401_models.GetCallerIdentityResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCallerIdentity',
            version='2015-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sts_20150401_models.GetCallerIdentityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_caller_identity(self) -> sts_20150401_models.GetCallerIdentityResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_caller_identity_with_options(runtime)

    async def get_caller_identity_async(self) -> sts_20150401_models.GetCallerIdentityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_caller_identity_with_options_async(runtime)
