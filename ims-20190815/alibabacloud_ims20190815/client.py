# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_ims20190815 import models as ims_20190815_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ims', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_user_sso_settings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.GetUserSsoSettingsResponse().from_map(self.do_request('GetUserSsoSettings', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def get_user_sso_settings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_sso_settings_with_options(request, runtime)

    def set_user_sso_settings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.SetUserSsoSettingsResponse().from_map(self.do_request('SetUserSsoSettings', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def set_user_sso_settings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_user_sso_settings_with_options(request, runtime)

    def set_default_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.SetDefaultDomainResponse().from_map(self.do_request('SetDefaultDomain', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def set_default_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_default_domain_with_options(request, runtime)

    def list_user_basic_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.ListUserBasicInfosResponse().from_map(self.do_request('ListUserBasicInfos', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def list_user_basic_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_basic_infos_with_options(request, runtime)

    def update_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.UpdateApplicationResponse().from_map(self.do_request('UpdateApplication', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def update_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_application_with_options(request, runtime)

    def list_applications_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.ListApplicationsResponse().from_map(self.do_request('ListApplications', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def list_applications(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_applications_with_options(request, runtime)

    def get_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.GetApplicationResponse().from_map(self.do_request('GetApplication', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def get_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_application_with_options(request, runtime)

    def delete_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.DeleteApplicationResponse().from_map(self.do_request('DeleteApplication', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def delete_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_application_with_options(request, runtime)

    def get_app_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.GetAppSecretResponse().from_map(self.do_request('GetAppSecret', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def get_app_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_app_secret_with_options(request, runtime)

    def create_app_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.CreateAppSecretResponse().from_map(self.do_request('CreateAppSecret', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def create_app_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_secret_with_options(request, runtime)

    def list_predefined_scopes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.ListPredefinedScopesResponse().from_map(self.do_request('ListPredefinedScopes', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def list_predefined_scopes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_predefined_scopes_with_options(request, runtime)

    def create_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.CreateApplicationResponse().from_map(self.do_request('CreateApplication', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def create_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    def delete_app_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.DeleteAppSecretResponse().from_map(self.do_request('DeleteAppSecret', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def delete_app_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_app_secret_with_options(request, runtime)

    def list_app_secret_ids_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.ListAppSecretIdsResponse().from_map(self.do_request('ListAppSecretIds', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def list_app_secret_ids(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_app_secret_ids_with_options(request, runtime)

    def generate_credential_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.GenerateCredentialReportResponse().from_map(self.do_request('GenerateCredentialReport', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def generate_credential_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_credential_report_with_options(request, runtime)

    def get_credential_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.GetCredentialReportResponse().from_map(self.do_request('GetCredentialReport', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def get_credential_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_credential_report_with_options(request, runtime)

    def update_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.UpdateUserResponse().from_map(self.do_request('UpdateUser', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def update_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    def update_samlprovider_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.UpdateSAMLProviderResponse().from_map(self.do_request('UpdateSAMLProvider', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def update_samlprovider(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_samlprovider_with_options(request, runtime)

    def update_login_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.UpdateLoginProfileResponse().from_map(self.do_request('UpdateLoginProfile', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def update_login_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_login_profile_with_options(request, runtime)

    def update_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.UpdateGroupResponse().from_map(self.do_request('UpdateGroup', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def update_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_group_with_options(request, runtime)

    def update_access_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.UpdateAccessKeyResponse().from_map(self.do_request('UpdateAccessKey', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def update_access_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_access_key_with_options(request, runtime)

    def unbind_mfadevice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.UnbindMFADeviceResponse().from_map(self.do_request('UnbindMFADevice', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def unbind_mfadevice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_mfadevice_with_options(request, runtime)

    def set_security_preference_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.SetSecurityPreferenceResponse().from_map(self.do_request('SetSecurityPreference', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def set_security_preference(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_security_preference_with_options(request, runtime)

    def set_password_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.SetPasswordPolicyResponse().from_map(self.do_request('SetPasswordPolicy', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def set_password_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_password_policy_with_options(request, runtime)

    def remove_user_from_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.RemoveUserFromGroupResponse().from_map(self.do_request('RemoveUserFromGroup', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def remove_user_from_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_user_from_group_with_options(request, runtime)

    def list_virtual_mfadevices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.ListVirtualMFADevicesResponse().from_map(self.do_request('ListVirtualMFADevices', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def list_virtual_mfadevices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_virtual_mfadevices_with_options(request, runtime)

    def list_users_for_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.ListUsersForGroupResponse().from_map(self.do_request('ListUsersForGroup', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def list_users_for_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_for_group_with_options(request, runtime)

    def list_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.ListUsersResponse().from_map(self.do_request('ListUsers', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    def list_samlproviders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.ListSAMLProvidersResponse().from_map(self.do_request('ListSAMLProviders', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def list_samlproviders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_samlproviders_with_options(request, runtime)

    def list_groups_for_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.ListGroupsForUserResponse().from_map(self.do_request('ListGroupsForUser', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def list_groups_for_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_groups_for_user_with_options(request, runtime)

    def list_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.ListGroupsResponse().from_map(self.do_request('ListGroups', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def list_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_groups_with_options(request, runtime)

    def list_access_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.ListAccessKeysResponse().from_map(self.do_request('ListAccessKeys', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def list_access_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_access_keys_with_options(request, runtime)

    def get_user_mfainfo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.GetUserMFAInfoResponse().from_map(self.do_request('GetUserMFAInfo', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def get_user_mfainfo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_mfainfo_with_options(request, runtime)

    def get_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.GetUserResponse().from_map(self.do_request('GetUser', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def get_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    def get_security_preference_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.GetSecurityPreferenceResponse().from_map(self.do_request('GetSecurityPreference', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def get_security_preference(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_security_preference_with_options(request, runtime)

    def get_samlprovider_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.GetSAMLProviderResponse().from_map(self.do_request('GetSAMLProvider', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def get_samlprovider(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_samlprovider_with_options(request, runtime)

    def get_password_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.GetPasswordPolicyResponse().from_map(self.do_request('GetPasswordPolicy', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def get_password_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_password_policy_with_options(request, runtime)

    def get_login_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.GetLoginProfileResponse().from_map(self.do_request('GetLoginProfile', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def get_login_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_login_profile_with_options(request, runtime)

    def get_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.GetGroupResponse().from_map(self.do_request('GetGroup', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def get_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_group_with_options(request, runtime)

    def get_default_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.GetDefaultDomainResponse().from_map(self.do_request('GetDefaultDomain', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def get_default_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_default_domain_with_options(request, runtime)

    def get_account_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.GetAccountSummaryResponse().from_map(self.do_request('GetAccountSummary', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def get_account_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_account_summary_with_options(request, runtime)

    def get_account_security_practice_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.GetAccountSecurityPracticeReportResponse().from_map(self.do_request('GetAccountSecurityPracticeReport', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def get_account_security_practice_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_account_security_practice_report_with_options(request, runtime)

    def get_account_mfainfo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.GetAccountMFAInfoResponse().from_map(self.do_request('GetAccountMFAInfo', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def get_account_mfainfo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_account_mfainfo_with_options(request, runtime)

    def get_access_key_last_used_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.GetAccessKeyLastUsedResponse().from_map(self.do_request('GetAccessKeyLastUsed', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def get_access_key_last_used(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_access_key_last_used_with_options(request, runtime)

    def disable_virtual_mfawith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.DisableVirtualMFAResponse().from_map(self.do_request('DisableVirtualMFA', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def disable_virtual_mfa(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_virtual_mfawith_options(request, runtime)

    def delete_virtual_mfadevice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.DeleteVirtualMFADeviceResponse().from_map(self.do_request('DeleteVirtualMFADevice', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def delete_virtual_mfadevice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_mfadevice_with_options(request, runtime)

    def delete_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.DeleteUserResponse().from_map(self.do_request('DeleteUser', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def delete_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    def delete_samlprovider_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.DeleteSAMLProviderResponse().from_map(self.do_request('DeleteSAMLProvider', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def delete_samlprovider(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_samlprovider_with_options(request, runtime)

    def delete_login_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.DeleteLoginProfileResponse().from_map(self.do_request('DeleteLoginProfile', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def delete_login_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_login_profile_with_options(request, runtime)

    def delete_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.DeleteGroupResponse().from_map(self.do_request('DeleteGroup', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def delete_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    def delete_access_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.DeleteAccessKeyResponse().from_map(self.do_request('DeleteAccessKey', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def delete_access_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_access_key_with_options(request, runtime)

    def create_virtual_mfadevice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.CreateVirtualMFADeviceResponse().from_map(self.do_request('CreateVirtualMFADevice', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def create_virtual_mfadevice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_mfadevice_with_options(request, runtime)

    def create_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.CreateUserResponse().from_map(self.do_request('CreateUser', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def create_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    def create_samlprovider_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.CreateSAMLProviderResponse().from_map(self.do_request('CreateSAMLProvider', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def create_samlprovider(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_samlprovider_with_options(request, runtime)

    def create_login_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.CreateLoginProfileResponse().from_map(self.do_request('CreateLoginProfile', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def create_login_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_login_profile_with_options(request, runtime)

    def create_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.CreateGroupResponse().from_map(self.do_request('CreateGroup', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def create_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    def create_access_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.CreateAccessKeyResponse().from_map(self.do_request('CreateAccessKey', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def create_access_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_access_key_with_options(request, runtime)

    def change_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.ChangePasswordResponse().from_map(self.do_request('ChangePassword', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def change_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_password_with_options(request, runtime)

    def bind_mfadevice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.BindMFADeviceResponse().from_map(self.do_request('BindMFADevice', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def bind_mfadevice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_mfadevice_with_options(request, runtime)

    def add_user_to_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ims_20190815_models.AddUserToGroupResponse().from_map(self.do_request('AddUserToGroup', 'HTTPS', 'POST', '2019-08-15', 'AK,BearerToken', None, TeaCore.to_map(request), runtime))

    def add_user_to_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_group_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
