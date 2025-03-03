# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_resourcemanager20200331 import models as resource_manager_20200331_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('resourcemanager', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def accept_handshake_with_options(
        self,
        request: resource_manager_20200331_models.AcceptHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.AcceptHandshakeResponse:
        """
        @summary Accepts an invitation.
        
        @description After an invited Alibaba Cloud account joins a resource directory, it becomes a member of the resource directory. By default, the name of the invited Alibaba Cloud account is used as the display name of the account in the resource directory.
        This topic provides an example on how to call the API operation to accept the invitation `h-Ih8IuPfvV0t0***` that is initiated to invite the Alibaba Cloud account `177242285274****` to join the resource directory `rd-3G****`.
        
        @param request: AcceptHandshakeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AcceptHandshakeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptHandshake',
            version='2020-03-31',
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
                resource_manager_20200331_models.AcceptHandshakeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.AcceptHandshakeResponse(),
                self.execute(params, req, runtime)
            )

    async def accept_handshake_with_options_async(
        self,
        request: resource_manager_20200331_models.AcceptHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.AcceptHandshakeResponse:
        """
        @summary Accepts an invitation.
        
        @description After an invited Alibaba Cloud account joins a resource directory, it becomes a member of the resource directory. By default, the name of the invited Alibaba Cloud account is used as the display name of the account in the resource directory.
        This topic provides an example on how to call the API operation to accept the invitation `h-Ih8IuPfvV0t0***` that is initiated to invite the Alibaba Cloud account `177242285274****` to join the resource directory `rd-3G****`.
        
        @param request: AcceptHandshakeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AcceptHandshakeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptHandshake',
            version='2020-03-31',
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
                resource_manager_20200331_models.AcceptHandshakeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.AcceptHandshakeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def accept_handshake(
        self,
        request: resource_manager_20200331_models.AcceptHandshakeRequest,
    ) -> resource_manager_20200331_models.AcceptHandshakeResponse:
        """
        @summary Accepts an invitation.
        
        @description After an invited Alibaba Cloud account joins a resource directory, it becomes a member of the resource directory. By default, the name of the invited Alibaba Cloud account is used as the display name of the account in the resource directory.
        This topic provides an example on how to call the API operation to accept the invitation `h-Ih8IuPfvV0t0***` that is initiated to invite the Alibaba Cloud account `177242285274****` to join the resource directory `rd-3G****`.
        
        @param request: AcceptHandshakeRequest
        @return: AcceptHandshakeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.accept_handshake_with_options(request, runtime)

    async def accept_handshake_async(
        self,
        request: resource_manager_20200331_models.AcceptHandshakeRequest,
    ) -> resource_manager_20200331_models.AcceptHandshakeResponse:
        """
        @summary Accepts an invitation.
        
        @description After an invited Alibaba Cloud account joins a resource directory, it becomes a member of the resource directory. By default, the name of the invited Alibaba Cloud account is used as the display name of the account in the resource directory.
        This topic provides an example on how to call the API operation to accept the invitation `h-Ih8IuPfvV0t0***` that is initiated to invite the Alibaba Cloud account `177242285274****` to join the resource directory `rd-3G****`.
        
        @param request: AcceptHandshakeRequest
        @return: AcceptHandshakeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.accept_handshake_with_options_async(request, runtime)

    def attach_control_policy_with_options(
        self,
        request: resource_manager_20200331_models.AttachControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.AttachControlPolicyResponse:
        """
        @description After you attach an access control policy, the operations performed on resources by using members are limited by the policy. Make sure that the attached policy meets your expectations. Otherwise, your business may be affected.
        By default, the system access control policy FullAliyunAccess is attached to each folder and member.
        The access control policy that is attached to a folder also applies to all its subfolders and all members in the subfolders.
        A maximum of 10 access control policies can be attached to a folder or member.
        This topic provides an example on how to call the API operation to attach the custom access control policy `cp-jExXAqIYkwHN***` to the folder `fd-ZDNPiT****`.
        
        @param request: AttachControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachControlPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.AttachControlPolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.AttachControlPolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def attach_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.AttachControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.AttachControlPolicyResponse:
        """
        @description After you attach an access control policy, the operations performed on resources by using members are limited by the policy. Make sure that the attached policy meets your expectations. Otherwise, your business may be affected.
        By default, the system access control policy FullAliyunAccess is attached to each folder and member.
        The access control policy that is attached to a folder also applies to all its subfolders and all members in the subfolders.
        A maximum of 10 access control policies can be attached to a folder or member.
        This topic provides an example on how to call the API operation to attach the custom access control policy `cp-jExXAqIYkwHN***` to the folder `fd-ZDNPiT****`.
        
        @param request: AttachControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachControlPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.AttachControlPolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.AttachControlPolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def attach_control_policy(
        self,
        request: resource_manager_20200331_models.AttachControlPolicyRequest,
    ) -> resource_manager_20200331_models.AttachControlPolicyResponse:
        """
        @description After you attach an access control policy, the operations performed on resources by using members are limited by the policy. Make sure that the attached policy meets your expectations. Otherwise, your business may be affected.
        By default, the system access control policy FullAliyunAccess is attached to each folder and member.
        The access control policy that is attached to a folder also applies to all its subfolders and all members in the subfolders.
        A maximum of 10 access control policies can be attached to a folder or member.
        This topic provides an example on how to call the API operation to attach the custom access control policy `cp-jExXAqIYkwHN***` to the folder `fd-ZDNPiT****`.
        
        @param request: AttachControlPolicyRequest
        @return: AttachControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_control_policy_with_options(request, runtime)

    async def attach_control_policy_async(
        self,
        request: resource_manager_20200331_models.AttachControlPolicyRequest,
    ) -> resource_manager_20200331_models.AttachControlPolicyResponse:
        """
        @description After you attach an access control policy, the operations performed on resources by using members are limited by the policy. Make sure that the attached policy meets your expectations. Otherwise, your business may be affected.
        By default, the system access control policy FullAliyunAccess is attached to each folder and member.
        The access control policy that is attached to a folder also applies to all its subfolders and all members in the subfolders.
        A maximum of 10 access control policies can be attached to a folder or member.
        This topic provides an example on how to call the API operation to attach the custom access control policy `cp-jExXAqIYkwHN***` to the folder `fd-ZDNPiT****`.
        
        @param request: AttachControlPolicyRequest
        @return: AttachControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_control_policy_with_options_async(request, runtime)

    def attach_policy_with_options(
        self,
        request: resource_manager_20200331_models.AttachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.AttachPolicyResponse:
        """
        @summary 为RAM身份授权
        
        @description In this example, the policy `AdministratorAccess` is attached to the RAM user `alice@demo.onaliyun.com` and takes effect only for resources in the `rg-9gLOoK***` resource group.
        
        @param request: AttachPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.AttachPolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.AttachPolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def attach_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.AttachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.AttachPolicyResponse:
        """
        @summary 为RAM身份授权
        
        @description In this example, the policy `AdministratorAccess` is attached to the RAM user `alice@demo.onaliyun.com` and takes effect only for resources in the `rg-9gLOoK***` resource group.
        
        @param request: AttachPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.AttachPolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.AttachPolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def attach_policy(
        self,
        request: resource_manager_20200331_models.AttachPolicyRequest,
    ) -> resource_manager_20200331_models.AttachPolicyResponse:
        """
        @summary 为RAM身份授权
        
        @description In this example, the policy `AdministratorAccess` is attached to the RAM user `alice@demo.onaliyun.com` and takes effect only for resources in the `rg-9gLOoK***` resource group.
        
        @param request: AttachPolicyRequest
        @return: AttachPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_policy_with_options(request, runtime)

    async def attach_policy_async(
        self,
        request: resource_manager_20200331_models.AttachPolicyRequest,
    ) -> resource_manager_20200331_models.AttachPolicyResponse:
        """
        @summary 为RAM身份授权
        
        @description In this example, the policy `AdministratorAccess` is attached to the RAM user `alice@demo.onaliyun.com` and takes effect only for resources in the `rg-9gLOoK***` resource group.
        
        @param request: AttachPolicyRequest
        @return: AttachPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_policy_with_options_async(request, runtime)

    def bind_secure_mobile_phone_with_options(
        self,
        request: resource_manager_20200331_models.BindSecureMobilePhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.BindSecureMobilePhoneResponse:
        """
        @summary 设置安全手机号
        
        @description You can call this API operation only to bind a mobile phone number to a member of the resource account type. You cannot call this API operation to change the mobile phone number that is bound to a member of the resource account type.
        To ensure that the system can record the operators of management operations, you must use a RAM user or RAM role to which the AliyunResourceDirectoryFullAccess policy is attached within the management account of your resource directory to call this API operation.
        This topic provides an example on how to call the API operation to bind a mobile phone number to the member `138660628348***` for security purposes.
        
        @param request: BindSecureMobilePhoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindSecureMobilePhoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        if not UtilClient.is_unset(request.verification_code):
            query['VerificationCode'] = request.verification_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindSecureMobilePhone',
            version='2020-03-31',
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
                resource_manager_20200331_models.BindSecureMobilePhoneResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.BindSecureMobilePhoneResponse(),
                self.execute(params, req, runtime)
            )

    async def bind_secure_mobile_phone_with_options_async(
        self,
        request: resource_manager_20200331_models.BindSecureMobilePhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.BindSecureMobilePhoneResponse:
        """
        @summary 设置安全手机号
        
        @description You can call this API operation only to bind a mobile phone number to a member of the resource account type. You cannot call this API operation to change the mobile phone number that is bound to a member of the resource account type.
        To ensure that the system can record the operators of management operations, you must use a RAM user or RAM role to which the AliyunResourceDirectoryFullAccess policy is attached within the management account of your resource directory to call this API operation.
        This topic provides an example on how to call the API operation to bind a mobile phone number to the member `138660628348***` for security purposes.
        
        @param request: BindSecureMobilePhoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindSecureMobilePhoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        if not UtilClient.is_unset(request.verification_code):
            query['VerificationCode'] = request.verification_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindSecureMobilePhone',
            version='2020-03-31',
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
                resource_manager_20200331_models.BindSecureMobilePhoneResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.BindSecureMobilePhoneResponse(),
                await self.execute_async(params, req, runtime)
            )

    def bind_secure_mobile_phone(
        self,
        request: resource_manager_20200331_models.BindSecureMobilePhoneRequest,
    ) -> resource_manager_20200331_models.BindSecureMobilePhoneResponse:
        """
        @summary 设置安全手机号
        
        @description You can call this API operation only to bind a mobile phone number to a member of the resource account type. You cannot call this API operation to change the mobile phone number that is bound to a member of the resource account type.
        To ensure that the system can record the operators of management operations, you must use a RAM user or RAM role to which the AliyunResourceDirectoryFullAccess policy is attached within the management account of your resource directory to call this API operation.
        This topic provides an example on how to call the API operation to bind a mobile phone number to the member `138660628348***` for security purposes.
        
        @param request: BindSecureMobilePhoneRequest
        @return: BindSecureMobilePhoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_secure_mobile_phone_with_options(request, runtime)

    async def bind_secure_mobile_phone_async(
        self,
        request: resource_manager_20200331_models.BindSecureMobilePhoneRequest,
    ) -> resource_manager_20200331_models.BindSecureMobilePhoneResponse:
        """
        @summary 设置安全手机号
        
        @description You can call this API operation only to bind a mobile phone number to a member of the resource account type. You cannot call this API operation to change the mobile phone number that is bound to a member of the resource account type.
        To ensure that the system can record the operators of management operations, you must use a RAM user or RAM role to which the AliyunResourceDirectoryFullAccess policy is attached within the management account of your resource directory to call this API operation.
        This topic provides an example on how to call the API operation to bind a mobile phone number to the member `138660628348***` for security purposes.
        
        @param request: BindSecureMobilePhoneRequest
        @return: BindSecureMobilePhoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_secure_mobile_phone_with_options_async(request, runtime)

    def cancel_change_account_email_with_options(
        self,
        request: resource_manager_20200331_models.CancelChangeAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelChangeAccountEmailResponse:
        """
        @summary 取消修改邮箱
        
        @param request: CancelChangeAccountEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelChangeAccountEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelChangeAccountEmail',
            version='2020-03-31',
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
                resource_manager_20200331_models.CancelChangeAccountEmailResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CancelChangeAccountEmailResponse(),
                self.execute(params, req, runtime)
            )

    async def cancel_change_account_email_with_options_async(
        self,
        request: resource_manager_20200331_models.CancelChangeAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelChangeAccountEmailResponse:
        """
        @summary 取消修改邮箱
        
        @param request: CancelChangeAccountEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelChangeAccountEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelChangeAccountEmail',
            version='2020-03-31',
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
                resource_manager_20200331_models.CancelChangeAccountEmailResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CancelChangeAccountEmailResponse(),
                await self.execute_async(params, req, runtime)
            )

    def cancel_change_account_email(
        self,
        request: resource_manager_20200331_models.CancelChangeAccountEmailRequest,
    ) -> resource_manager_20200331_models.CancelChangeAccountEmailResponse:
        """
        @summary 取消修改邮箱
        
        @param request: CancelChangeAccountEmailRequest
        @return: CancelChangeAccountEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_change_account_email_with_options(request, runtime)

    async def cancel_change_account_email_async(
        self,
        request: resource_manager_20200331_models.CancelChangeAccountEmailRequest,
    ) -> resource_manager_20200331_models.CancelChangeAccountEmailResponse:
        """
        @summary 取消修改邮箱
        
        @param request: CancelChangeAccountEmailRequest
        @return: CancelChangeAccountEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_change_account_email_with_options_async(request, runtime)

    def cancel_create_cloud_account_with_options(
        self,
        request: resource_manager_20200331_models.CancelCreateCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelCreateCloudAccountResponse:
        """
        @summary 取消创建云账号类型的成员
        
        @param request: CancelCreateCloudAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelCreateCloudAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelCreateCloudAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.CancelCreateCloudAccountResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CancelCreateCloudAccountResponse(),
                self.execute(params, req, runtime)
            )

    async def cancel_create_cloud_account_with_options_async(
        self,
        request: resource_manager_20200331_models.CancelCreateCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelCreateCloudAccountResponse:
        """
        @summary 取消创建云账号类型的成员
        
        @param request: CancelCreateCloudAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelCreateCloudAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelCreateCloudAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.CancelCreateCloudAccountResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CancelCreateCloudAccountResponse(),
                await self.execute_async(params, req, runtime)
            )

    def cancel_create_cloud_account(
        self,
        request: resource_manager_20200331_models.CancelCreateCloudAccountRequest,
    ) -> resource_manager_20200331_models.CancelCreateCloudAccountResponse:
        """
        @summary 取消创建云账号类型的成员
        
        @param request: CancelCreateCloudAccountRequest
        @return: CancelCreateCloudAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_create_cloud_account_with_options(request, runtime)

    async def cancel_create_cloud_account_async(
        self,
        request: resource_manager_20200331_models.CancelCreateCloudAccountRequest,
    ) -> resource_manager_20200331_models.CancelCreateCloudAccountResponse:
        """
        @summary 取消创建云账号类型的成员
        
        @param request: CancelCreateCloudAccountRequest
        @return: CancelCreateCloudAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_create_cloud_account_with_options_async(request, runtime)

    def cancel_handshake_with_options(
        self,
        request: resource_manager_20200331_models.CancelHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelHandshakeResponse:
        """
        @summary Cancels an invitation.
        
        @description This topic provides an example on how to call the API operation to cancel the invitation whose ID is `h-ycm4rp***`.
        
        @param request: CancelHandshakeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelHandshakeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelHandshake',
            version='2020-03-31',
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
                resource_manager_20200331_models.CancelHandshakeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CancelHandshakeResponse(),
                self.execute(params, req, runtime)
            )

    async def cancel_handshake_with_options_async(
        self,
        request: resource_manager_20200331_models.CancelHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelHandshakeResponse:
        """
        @summary Cancels an invitation.
        
        @description This topic provides an example on how to call the API operation to cancel the invitation whose ID is `h-ycm4rp***`.
        
        @param request: CancelHandshakeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelHandshakeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelHandshake',
            version='2020-03-31',
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
                resource_manager_20200331_models.CancelHandshakeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CancelHandshakeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def cancel_handshake(
        self,
        request: resource_manager_20200331_models.CancelHandshakeRequest,
    ) -> resource_manager_20200331_models.CancelHandshakeResponse:
        """
        @summary Cancels an invitation.
        
        @description This topic provides an example on how to call the API operation to cancel the invitation whose ID is `h-ycm4rp***`.
        
        @param request: CancelHandshakeRequest
        @return: CancelHandshakeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_handshake_with_options(request, runtime)

    async def cancel_handshake_async(
        self,
        request: resource_manager_20200331_models.CancelHandshakeRequest,
    ) -> resource_manager_20200331_models.CancelHandshakeResponse:
        """
        @summary Cancels an invitation.
        
        @description This topic provides an example on how to call the API operation to cancel the invitation whose ID is `h-ycm4rp***`.
        
        @param request: CancelHandshakeRequest
        @return: CancelHandshakeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_handshake_with_options_async(request, runtime)

    def cancel_promote_resource_account_with_options(
        self,
        request: resource_manager_20200331_models.CancelPromoteResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelPromoteResourceAccountResponse:
        """
        @summary 取消升级资源账号
        
        @param request: CancelPromoteResourceAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelPromoteResourceAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelPromoteResourceAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.CancelPromoteResourceAccountResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CancelPromoteResourceAccountResponse(),
                self.execute(params, req, runtime)
            )

    async def cancel_promote_resource_account_with_options_async(
        self,
        request: resource_manager_20200331_models.CancelPromoteResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelPromoteResourceAccountResponse:
        """
        @summary 取消升级资源账号
        
        @param request: CancelPromoteResourceAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelPromoteResourceAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelPromoteResourceAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.CancelPromoteResourceAccountResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CancelPromoteResourceAccountResponse(),
                await self.execute_async(params, req, runtime)
            )

    def cancel_promote_resource_account(
        self,
        request: resource_manager_20200331_models.CancelPromoteResourceAccountRequest,
    ) -> resource_manager_20200331_models.CancelPromoteResourceAccountResponse:
        """
        @summary 取消升级资源账号
        
        @param request: CancelPromoteResourceAccountRequest
        @return: CancelPromoteResourceAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_promote_resource_account_with_options(request, runtime)

    async def cancel_promote_resource_account_async(
        self,
        request: resource_manager_20200331_models.CancelPromoteResourceAccountRequest,
    ) -> resource_manager_20200331_models.CancelPromoteResourceAccountResponse:
        """
        @summary 取消升级资源账号
        
        @param request: CancelPromoteResourceAccountRequest
        @return: CancelPromoteResourceAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_promote_resource_account_with_options_async(request, runtime)

    def change_account_email_with_options(
        self,
        request: resource_manager_20200331_models.ChangeAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ChangeAccountEmailResponse:
        """
        @summary 成员账号设置安全邮箱
        
        @param request: ChangeAccountEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeAccountEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeAccountEmail',
            version='2020-03-31',
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
                resource_manager_20200331_models.ChangeAccountEmailResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ChangeAccountEmailResponse(),
                self.execute(params, req, runtime)
            )

    async def change_account_email_with_options_async(
        self,
        request: resource_manager_20200331_models.ChangeAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ChangeAccountEmailResponse:
        """
        @summary 成员账号设置安全邮箱
        
        @param request: ChangeAccountEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeAccountEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeAccountEmail',
            version='2020-03-31',
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
                resource_manager_20200331_models.ChangeAccountEmailResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ChangeAccountEmailResponse(),
                await self.execute_async(params, req, runtime)
            )

    def change_account_email(
        self,
        request: resource_manager_20200331_models.ChangeAccountEmailRequest,
    ) -> resource_manager_20200331_models.ChangeAccountEmailResponse:
        """
        @summary 成员账号设置安全邮箱
        
        @param request: ChangeAccountEmailRequest
        @return: ChangeAccountEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_account_email_with_options(request, runtime)

    async def change_account_email_async(
        self,
        request: resource_manager_20200331_models.ChangeAccountEmailRequest,
    ) -> resource_manager_20200331_models.ChangeAccountEmailResponse:
        """
        @summary 成员账号设置安全邮箱
        
        @param request: ChangeAccountEmailRequest
        @return: ChangeAccountEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_account_email_with_options_async(request, runtime)

    def check_account_delete_with_options(
        self,
        request: resource_manager_20200331_models.CheckAccountDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CheckAccountDeleteResponse:
        """
        @summary Performs a member deletion check.
        
        @description Before you delete a member, you must call this API operation to check whether the member can be deleted.
        This topic provides an example on how to call the API operation to perform a deletion check on the member whose ID is `179855839641***`.
        
        @param request: CheckAccountDeleteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckAccountDeleteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckAccountDelete',
            version='2020-03-31',
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
                resource_manager_20200331_models.CheckAccountDeleteResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CheckAccountDeleteResponse(),
                self.execute(params, req, runtime)
            )

    async def check_account_delete_with_options_async(
        self,
        request: resource_manager_20200331_models.CheckAccountDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CheckAccountDeleteResponse:
        """
        @summary Performs a member deletion check.
        
        @description Before you delete a member, you must call this API operation to check whether the member can be deleted.
        This topic provides an example on how to call the API operation to perform a deletion check on the member whose ID is `179855839641***`.
        
        @param request: CheckAccountDeleteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckAccountDeleteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckAccountDelete',
            version='2020-03-31',
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
                resource_manager_20200331_models.CheckAccountDeleteResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CheckAccountDeleteResponse(),
                await self.execute_async(params, req, runtime)
            )

    def check_account_delete(
        self,
        request: resource_manager_20200331_models.CheckAccountDeleteRequest,
    ) -> resource_manager_20200331_models.CheckAccountDeleteResponse:
        """
        @summary Performs a member deletion check.
        
        @description Before you delete a member, you must call this API operation to check whether the member can be deleted.
        This topic provides an example on how to call the API operation to perform a deletion check on the member whose ID is `179855839641***`.
        
        @param request: CheckAccountDeleteRequest
        @return: CheckAccountDeleteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_account_delete_with_options(request, runtime)

    async def check_account_delete_async(
        self,
        request: resource_manager_20200331_models.CheckAccountDeleteRequest,
    ) -> resource_manager_20200331_models.CheckAccountDeleteResponse:
        """
        @summary Performs a member deletion check.
        
        @description Before you delete a member, you must call this API operation to check whether the member can be deleted.
        This topic provides an example on how to call the API operation to perform a deletion check on the member whose ID is `179855839641***`.
        
        @param request: CheckAccountDeleteRequest
        @return: CheckAccountDeleteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_account_delete_with_options_async(request, runtime)

    def create_auto_grouping_rule_with_options(
        self,
        request: resource_manager_20200331_models.CreateAutoGroupingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateAutoGroupingRuleResponse:
        """
        @summary Creates a transfer rule. Custom transfer rules and transfer rules for associated resources are supported.
        
        @description You can create up to 10 custom transfer rules. Each custom transfer rule can contain up to 10 content records.
        
        @param request: CreateAutoGroupingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAutoGroupingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.exclude_region_ids_scope):
            query['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_group_ids_scope):
            query['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            query['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_types_scope):
            query['ExcludeResourceTypesScope'] = request.exclude_resource_types_scope
        if not UtilClient.is_unset(request.region_ids_scope):
            query['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            query['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_ids_scope):
            query['ResourceIdsScope'] = request.resource_ids_scope
        if not UtilClient.is_unset(request.resource_types_scope):
            query['ResourceTypesScope'] = request.resource_types_scope
        if not UtilClient.is_unset(request.rule_contents):
            query['RuleContents'] = request.rule_contents
        if not UtilClient.is_unset(request.rule_desc):
            query['RuleDesc'] = request.rule_desc
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAutoGroupingRule',
            version='2020-03-31',
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
                resource_manager_20200331_models.CreateAutoGroupingRuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CreateAutoGroupingRuleResponse(),
                self.execute(params, req, runtime)
            )

    async def create_auto_grouping_rule_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateAutoGroupingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateAutoGroupingRuleResponse:
        """
        @summary Creates a transfer rule. Custom transfer rules and transfer rules for associated resources are supported.
        
        @description You can create up to 10 custom transfer rules. Each custom transfer rule can contain up to 10 content records.
        
        @param request: CreateAutoGroupingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAutoGroupingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.exclude_region_ids_scope):
            query['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_group_ids_scope):
            query['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            query['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_types_scope):
            query['ExcludeResourceTypesScope'] = request.exclude_resource_types_scope
        if not UtilClient.is_unset(request.region_ids_scope):
            query['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            query['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_ids_scope):
            query['ResourceIdsScope'] = request.resource_ids_scope
        if not UtilClient.is_unset(request.resource_types_scope):
            query['ResourceTypesScope'] = request.resource_types_scope
        if not UtilClient.is_unset(request.rule_contents):
            query['RuleContents'] = request.rule_contents
        if not UtilClient.is_unset(request.rule_desc):
            query['RuleDesc'] = request.rule_desc
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAutoGroupingRule',
            version='2020-03-31',
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
                resource_manager_20200331_models.CreateAutoGroupingRuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CreateAutoGroupingRuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_auto_grouping_rule(
        self,
        request: resource_manager_20200331_models.CreateAutoGroupingRuleRequest,
    ) -> resource_manager_20200331_models.CreateAutoGroupingRuleResponse:
        """
        @summary Creates a transfer rule. Custom transfer rules and transfer rules for associated resources are supported.
        
        @description You can create up to 10 custom transfer rules. Each custom transfer rule can contain up to 10 content records.
        
        @param request: CreateAutoGroupingRuleRequest
        @return: CreateAutoGroupingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_auto_grouping_rule_with_options(request, runtime)

    async def create_auto_grouping_rule_async(
        self,
        request: resource_manager_20200331_models.CreateAutoGroupingRuleRequest,
    ) -> resource_manager_20200331_models.CreateAutoGroupingRuleResponse:
        """
        @summary Creates a transfer rule. Custom transfer rules and transfer rules for associated resources are supported.
        
        @description You can create up to 10 custom transfer rules. Each custom transfer rule can contain up to 10 content records.
        
        @param request: CreateAutoGroupingRuleRequest
        @return: CreateAutoGroupingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_auto_grouping_rule_with_options_async(request, runtime)

    def create_cloud_account_with_options(
        self,
        request: resource_manager_20200331_models.CreateCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateCloudAccountResponse:
        """
        @summary 创建云账号
        
        @description A resource directory supports two types of member accounts: resource accounts and cloud accounts.
        Resource account (recommended): A resource account is only used as a resource container and fully depends on a resource directory. Such member accounts are secure and easy-to-create. For more information about how to create a resource account, see [CreateResourceAccount](https://help.aliyun.com/document_detail/159392.html).
        >  A resource account can be upgraded to a cloud account. For more information, see [PromoteResourceAccount](https://help.aliyun.com/document_detail/159395.html) .
        Cloud account: A cloud account has all the features of an Alibaba Cloud account, including root permissions.
        
        @param request: CreateCloudAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCloudAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.payer_account_id):
            query['PayerAccountId'] = request.payer_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.CreateCloudAccountResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CreateCloudAccountResponse(),
                self.execute(params, req, runtime)
            )

    async def create_cloud_account_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateCloudAccountResponse:
        """
        @summary 创建云账号
        
        @description A resource directory supports two types of member accounts: resource accounts and cloud accounts.
        Resource account (recommended): A resource account is only used as a resource container and fully depends on a resource directory. Such member accounts are secure and easy-to-create. For more information about how to create a resource account, see [CreateResourceAccount](https://help.aliyun.com/document_detail/159392.html).
        >  A resource account can be upgraded to a cloud account. For more information, see [PromoteResourceAccount](https://help.aliyun.com/document_detail/159395.html) .
        Cloud account: A cloud account has all the features of an Alibaba Cloud account, including root permissions.
        
        @param request: CreateCloudAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCloudAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.payer_account_id):
            query['PayerAccountId'] = request.payer_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.CreateCloudAccountResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CreateCloudAccountResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_cloud_account(
        self,
        request: resource_manager_20200331_models.CreateCloudAccountRequest,
    ) -> resource_manager_20200331_models.CreateCloudAccountResponse:
        """
        @summary 创建云账号
        
        @description A resource directory supports two types of member accounts: resource accounts and cloud accounts.
        Resource account (recommended): A resource account is only used as a resource container and fully depends on a resource directory. Such member accounts are secure and easy-to-create. For more information about how to create a resource account, see [CreateResourceAccount](https://help.aliyun.com/document_detail/159392.html).
        >  A resource account can be upgraded to a cloud account. For more information, see [PromoteResourceAccount](https://help.aliyun.com/document_detail/159395.html) .
        Cloud account: A cloud account has all the features of an Alibaba Cloud account, including root permissions.
        
        @param request: CreateCloudAccountRequest
        @return: CreateCloudAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_account_with_options(request, runtime)

    async def create_cloud_account_async(
        self,
        request: resource_manager_20200331_models.CreateCloudAccountRequest,
    ) -> resource_manager_20200331_models.CreateCloudAccountResponse:
        """
        @summary 创建云账号
        
        @description A resource directory supports two types of member accounts: resource accounts and cloud accounts.
        Resource account (recommended): A resource account is only used as a resource container and fully depends on a resource directory. Such member accounts are secure and easy-to-create. For more information about how to create a resource account, see [CreateResourceAccount](https://help.aliyun.com/document_detail/159392.html).
        >  A resource account can be upgraded to a cloud account. For more information, see [PromoteResourceAccount](https://help.aliyun.com/document_detail/159395.html) .
        Cloud account: A cloud account has all the features of an Alibaba Cloud account, including root permissions.
        
        @param request: CreateCloudAccountRequest
        @return: CreateCloudAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cloud_account_with_options_async(request, runtime)

    def create_control_policy_with_options(
        self,
        request: resource_manager_20200331_models.CreateControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateControlPolicyResponse:
        """
        @description This topic provides an example on how to call the API operation to create a custom access control policy named `ExampleControlPolicy`. This access control policy is used to prohibit modifications to the ResourceDirectoryAccountAccessRole role and the permissions of the role.
        
        @param request: CreateControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.effect_scope):
            query['EffectScope'] = request.effect_scope
        if not UtilClient.is_unset(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateControlPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.CreateControlPolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CreateControlPolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def create_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateControlPolicyResponse:
        """
        @description This topic provides an example on how to call the API operation to create a custom access control policy named `ExampleControlPolicy`. This access control policy is used to prohibit modifications to the ResourceDirectoryAccountAccessRole role and the permissions of the role.
        
        @param request: CreateControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.effect_scope):
            query['EffectScope'] = request.effect_scope
        if not UtilClient.is_unset(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateControlPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.CreateControlPolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CreateControlPolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_control_policy(
        self,
        request: resource_manager_20200331_models.CreateControlPolicyRequest,
    ) -> resource_manager_20200331_models.CreateControlPolicyResponse:
        """
        @description This topic provides an example on how to call the API operation to create a custom access control policy named `ExampleControlPolicy`. This access control policy is used to prohibit modifications to the ResourceDirectoryAccountAccessRole role and the permissions of the role.
        
        @param request: CreateControlPolicyRequest
        @return: CreateControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_control_policy_with_options(request, runtime)

    async def create_control_policy_async(
        self,
        request: resource_manager_20200331_models.CreateControlPolicyRequest,
    ) -> resource_manager_20200331_models.CreateControlPolicyResponse:
        """
        @description This topic provides an example on how to call the API operation to create a custom access control policy named `ExampleControlPolicy`. This access control policy is used to prohibit modifications to the ResourceDirectoryAccountAccessRole role and the permissions of the role.
        
        @param request: CreateControlPolicyRequest
        @return: CreateControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_control_policy_with_options_async(request, runtime)

    def create_folder_with_options(
        self,
        request: resource_manager_20200331_models.CreateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateFolderResponse:
        """
        @description >  A maximum of five levels of folders can be created under the root folder.
        In this example, a folder named `rdFolder` is created under the root folder.
        
        @param request: CreateFolderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFolderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_name):
            query['FolderName'] = request.folder_name
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFolder',
            version='2020-03-31',
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
                resource_manager_20200331_models.CreateFolderResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CreateFolderResponse(),
                self.execute(params, req, runtime)
            )

    async def create_folder_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateFolderResponse:
        """
        @description >  A maximum of five levels of folders can be created under the root folder.
        In this example, a folder named `rdFolder` is created under the root folder.
        
        @param request: CreateFolderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFolderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_name):
            query['FolderName'] = request.folder_name
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFolder',
            version='2020-03-31',
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
                resource_manager_20200331_models.CreateFolderResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CreateFolderResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_folder(
        self,
        request: resource_manager_20200331_models.CreateFolderRequest,
    ) -> resource_manager_20200331_models.CreateFolderResponse:
        """
        @description >  A maximum of five levels of folders can be created under the root folder.
        In this example, a folder named `rdFolder` is created under the root folder.
        
        @param request: CreateFolderRequest
        @return: CreateFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_folder_with_options(request, runtime)

    async def create_folder_async(
        self,
        request: resource_manager_20200331_models.CreateFolderRequest,
    ) -> resource_manager_20200331_models.CreateFolderResponse:
        """
        @description >  A maximum of five levels of folders can be created under the root folder.
        In this example, a folder named `rdFolder` is created under the root folder.
        
        @param request: CreateFolderRequest
        @return: CreateFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_folder_with_options_async(request, runtime)

    def create_policy_with_options(
        self,
        request: resource_manager_20200331_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreatePolicyResponse:
        """
        @summary Creates a policy.
        
        @param request: CreatePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.CreatePolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CreatePolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def create_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreatePolicyResponse:
        """
        @summary Creates a policy.
        
        @param request: CreatePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.CreatePolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CreatePolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_policy(
        self,
        request: resource_manager_20200331_models.CreatePolicyRequest,
    ) -> resource_manager_20200331_models.CreatePolicyResponse:
        """
        @summary Creates a policy.
        
        @param request: CreatePolicyRequest
        @return: CreatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_policy_with_options(request, runtime)

    async def create_policy_async(
        self,
        request: resource_manager_20200331_models.CreatePolicyRequest,
    ) -> resource_manager_20200331_models.CreatePolicyResponse:
        """
        @summary Creates a policy.
        
        @param request: CreatePolicyRequest
        @return: CreatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_with_options_async(request, runtime)

    def create_policy_version_with_options(
        self,
        request: resource_manager_20200331_models.CreatePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreatePolicyVersionResponse:
        """
        @summary 创建权限策略版本
        
        @param request: CreatePolicyVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.set_as_default):
            query['SetAsDefault'] = request.set_as_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicyVersion',
            version='2020-03-31',
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
                resource_manager_20200331_models.CreatePolicyVersionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CreatePolicyVersionResponse(),
                self.execute(params, req, runtime)
            )

    async def create_policy_version_with_options_async(
        self,
        request: resource_manager_20200331_models.CreatePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreatePolicyVersionResponse:
        """
        @summary 创建权限策略版本
        
        @param request: CreatePolicyVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.set_as_default):
            query['SetAsDefault'] = request.set_as_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicyVersion',
            version='2020-03-31',
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
                resource_manager_20200331_models.CreatePolicyVersionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CreatePolicyVersionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_policy_version(
        self,
        request: resource_manager_20200331_models.CreatePolicyVersionRequest,
    ) -> resource_manager_20200331_models.CreatePolicyVersionResponse:
        """
        @summary 创建权限策略版本
        
        @param request: CreatePolicyVersionRequest
        @return: CreatePolicyVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_policy_version_with_options(request, runtime)

    async def create_policy_version_async(
        self,
        request: resource_manager_20200331_models.CreatePolicyVersionRequest,
    ) -> resource_manager_20200331_models.CreatePolicyVersionResponse:
        """
        @summary 创建权限策略版本
        
        @param request: CreatePolicyVersionRequest
        @return: CreatePolicyVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_version_with_options_async(request, runtime)

    def create_resource_account_with_options(
        self,
        request: resource_manager_20200331_models.CreateResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateResourceAccountResponse:
        """
        @summary Creates a member of the resource account type.
        
        @description A member serves as a container for resources and is also an organizational unit in a resource directory. A member indicates a project or application. The resources of different members are isolated.
        
        @param request: CreateResourceAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name_prefix):
            query['AccountNamePrefix'] = request.account_name_prefix
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.payer_account_id):
            query['PayerAccountId'] = request.payer_account_id
        if not UtilClient.is_unset(request.resell_account_type):
            query['ResellAccountType'] = request.resell_account_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.CreateResourceAccountResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CreateResourceAccountResponse(),
                self.execute(params, req, runtime)
            )

    async def create_resource_account_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateResourceAccountResponse:
        """
        @summary Creates a member of the resource account type.
        
        @description A member serves as a container for resources and is also an organizational unit in a resource directory. A member indicates a project or application. The resources of different members are isolated.
        
        @param request: CreateResourceAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name_prefix):
            query['AccountNamePrefix'] = request.account_name_prefix
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.payer_account_id):
            query['PayerAccountId'] = request.payer_account_id
        if not UtilClient.is_unset(request.resell_account_type):
            query['ResellAccountType'] = request.resell_account_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.CreateResourceAccountResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CreateResourceAccountResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_resource_account(
        self,
        request: resource_manager_20200331_models.CreateResourceAccountRequest,
    ) -> resource_manager_20200331_models.CreateResourceAccountResponse:
        """
        @summary Creates a member of the resource account type.
        
        @description A member serves as a container for resources and is also an organizational unit in a resource directory. A member indicates a project or application. The resources of different members are isolated.
        
        @param request: CreateResourceAccountRequest
        @return: CreateResourceAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_resource_account_with_options(request, runtime)

    async def create_resource_account_async(
        self,
        request: resource_manager_20200331_models.CreateResourceAccountRequest,
    ) -> resource_manager_20200331_models.CreateResourceAccountResponse:
        """
        @summary Creates a member of the resource account type.
        
        @description A member serves as a container for resources and is also an organizational unit in a resource directory. A member indicates a project or application. The resources of different members are isolated.
        
        @param request: CreateResourceAccountRequest
        @return: CreateResourceAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_account_with_options_async(request, runtime)

    def create_resource_group_with_options(
        self,
        request: resource_manager_20200331_models.CreateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateResourceGroupResponse:
        """
        @summary Creates a resource group.
        
        @description >  A maximum of 30 resource groups can be created within an Alibaba Cloud account.
        
        @param request: CreateResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceGroup',
            version='2020-03-31',
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
                resource_manager_20200331_models.CreateResourceGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CreateResourceGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def create_resource_group_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateResourceGroupResponse:
        """
        @summary Creates a resource group.
        
        @description >  A maximum of 30 resource groups can be created within an Alibaba Cloud account.
        
        @param request: CreateResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceGroup',
            version='2020-03-31',
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
                resource_manager_20200331_models.CreateResourceGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CreateResourceGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_resource_group(
        self,
        request: resource_manager_20200331_models.CreateResourceGroupRequest,
    ) -> resource_manager_20200331_models.CreateResourceGroupResponse:
        """
        @summary Creates a resource group.
        
        @description >  A maximum of 30 resource groups can be created within an Alibaba Cloud account.
        
        @param request: CreateResourceGroupRequest
        @return: CreateResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_resource_group_with_options(request, runtime)

    async def create_resource_group_async(
        self,
        request: resource_manager_20200331_models.CreateResourceGroupRequest,
    ) -> resource_manager_20200331_models.CreateResourceGroupResponse:
        """
        @summary Creates a resource group.
        
        @description >  A maximum of 30 resource groups can be created within an Alibaba Cloud account.
        
        @param request: CreateResourceGroupRequest
        @return: CreateResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_group_with_options_async(request, runtime)

    def create_role_with_options(
        self,
        request: resource_manager_20200331_models.CreateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateRoleResponse:
        """
        @summary Creates a RAM role.
        
        @param request: CreateRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.assume_role_policy_document):
            query['AssumeRolePolicyDocument'] = request.assume_role_policy_document
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.max_session_duration):
            query['MaxSessionDuration'] = request.max_session_duration
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRole',
            version='2020-03-31',
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
                resource_manager_20200331_models.CreateRoleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CreateRoleResponse(),
                self.execute(params, req, runtime)
            )

    async def create_role_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateRoleResponse:
        """
        @summary Creates a RAM role.
        
        @param request: CreateRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.assume_role_policy_document):
            query['AssumeRolePolicyDocument'] = request.assume_role_policy_document
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.max_session_duration):
            query['MaxSessionDuration'] = request.max_session_duration
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRole',
            version='2020-03-31',
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
                resource_manager_20200331_models.CreateRoleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CreateRoleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_role(
        self,
        request: resource_manager_20200331_models.CreateRoleRequest,
    ) -> resource_manager_20200331_models.CreateRoleResponse:
        """
        @summary Creates a RAM role.
        
        @param request: CreateRoleRequest
        @return: CreateRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_role_with_options(request, runtime)

    async def create_role_async(
        self,
        request: resource_manager_20200331_models.CreateRoleRequest,
    ) -> resource_manager_20200331_models.CreateRoleResponse:
        """
        @summary Creates a RAM role.
        
        @param request: CreateRoleRequest
        @return: CreateRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_role_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        request: resource_manager_20200331_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateServiceLinkedRoleResponse:
        """
        @summary 创建服务关联角色
        
        @param request: CreateServiceLinkedRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_suffix):
            query['CustomSuffix'] = request.custom_suffix
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2020-03-31',
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
                resource_manager_20200331_models.CreateServiceLinkedRoleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CreateServiceLinkedRoleResponse(),
                self.execute(params, req, runtime)
            )

    async def create_service_linked_role_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateServiceLinkedRoleResponse:
        """
        @summary 创建服务关联角色
        
        @param request: CreateServiceLinkedRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_suffix):
            query['CustomSuffix'] = request.custom_suffix
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2020-03-31',
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
                resource_manager_20200331_models.CreateServiceLinkedRoleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.CreateServiceLinkedRoleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_service_linked_role(
        self,
        request: resource_manager_20200331_models.CreateServiceLinkedRoleRequest,
    ) -> resource_manager_20200331_models.CreateServiceLinkedRoleResponse:
        """
        @summary 创建服务关联角色
        
        @param request: CreateServiceLinkedRoleRequest
        @return: CreateServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    async def create_service_linked_role_async(
        self,
        request: resource_manager_20200331_models.CreateServiceLinkedRoleRequest,
    ) -> resource_manager_20200331_models.CreateServiceLinkedRoleResponse:
        """
        @summary 创建服务关联角色
        
        @param request: CreateServiceLinkedRoleRequest
        @return: CreateServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_service_linked_role_with_options_async(request, runtime)

    def decline_handshake_with_options(
        self,
        request: resource_manager_20200331_models.DeclineHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeclineHandshakeResponse:
        """
        @summary Rejects an invitation.
        
        @param request: DeclineHandshakeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeclineHandshakeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeclineHandshake',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeclineHandshakeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeclineHandshakeResponse(),
                self.execute(params, req, runtime)
            )

    async def decline_handshake_with_options_async(
        self,
        request: resource_manager_20200331_models.DeclineHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeclineHandshakeResponse:
        """
        @summary Rejects an invitation.
        
        @param request: DeclineHandshakeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeclineHandshakeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeclineHandshake',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeclineHandshakeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeclineHandshakeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def decline_handshake(
        self,
        request: resource_manager_20200331_models.DeclineHandshakeRequest,
    ) -> resource_manager_20200331_models.DeclineHandshakeResponse:
        """
        @summary Rejects an invitation.
        
        @param request: DeclineHandshakeRequest
        @return: DeclineHandshakeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.decline_handshake_with_options(request, runtime)

    async def decline_handshake_async(
        self,
        request: resource_manager_20200331_models.DeclineHandshakeRequest,
    ) -> resource_manager_20200331_models.DeclineHandshakeResponse:
        """
        @summary Rejects an invitation.
        
        @param request: DeclineHandshakeRequest
        @return: DeclineHandshakeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.decline_handshake_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        tmp_req: resource_manager_20200331_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteAccountResponse:
        """
        @summary 账号一键删除
        
        @description The ID of the member that you want to delete.
        
        @param tmp_req: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(tmp_req)
        request = resource_manager_20200331_models.DeleteAccountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.abandonable_check_id):
            request.abandonable_check_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.abandonable_check_id, 'AbandonableCheckId', 'json')
        query = {}
        if not UtilClient.is_unset(request.abandonable_check_id_shrink):
            query['AbandonableCheckId'] = request.abandonable_check_id_shrink
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeleteAccountResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeleteAccountResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_account_with_options_async(
        self,
        tmp_req: resource_manager_20200331_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteAccountResponse:
        """
        @summary 账号一键删除
        
        @description The ID of the member that you want to delete.
        
        @param tmp_req: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(tmp_req)
        request = resource_manager_20200331_models.DeleteAccountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.abandonable_check_id):
            request.abandonable_check_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.abandonable_check_id, 'AbandonableCheckId', 'json')
        query = {}
        if not UtilClient.is_unset(request.abandonable_check_id_shrink):
            query['AbandonableCheckId'] = request.abandonable_check_id_shrink
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeleteAccountResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeleteAccountResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_account(
        self,
        request: resource_manager_20200331_models.DeleteAccountRequest,
    ) -> resource_manager_20200331_models.DeleteAccountResponse:
        """
        @summary 账号一键删除
        
        @description The ID of the member that you want to delete.
        
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: resource_manager_20200331_models.DeleteAccountRequest,
    ) -> resource_manager_20200331_models.DeleteAccountResponse:
        """
        @summary 账号一键删除
        
        @description The ID of the member that you want to delete.
        
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_auto_grouping_rule_with_options(
        self,
        request: resource_manager_20200331_models.DeleteAutoGroupingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteAutoGroupingRuleResponse:
        """
        @summary Deletes a transfer rule.
        
        @param request: DeleteAutoGroupingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAutoGroupingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoGroupingRule',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeleteAutoGroupingRuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeleteAutoGroupingRuleResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_auto_grouping_rule_with_options_async(
        self,
        request: resource_manager_20200331_models.DeleteAutoGroupingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteAutoGroupingRuleResponse:
        """
        @summary Deletes a transfer rule.
        
        @param request: DeleteAutoGroupingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAutoGroupingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoGroupingRule',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeleteAutoGroupingRuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeleteAutoGroupingRuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_auto_grouping_rule(
        self,
        request: resource_manager_20200331_models.DeleteAutoGroupingRuleRequest,
    ) -> resource_manager_20200331_models.DeleteAutoGroupingRuleResponse:
        """
        @summary Deletes a transfer rule.
        
        @param request: DeleteAutoGroupingRuleRequest
        @return: DeleteAutoGroupingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_grouping_rule_with_options(request, runtime)

    async def delete_auto_grouping_rule_async(
        self,
        request: resource_manager_20200331_models.DeleteAutoGroupingRuleRequest,
    ) -> resource_manager_20200331_models.DeleteAutoGroupingRuleResponse:
        """
        @summary Deletes a transfer rule.
        
        @param request: DeleteAutoGroupingRuleRequest
        @return: DeleteAutoGroupingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_auto_grouping_rule_with_options_async(request, runtime)

    def delete_control_policy_with_options(
        self,
        request: resource_manager_20200331_models.DeleteControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteControlPolicyResponse:
        """
        @summary 删除管控策略
        
        @description If you want to delete a custom control policy that is attached to folders or member accounts, you must call the [DetachControlPolicy](https://help.aliyun.com/document_detail/208331.html) operation to detach the policy before you delete it.
        In this example, the custom control policy `cp-SImPt8GCEwiq***` is deleted.
        
        @param request: DeleteControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteControlPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeleteControlPolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeleteControlPolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.DeleteControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteControlPolicyResponse:
        """
        @summary 删除管控策略
        
        @description If you want to delete a custom control policy that is attached to folders or member accounts, you must call the [DetachControlPolicy](https://help.aliyun.com/document_detail/208331.html) operation to detach the policy before you delete it.
        In this example, the custom control policy `cp-SImPt8GCEwiq***` is deleted.
        
        @param request: DeleteControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteControlPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeleteControlPolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeleteControlPolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_control_policy(
        self,
        request: resource_manager_20200331_models.DeleteControlPolicyRequest,
    ) -> resource_manager_20200331_models.DeleteControlPolicyResponse:
        """
        @summary 删除管控策略
        
        @description If you want to delete a custom control policy that is attached to folders or member accounts, you must call the [DetachControlPolicy](https://help.aliyun.com/document_detail/208331.html) operation to detach the policy before you delete it.
        In this example, the custom control policy `cp-SImPt8GCEwiq***` is deleted.
        
        @param request: DeleteControlPolicyRequest
        @return: DeleteControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_control_policy_with_options(request, runtime)

    async def delete_control_policy_async(
        self,
        request: resource_manager_20200331_models.DeleteControlPolicyRequest,
    ) -> resource_manager_20200331_models.DeleteControlPolicyResponse:
        """
        @summary 删除管控策略
        
        @description If you want to delete a custom control policy that is attached to folders or member accounts, you must call the [DetachControlPolicy](https://help.aliyun.com/document_detail/208331.html) operation to detach the policy before you delete it.
        In this example, the custom control policy `cp-SImPt8GCEwiq***` is deleted.
        
        @param request: DeleteControlPolicyRequest
        @return: DeleteControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_control_policy_with_options_async(request, runtime)

    def delete_folder_with_options(
        self,
        request: resource_manager_20200331_models.DeleteFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteFolderResponse:
        """
        @description >  Before you delete a folder, make sure that the folder does not contain any member accounts or child folders.
        
        @param request: DeleteFolderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFolderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFolder',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeleteFolderResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeleteFolderResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_folder_with_options_async(
        self,
        request: resource_manager_20200331_models.DeleteFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteFolderResponse:
        """
        @description >  Before you delete a folder, make sure that the folder does not contain any member accounts or child folders.
        
        @param request: DeleteFolderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFolderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFolder',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeleteFolderResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeleteFolderResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_folder(
        self,
        request: resource_manager_20200331_models.DeleteFolderRequest,
    ) -> resource_manager_20200331_models.DeleteFolderResponse:
        """
        @description >  Before you delete a folder, make sure that the folder does not contain any member accounts or child folders.
        
        @param request: DeleteFolderRequest
        @return: DeleteFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_folder_with_options(request, runtime)

    async def delete_folder_async(
        self,
        request: resource_manager_20200331_models.DeleteFolderRequest,
    ) -> resource_manager_20200331_models.DeleteFolderResponse:
        """
        @description >  Before you delete a folder, make sure that the folder does not contain any member accounts or child folders.
        
        @param request: DeleteFolderRequest
        @return: DeleteFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_folder_with_options_async(request, runtime)

    def delete_policy_with_options(
        self,
        request: resource_manager_20200331_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeletePolicyResponse:
        """
        @summary 删除权限策略
        
        @description >
        Before you delete a policy, you must delete all non-default versions of the policy. For more information about how to delete a policy version, see [DeletePolicyVersion](https://help.aliyun.com/document_detail/159041.html).
        Before you delete a policy, make sure that the policy is not referenced. This means that the policy is not attached to RAM users, RAM user groups, or RAM roles. For more information about how to detach a policy, see [DetachPolicy](https://help.aliyun.com/document_detail/159168.html).
        
        @param request: DeletePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeletePolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeletePolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeletePolicyResponse:
        """
        @summary 删除权限策略
        
        @description >
        Before you delete a policy, you must delete all non-default versions of the policy. For more information about how to delete a policy version, see [DeletePolicyVersion](https://help.aliyun.com/document_detail/159041.html).
        Before you delete a policy, make sure that the policy is not referenced. This means that the policy is not attached to RAM users, RAM user groups, or RAM roles. For more information about how to detach a policy, see [DetachPolicy](https://help.aliyun.com/document_detail/159168.html).
        
        @param request: DeletePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeletePolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeletePolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_policy(
        self,
        request: resource_manager_20200331_models.DeletePolicyRequest,
    ) -> resource_manager_20200331_models.DeletePolicyResponse:
        """
        @summary 删除权限策略
        
        @description >
        Before you delete a policy, you must delete all non-default versions of the policy. For more information about how to delete a policy version, see [DeletePolicyVersion](https://help.aliyun.com/document_detail/159041.html).
        Before you delete a policy, make sure that the policy is not referenced. This means that the policy is not attached to RAM users, RAM user groups, or RAM roles. For more information about how to detach a policy, see [DetachPolicy](https://help.aliyun.com/document_detail/159168.html).
        
        @param request: DeletePolicyRequest
        @return: DeletePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_with_options(request, runtime)

    async def delete_policy_async(
        self,
        request: resource_manager_20200331_models.DeletePolicyRequest,
    ) -> resource_manager_20200331_models.DeletePolicyResponse:
        """
        @summary 删除权限策略
        
        @description >
        Before you delete a policy, you must delete all non-default versions of the policy. For more information about how to delete a policy version, see [DeletePolicyVersion](https://help.aliyun.com/document_detail/159041.html).
        Before you delete a policy, make sure that the policy is not referenced. This means that the policy is not attached to RAM users, RAM user groups, or RAM roles. For more information about how to detach a policy, see [DetachPolicy](https://help.aliyun.com/document_detail/159168.html).
        
        @param request: DeletePolicyRequest
        @return: DeletePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_with_options_async(request, runtime)

    def delete_policy_version_with_options(
        self,
        request: resource_manager_20200331_models.DeletePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeletePolicyVersionResponse:
        """
        @summary 删除权限策略版本
        
        @description >  The default version of a permission policy cannot be deleted.
        
        @param request: DeletePolicyVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicyVersion',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeletePolicyVersionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeletePolicyVersionResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_policy_version_with_options_async(
        self,
        request: resource_manager_20200331_models.DeletePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeletePolicyVersionResponse:
        """
        @summary 删除权限策略版本
        
        @description >  The default version of a permission policy cannot be deleted.
        
        @param request: DeletePolicyVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicyVersion',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeletePolicyVersionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeletePolicyVersionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_policy_version(
        self,
        request: resource_manager_20200331_models.DeletePolicyVersionRequest,
    ) -> resource_manager_20200331_models.DeletePolicyVersionResponse:
        """
        @summary 删除权限策略版本
        
        @description >  The default version of a permission policy cannot be deleted.
        
        @param request: DeletePolicyVersionRequest
        @return: DeletePolicyVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_version_with_options(request, runtime)

    async def delete_policy_version_async(
        self,
        request: resource_manager_20200331_models.DeletePolicyVersionRequest,
    ) -> resource_manager_20200331_models.DeletePolicyVersionResponse:
        """
        @summary 删除权限策略版本
        
        @description >  The default version of a permission policy cannot be deleted.
        
        @param request: DeletePolicyVersionRequest
        @return: DeletePolicyVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_version_with_options_async(request, runtime)

    def delete_resource_group_with_options(
        self,
        request: resource_manager_20200331_models.DeleteResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteResourceGroupResponse:
        """
        @summary Deletes a resource group.
        
        @description >  Before you delete a resource group, you must delete all the resources in it.
        In this example, the resource group whose ID is `rg-9gLOoK***` is deleted.
        
        @param request: DeleteResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceGroup',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeleteResourceGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeleteResourceGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_resource_group_with_options_async(
        self,
        request: resource_manager_20200331_models.DeleteResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteResourceGroupResponse:
        """
        @summary Deletes a resource group.
        
        @description >  Before you delete a resource group, you must delete all the resources in it.
        In this example, the resource group whose ID is `rg-9gLOoK***` is deleted.
        
        @param request: DeleteResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceGroup',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeleteResourceGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeleteResourceGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_resource_group(
        self,
        request: resource_manager_20200331_models.DeleteResourceGroupRequest,
    ) -> resource_manager_20200331_models.DeleteResourceGroupResponse:
        """
        @summary Deletes a resource group.
        
        @description >  Before you delete a resource group, you must delete all the resources in it.
        In this example, the resource group whose ID is `rg-9gLOoK***` is deleted.
        
        @param request: DeleteResourceGroupRequest
        @return: DeleteResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_group_with_options(request, runtime)

    async def delete_resource_group_async(
        self,
        request: resource_manager_20200331_models.DeleteResourceGroupRequest,
    ) -> resource_manager_20200331_models.DeleteResourceGroupResponse:
        """
        @summary Deletes a resource group.
        
        @description >  Before you delete a resource group, you must delete all the resources in it.
        In this example, the resource group whose ID is `rg-9gLOoK***` is deleted.
        
        @param request: DeleteResourceGroupRequest
        @return: DeleteResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_resource_group_with_options_async(request, runtime)

    def delete_role_with_options(
        self,
        request: resource_manager_20200331_models.DeleteRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteRoleResponse:
        """
        @summary 删除角色
        
        @param request: DeleteRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRole',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeleteRoleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeleteRoleResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_role_with_options_async(
        self,
        request: resource_manager_20200331_models.DeleteRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteRoleResponse:
        """
        @summary 删除角色
        
        @param request: DeleteRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRole',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeleteRoleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeleteRoleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_role(
        self,
        request: resource_manager_20200331_models.DeleteRoleRequest,
    ) -> resource_manager_20200331_models.DeleteRoleResponse:
        """
        @summary 删除角色
        
        @param request: DeleteRoleRequest
        @return: DeleteRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_role_with_options(request, runtime)

    async def delete_role_async(
        self,
        request: resource_manager_20200331_models.DeleteRoleRequest,
    ) -> resource_manager_20200331_models.DeleteRoleResponse:
        """
        @summary 删除角色
        
        @param request: DeleteRoleRequest
        @return: DeleteRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_role_with_options_async(request, runtime)

    def delete_service_linked_role_with_options(
        self,
        request: resource_manager_20200331_models.DeleteServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteServiceLinkedRoleResponse:
        """
        @summary 删除服务关联角色
        
        @param request: DeleteServiceLinkedRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceLinkedRole',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeleteServiceLinkedRoleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeleteServiceLinkedRoleResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_service_linked_role_with_options_async(
        self,
        request: resource_manager_20200331_models.DeleteServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteServiceLinkedRoleResponse:
        """
        @summary 删除服务关联角色
        
        @param request: DeleteServiceLinkedRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceLinkedRole',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeleteServiceLinkedRoleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeleteServiceLinkedRoleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_service_linked_role(
        self,
        request: resource_manager_20200331_models.DeleteServiceLinkedRoleRequest,
    ) -> resource_manager_20200331_models.DeleteServiceLinkedRoleResponse:
        """
        @summary 删除服务关联角色
        
        @param request: DeleteServiceLinkedRoleRequest
        @return: DeleteServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_service_linked_role_with_options(request, runtime)

    async def delete_service_linked_role_async(
        self,
        request: resource_manager_20200331_models.DeleteServiceLinkedRoleRequest,
    ) -> resource_manager_20200331_models.DeleteServiceLinkedRoleResponse:
        """
        @summary 删除服务关联角色
        
        @param request: DeleteServiceLinkedRoleRequest
        @return: DeleteServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_linked_role_with_options_async(request, runtime)

    def deregister_delegated_administrator_with_options(
        self,
        request: resource_manager_20200331_models.DeregisterDelegatedAdministratorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeregisterDelegatedAdministratorResponse:
        """
        @summary 注销代理管理员
        
        @description >  If the delegated administrator account that you want to remove has historical management tasks in the related trusted service, the trusted service may be affected after the delegated administrator account is removed. Therefore, proceed with caution.
        This topic provides an example on how to call the API operation to remove the delegated administrator account `181761095690***` for Cloud Firewall.
        
        @param request: DeregisterDelegatedAdministratorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeregisterDelegatedAdministratorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterDelegatedAdministrator',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeregisterDelegatedAdministratorResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeregisterDelegatedAdministratorResponse(),
                self.execute(params, req, runtime)
            )

    async def deregister_delegated_administrator_with_options_async(
        self,
        request: resource_manager_20200331_models.DeregisterDelegatedAdministratorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeregisterDelegatedAdministratorResponse:
        """
        @summary 注销代理管理员
        
        @description >  If the delegated administrator account that you want to remove has historical management tasks in the related trusted service, the trusted service may be affected after the delegated administrator account is removed. Therefore, proceed with caution.
        This topic provides an example on how to call the API operation to remove the delegated administrator account `181761095690***` for Cloud Firewall.
        
        @param request: DeregisterDelegatedAdministratorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeregisterDelegatedAdministratorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterDelegatedAdministrator',
            version='2020-03-31',
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
                resource_manager_20200331_models.DeregisterDelegatedAdministratorResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DeregisterDelegatedAdministratorResponse(),
                await self.execute_async(params, req, runtime)
            )

    def deregister_delegated_administrator(
        self,
        request: resource_manager_20200331_models.DeregisterDelegatedAdministratorRequest,
    ) -> resource_manager_20200331_models.DeregisterDelegatedAdministratorResponse:
        """
        @summary 注销代理管理员
        
        @description >  If the delegated administrator account that you want to remove has historical management tasks in the related trusted service, the trusted service may be affected after the delegated administrator account is removed. Therefore, proceed with caution.
        This topic provides an example on how to call the API operation to remove the delegated administrator account `181761095690***` for Cloud Firewall.
        
        @param request: DeregisterDelegatedAdministratorRequest
        @return: DeregisterDelegatedAdministratorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deregister_delegated_administrator_with_options(request, runtime)

    async def deregister_delegated_administrator_async(
        self,
        request: resource_manager_20200331_models.DeregisterDelegatedAdministratorRequest,
    ) -> resource_manager_20200331_models.DeregisterDelegatedAdministratorResponse:
        """
        @summary 注销代理管理员
        
        @description >  If the delegated administrator account that you want to remove has historical management tasks in the related trusted service, the trusted service may be affected after the delegated administrator account is removed. Therefore, proceed with caution.
        This topic provides an example on how to call the API operation to remove the delegated administrator account `181761095690***` for Cloud Firewall.
        
        @param request: DeregisterDelegatedAdministratorRequest
        @return: DeregisterDelegatedAdministratorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.deregister_delegated_administrator_with_options_async(request, runtime)

    def destroy_resource_directory_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DestroyResourceDirectoryResponse:
        """
        @description Before you disable a resource directory, make sure that the following requirements are met:
        All member accounts must be removed from the resource directory. For more information about how to remove a member account, see [RemoveCloudAccount](https://help.aliyun.com/document_detail/159431.html).
        All folders except the root folder must be deleted from the resource directory. For more information about how to delete a folder, see [DeleteFolder](https://help.aliyun.com/document_detail/159432.html).
        
        @param request: DestroyResourceDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DestroyResourceDirectoryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DestroyResourceDirectory',
            version='2020-03-31',
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
                resource_manager_20200331_models.DestroyResourceDirectoryResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DestroyResourceDirectoryResponse(),
                self.execute(params, req, runtime)
            )

    async def destroy_resource_directory_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DestroyResourceDirectoryResponse:
        """
        @description Before you disable a resource directory, make sure that the following requirements are met:
        All member accounts must be removed from the resource directory. For more information about how to remove a member account, see [RemoveCloudAccount](https://help.aliyun.com/document_detail/159431.html).
        All folders except the root folder must be deleted from the resource directory. For more information about how to delete a folder, see [DeleteFolder](https://help.aliyun.com/document_detail/159432.html).
        
        @param request: DestroyResourceDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DestroyResourceDirectoryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DestroyResourceDirectory',
            version='2020-03-31',
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
                resource_manager_20200331_models.DestroyResourceDirectoryResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DestroyResourceDirectoryResponse(),
                await self.execute_async(params, req, runtime)
            )

    def destroy_resource_directory(self) -> resource_manager_20200331_models.DestroyResourceDirectoryResponse:
        """
        @description Before you disable a resource directory, make sure that the following requirements are met:
        All member accounts must be removed from the resource directory. For more information about how to remove a member account, see [RemoveCloudAccount](https://help.aliyun.com/document_detail/159431.html).
        All folders except the root folder must be deleted from the resource directory. For more information about how to delete a folder, see [DeleteFolder](https://help.aliyun.com/document_detail/159432.html).
        
        @return: DestroyResourceDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.destroy_resource_directory_with_options(runtime)

    async def destroy_resource_directory_async(self) -> resource_manager_20200331_models.DestroyResourceDirectoryResponse:
        """
        @description Before you disable a resource directory, make sure that the following requirements are met:
        All member accounts must be removed from the resource directory. For more information about how to remove a member account, see [RemoveCloudAccount](https://help.aliyun.com/document_detail/159431.html).
        All folders except the root folder must be deleted from the resource directory. For more information about how to delete a folder, see [DeleteFolder](https://help.aliyun.com/document_detail/159432.html).
        
        @return: DestroyResourceDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.destroy_resource_directory_with_options_async(runtime)

    def detach_control_policy_with_options(
        self,
        request: resource_manager_20200331_models.DetachControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DetachControlPolicyResponse:
        """
        @summary 解绑管控策略
        
        @description After you detach an access control policy, the operations performed on resources by using members are not limited by the policy. Make sure that the detached policy meets your expectations. Otherwise, your business may be affected.
        Both the system and custom access control policies can be detached. If an object has only one access control policy attached, the policy cannot be detached.
        This topic provides an example on how to call the API operation to detach the custom control policy `cp-jExXAqIYkwHN***` from the folder `fd-ZDNPiT****`.
        
        @param request: DetachControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachControlPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.DetachControlPolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DetachControlPolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def detach_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.DetachControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DetachControlPolicyResponse:
        """
        @summary 解绑管控策略
        
        @description After you detach an access control policy, the operations performed on resources by using members are not limited by the policy. Make sure that the detached policy meets your expectations. Otherwise, your business may be affected.
        Both the system and custom access control policies can be detached. If an object has only one access control policy attached, the policy cannot be detached.
        This topic provides an example on how to call the API operation to detach the custom control policy `cp-jExXAqIYkwHN***` from the folder `fd-ZDNPiT****`.
        
        @param request: DetachControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachControlPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.DetachControlPolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DetachControlPolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def detach_control_policy(
        self,
        request: resource_manager_20200331_models.DetachControlPolicyRequest,
    ) -> resource_manager_20200331_models.DetachControlPolicyResponse:
        """
        @summary 解绑管控策略
        
        @description After you detach an access control policy, the operations performed on resources by using members are not limited by the policy. Make sure that the detached policy meets your expectations. Otherwise, your business may be affected.
        Both the system and custom access control policies can be detached. If an object has only one access control policy attached, the policy cannot be detached.
        This topic provides an example on how to call the API operation to detach the custom control policy `cp-jExXAqIYkwHN***` from the folder `fd-ZDNPiT****`.
        
        @param request: DetachControlPolicyRequest
        @return: DetachControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_control_policy_with_options(request, runtime)

    async def detach_control_policy_async(
        self,
        request: resource_manager_20200331_models.DetachControlPolicyRequest,
    ) -> resource_manager_20200331_models.DetachControlPolicyResponse:
        """
        @summary 解绑管控策略
        
        @description After you detach an access control policy, the operations performed on resources by using members are not limited by the policy. Make sure that the detached policy meets your expectations. Otherwise, your business may be affected.
        Both the system and custom access control policies can be detached. If an object has only one access control policy attached, the policy cannot be detached.
        This topic provides an example on how to call the API operation to detach the custom control policy `cp-jExXAqIYkwHN***` from the folder `fd-ZDNPiT****`.
        
        @param request: DetachControlPolicyRequest
        @return: DetachControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_control_policy_with_options_async(request, runtime)

    def detach_policy_with_options(
        self,
        request: resource_manager_20200331_models.DetachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DetachPolicyResponse:
        """
        @summary 为RAM身份移除权限
        
        @param request: DetachPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.DetachPolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DetachPolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def detach_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.DetachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DetachPolicyResponse:
        """
        @summary 为RAM身份移除权限
        
        @param request: DetachPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.DetachPolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DetachPolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def detach_policy(
        self,
        request: resource_manager_20200331_models.DetachPolicyRequest,
    ) -> resource_manager_20200331_models.DetachPolicyResponse:
        """
        @summary 为RAM身份移除权限
        
        @param request: DetachPolicyRequest
        @return: DetachPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_policy_with_options(request, runtime)

    async def detach_policy_async(
        self,
        request: resource_manager_20200331_models.DetachPolicyRequest,
    ) -> resource_manager_20200331_models.DetachPolicyResponse:
        """
        @summary 为RAM身份移除权限
        
        @param request: DetachPolicyRequest
        @return: DetachPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_policy_with_options_async(request, runtime)

    def disable_associated_transfer_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DisableAssociatedTransferResponse:
        """
        @summary Disables the Transfer Associated Resources feature.
        
        @param request: DisableAssociatedTransferRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableAssociatedTransferResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableAssociatedTransfer',
            version='2020-03-31',
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
                resource_manager_20200331_models.DisableAssociatedTransferResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DisableAssociatedTransferResponse(),
                self.execute(params, req, runtime)
            )

    async def disable_associated_transfer_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DisableAssociatedTransferResponse:
        """
        @summary Disables the Transfer Associated Resources feature.
        
        @param request: DisableAssociatedTransferRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableAssociatedTransferResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableAssociatedTransfer',
            version='2020-03-31',
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
                resource_manager_20200331_models.DisableAssociatedTransferResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DisableAssociatedTransferResponse(),
                await self.execute_async(params, req, runtime)
            )

    def disable_associated_transfer(self) -> resource_manager_20200331_models.DisableAssociatedTransferResponse:
        """
        @summary Disables the Transfer Associated Resources feature.
        
        @return: DisableAssociatedTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_associated_transfer_with_options(runtime)

    async def disable_associated_transfer_async(self) -> resource_manager_20200331_models.DisableAssociatedTransferResponse:
        """
        @summary Disables the Transfer Associated Resources feature.
        
        @return: DisableAssociatedTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_associated_transfer_with_options_async(runtime)

    def disable_auto_grouping_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DisableAutoGroupingResponse:
        """
        @summary Disables the Automatic Resource Transfer feature. After the feature is disabled, existing custom transfer rules and existing transfer rules for associated resources are deleted. However, existing relationships between resources and resource groups are not affected. If you still want to use this feature, you can enable it again 1 minute later.
        
        @param request: DisableAutoGroupingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableAutoGroupingResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableAutoGrouping',
            version='2020-03-31',
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
                resource_manager_20200331_models.DisableAutoGroupingResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DisableAutoGroupingResponse(),
                self.execute(params, req, runtime)
            )

    async def disable_auto_grouping_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DisableAutoGroupingResponse:
        """
        @summary Disables the Automatic Resource Transfer feature. After the feature is disabled, existing custom transfer rules and existing transfer rules for associated resources are deleted. However, existing relationships between resources and resource groups are not affected. If you still want to use this feature, you can enable it again 1 minute later.
        
        @param request: DisableAutoGroupingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableAutoGroupingResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableAutoGrouping',
            version='2020-03-31',
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
                resource_manager_20200331_models.DisableAutoGroupingResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DisableAutoGroupingResponse(),
                await self.execute_async(params, req, runtime)
            )

    def disable_auto_grouping(self) -> resource_manager_20200331_models.DisableAutoGroupingResponse:
        """
        @summary Disables the Automatic Resource Transfer feature. After the feature is disabled, existing custom transfer rules and existing transfer rules for associated resources are deleted. However, existing relationships between resources and resource groups are not affected. If you still want to use this feature, you can enable it again 1 minute later.
        
        @return: DisableAutoGroupingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_auto_grouping_with_options(runtime)

    async def disable_auto_grouping_async(self) -> resource_manager_20200331_models.DisableAutoGroupingResponse:
        """
        @summary Disables the Automatic Resource Transfer feature. After the feature is disabled, existing custom transfer rules and existing transfer rules for associated resources are deleted. However, existing relationships between resources and resource groups are not affected. If you still want to use this feature, you can enable it again 1 minute later.
        
        @return: DisableAutoGroupingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_auto_grouping_with_options_async(runtime)

    def disable_control_policy_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DisableControlPolicyResponse:
        """
        @summary 禁用管控策略
        
        @description After you disable the Control Policy feature, the system automatically detaches all control policies that are attached to folders and member accounts. The system does not delete these control policies, but you cannot attach them to folders or member accounts again.
        >  If you disable the Control Policy feature, the permissions of all folders and member accounts in a resource directory are affected. You must proceed with caution.
        
        @param request: DisableControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableControlPolicyResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableControlPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.DisableControlPolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DisableControlPolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def disable_control_policy_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DisableControlPolicyResponse:
        """
        @summary 禁用管控策略
        
        @description After you disable the Control Policy feature, the system automatically detaches all control policies that are attached to folders and member accounts. The system does not delete these control policies, but you cannot attach them to folders or member accounts again.
        >  If you disable the Control Policy feature, the permissions of all folders and member accounts in a resource directory are affected. You must proceed with caution.
        
        @param request: DisableControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableControlPolicyResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableControlPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.DisableControlPolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.DisableControlPolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def disable_control_policy(self) -> resource_manager_20200331_models.DisableControlPolicyResponse:
        """
        @summary 禁用管控策略
        
        @description After you disable the Control Policy feature, the system automatically detaches all control policies that are attached to folders and member accounts. The system does not delete these control policies, but you cannot attach them to folders or member accounts again.
        >  If you disable the Control Policy feature, the permissions of all folders and member accounts in a resource directory are affected. You must proceed with caution.
        
        @return: DisableControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_control_policy_with_options(runtime)

    async def disable_control_policy_async(self) -> resource_manager_20200331_models.DisableControlPolicyResponse:
        """
        @summary 禁用管控策略
        
        @description After you disable the Control Policy feature, the system automatically detaches all control policies that are attached to folders and member accounts. The system does not delete these control policies, but you cannot attach them to folders or member accounts again.
        >  If you disable the Control Policy feature, the permissions of all folders and member accounts in a resource directory are affected. You must proceed with caution.
        
        @return: DisableControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_control_policy_with_options_async(runtime)

    def enable_associated_transfer_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.EnableAssociatedTransferResponse:
        """
        @summary Enables the Transfer Associated Resources feature.
        
        @param request: EnableAssociatedTransferRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableAssociatedTransferResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableAssociatedTransfer',
            version='2020-03-31',
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
                resource_manager_20200331_models.EnableAssociatedTransferResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.EnableAssociatedTransferResponse(),
                self.execute(params, req, runtime)
            )

    async def enable_associated_transfer_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.EnableAssociatedTransferResponse:
        """
        @summary Enables the Transfer Associated Resources feature.
        
        @param request: EnableAssociatedTransferRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableAssociatedTransferResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableAssociatedTransfer',
            version='2020-03-31',
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
                resource_manager_20200331_models.EnableAssociatedTransferResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.EnableAssociatedTransferResponse(),
                await self.execute_async(params, req, runtime)
            )

    def enable_associated_transfer(self) -> resource_manager_20200331_models.EnableAssociatedTransferResponse:
        """
        @summary Enables the Transfer Associated Resources feature.
        
        @return: EnableAssociatedTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_associated_transfer_with_options(runtime)

    async def enable_associated_transfer_async(self) -> resource_manager_20200331_models.EnableAssociatedTransferResponse:
        """
        @summary Enables the Transfer Associated Resources feature.
        
        @return: EnableAssociatedTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_associated_transfer_with_options_async(runtime)

    def enable_auto_grouping_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.EnableAutoGroupingResponse:
        """
        @summary Enables the Automatic Resource Transfer feature. After the feature is enabled, you can create, update, delete, and query transfer rules.
        
        @param request: EnableAutoGroupingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableAutoGroupingResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableAutoGrouping',
            version='2020-03-31',
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
                resource_manager_20200331_models.EnableAutoGroupingResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.EnableAutoGroupingResponse(),
                self.execute(params, req, runtime)
            )

    async def enable_auto_grouping_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.EnableAutoGroupingResponse:
        """
        @summary Enables the Automatic Resource Transfer feature. After the feature is enabled, you can create, update, delete, and query transfer rules.
        
        @param request: EnableAutoGroupingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableAutoGroupingResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableAutoGrouping',
            version='2020-03-31',
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
                resource_manager_20200331_models.EnableAutoGroupingResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.EnableAutoGroupingResponse(),
                await self.execute_async(params, req, runtime)
            )

    def enable_auto_grouping(self) -> resource_manager_20200331_models.EnableAutoGroupingResponse:
        """
        @summary Enables the Automatic Resource Transfer feature. After the feature is enabled, you can create, update, delete, and query transfer rules.
        
        @return: EnableAutoGroupingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_auto_grouping_with_options(runtime)

    async def enable_auto_grouping_async(self) -> resource_manager_20200331_models.EnableAutoGroupingResponse:
        """
        @summary Enables the Automatic Resource Transfer feature. After the feature is enabled, you can create, update, delete, and query transfer rules.
        
        @return: EnableAutoGroupingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_auto_grouping_with_options_async(runtime)

    def enable_control_policy_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.EnableControlPolicyResponse:
        """
        @summary Enables the Control Policy feature.
        
        @description The Control Policy feature allows you to manage the permission boundaries of the folders or member accounts in a resource directory in a centralized manner. This feature is implemented based on the resource directory. You can use this feature to develop common or dedicated rules for access control. The Control Policy feature does not grant permissions but only defines permission boundaries. A member account in a resource directory can be used to access resources only after it is granted the required permissions by using the Resource Access Management (RAM) service. For more information, see [Overview of the Control Policy feature](https://help.aliyun.com/document_detail/178671.html).
        
        @param request: EnableControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableControlPolicyResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableControlPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.EnableControlPolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.EnableControlPolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def enable_control_policy_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.EnableControlPolicyResponse:
        """
        @summary Enables the Control Policy feature.
        
        @description The Control Policy feature allows you to manage the permission boundaries of the folders or member accounts in a resource directory in a centralized manner. This feature is implemented based on the resource directory. You can use this feature to develop common or dedicated rules for access control. The Control Policy feature does not grant permissions but only defines permission boundaries. A member account in a resource directory can be used to access resources only after it is granted the required permissions by using the Resource Access Management (RAM) service. For more information, see [Overview of the Control Policy feature](https://help.aliyun.com/document_detail/178671.html).
        
        @param request: EnableControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableControlPolicyResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableControlPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.EnableControlPolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.EnableControlPolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def enable_control_policy(self) -> resource_manager_20200331_models.EnableControlPolicyResponse:
        """
        @summary Enables the Control Policy feature.
        
        @description The Control Policy feature allows you to manage the permission boundaries of the folders or member accounts in a resource directory in a centralized manner. This feature is implemented based on the resource directory. You can use this feature to develop common or dedicated rules for access control. The Control Policy feature does not grant permissions but only defines permission boundaries. A member account in a resource directory can be used to access resources only after it is granted the required permissions by using the Resource Access Management (RAM) service. For more information, see [Overview of the Control Policy feature](https://help.aliyun.com/document_detail/178671.html).
        
        @return: EnableControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_control_policy_with_options(runtime)

    async def enable_control_policy_async(self) -> resource_manager_20200331_models.EnableControlPolicyResponse:
        """
        @summary Enables the Control Policy feature.
        
        @description The Control Policy feature allows you to manage the permission boundaries of the folders or member accounts in a resource directory in a centralized manner. This feature is implemented based on the resource directory. You can use this feature to develop common or dedicated rules for access control. The Control Policy feature does not grant permissions but only defines permission boundaries. A member account in a resource directory can be used to access resources only after it is granted the required permissions by using the Resource Access Management (RAM) service. For more information, see [Overview of the Control Policy feature](https://help.aliyun.com/document_detail/178671.html).
        
        @return: EnableControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_control_policy_with_options_async(runtime)

    def enable_resource_directory_with_options(
        self,
        request: resource_manager_20200331_models.EnableResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.EnableResourceDirectoryResponse:
        """
        @summary 开启RD
        
        @description You can use the current account or a newly created account to enable a resource directory. For more information, see [Enable a resource directory](https://help.aliyun.com/document_detail/111215.html).
        In this example, the current account is used to enable a resource directory.
        
        @param request: EnableResourceDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableResourceDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_mode):
            query['EnableMode'] = request.enable_mode
        if not UtilClient.is_unset(request.maname):
            query['MAName'] = request.maname
        if not UtilClient.is_unset(request.masecure_mobile_phone):
            query['MASecureMobilePhone'] = request.masecure_mobile_phone
        if not UtilClient.is_unset(request.verification_code):
            query['VerificationCode'] = request.verification_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableResourceDirectory',
            version='2020-03-31',
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
                resource_manager_20200331_models.EnableResourceDirectoryResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.EnableResourceDirectoryResponse(),
                self.execute(params, req, runtime)
            )

    async def enable_resource_directory_with_options_async(
        self,
        request: resource_manager_20200331_models.EnableResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.EnableResourceDirectoryResponse:
        """
        @summary 开启RD
        
        @description You can use the current account or a newly created account to enable a resource directory. For more information, see [Enable a resource directory](https://help.aliyun.com/document_detail/111215.html).
        In this example, the current account is used to enable a resource directory.
        
        @param request: EnableResourceDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableResourceDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_mode):
            query['EnableMode'] = request.enable_mode
        if not UtilClient.is_unset(request.maname):
            query['MAName'] = request.maname
        if not UtilClient.is_unset(request.masecure_mobile_phone):
            query['MASecureMobilePhone'] = request.masecure_mobile_phone
        if not UtilClient.is_unset(request.verification_code):
            query['VerificationCode'] = request.verification_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableResourceDirectory',
            version='2020-03-31',
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
                resource_manager_20200331_models.EnableResourceDirectoryResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.EnableResourceDirectoryResponse(),
                await self.execute_async(params, req, runtime)
            )

    def enable_resource_directory(
        self,
        request: resource_manager_20200331_models.EnableResourceDirectoryRequest,
    ) -> resource_manager_20200331_models.EnableResourceDirectoryResponse:
        """
        @summary 开启RD
        
        @description You can use the current account or a newly created account to enable a resource directory. For more information, see [Enable a resource directory](https://help.aliyun.com/document_detail/111215.html).
        In this example, the current account is used to enable a resource directory.
        
        @param request: EnableResourceDirectoryRequest
        @return: EnableResourceDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_resource_directory_with_options(request, runtime)

    async def enable_resource_directory_async(
        self,
        request: resource_manager_20200331_models.EnableResourceDirectoryRequest,
    ) -> resource_manager_20200331_models.EnableResourceDirectoryResponse:
        """
        @summary 开启RD
        
        @description You can use the current account or a newly created account to enable a resource directory. For more information, see [Enable a resource directory](https://help.aliyun.com/document_detail/111215.html).
        In this example, the current account is used to enable a resource directory.
        
        @param request: EnableResourceDirectoryRequest
        @return: EnableResourceDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_resource_directory_with_options_async(request, runtime)

    def get_account_with_options(
        self,
        request: resource_manager_20200331_models.GetAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetAccountResponse:
        """
        @description This topic provides an example on how to call the API operation to query the information of the member whose Alibaba Cloud account ID is `181761095690***`.
        
        @param request: GetAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetAccountResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetAccountResponse(),
                self.execute(params, req, runtime)
            )

    async def get_account_with_options_async(
        self,
        request: resource_manager_20200331_models.GetAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetAccountResponse:
        """
        @description This topic provides an example on how to call the API operation to query the information of the member whose Alibaba Cloud account ID is `181761095690***`.
        
        @param request: GetAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetAccountResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetAccountResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_account(
        self,
        request: resource_manager_20200331_models.GetAccountRequest,
    ) -> resource_manager_20200331_models.GetAccountResponse:
        """
        @description This topic provides an example on how to call the API operation to query the information of the member whose Alibaba Cloud account ID is `181761095690***`.
        
        @param request: GetAccountRequest
        @return: GetAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_account_with_options(request, runtime)

    async def get_account_async(
        self,
        request: resource_manager_20200331_models.GetAccountRequest,
    ) -> resource_manager_20200331_models.GetAccountResponse:
        """
        @description This topic provides an example on how to call the API operation to query the information of the member whose Alibaba Cloud account ID is `181761095690***`.
        
        @param request: GetAccountRequest
        @return: GetAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_account_with_options_async(request, runtime)

    def get_account_deletion_check_result_with_options(
        self,
        request: resource_manager_20200331_models.GetAccountDeletionCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetAccountDeletionCheckResultResponse:
        """
        @summary Queries the result of a member deletion check.
        
        @description After you call the [CheckAccountDelete](https://help.aliyun.com/document_detail/448542.html) operation to perform a member deletion check, you can call the GetAccountDeletionCheckResult operation to query the check result. If the check result shows that the member meets deletion requirements, you can delete the member. Otherwise, you need to first modify the items that do not meet requirements.
        This topic provides an example on how to call the API operation to query the result of the deletion check for the member whose ID is `179855839641***`. The response shows that the member does not meet deletion requirements.
        
        @param request: GetAccountDeletionCheckResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccountDeletionCheckResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountDeletionCheckResult',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetAccountDeletionCheckResultResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetAccountDeletionCheckResultResponse(),
                self.execute(params, req, runtime)
            )

    async def get_account_deletion_check_result_with_options_async(
        self,
        request: resource_manager_20200331_models.GetAccountDeletionCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetAccountDeletionCheckResultResponse:
        """
        @summary Queries the result of a member deletion check.
        
        @description After you call the [CheckAccountDelete](https://help.aliyun.com/document_detail/448542.html) operation to perform a member deletion check, you can call the GetAccountDeletionCheckResult operation to query the check result. If the check result shows that the member meets deletion requirements, you can delete the member. Otherwise, you need to first modify the items that do not meet requirements.
        This topic provides an example on how to call the API operation to query the result of the deletion check for the member whose ID is `179855839641***`. The response shows that the member does not meet deletion requirements.
        
        @param request: GetAccountDeletionCheckResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccountDeletionCheckResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountDeletionCheckResult',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetAccountDeletionCheckResultResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetAccountDeletionCheckResultResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_account_deletion_check_result(
        self,
        request: resource_manager_20200331_models.GetAccountDeletionCheckResultRequest,
    ) -> resource_manager_20200331_models.GetAccountDeletionCheckResultResponse:
        """
        @summary Queries the result of a member deletion check.
        
        @description After you call the [CheckAccountDelete](https://help.aliyun.com/document_detail/448542.html) operation to perform a member deletion check, you can call the GetAccountDeletionCheckResult operation to query the check result. If the check result shows that the member meets deletion requirements, you can delete the member. Otherwise, you need to first modify the items that do not meet requirements.
        This topic provides an example on how to call the API operation to query the result of the deletion check for the member whose ID is `179855839641***`. The response shows that the member does not meet deletion requirements.
        
        @param request: GetAccountDeletionCheckResultRequest
        @return: GetAccountDeletionCheckResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_account_deletion_check_result_with_options(request, runtime)

    async def get_account_deletion_check_result_async(
        self,
        request: resource_manager_20200331_models.GetAccountDeletionCheckResultRequest,
    ) -> resource_manager_20200331_models.GetAccountDeletionCheckResultResponse:
        """
        @summary Queries the result of a member deletion check.
        
        @description After you call the [CheckAccountDelete](https://help.aliyun.com/document_detail/448542.html) operation to perform a member deletion check, you can call the GetAccountDeletionCheckResult operation to query the check result. If the check result shows that the member meets deletion requirements, you can delete the member. Otherwise, you need to first modify the items that do not meet requirements.
        This topic provides an example on how to call the API operation to query the result of the deletion check for the member whose ID is `179855839641***`. The response shows that the member does not meet deletion requirements.
        
        @param request: GetAccountDeletionCheckResultRequest
        @return: GetAccountDeletionCheckResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_account_deletion_check_result_with_options_async(request, runtime)

    def get_account_deletion_status_with_options(
        self,
        request: resource_manager_20200331_models.GetAccountDeletionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetAccountDeletionStatusResponse:
        """
        @summary 获取账号删除状态
        
        @description This topic provides an example on how to call the API operation to query the deletion status of the member whose Alibaba Cloud account ID is `169946124551***`. The response shows that the member is deleted.
        
        @param request: GetAccountDeletionStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccountDeletionStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountDeletionStatus',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetAccountDeletionStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetAccountDeletionStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def get_account_deletion_status_with_options_async(
        self,
        request: resource_manager_20200331_models.GetAccountDeletionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetAccountDeletionStatusResponse:
        """
        @summary 获取账号删除状态
        
        @description This topic provides an example on how to call the API operation to query the deletion status of the member whose Alibaba Cloud account ID is `169946124551***`. The response shows that the member is deleted.
        
        @param request: GetAccountDeletionStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccountDeletionStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountDeletionStatus',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetAccountDeletionStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetAccountDeletionStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_account_deletion_status(
        self,
        request: resource_manager_20200331_models.GetAccountDeletionStatusRequest,
    ) -> resource_manager_20200331_models.GetAccountDeletionStatusResponse:
        """
        @summary 获取账号删除状态
        
        @description This topic provides an example on how to call the API operation to query the deletion status of the member whose Alibaba Cloud account ID is `169946124551***`. The response shows that the member is deleted.
        
        @param request: GetAccountDeletionStatusRequest
        @return: GetAccountDeletionStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_account_deletion_status_with_options(request, runtime)

    async def get_account_deletion_status_async(
        self,
        request: resource_manager_20200331_models.GetAccountDeletionStatusRequest,
    ) -> resource_manager_20200331_models.GetAccountDeletionStatusResponse:
        """
        @summary 获取账号删除状态
        
        @description This topic provides an example on how to call the API operation to query the deletion status of the member whose Alibaba Cloud account ID is `169946124551***`. The response shows that the member is deleted.
        
        @param request: GetAccountDeletionStatusRequest
        @return: GetAccountDeletionStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_account_deletion_status_with_options_async(request, runtime)

    def get_auto_grouping_rule_with_options(
        self,
        request: resource_manager_20200331_models.GetAutoGroupingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetAutoGroupingRuleResponse:
        """
        @summary Queries the information about a transfer rule.
        
        @param request: GetAutoGroupingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoGroupingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoGroupingRule',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetAutoGroupingRuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetAutoGroupingRuleResponse(),
                self.execute(params, req, runtime)
            )

    async def get_auto_grouping_rule_with_options_async(
        self,
        request: resource_manager_20200331_models.GetAutoGroupingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetAutoGroupingRuleResponse:
        """
        @summary Queries the information about a transfer rule.
        
        @param request: GetAutoGroupingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoGroupingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoGroupingRule',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetAutoGroupingRuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetAutoGroupingRuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_auto_grouping_rule(
        self,
        request: resource_manager_20200331_models.GetAutoGroupingRuleRequest,
    ) -> resource_manager_20200331_models.GetAutoGroupingRuleResponse:
        """
        @summary Queries the information about a transfer rule.
        
        @param request: GetAutoGroupingRuleRequest
        @return: GetAutoGroupingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_auto_grouping_rule_with_options(request, runtime)

    async def get_auto_grouping_rule_async(
        self,
        request: resource_manager_20200331_models.GetAutoGroupingRuleRequest,
    ) -> resource_manager_20200331_models.GetAutoGroupingRuleResponse:
        """
        @summary Queries the information about a transfer rule.
        
        @param request: GetAutoGroupingRuleRequest
        @return: GetAutoGroupingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_grouping_rule_with_options_async(request, runtime)

    def get_auto_grouping_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetAutoGroupingStatusResponse:
        """
        @summary Queries the status of the Automatic Resource Transfer feature.
        
        @param request: GetAutoGroupingStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoGroupingStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAutoGroupingStatus',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetAutoGroupingStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetAutoGroupingStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def get_auto_grouping_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetAutoGroupingStatusResponse:
        """
        @summary Queries the status of the Automatic Resource Transfer feature.
        
        @param request: GetAutoGroupingStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoGroupingStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAutoGroupingStatus',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetAutoGroupingStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetAutoGroupingStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_auto_grouping_status(self) -> resource_manager_20200331_models.GetAutoGroupingStatusResponse:
        """
        @summary Queries the status of the Automatic Resource Transfer feature.
        
        @return: GetAutoGroupingStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_auto_grouping_status_with_options(runtime)

    async def get_auto_grouping_status_async(self) -> resource_manager_20200331_models.GetAutoGroupingStatusResponse:
        """
        @summary Queries the status of the Automatic Resource Transfer feature.
        
        @return: GetAutoGroupingStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_grouping_status_with_options_async(runtime)

    def get_control_policy_with_options(
        self,
        request: resource_manager_20200331_models.GetControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetControlPolicyResponse:
        """
        @description This topic provides an example on how to call the API operation to query the details of the access control policy whose ID is `cp-SImPt8GCEwiq***`.
        
        @param request: GetControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetControlPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetControlPolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetControlPolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def get_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.GetControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetControlPolicyResponse:
        """
        @description This topic provides an example on how to call the API operation to query the details of the access control policy whose ID is `cp-SImPt8GCEwiq***`.
        
        @param request: GetControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetControlPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetControlPolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetControlPolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_control_policy(
        self,
        request: resource_manager_20200331_models.GetControlPolicyRequest,
    ) -> resource_manager_20200331_models.GetControlPolicyResponse:
        """
        @description This topic provides an example on how to call the API operation to query the details of the access control policy whose ID is `cp-SImPt8GCEwiq***`.
        
        @param request: GetControlPolicyRequest
        @return: GetControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_control_policy_with_options(request, runtime)

    async def get_control_policy_async(
        self,
        request: resource_manager_20200331_models.GetControlPolicyRequest,
    ) -> resource_manager_20200331_models.GetControlPolicyResponse:
        """
        @description This topic provides an example on how to call the API operation to query the details of the access control policy whose ID is `cp-SImPt8GCEwiq***`.
        
        @param request: GetControlPolicyRequest
        @return: GetControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_control_policy_with_options_async(request, runtime)

    def get_control_policy_enablement_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetControlPolicyEnablementStatusResponse:
        """
        @summary Queries the status of the Control Policy feature.
        
        @param request: GetControlPolicyEnablementStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetControlPolicyEnablementStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetControlPolicyEnablementStatus',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetControlPolicyEnablementStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetControlPolicyEnablementStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def get_control_policy_enablement_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetControlPolicyEnablementStatusResponse:
        """
        @summary Queries the status of the Control Policy feature.
        
        @param request: GetControlPolicyEnablementStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetControlPolicyEnablementStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetControlPolicyEnablementStatus',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetControlPolicyEnablementStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetControlPolicyEnablementStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_control_policy_enablement_status(self) -> resource_manager_20200331_models.GetControlPolicyEnablementStatusResponse:
        """
        @summary Queries the status of the Control Policy feature.
        
        @return: GetControlPolicyEnablementStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_control_policy_enablement_status_with_options(runtime)

    async def get_control_policy_enablement_status_async(self) -> resource_manager_20200331_models.GetControlPolicyEnablementStatusResponse:
        """
        @summary Queries the status of the Control Policy feature.
        
        @return: GetControlPolicyEnablementStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_control_policy_enablement_status_with_options_async(runtime)

    def get_folder_with_options(
        self,
        request: resource_manager_20200331_models.GetFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetFolderResponse:
        """
        @description In this example, the information of the folder `fd-Jyl5U7***` is queried.
        
        @param request: GetFolderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFolderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFolder',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetFolderResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetFolderResponse(),
                self.execute(params, req, runtime)
            )

    async def get_folder_with_options_async(
        self,
        request: resource_manager_20200331_models.GetFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetFolderResponse:
        """
        @description In this example, the information of the folder `fd-Jyl5U7***` is queried.
        
        @param request: GetFolderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFolderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFolder',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetFolderResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetFolderResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_folder(
        self,
        request: resource_manager_20200331_models.GetFolderRequest,
    ) -> resource_manager_20200331_models.GetFolderResponse:
        """
        @description In this example, the information of the folder `fd-Jyl5U7***` is queried.
        
        @param request: GetFolderRequest
        @return: GetFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_folder_with_options(request, runtime)

    async def get_folder_async(
        self,
        request: resource_manager_20200331_models.GetFolderRequest,
    ) -> resource_manager_20200331_models.GetFolderResponse:
        """
        @description In this example, the information of the folder `fd-Jyl5U7***` is queried.
        
        @param request: GetFolderRequest
        @return: GetFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_folder_with_options_async(request, runtime)

    def get_handshake_with_options(
        self,
        request: resource_manager_20200331_models.GetHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetHandshakeResponse:
        """
        @summary Queries the information of an invitation.
        
        @description In this example, the information of the invitation whose ID is `h-ycm4rp***` is queried.
        
        @param request: GetHandshakeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHandshakeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHandshake',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetHandshakeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetHandshakeResponse(),
                self.execute(params, req, runtime)
            )

    async def get_handshake_with_options_async(
        self,
        request: resource_manager_20200331_models.GetHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetHandshakeResponse:
        """
        @summary Queries the information of an invitation.
        
        @description In this example, the information of the invitation whose ID is `h-ycm4rp***` is queried.
        
        @param request: GetHandshakeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHandshakeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHandshake',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetHandshakeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetHandshakeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_handshake(
        self,
        request: resource_manager_20200331_models.GetHandshakeRequest,
    ) -> resource_manager_20200331_models.GetHandshakeResponse:
        """
        @summary Queries the information of an invitation.
        
        @description In this example, the information of the invitation whose ID is `h-ycm4rp***` is queried.
        
        @param request: GetHandshakeRequest
        @return: GetHandshakeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_handshake_with_options(request, runtime)

    async def get_handshake_async(
        self,
        request: resource_manager_20200331_models.GetHandshakeRequest,
    ) -> resource_manager_20200331_models.GetHandshakeResponse:
        """
        @summary Queries the information of an invitation.
        
        @description In this example, the information of the invitation whose ID is `h-ycm4rp***` is queried.
        
        @param request: GetHandshakeRequest
        @return: GetHandshakeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_handshake_with_options_async(request, runtime)

    def get_payer_for_account_with_options(
        self,
        request: resource_manager_20200331_models.GetPayerForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPayerForAccountResponse:
        """
        @param request: GetPayerForAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPayerForAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPayerForAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetPayerForAccountResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetPayerForAccountResponse(),
                self.execute(params, req, runtime)
            )

    async def get_payer_for_account_with_options_async(
        self,
        request: resource_manager_20200331_models.GetPayerForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPayerForAccountResponse:
        """
        @param request: GetPayerForAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPayerForAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPayerForAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetPayerForAccountResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetPayerForAccountResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_payer_for_account(
        self,
        request: resource_manager_20200331_models.GetPayerForAccountRequest,
    ) -> resource_manager_20200331_models.GetPayerForAccountResponse:
        """
        @param request: GetPayerForAccountRequest
        @return: GetPayerForAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_payer_for_account_with_options(request, runtime)

    async def get_payer_for_account_async(
        self,
        request: resource_manager_20200331_models.GetPayerForAccountRequest,
    ) -> resource_manager_20200331_models.GetPayerForAccountResponse:
        """
        @param request: GetPayerForAccountRequest
        @return: GetPayerForAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_payer_for_account_with_options_async(request, runtime)

    def get_policy_with_options(
        self,
        request: resource_manager_20200331_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPolicyResponse:
        """
        @summary Queries the information of a policy.
        
        @param request: GetPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetPolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetPolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def get_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPolicyResponse:
        """
        @summary Queries the information of a policy.
        
        @param request: GetPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetPolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetPolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_policy(
        self,
        request: resource_manager_20200331_models.GetPolicyRequest,
    ) -> resource_manager_20200331_models.GetPolicyResponse:
        """
        @summary Queries the information of a policy.
        
        @param request: GetPolicyRequest
        @return: GetPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_policy_with_options(request, runtime)

    async def get_policy_async(
        self,
        request: resource_manager_20200331_models.GetPolicyRequest,
    ) -> resource_manager_20200331_models.GetPolicyResponse:
        """
        @summary Queries the information of a policy.
        
        @param request: GetPolicyRequest
        @return: GetPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_with_options_async(request, runtime)

    def get_policy_version_with_options(
        self,
        request: resource_manager_20200331_models.GetPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPolicyVersionResponse:
        """
        @summary 获取权限策略的指定版本
        
        @param request: GetPolicyVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicyVersion',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetPolicyVersionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetPolicyVersionResponse(),
                self.execute(params, req, runtime)
            )

    async def get_policy_version_with_options_async(
        self,
        request: resource_manager_20200331_models.GetPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPolicyVersionResponse:
        """
        @summary 获取权限策略的指定版本
        
        @param request: GetPolicyVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicyVersion',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetPolicyVersionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetPolicyVersionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_policy_version(
        self,
        request: resource_manager_20200331_models.GetPolicyVersionRequest,
    ) -> resource_manager_20200331_models.GetPolicyVersionResponse:
        """
        @summary 获取权限策略的指定版本
        
        @param request: GetPolicyVersionRequest
        @return: GetPolicyVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_policy_version_with_options(request, runtime)

    async def get_policy_version_async(
        self,
        request: resource_manager_20200331_models.GetPolicyVersionRequest,
    ) -> resource_manager_20200331_models.GetPolicyVersionResponse:
        """
        @summary 获取权限策略的指定版本
        
        @param request: GetPolicyVersionRequest
        @return: GetPolicyVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_version_with_options_async(request, runtime)

    def get_resource_directory_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetResourceDirectoryResponse:
        """
        @summary Queries the information of a resource directory. If you use a management account to call this API operation, the system returns the information of the resource directory that is enabled by using the management account. If you use a member to call this operation, the system returns the information of
        
        @description This topic provides an example on how to use a management account to call the API operation to query the information of the resource directory that is enabled by using the management account.
        
        @param request: GetResourceDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceDirectoryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceDirectory',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetResourceDirectoryResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetResourceDirectoryResponse(),
                self.execute(params, req, runtime)
            )

    async def get_resource_directory_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetResourceDirectoryResponse:
        """
        @summary Queries the information of a resource directory. If you use a management account to call this API operation, the system returns the information of the resource directory that is enabled by using the management account. If you use a member to call this operation, the system returns the information of
        
        @description This topic provides an example on how to use a management account to call the API operation to query the information of the resource directory that is enabled by using the management account.
        
        @param request: GetResourceDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceDirectoryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceDirectory',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetResourceDirectoryResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetResourceDirectoryResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_resource_directory(self) -> resource_manager_20200331_models.GetResourceDirectoryResponse:
        """
        @summary Queries the information of a resource directory. If you use a management account to call this API operation, the system returns the information of the resource directory that is enabled by using the management account. If you use a member to call this operation, the system returns the information of
        
        @description This topic provides an example on how to use a management account to call the API operation to query the information of the resource directory that is enabled by using the management account.
        
        @return: GetResourceDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_directory_with_options(runtime)

    async def get_resource_directory_async(self) -> resource_manager_20200331_models.GetResourceDirectoryResponse:
        """
        @summary Queries the information of a resource directory. If you use a management account to call this API operation, the system returns the information of the resource directory that is enabled by using the management account. If you use a member to call this operation, the system returns the information of
        
        @description This topic provides an example on how to use a management account to call the API operation to query the information of the resource directory that is enabled by using the management account.
        
        @return: GetResourceDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_directory_with_options_async(runtime)

    def get_resource_group_with_options(
        self,
        request: resource_manager_20200331_models.GetResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetResourceGroupResponse:
        """
        @summary In this example, the information of the resource group whose ID is `rg-9gLOoK***` is queried.
        
        @description For more information about common request parameters, see [Common parameters](https://help.aliyun.com/document_detail/159973.html).
        
        @param request: GetResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceGroup',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetResourceGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetResourceGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def get_resource_group_with_options_async(
        self,
        request: resource_manager_20200331_models.GetResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetResourceGroupResponse:
        """
        @summary In this example, the information of the resource group whose ID is `rg-9gLOoK***` is queried.
        
        @description For more information about common request parameters, see [Common parameters](https://help.aliyun.com/document_detail/159973.html).
        
        @param request: GetResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceGroup',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetResourceGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetResourceGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_resource_group(
        self,
        request: resource_manager_20200331_models.GetResourceGroupRequest,
    ) -> resource_manager_20200331_models.GetResourceGroupResponse:
        """
        @summary In this example, the information of the resource group whose ID is `rg-9gLOoK***` is queried.
        
        @description For more information about common request parameters, see [Common parameters](https://help.aliyun.com/document_detail/159973.html).
        
        @param request: GetResourceGroupRequest
        @return: GetResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_group_with_options(request, runtime)

    async def get_resource_group_async(
        self,
        request: resource_manager_20200331_models.GetResourceGroupRequest,
    ) -> resource_manager_20200331_models.GetResourceGroupResponse:
        """
        @summary In this example, the information of the resource group whose ID is `rg-9gLOoK***` is queried.
        
        @description For more information about common request parameters, see [Common parameters](https://help.aliyun.com/document_detail/159973.html).
        
        @param request: GetResourceGroupRequest
        @return: GetResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_group_with_options_async(request, runtime)

    def get_role_with_options(
        self,
        request: resource_manager_20200331_models.GetRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetRoleResponse:
        """
        @summary Queries the information of a RAM role.
        
        @param request: GetRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRole',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetRoleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetRoleResponse(),
                self.execute(params, req, runtime)
            )

    async def get_role_with_options_async(
        self,
        request: resource_manager_20200331_models.GetRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetRoleResponse:
        """
        @summary Queries the information of a RAM role.
        
        @param request: GetRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRole',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetRoleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetRoleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_role(
        self,
        request: resource_manager_20200331_models.GetRoleRequest,
    ) -> resource_manager_20200331_models.GetRoleResponse:
        """
        @summary Queries the information of a RAM role.
        
        @param request: GetRoleRequest
        @return: GetRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_role_with_options(request, runtime)

    async def get_role_async(
        self,
        request: resource_manager_20200331_models.GetRoleRequest,
    ) -> resource_manager_20200331_models.GetRoleResponse:
        """
        @summary Queries the information of a RAM role.
        
        @param request: GetRoleRequest
        @return: GetRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_role_with_options_async(request, runtime)

    def get_service_linked_role_deletion_status_with_options(
        self,
        request: resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse:
        """
        @summary Query the status of the deletion task for a service linked role.
        
        @param request: GetServiceLinkedRoleDeletionStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceLinkedRoleDeletionStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_task_id):
            query['DeletionTaskId'] = request.deletion_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceLinkedRoleDeletionStatus',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def get_service_linked_role_deletion_status_with_options_async(
        self,
        request: resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse:
        """
        @summary Query the status of the deletion task for a service linked role.
        
        @param request: GetServiceLinkedRoleDeletionStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceLinkedRoleDeletionStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_task_id):
            query['DeletionTaskId'] = request.deletion_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceLinkedRoleDeletionStatus',
            version='2020-03-31',
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
                resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_service_linked_role_deletion_status(
        self,
        request: resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusRequest,
    ) -> resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse:
        """
        @summary Query the status of the deletion task for a service linked role.
        
        @param request: GetServiceLinkedRoleDeletionStatusRequest
        @return: GetServiceLinkedRoleDeletionStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_service_linked_role_deletion_status_with_options(request, runtime)

    async def get_service_linked_role_deletion_status_async(
        self,
        request: resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusRequest,
    ) -> resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse:
        """
        @summary Query the status of the deletion task for a service linked role.
        
        @param request: GetServiceLinkedRoleDeletionStatusRequest
        @return: GetServiceLinkedRoleDeletionStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_linked_role_deletion_status_with_options_async(request, runtime)

    def init_resource_directory_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.InitResourceDirectoryResponse:
        """
        @summary Enables a resource directory. After you enable a resource directory, the system automatically creates a root folder and sets the current account as the enterprise management account of the resource directory. The enterprise management account has all administrative permissions on this resource direc
        
        @description >
        An account can be used to enable a resource directory only after it passes enterprise real-name verification. An account that only passed individual real-name verification cannot be used to enable a resource directory.
        We recommend that you only use the enterprise management account as the administrator of the resource directory. Do not use the enterprise management account to purchase cloud resources.
        
        @param request: InitResourceDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitResourceDirectoryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='InitResourceDirectory',
            version='2020-03-31',
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
                resource_manager_20200331_models.InitResourceDirectoryResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.InitResourceDirectoryResponse(),
                self.execute(params, req, runtime)
            )

    async def init_resource_directory_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.InitResourceDirectoryResponse:
        """
        @summary Enables a resource directory. After you enable a resource directory, the system automatically creates a root folder and sets the current account as the enterprise management account of the resource directory. The enterprise management account has all administrative permissions on this resource direc
        
        @description >
        An account can be used to enable a resource directory only after it passes enterprise real-name verification. An account that only passed individual real-name verification cannot be used to enable a resource directory.
        We recommend that you only use the enterprise management account as the administrator of the resource directory. Do not use the enterprise management account to purchase cloud resources.
        
        @param request: InitResourceDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitResourceDirectoryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='InitResourceDirectory',
            version='2020-03-31',
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
                resource_manager_20200331_models.InitResourceDirectoryResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.InitResourceDirectoryResponse(),
                await self.execute_async(params, req, runtime)
            )

    def init_resource_directory(self) -> resource_manager_20200331_models.InitResourceDirectoryResponse:
        """
        @summary Enables a resource directory. After you enable a resource directory, the system automatically creates a root folder and sets the current account as the enterprise management account of the resource directory. The enterprise management account has all administrative permissions on this resource direc
        
        @description >
        An account can be used to enable a resource directory only after it passes enterprise real-name verification. An account that only passed individual real-name verification cannot be used to enable a resource directory.
        We recommend that you only use the enterprise management account as the administrator of the resource directory. Do not use the enterprise management account to purchase cloud resources.
        
        @return: InitResourceDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.init_resource_directory_with_options(runtime)

    async def init_resource_directory_async(self) -> resource_manager_20200331_models.InitResourceDirectoryResponse:
        """
        @summary Enables a resource directory. After you enable a resource directory, the system automatically creates a root folder and sets the current account as the enterprise management account of the resource directory. The enterprise management account has all administrative permissions on this resource direc
        
        @description >
        An account can be used to enable a resource directory only after it passes enterprise real-name verification. An account that only passed individual real-name verification cannot be used to enable a resource directory.
        We recommend that you only use the enterprise management account as the administrator of the resource directory. Do not use the enterprise management account to purchase cloud resources.
        
        @return: InitResourceDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.init_resource_directory_with_options_async(runtime)

    def invite_account_to_resource_directory_with_options(
        self,
        request: resource_manager_20200331_models.InviteAccountToResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse:
        """
        @summary Invites an account to join a resource directory.
        
        @description This topic provides an example on how to call the API operation to invite the account `someone@example.com` to join a resource directory.
        
        @param request: InviteAccountToResourceDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InviteAccountToResourceDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.target_entity):
            query['TargetEntity'] = request.target_entity
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InviteAccountToResourceDirectory',
            version='2020-03-31',
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
                resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse(),
                self.execute(params, req, runtime)
            )

    async def invite_account_to_resource_directory_with_options_async(
        self,
        request: resource_manager_20200331_models.InviteAccountToResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse:
        """
        @summary Invites an account to join a resource directory.
        
        @description This topic provides an example on how to call the API operation to invite the account `someone@example.com` to join a resource directory.
        
        @param request: InviteAccountToResourceDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InviteAccountToResourceDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.target_entity):
            query['TargetEntity'] = request.target_entity
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InviteAccountToResourceDirectory',
            version='2020-03-31',
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
                resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse(),
                await self.execute_async(params, req, runtime)
            )

    def invite_account_to_resource_directory(
        self,
        request: resource_manager_20200331_models.InviteAccountToResourceDirectoryRequest,
    ) -> resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse:
        """
        @summary Invites an account to join a resource directory.
        
        @description This topic provides an example on how to call the API operation to invite the account `someone@example.com` to join a resource directory.
        
        @param request: InviteAccountToResourceDirectoryRequest
        @return: InviteAccountToResourceDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.invite_account_to_resource_directory_with_options(request, runtime)

    async def invite_account_to_resource_directory_async(
        self,
        request: resource_manager_20200331_models.InviteAccountToResourceDirectoryRequest,
    ) -> resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse:
        """
        @summary Invites an account to join a resource directory.
        
        @description This topic provides an example on how to call the API operation to invite the account `someone@example.com` to join a resource directory.
        
        @param request: InviteAccountToResourceDirectoryRequest
        @return: InviteAccountToResourceDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.invite_account_to_resource_directory_with_options_async(request, runtime)

    def list_accounts_with_options(
        self,
        request: resource_manager_20200331_models.ListAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAccountsResponse:
        """
        @summary Queries all the members in a resource directory.
        
        @description You can use only the management account of a resource directory or a delegated administrator account of a trusted service to call this operation.
        
        @param request: ListAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccounts',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListAccountsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListAccountsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_accounts_with_options_async(
        self,
        request: resource_manager_20200331_models.ListAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAccountsResponse:
        """
        @summary Queries all the members in a resource directory.
        
        @description You can use only the management account of a resource directory or a delegated administrator account of a trusted service to call this operation.
        
        @param request: ListAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccounts',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListAccountsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListAccountsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_accounts(
        self,
        request: resource_manager_20200331_models.ListAccountsRequest,
    ) -> resource_manager_20200331_models.ListAccountsResponse:
        """
        @summary Queries all the members in a resource directory.
        
        @description You can use only the management account of a resource directory or a delegated administrator account of a trusted service to call this operation.
        
        @param request: ListAccountsRequest
        @return: ListAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_accounts_with_options(request, runtime)

    async def list_accounts_async(
        self,
        request: resource_manager_20200331_models.ListAccountsRequest,
    ) -> resource_manager_20200331_models.ListAccountsResponse:
        """
        @summary Queries all the members in a resource directory.
        
        @description You can use only the management account of a resource directory or a delegated administrator account of a trusted service to call this operation.
        
        @param request: ListAccountsRequest
        @return: ListAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_accounts_with_options_async(request, runtime)

    def list_accounts_for_parent_with_options(
        self,
        request: resource_manager_20200331_models.ListAccountsForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAccountsForParentResponse:
        """
        @summary Queries the information of members in a folder.
        
        @param request: ListAccountsForParentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccountsForParentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccountsForParent',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListAccountsForParentResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListAccountsForParentResponse(),
                self.execute(params, req, runtime)
            )

    async def list_accounts_for_parent_with_options_async(
        self,
        request: resource_manager_20200331_models.ListAccountsForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAccountsForParentResponse:
        """
        @summary Queries the information of members in a folder.
        
        @param request: ListAccountsForParentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccountsForParentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccountsForParent',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListAccountsForParentResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListAccountsForParentResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_accounts_for_parent(
        self,
        request: resource_manager_20200331_models.ListAccountsForParentRequest,
    ) -> resource_manager_20200331_models.ListAccountsForParentResponse:
        """
        @summary Queries the information of members in a folder.
        
        @param request: ListAccountsForParentRequest
        @return: ListAccountsForParentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_accounts_for_parent_with_options(request, runtime)

    async def list_accounts_for_parent_async(
        self,
        request: resource_manager_20200331_models.ListAccountsForParentRequest,
    ) -> resource_manager_20200331_models.ListAccountsForParentResponse:
        """
        @summary Queries the information of members in a folder.
        
        @param request: ListAccountsForParentRequest
        @return: ListAccountsForParentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_accounts_for_parent_with_options_async(request, runtime)

    def list_ancestors_with_options(
        self,
        request: resource_manager_20200331_models.ListAncestorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAncestorsResponse:
        """
        @param request: ListAncestorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAncestorsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_id):
            query['ChildId'] = request.child_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAncestors',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListAncestorsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListAncestorsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_ancestors_with_options_async(
        self,
        request: resource_manager_20200331_models.ListAncestorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAncestorsResponse:
        """
        @param request: ListAncestorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAncestorsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_id):
            query['ChildId'] = request.child_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAncestors',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListAncestorsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListAncestorsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_ancestors(
        self,
        request: resource_manager_20200331_models.ListAncestorsRequest,
    ) -> resource_manager_20200331_models.ListAncestorsResponse:
        """
        @param request: ListAncestorsRequest
        @return: ListAncestorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ancestors_with_options(request, runtime)

    async def list_ancestors_async(
        self,
        request: resource_manager_20200331_models.ListAncestorsRequest,
    ) -> resource_manager_20200331_models.ListAncestorsResponse:
        """
        @param request: ListAncestorsRequest
        @return: ListAncestorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ancestors_with_options_async(request, runtime)

    def list_associated_transfer_setting_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAssociatedTransferSettingResponse:
        """
        @summary Queries the settings of the Transfer Associated Resources feature.
        
        @param request: ListAssociatedTransferSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAssociatedTransferSettingResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListAssociatedTransferSetting',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListAssociatedTransferSettingResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListAssociatedTransferSettingResponse(),
                self.execute(params, req, runtime)
            )

    async def list_associated_transfer_setting_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAssociatedTransferSettingResponse:
        """
        @summary Queries the settings of the Transfer Associated Resources feature.
        
        @param request: ListAssociatedTransferSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAssociatedTransferSettingResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListAssociatedTransferSetting',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListAssociatedTransferSettingResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListAssociatedTransferSettingResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_associated_transfer_setting(self) -> resource_manager_20200331_models.ListAssociatedTransferSettingResponse:
        """
        @summary Queries the settings of the Transfer Associated Resources feature.
        
        @return: ListAssociatedTransferSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_associated_transfer_setting_with_options(runtime)

    async def list_associated_transfer_setting_async(self) -> resource_manager_20200331_models.ListAssociatedTransferSettingResponse:
        """
        @summary Queries the settings of the Transfer Associated Resources feature.
        
        @return: ListAssociatedTransferSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_associated_transfer_setting_with_options_async(runtime)

    def list_auto_grouping_rules_with_options(
        self,
        request: resource_manager_20200331_models.ListAutoGroupingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAutoGroupingRulesResponse:
        """
        @summary Queries a list of transfer rules.
        
        @param request: ListAutoGroupingRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAutoGroupingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAutoGroupingRules',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListAutoGroupingRulesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListAutoGroupingRulesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_auto_grouping_rules_with_options_async(
        self,
        request: resource_manager_20200331_models.ListAutoGroupingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAutoGroupingRulesResponse:
        """
        @summary Queries a list of transfer rules.
        
        @param request: ListAutoGroupingRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAutoGroupingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAutoGroupingRules',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListAutoGroupingRulesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListAutoGroupingRulesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_auto_grouping_rules(
        self,
        request: resource_manager_20200331_models.ListAutoGroupingRulesRequest,
    ) -> resource_manager_20200331_models.ListAutoGroupingRulesResponse:
        """
        @summary Queries a list of transfer rules.
        
        @param request: ListAutoGroupingRulesRequest
        @return: ListAutoGroupingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_auto_grouping_rules_with_options(request, runtime)

    async def list_auto_grouping_rules_async(
        self,
        request: resource_manager_20200331_models.ListAutoGroupingRulesRequest,
    ) -> resource_manager_20200331_models.ListAutoGroupingRulesResponse:
        """
        @summary Queries a list of transfer rules.
        
        @param request: ListAutoGroupingRulesRequest
        @return: ListAutoGroupingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_auto_grouping_rules_with_options_async(request, runtime)

    def list_control_policies_with_options(
        self,
        request: resource_manager_20200331_models.ListControlPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListControlPoliciesResponse:
        """
        @summary Queries access control policies.
        
        @description This topic provides an example on how to call the API operation to query the system access control policies within a resource directory. The response shows that the resource directory has only one system access control policy. The policy is named `FullAliyunAccess`.
        
        @param request: ListControlPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListControlPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListControlPolicies',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListControlPoliciesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListControlPoliciesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_control_policies_with_options_async(
        self,
        request: resource_manager_20200331_models.ListControlPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListControlPoliciesResponse:
        """
        @summary Queries access control policies.
        
        @description This topic provides an example on how to call the API operation to query the system access control policies within a resource directory. The response shows that the resource directory has only one system access control policy. The policy is named `FullAliyunAccess`.
        
        @param request: ListControlPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListControlPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListControlPolicies',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListControlPoliciesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListControlPoliciesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_control_policies(
        self,
        request: resource_manager_20200331_models.ListControlPoliciesRequest,
    ) -> resource_manager_20200331_models.ListControlPoliciesResponse:
        """
        @summary Queries access control policies.
        
        @description This topic provides an example on how to call the API operation to query the system access control policies within a resource directory. The response shows that the resource directory has only one system access control policy. The policy is named `FullAliyunAccess`.
        
        @param request: ListControlPoliciesRequest
        @return: ListControlPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_control_policies_with_options(request, runtime)

    async def list_control_policies_async(
        self,
        request: resource_manager_20200331_models.ListControlPoliciesRequest,
    ) -> resource_manager_20200331_models.ListControlPoliciesResponse:
        """
        @summary Queries access control policies.
        
        @description This topic provides an example on how to call the API operation to query the system access control policies within a resource directory. The response shows that the resource directory has only one system access control policy. The policy is named `FullAliyunAccess`.
        
        @param request: ListControlPoliciesRequest
        @return: ListControlPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_control_policies_with_options_async(request, runtime)

    def list_control_policy_attachments_for_target_with_options(
        self,
        request: resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetResponse:
        """
        @description This topic provides an example on how to call the API operation to query the access control policies that are attached to the folder `fd-ZDNPiT***`.
        
        @param request: ListControlPolicyAttachmentsForTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListControlPolicyAttachmentsForTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListControlPolicyAttachmentsForTarget',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetResponse(),
                self.execute(params, req, runtime)
            )

    async def list_control_policy_attachments_for_target_with_options_async(
        self,
        request: resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetResponse:
        """
        @description This topic provides an example on how to call the API operation to query the access control policies that are attached to the folder `fd-ZDNPiT***`.
        
        @param request: ListControlPolicyAttachmentsForTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListControlPolicyAttachmentsForTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListControlPolicyAttachmentsForTarget',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_control_policy_attachments_for_target(
        self,
        request: resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetRequest,
    ) -> resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetResponse:
        """
        @description This topic provides an example on how to call the API operation to query the access control policies that are attached to the folder `fd-ZDNPiT***`.
        
        @param request: ListControlPolicyAttachmentsForTargetRequest
        @return: ListControlPolicyAttachmentsForTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_control_policy_attachments_for_target_with_options(request, runtime)

    async def list_control_policy_attachments_for_target_async(
        self,
        request: resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetRequest,
    ) -> resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetResponse:
        """
        @description This topic provides an example on how to call the API operation to query the access control policies that are attached to the folder `fd-ZDNPiT***`.
        
        @param request: ListControlPolicyAttachmentsForTargetRequest
        @return: ListControlPolicyAttachmentsForTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_control_policy_attachments_for_target_with_options_async(request, runtime)

    def list_delegated_administrators_with_options(
        self,
        request: resource_manager_20200331_models.ListDelegatedAdministratorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListDelegatedAdministratorsResponse:
        """
        @summary 列出所有的代理管理员
        
        @description This topic provides an example on how to call the API operation to query all delegated administrator accounts in a resource directory. The response shows that two delegated administrator accounts for Cloud Firewall exist in the resource directory.
        
        @param request: ListDelegatedAdministratorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDelegatedAdministratorsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDelegatedAdministrators',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListDelegatedAdministratorsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListDelegatedAdministratorsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_delegated_administrators_with_options_async(
        self,
        request: resource_manager_20200331_models.ListDelegatedAdministratorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListDelegatedAdministratorsResponse:
        """
        @summary 列出所有的代理管理员
        
        @description This topic provides an example on how to call the API operation to query all delegated administrator accounts in a resource directory. The response shows that two delegated administrator accounts for Cloud Firewall exist in the resource directory.
        
        @param request: ListDelegatedAdministratorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDelegatedAdministratorsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDelegatedAdministrators',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListDelegatedAdministratorsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListDelegatedAdministratorsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_delegated_administrators(
        self,
        request: resource_manager_20200331_models.ListDelegatedAdministratorsRequest,
    ) -> resource_manager_20200331_models.ListDelegatedAdministratorsResponse:
        """
        @summary 列出所有的代理管理员
        
        @description This topic provides an example on how to call the API operation to query all delegated administrator accounts in a resource directory. The response shows that two delegated administrator accounts for Cloud Firewall exist in the resource directory.
        
        @param request: ListDelegatedAdministratorsRequest
        @return: ListDelegatedAdministratorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_delegated_administrators_with_options(request, runtime)

    async def list_delegated_administrators_async(
        self,
        request: resource_manager_20200331_models.ListDelegatedAdministratorsRequest,
    ) -> resource_manager_20200331_models.ListDelegatedAdministratorsResponse:
        """
        @summary 列出所有的代理管理员
        
        @description This topic provides an example on how to call the API operation to query all delegated administrator accounts in a resource directory. The response shows that two delegated administrator accounts for Cloud Firewall exist in the resource directory.
        
        @param request: ListDelegatedAdministratorsRequest
        @return: ListDelegatedAdministratorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_delegated_administrators_with_options_async(request, runtime)

    def list_delegated_services_for_account_with_options(
        self,
        request: resource_manager_20200331_models.ListDelegatedServicesForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListDelegatedServicesForAccountResponse:
        """
        @summary 查看指定账号被设置为哪些可信服务的委派管理员
        
        @description This topic provides an example on how to call the API operation to query the trusted services for which the member `138660628348***` is specified as a delegated administrator account. The response shows that the member is specified as a delegated administrator account of Cloud Firewall.
        
        @param request: ListDelegatedServicesForAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDelegatedServicesForAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDelegatedServicesForAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListDelegatedServicesForAccountResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListDelegatedServicesForAccountResponse(),
                self.execute(params, req, runtime)
            )

    async def list_delegated_services_for_account_with_options_async(
        self,
        request: resource_manager_20200331_models.ListDelegatedServicesForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListDelegatedServicesForAccountResponse:
        """
        @summary 查看指定账号被设置为哪些可信服务的委派管理员
        
        @description This topic provides an example on how to call the API operation to query the trusted services for which the member `138660628348***` is specified as a delegated administrator account. The response shows that the member is specified as a delegated administrator account of Cloud Firewall.
        
        @param request: ListDelegatedServicesForAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDelegatedServicesForAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDelegatedServicesForAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListDelegatedServicesForAccountResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListDelegatedServicesForAccountResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_delegated_services_for_account(
        self,
        request: resource_manager_20200331_models.ListDelegatedServicesForAccountRequest,
    ) -> resource_manager_20200331_models.ListDelegatedServicesForAccountResponse:
        """
        @summary 查看指定账号被设置为哪些可信服务的委派管理员
        
        @description This topic provides an example on how to call the API operation to query the trusted services for which the member `138660628348***` is specified as a delegated administrator account. The response shows that the member is specified as a delegated administrator account of Cloud Firewall.
        
        @param request: ListDelegatedServicesForAccountRequest
        @return: ListDelegatedServicesForAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_delegated_services_for_account_with_options(request, runtime)

    async def list_delegated_services_for_account_async(
        self,
        request: resource_manager_20200331_models.ListDelegatedServicesForAccountRequest,
    ) -> resource_manager_20200331_models.ListDelegatedServicesForAccountResponse:
        """
        @summary 查看指定账号被设置为哪些可信服务的委派管理员
        
        @description This topic provides an example on how to call the API operation to query the trusted services for which the member `138660628348***` is specified as a delegated administrator account. The response shows that the member is specified as a delegated administrator account of Cloud Firewall.
        
        @param request: ListDelegatedServicesForAccountRequest
        @return: ListDelegatedServicesForAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_delegated_services_for_account_with_options_async(request, runtime)

    def list_folders_for_parent_with_options(
        self,
        request: resource_manager_20200331_models.ListFoldersForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListFoldersForParentResponse:
        """
        @description >  You can view the information of only the first-level subfolders of a folder.
        
        @param request: ListFoldersForParentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFoldersForParentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFoldersForParent',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListFoldersForParentResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListFoldersForParentResponse(),
                self.execute(params, req, runtime)
            )

    async def list_folders_for_parent_with_options_async(
        self,
        request: resource_manager_20200331_models.ListFoldersForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListFoldersForParentResponse:
        """
        @description >  You can view the information of only the first-level subfolders of a folder.
        
        @param request: ListFoldersForParentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFoldersForParentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFoldersForParent',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListFoldersForParentResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListFoldersForParentResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_folders_for_parent(
        self,
        request: resource_manager_20200331_models.ListFoldersForParentRequest,
    ) -> resource_manager_20200331_models.ListFoldersForParentResponse:
        """
        @description >  You can view the information of only the first-level subfolders of a folder.
        
        @param request: ListFoldersForParentRequest
        @return: ListFoldersForParentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_folders_for_parent_with_options(request, runtime)

    async def list_folders_for_parent_async(
        self,
        request: resource_manager_20200331_models.ListFoldersForParentRequest,
    ) -> resource_manager_20200331_models.ListFoldersForParentResponse:
        """
        @description >  You can view the information of only the first-level subfolders of a folder.
        
        @param request: ListFoldersForParentRequest
        @return: ListFoldersForParentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_folders_for_parent_with_options_async(request, runtime)

    def list_handshakes_for_account_with_options(
        self,
        request: resource_manager_20200331_models.ListHandshakesForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListHandshakesForAccountResponse:
        """
        @summary Queries the invitations that are associated with an account.
        
        @description This topic provides an example on how to call the API operation to query the invitations that are associated with the management account `172841235500***`. The response shows that two invitations are associated with the management account.
        
        @param request: ListHandshakesForAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHandshakesForAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHandshakesForAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListHandshakesForAccountResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListHandshakesForAccountResponse(),
                self.execute(params, req, runtime)
            )

    async def list_handshakes_for_account_with_options_async(
        self,
        request: resource_manager_20200331_models.ListHandshakesForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListHandshakesForAccountResponse:
        """
        @summary Queries the invitations that are associated with an account.
        
        @description This topic provides an example on how to call the API operation to query the invitations that are associated with the management account `172841235500***`. The response shows that two invitations are associated with the management account.
        
        @param request: ListHandshakesForAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHandshakesForAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHandshakesForAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListHandshakesForAccountResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListHandshakesForAccountResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_handshakes_for_account(
        self,
        request: resource_manager_20200331_models.ListHandshakesForAccountRequest,
    ) -> resource_manager_20200331_models.ListHandshakesForAccountResponse:
        """
        @summary Queries the invitations that are associated with an account.
        
        @description This topic provides an example on how to call the API operation to query the invitations that are associated with the management account `172841235500***`. The response shows that two invitations are associated with the management account.
        
        @param request: ListHandshakesForAccountRequest
        @return: ListHandshakesForAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_handshakes_for_account_with_options(request, runtime)

    async def list_handshakes_for_account_async(
        self,
        request: resource_manager_20200331_models.ListHandshakesForAccountRequest,
    ) -> resource_manager_20200331_models.ListHandshakesForAccountResponse:
        """
        @summary Queries the invitations that are associated with an account.
        
        @description This topic provides an example on how to call the API operation to query the invitations that are associated with the management account `172841235500***`. The response shows that two invitations are associated with the management account.
        
        @param request: ListHandshakesForAccountRequest
        @return: ListHandshakesForAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_handshakes_for_account_with_options_async(request, runtime)

    def list_handshakes_for_resource_directory_with_options(
        self,
        request: resource_manager_20200331_models.ListHandshakesForResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse:
        """
        @summary Queries invitations in a resource directory.
        
        @param request: ListHandshakesForResourceDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHandshakesForResourceDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHandshakesForResourceDirectory',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse(),
                self.execute(params, req, runtime)
            )

    async def list_handshakes_for_resource_directory_with_options_async(
        self,
        request: resource_manager_20200331_models.ListHandshakesForResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse:
        """
        @summary Queries invitations in a resource directory.
        
        @param request: ListHandshakesForResourceDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHandshakesForResourceDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHandshakesForResourceDirectory',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_handshakes_for_resource_directory(
        self,
        request: resource_manager_20200331_models.ListHandshakesForResourceDirectoryRequest,
    ) -> resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse:
        """
        @summary Queries invitations in a resource directory.
        
        @param request: ListHandshakesForResourceDirectoryRequest
        @return: ListHandshakesForResourceDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_handshakes_for_resource_directory_with_options(request, runtime)

    async def list_handshakes_for_resource_directory_async(
        self,
        request: resource_manager_20200331_models.ListHandshakesForResourceDirectoryRequest,
    ) -> resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse:
        """
        @summary Queries invitations in a resource directory.
        
        @param request: ListHandshakesForResourceDirectoryRequest
        @return: ListHandshakesForResourceDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_handshakes_for_resource_directory_with_options_async(request, runtime)

    def list_policies_with_options(
        self,
        request: resource_manager_20200331_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPoliciesResponse:
        """
        @summary Queries policies.
        
        @param request: ListPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicies',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListPoliciesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListPoliciesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_policies_with_options_async(
        self,
        request: resource_manager_20200331_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPoliciesResponse:
        """
        @summary Queries policies.
        
        @param request: ListPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicies',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListPoliciesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListPoliciesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_policies(
        self,
        request: resource_manager_20200331_models.ListPoliciesRequest,
    ) -> resource_manager_20200331_models.ListPoliciesResponse:
        """
        @summary Queries policies.
        
        @param request: ListPoliciesRequest
        @return: ListPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_policies_with_options(request, runtime)

    async def list_policies_async(
        self,
        request: resource_manager_20200331_models.ListPoliciesRequest,
    ) -> resource_manager_20200331_models.ListPoliciesResponse:
        """
        @summary Queries policies.
        
        @param request: ListPoliciesRequest
        @return: ListPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_policies_with_options_async(request, runtime)

    def list_policy_attachments_with_options(
        self,
        request: resource_manager_20200331_models.ListPolicyAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPolicyAttachmentsResponse:
        """
        @summary Queries policy attachment records.
        
        @description You can view the following information:
        Policy attachment records under an Alibaba Cloud account or a resource group
        Policies attached to RAM users, RAM user groups, or RAM roles
        RAM users, RAM user groups, or RAM roles to which policies are attached under an Alibaba Cloud account or a resource group
        
        @param request: ListPolicyAttachmentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPolicyAttachmentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicyAttachments',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListPolicyAttachmentsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListPolicyAttachmentsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_policy_attachments_with_options_async(
        self,
        request: resource_manager_20200331_models.ListPolicyAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPolicyAttachmentsResponse:
        """
        @summary Queries policy attachment records.
        
        @description You can view the following information:
        Policy attachment records under an Alibaba Cloud account or a resource group
        Policies attached to RAM users, RAM user groups, or RAM roles
        RAM users, RAM user groups, or RAM roles to which policies are attached under an Alibaba Cloud account or a resource group
        
        @param request: ListPolicyAttachmentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPolicyAttachmentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicyAttachments',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListPolicyAttachmentsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListPolicyAttachmentsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_policy_attachments(
        self,
        request: resource_manager_20200331_models.ListPolicyAttachmentsRequest,
    ) -> resource_manager_20200331_models.ListPolicyAttachmentsResponse:
        """
        @summary Queries policy attachment records.
        
        @description You can view the following information:
        Policy attachment records under an Alibaba Cloud account or a resource group
        Policies attached to RAM users, RAM user groups, or RAM roles
        RAM users, RAM user groups, or RAM roles to which policies are attached under an Alibaba Cloud account or a resource group
        
        @param request: ListPolicyAttachmentsRequest
        @return: ListPolicyAttachmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_policy_attachments_with_options(request, runtime)

    async def list_policy_attachments_async(
        self,
        request: resource_manager_20200331_models.ListPolicyAttachmentsRequest,
    ) -> resource_manager_20200331_models.ListPolicyAttachmentsResponse:
        """
        @summary Queries policy attachment records.
        
        @description You can view the following information:
        Policy attachment records under an Alibaba Cloud account or a resource group
        Policies attached to RAM users, RAM user groups, or RAM roles
        RAM users, RAM user groups, or RAM roles to which policies are attached under an Alibaba Cloud account or a resource group
        
        @param request: ListPolicyAttachmentsRequest
        @return: ListPolicyAttachmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_policy_attachments_with_options_async(request, runtime)

    def list_policy_versions_with_options(
        self,
        request: resource_manager_20200331_models.ListPolicyVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPolicyVersionsResponse:
        """
        @summary 查看权限策略版本列表
        
        @param request: ListPolicyVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPolicyVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicyVersions',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListPolicyVersionsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListPolicyVersionsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_policy_versions_with_options_async(
        self,
        request: resource_manager_20200331_models.ListPolicyVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPolicyVersionsResponse:
        """
        @summary 查看权限策略版本列表
        
        @param request: ListPolicyVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPolicyVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicyVersions',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListPolicyVersionsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListPolicyVersionsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_policy_versions(
        self,
        request: resource_manager_20200331_models.ListPolicyVersionsRequest,
    ) -> resource_manager_20200331_models.ListPolicyVersionsResponse:
        """
        @summary 查看权限策略版本列表
        
        @param request: ListPolicyVersionsRequest
        @return: ListPolicyVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_policy_versions_with_options(request, runtime)

    async def list_policy_versions_async(
        self,
        request: resource_manager_20200331_models.ListPolicyVersionsRequest,
    ) -> resource_manager_20200331_models.ListPolicyVersionsResponse:
        """
        @summary 查看权限策略版本列表
        
        @param request: ListPolicyVersionsRequest
        @return: ListPolicyVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_policy_versions_with_options_async(request, runtime)

    def list_resource_groups_with_options(
        self,
        request: resource_manager_20200331_models.ListResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListResourceGroupsResponse:
        """
        @description You can call this API operation to query all resource groups within the current account. You can also call this API operation to query a specific resource group based on the status, ID, identifier, or display name of the resource group.
        This topic provides an example on how to call the API operation to query the basic information about the resource groups `rg-1hSBH2***` and `rg-9gLOoK****` within the current account.
        
        @param request: ListResourceGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceGroups',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListResourceGroupsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListResourceGroupsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_resource_groups_with_options_async(
        self,
        request: resource_manager_20200331_models.ListResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListResourceGroupsResponse:
        """
        @description You can call this API operation to query all resource groups within the current account. You can also call this API operation to query a specific resource group based on the status, ID, identifier, or display name of the resource group.
        This topic provides an example on how to call the API operation to query the basic information about the resource groups `rg-1hSBH2***` and `rg-9gLOoK****` within the current account.
        
        @param request: ListResourceGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceGroups',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListResourceGroupsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListResourceGroupsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_resource_groups(
        self,
        request: resource_manager_20200331_models.ListResourceGroupsRequest,
    ) -> resource_manager_20200331_models.ListResourceGroupsResponse:
        """
        @description You can call this API operation to query all resource groups within the current account. You can also call this API operation to query a specific resource group based on the status, ID, identifier, or display name of the resource group.
        This topic provides an example on how to call the API operation to query the basic information about the resource groups `rg-1hSBH2***` and `rg-9gLOoK****` within the current account.
        
        @param request: ListResourceGroupsRequest
        @return: ListResourceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_groups_with_options(request, runtime)

    async def list_resource_groups_async(
        self,
        request: resource_manager_20200331_models.ListResourceGroupsRequest,
    ) -> resource_manager_20200331_models.ListResourceGroupsResponse:
        """
        @description You can call this API operation to query all resource groups within the current account. You can also call this API operation to query a specific resource group based on the status, ID, identifier, or display name of the resource group.
        This topic provides an example on how to call the API operation to query the basic information about the resource groups `rg-1hSBH2***` and `rg-9gLOoK****` within the current account.
        
        @param request: ListResourceGroupsRequest
        @return: ListResourceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_groups_with_options_async(request, runtime)

    def list_resources_with_options(
        self,
        request: resource_manager_20200331_models.ListResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListResourcesResponse:
        """
        @summary Queries resources that can be accessed by the current account in resource groups.
        
        @description >  You can use a RAM role that is not associated with a session policy to call this API operation.
        This topic provides an example on how to call the API operation to query resources that can be accessed by the current account in resource groups. The response shows that the current account can access only the Elastic Compute Service (ECS) instance `i-23v38***` in the resource group `rg-uPJpP****`.
        
        @param request: ListResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_resources_with_options_async(
        self,
        request: resource_manager_20200331_models.ListResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListResourcesResponse:
        """
        @summary Queries resources that can be accessed by the current account in resource groups.
        
        @description >  You can use a RAM role that is not associated with a session policy to call this API operation.
        This topic provides an example on how to call the API operation to query resources that can be accessed by the current account in resource groups. The response shows that the current account can access only the Elastic Compute Service (ECS) instance `i-23v38***` in the resource group `rg-uPJpP****`.
        
        @param request: ListResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_resources(
        self,
        request: resource_manager_20200331_models.ListResourcesRequest,
    ) -> resource_manager_20200331_models.ListResourcesResponse:
        """
        @summary Queries resources that can be accessed by the current account in resource groups.
        
        @description >  You can use a RAM role that is not associated with a session policy to call this API operation.
        This topic provides an example on how to call the API operation to query resources that can be accessed by the current account in resource groups. The response shows that the current account can access only the Elastic Compute Service (ECS) instance `i-23v38***` in the resource group `rg-uPJpP****`.
        
        @param request: ListResourcesRequest
        @return: ListResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resources_with_options(request, runtime)

    async def list_resources_async(
        self,
        request: resource_manager_20200331_models.ListResourcesRequest,
    ) -> resource_manager_20200331_models.ListResourcesResponse:
        """
        @summary Queries resources that can be accessed by the current account in resource groups.
        
        @description >  You can use a RAM role that is not associated with a session policy to call this API operation.
        This topic provides an example on how to call the API operation to query resources that can be accessed by the current account in resource groups. The response shows that the current account can access only the Elastic Compute Service (ECS) instance `i-23v38***` in the resource group `rg-uPJpP****`.
        
        @param request: ListResourcesRequest
        @return: ListResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resources_with_options_async(request, runtime)

    def list_roles_with_options(
        self,
        request: resource_manager_20200331_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListRolesResponse:
        """
        @summary Queries RAM roles.
        
        @param request: ListRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRolesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListRolesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListRolesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_roles_with_options_async(
        self,
        request: resource_manager_20200331_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListRolesResponse:
        """
        @summary Queries RAM roles.
        
        @param request: ListRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRolesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListRolesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListRolesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_roles(
        self,
        request: resource_manager_20200331_models.ListRolesRequest,
    ) -> resource_manager_20200331_models.ListRolesResponse:
        """
        @summary Queries RAM roles.
        
        @param request: ListRolesRequest
        @return: ListRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    async def list_roles_async(
        self,
        request: resource_manager_20200331_models.ListRolesRequest,
    ) -> resource_manager_20200331_models.ListRolesResponse:
        """
        @summary Queries RAM roles.
        
        @param request: ListRolesRequest
        @return: ListRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_roles_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: resource_manager_20200331_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTagKeysResponse:
        """
        @summary 列出所有的Tag key
        
        @description This topic provides an example on how to call the API operation to query tag keys. The response shows that the custom tag key team exists.
        
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_filter):
            query['KeyFilter'] = request.key_filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListTagKeysResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListTagKeysResponse(),
                self.execute(params, req, runtime)
            )

    async def list_tag_keys_with_options_async(
        self,
        request: resource_manager_20200331_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTagKeysResponse:
        """
        @summary 列出所有的Tag key
        
        @description This topic provides an example on how to call the API operation to query tag keys. The response shows that the custom tag key team exists.
        
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_filter):
            query['KeyFilter'] = request.key_filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListTagKeysResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListTagKeysResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_tag_keys(
        self,
        request: resource_manager_20200331_models.ListTagKeysRequest,
    ) -> resource_manager_20200331_models.ListTagKeysResponse:
        """
        @summary 列出所有的Tag key
        
        @description This topic provides an example on how to call the API operation to query tag keys. The response shows that the custom tag key team exists.
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: resource_manager_20200331_models.ListTagKeysRequest,
    ) -> resource_manager_20200331_models.ListTagKeysResponse:
        """
        @summary 列出所有的Tag key
        
        @description This topic provides an example on how to call the API operation to query tag keys. The response shows that the custom tag key team exists.
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: resource_manager_20200331_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to resource groups or the members in a resource directory.
        
        @description This topic provides an example on how to call the API operation to query the tags that are added to the resource group with an ID of `rg-aekz6bre2uq***`. The response shows that only the `k1:v1` tag is added to the resource group.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListTagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListTagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_tag_resources_with_options_async(
        self,
        request: resource_manager_20200331_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to resource groups or the members in a resource directory.
        
        @description This topic provides an example on how to call the API operation to query the tags that are added to the resource group with an ID of `rg-aekz6bre2uq***`. The response shows that only the `k1:v1` tag is added to the resource group.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListTagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListTagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_tag_resources(
        self,
        request: resource_manager_20200331_models.ListTagResourcesRequest,
    ) -> resource_manager_20200331_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to resource groups or the members in a resource directory.
        
        @description This topic provides an example on how to call the API operation to query the tags that are added to the resource group with an ID of `rg-aekz6bre2uq***`. The response shows that only the `k1:v1` tag is added to the resource group.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: resource_manager_20200331_models.ListTagResourcesRequest,
    ) -> resource_manager_20200331_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to resource groups or the members in a resource directory.
        
        @description This topic provides an example on how to call the API operation to query the tags that are added to the resource group with an ID of `rg-aekz6bre2uq***`. The response shows that only the `k1:v1` tag is added to the resource group.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: resource_manager_20200331_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTagValuesResponse:
        """
        @summary 列出所有的Tag values
        
        @description This topic provides an example on how to call the API operation to query the tag values of the tag key k1. The response shows that the tag value of the tag key k1 is v1.
        
        @param request: ListTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.value_filter):
            query['ValueFilter'] = request.value_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListTagValuesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListTagValuesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_tag_values_with_options_async(
        self,
        request: resource_manager_20200331_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTagValuesResponse:
        """
        @summary 列出所有的Tag values
        
        @description This topic provides an example on how to call the API operation to query the tag values of the tag key k1. The response shows that the tag value of the tag key k1 is v1.
        
        @param request: ListTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.value_filter):
            query['ValueFilter'] = request.value_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListTagValuesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListTagValuesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_tag_values(
        self,
        request: resource_manager_20200331_models.ListTagValuesRequest,
    ) -> resource_manager_20200331_models.ListTagValuesResponse:
        """
        @summary 列出所有的Tag values
        
        @description This topic provides an example on how to call the API operation to query the tag values of the tag key k1. The response shows that the tag value of the tag key k1 is v1.
        
        @param request: ListTagValuesRequest
        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: resource_manager_20200331_models.ListTagValuesRequest,
    ) -> resource_manager_20200331_models.ListTagValuesResponse:
        """
        @summary 列出所有的Tag values
        
        @description This topic provides an example on how to call the API operation to query the tag values of the tag key k1. The response shows that the tag value of the tag key k1 is v1.
        
        @param request: ListTagValuesRequest
        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def list_target_attachments_for_control_policy_with_options(
        self,
        request: resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyResponse:
        """
        @summary Queries the objects to which a specific control policy is attached.
        
        @description In this example, the folders or member accounts to which the control policy `cp-jExXAqIYkwHN***` is attached are queried. The returned result shows that the control policy is attached to the folder `fd-ZDNPiT****`.
        
        @param request: ListTargetAttachmentsForControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTargetAttachmentsForControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTargetAttachmentsForControlPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def list_target_attachments_for_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyResponse:
        """
        @summary Queries the objects to which a specific control policy is attached.
        
        @description In this example, the folders or member accounts to which the control policy `cp-jExXAqIYkwHN***` is attached are queried. The returned result shows that the control policy is attached to the folder `fd-ZDNPiT****`.
        
        @param request: ListTargetAttachmentsForControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTargetAttachmentsForControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTargetAttachmentsForControlPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_target_attachments_for_control_policy(
        self,
        request: resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyRequest,
    ) -> resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyResponse:
        """
        @summary Queries the objects to which a specific control policy is attached.
        
        @description In this example, the folders or member accounts to which the control policy `cp-jExXAqIYkwHN***` is attached are queried. The returned result shows that the control policy is attached to the folder `fd-ZDNPiT****`.
        
        @param request: ListTargetAttachmentsForControlPolicyRequest
        @return: ListTargetAttachmentsForControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_target_attachments_for_control_policy_with_options(request, runtime)

    async def list_target_attachments_for_control_policy_async(
        self,
        request: resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyRequest,
    ) -> resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyResponse:
        """
        @summary Queries the objects to which a specific control policy is attached.
        
        @description In this example, the folders or member accounts to which the control policy `cp-jExXAqIYkwHN***` is attached are queried. The returned result shows that the control policy is attached to the folder `fd-ZDNPiT****`.
        
        @param request: ListTargetAttachmentsForControlPolicyRequest
        @return: ListTargetAttachmentsForControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_target_attachments_for_control_policy_with_options_async(request, runtime)

    def list_trusted_service_status_with_options(
        self,
        request: resource_manager_20200331_models.ListTrustedServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTrustedServiceStatusResponse:
        """
        @description >  Only an enterprise management account or delegated administrator account can be used to call this operation.
        In this example, the trusted services that are enabled within an enterprise management account are queried. The returned result shows that the trusted services Cloud Config and ActionTrail are enabled within the enterprise management account.
        
        @param request: ListTrustedServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTrustedServiceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.admin_account_id):
            query['AdminAccountId'] = request.admin_account_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrustedServiceStatus',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListTrustedServiceStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListTrustedServiceStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def list_trusted_service_status_with_options_async(
        self,
        request: resource_manager_20200331_models.ListTrustedServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTrustedServiceStatusResponse:
        """
        @description >  Only an enterprise management account or delegated administrator account can be used to call this operation.
        In this example, the trusted services that are enabled within an enterprise management account are queried. The returned result shows that the trusted services Cloud Config and ActionTrail are enabled within the enterprise management account.
        
        @param request: ListTrustedServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTrustedServiceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.admin_account_id):
            query['AdminAccountId'] = request.admin_account_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrustedServiceStatus',
            version='2020-03-31',
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
                resource_manager_20200331_models.ListTrustedServiceStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ListTrustedServiceStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_trusted_service_status(
        self,
        request: resource_manager_20200331_models.ListTrustedServiceStatusRequest,
    ) -> resource_manager_20200331_models.ListTrustedServiceStatusResponse:
        """
        @description >  Only an enterprise management account or delegated administrator account can be used to call this operation.
        In this example, the trusted services that are enabled within an enterprise management account are queried. The returned result shows that the trusted services Cloud Config and ActionTrail are enabled within the enterprise management account.
        
        @param request: ListTrustedServiceStatusRequest
        @return: ListTrustedServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_trusted_service_status_with_options(request, runtime)

    async def list_trusted_service_status_async(
        self,
        request: resource_manager_20200331_models.ListTrustedServiceStatusRequest,
    ) -> resource_manager_20200331_models.ListTrustedServiceStatusResponse:
        """
        @description >  Only an enterprise management account or delegated administrator account can be used to call this operation.
        In this example, the trusted services that are enabled within an enterprise management account are queried. The returned result shows that the trusted services Cloud Config and ActionTrail are enabled within the enterprise management account.
        
        @param request: ListTrustedServiceStatusRequest
        @return: ListTrustedServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_trusted_service_status_with_options_async(request, runtime)

    def move_account_with_options(
        self,
        request: resource_manager_20200331_models.MoveAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.MoveAccountResponse:
        """
        @summary 移动账号
        
        @param request: MoveAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.destination_folder_id):
            query['DestinationFolderId'] = request.destination_folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.MoveAccountResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.MoveAccountResponse(),
                self.execute(params, req, runtime)
            )

    async def move_account_with_options_async(
        self,
        request: resource_manager_20200331_models.MoveAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.MoveAccountResponse:
        """
        @summary 移动账号
        
        @param request: MoveAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.destination_folder_id):
            query['DestinationFolderId'] = request.destination_folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.MoveAccountResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.MoveAccountResponse(),
                await self.execute_async(params, req, runtime)
            )

    def move_account(
        self,
        request: resource_manager_20200331_models.MoveAccountRequest,
    ) -> resource_manager_20200331_models.MoveAccountResponse:
        """
        @summary 移动账号
        
        @param request: MoveAccountRequest
        @return: MoveAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_account_with_options(request, runtime)

    async def move_account_async(
        self,
        request: resource_manager_20200331_models.MoveAccountRequest,
    ) -> resource_manager_20200331_models.MoveAccountResponse:
        """
        @summary 移动账号
        
        @param request: MoveAccountRequest
        @return: MoveAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_account_with_options_async(request, runtime)

    def move_resources_with_options(
        self,
        request: resource_manager_20200331_models.MoveResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.MoveResourcesResponse:
        """
        @summary Moves resources from one resource group to another. You can move multiple resources that reside in different regions, are used by different Alibaba Cloud services, or belong to different resource groups.
        
        @description For more information about Alibaba Cloud services whose resources can be moved between resource groups, see the *Supported by the API** column in [Alibaba Cloud services that support resource groups](https://help.aliyun.com/document_detail/94479.html).
        In this example, two virtual private clouds (VPCs) `vpc-bp1sig0mjktx5ewx1***` and `vpc-bp1visxm225pv49dz****` that reside in different regions and belong to different resource groups are moved to the resource group `rg-aekzmeobk5w****`.
        
        @param request: MoveResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResources',
            version='2020-03-31',
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
                resource_manager_20200331_models.MoveResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.MoveResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def move_resources_with_options_async(
        self,
        request: resource_manager_20200331_models.MoveResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.MoveResourcesResponse:
        """
        @summary Moves resources from one resource group to another. You can move multiple resources that reside in different regions, are used by different Alibaba Cloud services, or belong to different resource groups.
        
        @description For more information about Alibaba Cloud services whose resources can be moved between resource groups, see the *Supported by the API** column in [Alibaba Cloud services that support resource groups](https://help.aliyun.com/document_detail/94479.html).
        In this example, two virtual private clouds (VPCs) `vpc-bp1sig0mjktx5ewx1***` and `vpc-bp1visxm225pv49dz****` that reside in different regions and belong to different resource groups are moved to the resource group `rg-aekzmeobk5w****`.
        
        @param request: MoveResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResources',
            version='2020-03-31',
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
                resource_manager_20200331_models.MoveResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.MoveResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def move_resources(
        self,
        request: resource_manager_20200331_models.MoveResourcesRequest,
    ) -> resource_manager_20200331_models.MoveResourcesResponse:
        """
        @summary Moves resources from one resource group to another. You can move multiple resources that reside in different regions, are used by different Alibaba Cloud services, or belong to different resource groups.
        
        @description For more information about Alibaba Cloud services whose resources can be moved between resource groups, see the *Supported by the API** column in [Alibaba Cloud services that support resource groups](https://help.aliyun.com/document_detail/94479.html).
        In this example, two virtual private clouds (VPCs) `vpc-bp1sig0mjktx5ewx1***` and `vpc-bp1visxm225pv49dz****` that reside in different regions and belong to different resource groups are moved to the resource group `rg-aekzmeobk5w****`.
        
        @param request: MoveResourcesRequest
        @return: MoveResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_resources_with_options(request, runtime)

    async def move_resources_async(
        self,
        request: resource_manager_20200331_models.MoveResourcesRequest,
    ) -> resource_manager_20200331_models.MoveResourcesResponse:
        """
        @summary Moves resources from one resource group to another. You can move multiple resources that reside in different regions, are used by different Alibaba Cloud services, or belong to different resource groups.
        
        @description For more information about Alibaba Cloud services whose resources can be moved between resource groups, see the *Supported by the API** column in [Alibaba Cloud services that support resource groups](https://help.aliyun.com/document_detail/94479.html).
        In this example, two virtual private clouds (VPCs) `vpc-bp1sig0mjktx5ewx1***` and `vpc-bp1visxm225pv49dz****` that reside in different regions and belong to different resource groups are moved to the resource group `rg-aekzmeobk5w****`.
        
        @param request: MoveResourcesRequest
        @return: MoveResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_resources_with_options_async(request, runtime)

    def promote_resource_account_with_options(
        self,
        request: resource_manager_20200331_models.PromoteResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.PromoteResourceAccountResponse:
        """
        @summary 升级资源账号
        
        @param request: PromoteResourceAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PromoteResourceAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PromoteResourceAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.PromoteResourceAccountResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.PromoteResourceAccountResponse(),
                self.execute(params, req, runtime)
            )

    async def promote_resource_account_with_options_async(
        self,
        request: resource_manager_20200331_models.PromoteResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.PromoteResourceAccountResponse:
        """
        @summary 升级资源账号
        
        @param request: PromoteResourceAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PromoteResourceAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PromoteResourceAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.PromoteResourceAccountResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.PromoteResourceAccountResponse(),
                await self.execute_async(params, req, runtime)
            )

    def promote_resource_account(
        self,
        request: resource_manager_20200331_models.PromoteResourceAccountRequest,
    ) -> resource_manager_20200331_models.PromoteResourceAccountResponse:
        """
        @summary 升级资源账号
        
        @param request: PromoteResourceAccountRequest
        @return: PromoteResourceAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.promote_resource_account_with_options(request, runtime)

    async def promote_resource_account_async(
        self,
        request: resource_manager_20200331_models.PromoteResourceAccountRequest,
    ) -> resource_manager_20200331_models.PromoteResourceAccountResponse:
        """
        @summary 升级资源账号
        
        @param request: PromoteResourceAccountRequest
        @return: PromoteResourceAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.promote_resource_account_with_options_async(request, runtime)

    def register_delegated_administrator_with_options(
        self,
        request: resource_manager_20200331_models.RegisterDelegatedAdministratorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.RegisterDelegatedAdministratorResponse:
        """
        @description The delegated administrator account can be used to access the information of the resource directory and view the structure and members of the resource directory. The delegated administrator account can also be used to perform service-related management operations in the trusted service on behalf of the management account of the resource directory.
        When you call this operation, you must take note of the following limits:
        Only some trusted services support delegated administrator accounts. For more information, see [Supported trusted services](https://help.aliyun.com/document_detail/208133.html).
        Only the management account of a resource directory or an authorized RAM user or RAM role of the management account can be used to call this operation.
        The number of delegated administrator accounts that are allowed for a trusted service is defined by the trusted service.
        This topic provides an example on how to call the API operation to specify the member `181761095690***` as a delegated administrator account of Cloud Firewall.
        
        @param request: RegisterDelegatedAdministratorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterDelegatedAdministratorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterDelegatedAdministrator',
            version='2020-03-31',
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
                resource_manager_20200331_models.RegisterDelegatedAdministratorResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.RegisterDelegatedAdministratorResponse(),
                self.execute(params, req, runtime)
            )

    async def register_delegated_administrator_with_options_async(
        self,
        request: resource_manager_20200331_models.RegisterDelegatedAdministratorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.RegisterDelegatedAdministratorResponse:
        """
        @description The delegated administrator account can be used to access the information of the resource directory and view the structure and members of the resource directory. The delegated administrator account can also be used to perform service-related management operations in the trusted service on behalf of the management account of the resource directory.
        When you call this operation, you must take note of the following limits:
        Only some trusted services support delegated administrator accounts. For more information, see [Supported trusted services](https://help.aliyun.com/document_detail/208133.html).
        Only the management account of a resource directory or an authorized RAM user or RAM role of the management account can be used to call this operation.
        The number of delegated administrator accounts that are allowed for a trusted service is defined by the trusted service.
        This topic provides an example on how to call the API operation to specify the member `181761095690***` as a delegated administrator account of Cloud Firewall.
        
        @param request: RegisterDelegatedAdministratorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterDelegatedAdministratorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterDelegatedAdministrator',
            version='2020-03-31',
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
                resource_manager_20200331_models.RegisterDelegatedAdministratorResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.RegisterDelegatedAdministratorResponse(),
                await self.execute_async(params, req, runtime)
            )

    def register_delegated_administrator(
        self,
        request: resource_manager_20200331_models.RegisterDelegatedAdministratorRequest,
    ) -> resource_manager_20200331_models.RegisterDelegatedAdministratorResponse:
        """
        @description The delegated administrator account can be used to access the information of the resource directory and view the structure and members of the resource directory. The delegated administrator account can also be used to perform service-related management operations in the trusted service on behalf of the management account of the resource directory.
        When you call this operation, you must take note of the following limits:
        Only some trusted services support delegated administrator accounts. For more information, see [Supported trusted services](https://help.aliyun.com/document_detail/208133.html).
        Only the management account of a resource directory or an authorized RAM user or RAM role of the management account can be used to call this operation.
        The number of delegated administrator accounts that are allowed for a trusted service is defined by the trusted service.
        This topic provides an example on how to call the API operation to specify the member `181761095690***` as a delegated administrator account of Cloud Firewall.
        
        @param request: RegisterDelegatedAdministratorRequest
        @return: RegisterDelegatedAdministratorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.register_delegated_administrator_with_options(request, runtime)

    async def register_delegated_administrator_async(
        self,
        request: resource_manager_20200331_models.RegisterDelegatedAdministratorRequest,
    ) -> resource_manager_20200331_models.RegisterDelegatedAdministratorResponse:
        """
        @description The delegated administrator account can be used to access the information of the resource directory and view the structure and members of the resource directory. The delegated administrator account can also be used to perform service-related management operations in the trusted service on behalf of the management account of the resource directory.
        When you call this operation, you must take note of the following limits:
        Only some trusted services support delegated administrator accounts. For more information, see [Supported trusted services](https://help.aliyun.com/document_detail/208133.html).
        Only the management account of a resource directory or an authorized RAM user or RAM role of the management account can be used to call this operation.
        The number of delegated administrator accounts that are allowed for a trusted service is defined by the trusted service.
        This topic provides an example on how to call the API operation to specify the member `181761095690***` as a delegated administrator account of Cloud Firewall.
        
        @param request: RegisterDelegatedAdministratorRequest
        @return: RegisterDelegatedAdministratorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.register_delegated_administrator_with_options_async(request, runtime)

    def remove_cloud_account_with_options(
        self,
        request: resource_manager_20200331_models.RemoveCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.RemoveCloudAccountResponse:
        """
        @description This topic provides an example on how to call the API operation to remove the member `177242285274***` from a resource directory.
        
        @param request: RemoveCloudAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveCloudAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveCloudAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.RemoveCloudAccountResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.RemoveCloudAccountResponse(),
                self.execute(params, req, runtime)
            )

    async def remove_cloud_account_with_options_async(
        self,
        request: resource_manager_20200331_models.RemoveCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.RemoveCloudAccountResponse:
        """
        @description This topic provides an example on how to call the API operation to remove the member `177242285274***` from a resource directory.
        
        @param request: RemoveCloudAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveCloudAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveCloudAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.RemoveCloudAccountResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.RemoveCloudAccountResponse(),
                await self.execute_async(params, req, runtime)
            )

    def remove_cloud_account(
        self,
        request: resource_manager_20200331_models.RemoveCloudAccountRequest,
    ) -> resource_manager_20200331_models.RemoveCloudAccountResponse:
        """
        @description This topic provides an example on how to call the API operation to remove the member `177242285274***` from a resource directory.
        
        @param request: RemoveCloudAccountRequest
        @return: RemoveCloudAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_cloud_account_with_options(request, runtime)

    async def remove_cloud_account_async(
        self,
        request: resource_manager_20200331_models.RemoveCloudAccountRequest,
    ) -> resource_manager_20200331_models.RemoveCloudAccountResponse:
        """
        @description This topic provides an example on how to call the API operation to remove the member `177242285274***` from a resource directory.
        
        @param request: RemoveCloudAccountRequest
        @return: RemoveCloudAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_cloud_account_with_options_async(request, runtime)

    def resend_create_cloud_account_email_with_options(
        self,
        request: resource_manager_20200331_models.ResendCreateCloudAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse:
        """
        @summary 重新发送创建云账号的邮箱验证
        
        @param request: ResendCreateCloudAccountEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResendCreateCloudAccountEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResendCreateCloudAccountEmail',
            version='2020-03-31',
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
                resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse(),
                self.execute(params, req, runtime)
            )

    async def resend_create_cloud_account_email_with_options_async(
        self,
        request: resource_manager_20200331_models.ResendCreateCloudAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse:
        """
        @summary 重新发送创建云账号的邮箱验证
        
        @param request: ResendCreateCloudAccountEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResendCreateCloudAccountEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResendCreateCloudAccountEmail',
            version='2020-03-31',
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
                resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse(),
                await self.execute_async(params, req, runtime)
            )

    def resend_create_cloud_account_email(
        self,
        request: resource_manager_20200331_models.ResendCreateCloudAccountEmailRequest,
    ) -> resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse:
        """
        @summary 重新发送创建云账号的邮箱验证
        
        @param request: ResendCreateCloudAccountEmailRequest
        @return: ResendCreateCloudAccountEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resend_create_cloud_account_email_with_options(request, runtime)

    async def resend_create_cloud_account_email_async(
        self,
        request: resource_manager_20200331_models.ResendCreateCloudAccountEmailRequest,
    ) -> resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse:
        """
        @summary 重新发送创建云账号的邮箱验证
        
        @param request: ResendCreateCloudAccountEmailRequest
        @return: ResendCreateCloudAccountEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resend_create_cloud_account_email_with_options_async(request, runtime)

    def resend_promote_resource_account_email_with_options(
        self,
        request: resource_manager_20200331_models.ResendPromoteResourceAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse:
        """
        @summary 重新发送升级资源账号的邮箱验证
        
        @param request: ResendPromoteResourceAccountEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResendPromoteResourceAccountEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResendPromoteResourceAccountEmail',
            version='2020-03-31',
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
                resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse(),
                self.execute(params, req, runtime)
            )

    async def resend_promote_resource_account_email_with_options_async(
        self,
        request: resource_manager_20200331_models.ResendPromoteResourceAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse:
        """
        @summary 重新发送升级资源账号的邮箱验证
        
        @param request: ResendPromoteResourceAccountEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResendPromoteResourceAccountEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResendPromoteResourceAccountEmail',
            version='2020-03-31',
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
                resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse(),
                await self.execute_async(params, req, runtime)
            )

    def resend_promote_resource_account_email(
        self,
        request: resource_manager_20200331_models.ResendPromoteResourceAccountEmailRequest,
    ) -> resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse:
        """
        @summary 重新发送升级资源账号的邮箱验证
        
        @param request: ResendPromoteResourceAccountEmailRequest
        @return: ResendPromoteResourceAccountEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resend_promote_resource_account_email_with_options(request, runtime)

    async def resend_promote_resource_account_email_async(
        self,
        request: resource_manager_20200331_models.ResendPromoteResourceAccountEmailRequest,
    ) -> resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse:
        """
        @summary 重新发送升级资源账号的邮箱验证
        
        @param request: ResendPromoteResourceAccountEmailRequest
        @return: ResendPromoteResourceAccountEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resend_promote_resource_account_email_with_options_async(request, runtime)

    def retry_change_account_email_with_options(
        self,
        request: resource_manager_20200331_models.RetryChangeAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.RetryChangeAccountEmailResponse:
        """
        @summary 重新发送确认邮件
        
        @param request: RetryChangeAccountEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetryChangeAccountEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryChangeAccountEmail',
            version='2020-03-31',
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
                resource_manager_20200331_models.RetryChangeAccountEmailResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.RetryChangeAccountEmailResponse(),
                self.execute(params, req, runtime)
            )

    async def retry_change_account_email_with_options_async(
        self,
        request: resource_manager_20200331_models.RetryChangeAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.RetryChangeAccountEmailResponse:
        """
        @summary 重新发送确认邮件
        
        @param request: RetryChangeAccountEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetryChangeAccountEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryChangeAccountEmail',
            version='2020-03-31',
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
                resource_manager_20200331_models.RetryChangeAccountEmailResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.RetryChangeAccountEmailResponse(),
                await self.execute_async(params, req, runtime)
            )

    def retry_change_account_email(
        self,
        request: resource_manager_20200331_models.RetryChangeAccountEmailRequest,
    ) -> resource_manager_20200331_models.RetryChangeAccountEmailResponse:
        """
        @summary 重新发送确认邮件
        
        @param request: RetryChangeAccountEmailRequest
        @return: RetryChangeAccountEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.retry_change_account_email_with_options(request, runtime)

    async def retry_change_account_email_async(
        self,
        request: resource_manager_20200331_models.RetryChangeAccountEmailRequest,
    ) -> resource_manager_20200331_models.RetryChangeAccountEmailResponse:
        """
        @summary 重新发送确认邮件
        
        @param request: RetryChangeAccountEmailRequest
        @return: RetryChangeAccountEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.retry_change_account_email_with_options_async(request, runtime)

    def send_verification_code_for_bind_secure_mobile_phone_with_options(
        self,
        request: resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneResponse:
        """
        @summary 发送绑定安全手机验证码
        
        @description To ensure that the system can record the operators of management operations, you must use a RAM user or RAM role to which the AliyunResourceDirectoryFullAccess policy is attached within the management account of your resource directory to call this operation.
        In this example, a verification code is sent to the mobile phone number that you want to bind to the resource account `138660628348***`.
        
        @param request: SendVerificationCodeForBindSecureMobilePhoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendVerificationCodeForBindSecureMobilePhoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerificationCodeForBindSecureMobilePhone',
            version='2020-03-31',
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
                resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneResponse(),
                self.execute(params, req, runtime)
            )

    async def send_verification_code_for_bind_secure_mobile_phone_with_options_async(
        self,
        request: resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneResponse:
        """
        @summary 发送绑定安全手机验证码
        
        @description To ensure that the system can record the operators of management operations, you must use a RAM user or RAM role to which the AliyunResourceDirectoryFullAccess policy is attached within the management account of your resource directory to call this operation.
        In this example, a verification code is sent to the mobile phone number that you want to bind to the resource account `138660628348***`.
        
        @param request: SendVerificationCodeForBindSecureMobilePhoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendVerificationCodeForBindSecureMobilePhoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerificationCodeForBindSecureMobilePhone',
            version='2020-03-31',
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
                resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneResponse(),
                await self.execute_async(params, req, runtime)
            )

    def send_verification_code_for_bind_secure_mobile_phone(
        self,
        request: resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneRequest,
    ) -> resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneResponse:
        """
        @summary 发送绑定安全手机验证码
        
        @description To ensure that the system can record the operators of management operations, you must use a RAM user or RAM role to which the AliyunResourceDirectoryFullAccess policy is attached within the management account of your resource directory to call this operation.
        In this example, a verification code is sent to the mobile phone number that you want to bind to the resource account `138660628348***`.
        
        @param request: SendVerificationCodeForBindSecureMobilePhoneRequest
        @return: SendVerificationCodeForBindSecureMobilePhoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_verification_code_for_bind_secure_mobile_phone_with_options(request, runtime)

    async def send_verification_code_for_bind_secure_mobile_phone_async(
        self,
        request: resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneRequest,
    ) -> resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneResponse:
        """
        @summary 发送绑定安全手机验证码
        
        @description To ensure that the system can record the operators of management operations, you must use a RAM user or RAM role to which the AliyunResourceDirectoryFullAccess policy is attached within the management account of your resource directory to call this operation.
        In this example, a verification code is sent to the mobile phone number that you want to bind to the resource account `138660628348***`.
        
        @param request: SendVerificationCodeForBindSecureMobilePhoneRequest
        @return: SendVerificationCodeForBindSecureMobilePhoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_verification_code_for_bind_secure_mobile_phone_with_options_async(request, runtime)

    def send_verification_code_for_enable_rdwith_options(
        self,
        request: resource_manager_20200331_models.SendVerificationCodeForEnableRDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.SendVerificationCodeForEnableRDResponse:
        """
        @summary 发送开启资源目录短信
        
        @description Each Alibaba Cloud account can be used to send a maximum of 100 verification codes per day.
        
        @param request: SendVerificationCodeForEnableRDRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendVerificationCodeForEnableRDResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerificationCodeForEnableRD',
            version='2020-03-31',
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
                resource_manager_20200331_models.SendVerificationCodeForEnableRDResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.SendVerificationCodeForEnableRDResponse(),
                self.execute(params, req, runtime)
            )

    async def send_verification_code_for_enable_rdwith_options_async(
        self,
        request: resource_manager_20200331_models.SendVerificationCodeForEnableRDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.SendVerificationCodeForEnableRDResponse:
        """
        @summary 发送开启资源目录短信
        
        @description Each Alibaba Cloud account can be used to send a maximum of 100 verification codes per day.
        
        @param request: SendVerificationCodeForEnableRDRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendVerificationCodeForEnableRDResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerificationCodeForEnableRD',
            version='2020-03-31',
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
                resource_manager_20200331_models.SendVerificationCodeForEnableRDResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.SendVerificationCodeForEnableRDResponse(),
                await self.execute_async(params, req, runtime)
            )

    def send_verification_code_for_enable_rd(
        self,
        request: resource_manager_20200331_models.SendVerificationCodeForEnableRDRequest,
    ) -> resource_manager_20200331_models.SendVerificationCodeForEnableRDResponse:
        """
        @summary 发送开启资源目录短信
        
        @description Each Alibaba Cloud account can be used to send a maximum of 100 verification codes per day.
        
        @param request: SendVerificationCodeForEnableRDRequest
        @return: SendVerificationCodeForEnableRDResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_verification_code_for_enable_rdwith_options(request, runtime)

    async def send_verification_code_for_enable_rd_async(
        self,
        request: resource_manager_20200331_models.SendVerificationCodeForEnableRDRequest,
    ) -> resource_manager_20200331_models.SendVerificationCodeForEnableRDResponse:
        """
        @summary 发送开启资源目录短信
        
        @description Each Alibaba Cloud account can be used to send a maximum of 100 verification codes per day.
        
        @param request: SendVerificationCodeForEnableRDRequest
        @return: SendVerificationCodeForEnableRDResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_verification_code_for_enable_rdwith_options_async(request, runtime)

    def set_default_policy_version_with_options(
        self,
        request: resource_manager_20200331_models.SetDefaultPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.SetDefaultPolicyVersionResponse:
        """
        @summary 设置权限策略默认版本
        
        @param request: SetDefaultPolicyVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDefaultPolicyVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultPolicyVersion',
            version='2020-03-31',
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
                resource_manager_20200331_models.SetDefaultPolicyVersionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.SetDefaultPolicyVersionResponse(),
                self.execute(params, req, runtime)
            )

    async def set_default_policy_version_with_options_async(
        self,
        request: resource_manager_20200331_models.SetDefaultPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.SetDefaultPolicyVersionResponse:
        """
        @summary 设置权限策略默认版本
        
        @param request: SetDefaultPolicyVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDefaultPolicyVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultPolicyVersion',
            version='2020-03-31',
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
                resource_manager_20200331_models.SetDefaultPolicyVersionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.SetDefaultPolicyVersionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def set_default_policy_version(
        self,
        request: resource_manager_20200331_models.SetDefaultPolicyVersionRequest,
    ) -> resource_manager_20200331_models.SetDefaultPolicyVersionResponse:
        """
        @summary 设置权限策略默认版本
        
        @param request: SetDefaultPolicyVersionRequest
        @return: SetDefaultPolicyVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_default_policy_version_with_options(request, runtime)

    async def set_default_policy_version_async(
        self,
        request: resource_manager_20200331_models.SetDefaultPolicyVersionRequest,
    ) -> resource_manager_20200331_models.SetDefaultPolicyVersionResponse:
        """
        @summary 设置权限策略默认版本
        
        @param request: SetDefaultPolicyVersionRequest
        @return: SetDefaultPolicyVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_default_policy_version_with_options_async(request, runtime)

    def set_member_deletion_permission_with_options(
        self,
        request: resource_manager_20200331_models.SetMemberDeletionPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.SetMemberDeletionPermissionResponse:
        """
        @summary 开启或关闭成员删除许可
        
        @description Members of the resource account type can be deleted only after the member deletion feature is enabled.
        
        @param request: SetMemberDeletionPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetMemberDeletionPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetMemberDeletionPermission',
            version='2020-03-31',
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
                resource_manager_20200331_models.SetMemberDeletionPermissionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.SetMemberDeletionPermissionResponse(),
                self.execute(params, req, runtime)
            )

    async def set_member_deletion_permission_with_options_async(
        self,
        request: resource_manager_20200331_models.SetMemberDeletionPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.SetMemberDeletionPermissionResponse:
        """
        @summary 开启或关闭成员删除许可
        
        @description Members of the resource account type can be deleted only after the member deletion feature is enabled.
        
        @param request: SetMemberDeletionPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetMemberDeletionPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetMemberDeletionPermission',
            version='2020-03-31',
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
                resource_manager_20200331_models.SetMemberDeletionPermissionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.SetMemberDeletionPermissionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def set_member_deletion_permission(
        self,
        request: resource_manager_20200331_models.SetMemberDeletionPermissionRequest,
    ) -> resource_manager_20200331_models.SetMemberDeletionPermissionResponse:
        """
        @summary 开启或关闭成员删除许可
        
        @description Members of the resource account type can be deleted only after the member deletion feature is enabled.
        
        @param request: SetMemberDeletionPermissionRequest
        @return: SetMemberDeletionPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_member_deletion_permission_with_options(request, runtime)

    async def set_member_deletion_permission_async(
        self,
        request: resource_manager_20200331_models.SetMemberDeletionPermissionRequest,
    ) -> resource_manager_20200331_models.SetMemberDeletionPermissionResponse:
        """
        @summary 开启或关闭成员删除许可
        
        @description Members of the resource account type can be deleted only after the member deletion feature is enabled.
        
        @param request: SetMemberDeletionPermissionRequest
        @return: SetMemberDeletionPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_member_deletion_permission_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: resource_manager_20200331_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.TagResourcesResponse:
        """
        @summary Adds tags to resource groups or the members in a resource directory.
        
        @description This topic provides an example on how to call the API operation to add the tag `k1:v1` to the resource group with an ID of `rg-aekz6bre2uq***`.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-03-31',
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
                resource_manager_20200331_models.TagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.TagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def tag_resources_with_options_async(
        self,
        request: resource_manager_20200331_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.TagResourcesResponse:
        """
        @summary Adds tags to resource groups or the members in a resource directory.
        
        @description This topic provides an example on how to call the API operation to add the tag `k1:v1` to the resource group with an ID of `rg-aekz6bre2uq***`.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-03-31',
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
                resource_manager_20200331_models.TagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.TagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def tag_resources(
        self,
        request: resource_manager_20200331_models.TagResourcesRequest,
    ) -> resource_manager_20200331_models.TagResourcesResponse:
        """
        @summary Adds tags to resource groups or the members in a resource directory.
        
        @description This topic provides an example on how to call the API operation to add the tag `k1:v1` to the resource group with an ID of `rg-aekz6bre2uq***`.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: resource_manager_20200331_models.TagResourcesRequest,
    ) -> resource_manager_20200331_models.TagResourcesResponse:
        """
        @summary Adds tags to resource groups or the members in a resource directory.
        
        @description This topic provides an example on how to call the API operation to add the tag `k1:v1` to the resource group with an ID of `rg-aekz6bre2uq***`.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: resource_manager_20200331_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UntagResourcesResponse:
        """
        @summary Removes tags from resource groups or the members in a resource directory.
        
        @description This topic provides an example on how to call the API operation to remove the tag whose tag key is `k1` from the resource group whose ID is `rg-aek2dpwyrfr***`.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-03-31',
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
                resource_manager_20200331_models.UntagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.UntagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def untag_resources_with_options_async(
        self,
        request: resource_manager_20200331_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UntagResourcesResponse:
        """
        @summary Removes tags from resource groups or the members in a resource directory.
        
        @description This topic provides an example on how to call the API operation to remove the tag whose tag key is `k1` from the resource group whose ID is `rg-aek2dpwyrfr***`.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-03-31',
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
                resource_manager_20200331_models.UntagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.UntagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def untag_resources(
        self,
        request: resource_manager_20200331_models.UntagResourcesRequest,
    ) -> resource_manager_20200331_models.UntagResourcesResponse:
        """
        @summary Removes tags from resource groups or the members in a resource directory.
        
        @description This topic provides an example on how to call the API operation to remove the tag whose tag key is `k1` from the resource group whose ID is `rg-aek2dpwyrfr***`.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: resource_manager_20200331_models.UntagResourcesRequest,
    ) -> resource_manager_20200331_models.UntagResourcesResponse:
        """
        @summary Removes tags from resource groups or the members in a resource directory.
        
        @description This topic provides an example on how to call the API operation to remove the tag whose tag key is `k1` from the resource group whose ID is `rg-aek2dpwyrfr***`.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_account_with_options(
        self,
        request: resource_manager_20200331_models.UpdateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateAccountResponse:
        """
        @description    To ensure that the system can record the operators of management operations, you must use a RAM user or RAM role to which the AliyunResourceDirectoryFullAccess policy is attached within the management account of your resource directory to call this operation.
        Before you switch the type of a member from resource account to cloud account, make sure that specific conditions are met. For more information about the conditions, see [Switch a resource account to a cloud account](https://help.aliyun.com/document_detail/111233.html).
        Before you switch the type of a member from cloud account to resource account, make sure that specific conditions are met. For more information about the conditions, see [Switch a cloud account to a resource account](https://help.aliyun.com/document_detail/209980.html).
        This example provides an example on how to call the API operation to change the display name of the member `12323344***` to `admin`.
        
        @param request: UpdateAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.new_account_type):
            query['NewAccountType'] = request.new_account_type
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.UpdateAccountResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.UpdateAccountResponse(),
                self.execute(params, req, runtime)
            )

    async def update_account_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateAccountResponse:
        """
        @description    To ensure that the system can record the operators of management operations, you must use a RAM user or RAM role to which the AliyunResourceDirectoryFullAccess policy is attached within the management account of your resource directory to call this operation.
        Before you switch the type of a member from resource account to cloud account, make sure that specific conditions are met. For more information about the conditions, see [Switch a resource account to a cloud account](https://help.aliyun.com/document_detail/111233.html).
        Before you switch the type of a member from cloud account to resource account, make sure that specific conditions are met. For more information about the conditions, see [Switch a cloud account to a resource account](https://help.aliyun.com/document_detail/209980.html).
        This example provides an example on how to call the API operation to change the display name of the member `12323344***` to `admin`.
        
        @param request: UpdateAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.new_account_type):
            query['NewAccountType'] = request.new_account_type
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccount',
            version='2020-03-31',
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
                resource_manager_20200331_models.UpdateAccountResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.UpdateAccountResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_account(
        self,
        request: resource_manager_20200331_models.UpdateAccountRequest,
    ) -> resource_manager_20200331_models.UpdateAccountResponse:
        """
        @description    To ensure that the system can record the operators of management operations, you must use a RAM user or RAM role to which the AliyunResourceDirectoryFullAccess policy is attached within the management account of your resource directory to call this operation.
        Before you switch the type of a member from resource account to cloud account, make sure that specific conditions are met. For more information about the conditions, see [Switch a resource account to a cloud account](https://help.aliyun.com/document_detail/111233.html).
        Before you switch the type of a member from cloud account to resource account, make sure that specific conditions are met. For more information about the conditions, see [Switch a cloud account to a resource account](https://help.aliyun.com/document_detail/209980.html).
        This example provides an example on how to call the API operation to change the display name of the member `12323344***` to `admin`.
        
        @param request: UpdateAccountRequest
        @return: UpdateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_account_with_options(request, runtime)

    async def update_account_async(
        self,
        request: resource_manager_20200331_models.UpdateAccountRequest,
    ) -> resource_manager_20200331_models.UpdateAccountResponse:
        """
        @description    To ensure that the system can record the operators of management operations, you must use a RAM user or RAM role to which the AliyunResourceDirectoryFullAccess policy is attached within the management account of your resource directory to call this operation.
        Before you switch the type of a member from resource account to cloud account, make sure that specific conditions are met. For more information about the conditions, see [Switch a resource account to a cloud account](https://help.aliyun.com/document_detail/111233.html).
        Before you switch the type of a member from cloud account to resource account, make sure that specific conditions are met. For more information about the conditions, see [Switch a cloud account to a resource account](https://help.aliyun.com/document_detail/209980.html).
        This example provides an example on how to call the API operation to change the display name of the member `12323344***` to `admin`.
        
        @param request: UpdateAccountRequest
        @return: UpdateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_account_with_options_async(request, runtime)

    def update_associated_transfer_setting_with_options(
        self,
        request: resource_manager_20200331_models.UpdateAssociatedTransferSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateAssociatedTransferSettingResponse:
        """
        @summary Updates the settings of the Transfer Associated Resources feature.
        
        @description For information about the resources that support the Transfer Associated Resources feature, see [Use the Transfer Associated Resources feature](https://help.aliyun.com/document_detail/606232.html).
        
        @param request: UpdateAssociatedTransferSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAssociatedTransferSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_existing_resources_transfer):
            query['EnableExistingResourcesTransfer'] = request.enable_existing_resources_transfer
        if not UtilClient.is_unset(request.rule_settings):
            query['RuleSettings'] = request.rule_settings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAssociatedTransferSetting',
            version='2020-03-31',
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
                resource_manager_20200331_models.UpdateAssociatedTransferSettingResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.UpdateAssociatedTransferSettingResponse(),
                self.execute(params, req, runtime)
            )

    async def update_associated_transfer_setting_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateAssociatedTransferSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateAssociatedTransferSettingResponse:
        """
        @summary Updates the settings of the Transfer Associated Resources feature.
        
        @description For information about the resources that support the Transfer Associated Resources feature, see [Use the Transfer Associated Resources feature](https://help.aliyun.com/document_detail/606232.html).
        
        @param request: UpdateAssociatedTransferSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAssociatedTransferSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_existing_resources_transfer):
            query['EnableExistingResourcesTransfer'] = request.enable_existing_resources_transfer
        if not UtilClient.is_unset(request.rule_settings):
            query['RuleSettings'] = request.rule_settings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAssociatedTransferSetting',
            version='2020-03-31',
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
                resource_manager_20200331_models.UpdateAssociatedTransferSettingResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.UpdateAssociatedTransferSettingResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_associated_transfer_setting(
        self,
        request: resource_manager_20200331_models.UpdateAssociatedTransferSettingRequest,
    ) -> resource_manager_20200331_models.UpdateAssociatedTransferSettingResponse:
        """
        @summary Updates the settings of the Transfer Associated Resources feature.
        
        @description For information about the resources that support the Transfer Associated Resources feature, see [Use the Transfer Associated Resources feature](https://help.aliyun.com/document_detail/606232.html).
        
        @param request: UpdateAssociatedTransferSettingRequest
        @return: UpdateAssociatedTransferSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_associated_transfer_setting_with_options(request, runtime)

    async def update_associated_transfer_setting_async(
        self,
        request: resource_manager_20200331_models.UpdateAssociatedTransferSettingRequest,
    ) -> resource_manager_20200331_models.UpdateAssociatedTransferSettingResponse:
        """
        @summary Updates the settings of the Transfer Associated Resources feature.
        
        @description For information about the resources that support the Transfer Associated Resources feature, see [Use the Transfer Associated Resources feature](https://help.aliyun.com/document_detail/606232.html).
        
        @param request: UpdateAssociatedTransferSettingRequest
        @return: UpdateAssociatedTransferSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_associated_transfer_setting_with_options_async(request, runtime)

    def update_auto_grouping_config_with_options(
        self,
        request: resource_manager_20200331_models.UpdateAutoGroupingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateAutoGroupingConfigResponse:
        """
        @summary Updates the configuration of the Automatic Resource Transfer feature. You can update only the configuration of the Transfer Existing Associated Resources feature.
        
        @param request: UpdateAutoGroupingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAutoGroupingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_existing_resources_transfer):
            query['EnableExistingResourcesTransfer'] = request.enable_existing_resources_transfer
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAutoGroupingConfig',
            version='2020-03-31',
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
                resource_manager_20200331_models.UpdateAutoGroupingConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.UpdateAutoGroupingConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def update_auto_grouping_config_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateAutoGroupingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateAutoGroupingConfigResponse:
        """
        @summary Updates the configuration of the Automatic Resource Transfer feature. You can update only the configuration of the Transfer Existing Associated Resources feature.
        
        @param request: UpdateAutoGroupingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAutoGroupingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_existing_resources_transfer):
            query['EnableExistingResourcesTransfer'] = request.enable_existing_resources_transfer
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAutoGroupingConfig',
            version='2020-03-31',
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
                resource_manager_20200331_models.UpdateAutoGroupingConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.UpdateAutoGroupingConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_auto_grouping_config(
        self,
        request: resource_manager_20200331_models.UpdateAutoGroupingConfigRequest,
    ) -> resource_manager_20200331_models.UpdateAutoGroupingConfigResponse:
        """
        @summary Updates the configuration of the Automatic Resource Transfer feature. You can update only the configuration of the Transfer Existing Associated Resources feature.
        
        @param request: UpdateAutoGroupingConfigRequest
        @return: UpdateAutoGroupingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_auto_grouping_config_with_options(request, runtime)

    async def update_auto_grouping_config_async(
        self,
        request: resource_manager_20200331_models.UpdateAutoGroupingConfigRequest,
    ) -> resource_manager_20200331_models.UpdateAutoGroupingConfigResponse:
        """
        @summary Updates the configuration of the Automatic Resource Transfer feature. You can update only the configuration of the Transfer Existing Associated Resources feature.
        
        @param request: UpdateAutoGroupingConfigRequest
        @return: UpdateAutoGroupingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_auto_grouping_config_with_options_async(request, runtime)

    def update_auto_grouping_rule_with_options(
        self,
        request: resource_manager_20200331_models.UpdateAutoGroupingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateAutoGroupingRuleResponse:
        """
        @summary Updates a transfer rule.
        
        @param request: UpdateAutoGroupingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAutoGroupingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.exclude_region_ids_scope):
            query['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_group_ids_scope):
            query['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            query['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_types_scope):
            query['ExcludeResourceTypesScope'] = request.exclude_resource_types_scope
        if not UtilClient.is_unset(request.region_ids_scope):
            query['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            query['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_ids_scope):
            query['ResourceIdsScope'] = request.resource_ids_scope
        if not UtilClient.is_unset(request.resource_types_scope):
            query['ResourceTypesScope'] = request.resource_types_scope
        if not UtilClient.is_unset(request.rule_contents):
            query['RuleContents'] = request.rule_contents
        if not UtilClient.is_unset(request.rule_desc):
            query['RuleDesc'] = request.rule_desc
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAutoGroupingRule',
            version='2020-03-31',
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
                resource_manager_20200331_models.UpdateAutoGroupingRuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.UpdateAutoGroupingRuleResponse(),
                self.execute(params, req, runtime)
            )

    async def update_auto_grouping_rule_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateAutoGroupingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateAutoGroupingRuleResponse:
        """
        @summary Updates a transfer rule.
        
        @param request: UpdateAutoGroupingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAutoGroupingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.exclude_region_ids_scope):
            query['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_group_ids_scope):
            query['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            query['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_types_scope):
            query['ExcludeResourceTypesScope'] = request.exclude_resource_types_scope
        if not UtilClient.is_unset(request.region_ids_scope):
            query['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            query['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_ids_scope):
            query['ResourceIdsScope'] = request.resource_ids_scope
        if not UtilClient.is_unset(request.resource_types_scope):
            query['ResourceTypesScope'] = request.resource_types_scope
        if not UtilClient.is_unset(request.rule_contents):
            query['RuleContents'] = request.rule_contents
        if not UtilClient.is_unset(request.rule_desc):
            query['RuleDesc'] = request.rule_desc
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAutoGroupingRule',
            version='2020-03-31',
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
                resource_manager_20200331_models.UpdateAutoGroupingRuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.UpdateAutoGroupingRuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_auto_grouping_rule(
        self,
        request: resource_manager_20200331_models.UpdateAutoGroupingRuleRequest,
    ) -> resource_manager_20200331_models.UpdateAutoGroupingRuleResponse:
        """
        @summary Updates a transfer rule.
        
        @param request: UpdateAutoGroupingRuleRequest
        @return: UpdateAutoGroupingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_auto_grouping_rule_with_options(request, runtime)

    async def update_auto_grouping_rule_async(
        self,
        request: resource_manager_20200331_models.UpdateAutoGroupingRuleRequest,
    ) -> resource_manager_20200331_models.UpdateAutoGroupingRuleResponse:
        """
        @summary Updates a transfer rule.
        
        @param request: UpdateAutoGroupingRuleRequest
        @return: UpdateAutoGroupingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_auto_grouping_rule_with_options_async(request, runtime)

    def update_control_policy_with_options(
        self,
        request: resource_manager_20200331_models.UpdateControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateControlPolicyResponse:
        """
        @description In this example, the name of the access control policy whose ID is `cp-jExXAqIYkwHN***` is changed to `NewControlPolicy`.
        
        @param request: UpdateControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_policy_document):
            query['NewPolicyDocument'] = request.new_policy_document
        if not UtilClient.is_unset(request.new_policy_name):
            query['NewPolicyName'] = request.new_policy_name
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateControlPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.UpdateControlPolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.UpdateControlPolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def update_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateControlPolicyResponse:
        """
        @description In this example, the name of the access control policy whose ID is `cp-jExXAqIYkwHN***` is changed to `NewControlPolicy`.
        
        @param request: UpdateControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_policy_document):
            query['NewPolicyDocument'] = request.new_policy_document
        if not UtilClient.is_unset(request.new_policy_name):
            query['NewPolicyName'] = request.new_policy_name
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateControlPolicy',
            version='2020-03-31',
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
                resource_manager_20200331_models.UpdateControlPolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.UpdateControlPolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_control_policy(
        self,
        request: resource_manager_20200331_models.UpdateControlPolicyRequest,
    ) -> resource_manager_20200331_models.UpdateControlPolicyResponse:
        """
        @description In this example, the name of the access control policy whose ID is `cp-jExXAqIYkwHN***` is changed to `NewControlPolicy`.
        
        @param request: UpdateControlPolicyRequest
        @return: UpdateControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_control_policy_with_options(request, runtime)

    async def update_control_policy_async(
        self,
        request: resource_manager_20200331_models.UpdateControlPolicyRequest,
    ) -> resource_manager_20200331_models.UpdateControlPolicyResponse:
        """
        @description In this example, the name of the access control policy whose ID is `cp-jExXAqIYkwHN***` is changed to `NewControlPolicy`.
        
        @param request: UpdateControlPolicyRequest
        @return: UpdateControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_control_policy_with_options_async(request, runtime)

    def update_folder_with_options(
        self,
        request: resource_manager_20200331_models.UpdateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateFolderResponse:
        """
        @param request: UpdateFolderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFolderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.new_folder_name):
            query['NewFolderName'] = request.new_folder_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFolder',
            version='2020-03-31',
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
                resource_manager_20200331_models.UpdateFolderResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.UpdateFolderResponse(),
                self.execute(params, req, runtime)
            )

    async def update_folder_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateFolderResponse:
        """
        @param request: UpdateFolderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFolderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.new_folder_name):
            query['NewFolderName'] = request.new_folder_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFolder',
            version='2020-03-31',
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
                resource_manager_20200331_models.UpdateFolderResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.UpdateFolderResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_folder(
        self,
        request: resource_manager_20200331_models.UpdateFolderRequest,
    ) -> resource_manager_20200331_models.UpdateFolderResponse:
        """
        @param request: UpdateFolderRequest
        @return: UpdateFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_folder_with_options(request, runtime)

    async def update_folder_async(
        self,
        request: resource_manager_20200331_models.UpdateFolderRequest,
    ) -> resource_manager_20200331_models.UpdateFolderResponse:
        """
        @param request: UpdateFolderRequest
        @return: UpdateFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_folder_with_options_async(request, runtime)

    def update_resource_group_with_options(
        self,
        request: resource_manager_20200331_models.UpdateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateResourceGroupResponse:
        """
        @description In this example, the display name of the resource group `rg-9gLOoK***` is changed to `project`.
        
        @param request: UpdateResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceGroup',
            version='2020-03-31',
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
                resource_manager_20200331_models.UpdateResourceGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.UpdateResourceGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def update_resource_group_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateResourceGroupResponse:
        """
        @description In this example, the display name of the resource group `rg-9gLOoK***` is changed to `project`.
        
        @param request: UpdateResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceGroup',
            version='2020-03-31',
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
                resource_manager_20200331_models.UpdateResourceGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.UpdateResourceGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_resource_group(
        self,
        request: resource_manager_20200331_models.UpdateResourceGroupRequest,
    ) -> resource_manager_20200331_models.UpdateResourceGroupResponse:
        """
        @description In this example, the display name of the resource group `rg-9gLOoK***` is changed to `project`.
        
        @param request: UpdateResourceGroupRequest
        @return: UpdateResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_resource_group_with_options(request, runtime)

    async def update_resource_group_async(
        self,
        request: resource_manager_20200331_models.UpdateResourceGroupRequest,
    ) -> resource_manager_20200331_models.UpdateResourceGroupResponse:
        """
        @description In this example, the display name of the resource group `rg-9gLOoK***` is changed to `project`.
        
        @param request: UpdateResourceGroupRequest
        @return: UpdateResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_resource_group_with_options_async(request, runtime)

    def update_role_with_options(
        self,
        request: resource_manager_20200331_models.UpdateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateRoleResponse:
        """
        @summary Updates the information of a Resource Access Management (RAM) role.
        
        @description In this example, the description of the RAM role `ECSAdmin` is updated to `ECS administrator`.
        
        @param request: UpdateRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_assume_role_policy_document):
            query['NewAssumeRolePolicyDocument'] = request.new_assume_role_policy_document
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_max_session_duration):
            query['NewMaxSessionDuration'] = request.new_max_session_duration
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRole',
            version='2020-03-31',
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
                resource_manager_20200331_models.UpdateRoleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.UpdateRoleResponse(),
                self.execute(params, req, runtime)
            )

    async def update_role_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateRoleResponse:
        """
        @summary Updates the information of a Resource Access Management (RAM) role.
        
        @description In this example, the description of the RAM role `ECSAdmin` is updated to `ECS administrator`.
        
        @param request: UpdateRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_assume_role_policy_document):
            query['NewAssumeRolePolicyDocument'] = request.new_assume_role_policy_document
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_max_session_duration):
            query['NewMaxSessionDuration'] = request.new_max_session_duration
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRole',
            version='2020-03-31',
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
                resource_manager_20200331_models.UpdateRoleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                resource_manager_20200331_models.UpdateRoleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_role(
        self,
        request: resource_manager_20200331_models.UpdateRoleRequest,
    ) -> resource_manager_20200331_models.UpdateRoleResponse:
        """
        @summary Updates the information of a Resource Access Management (RAM) role.
        
        @description In this example, the description of the RAM role `ECSAdmin` is updated to `ECS administrator`.
        
        @param request: UpdateRoleRequest
        @return: UpdateRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_role_with_options(request, runtime)

    async def update_role_async(
        self,
        request: resource_manager_20200331_models.UpdateRoleRequest,
    ) -> resource_manager_20200331_models.UpdateRoleResponse:
        """
        @summary Updates the information of a Resource Access Management (RAM) role.
        
        @description In this example, the description of the RAM role `ECSAdmin` is updated to `ECS administrator`.
        
        @param request: UpdateRoleRequest
        @return: UpdateRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_role_with_options_async(request, runtime)
