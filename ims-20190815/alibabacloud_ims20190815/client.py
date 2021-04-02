# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_ims20190815 import models as ims_20190815_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(
        self, 
        config: rpc_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ims', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_user_sso_settings_with_options(
        self,
        request: ims_20190815_models.GetUserSsoSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetUserSsoSettingsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetUserSsoSettingsResponse(),
            self.do_request('GetUserSsoSettings', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_user_sso_settings_with_options_async(
        self,
        request: ims_20190815_models.GetUserSsoSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetUserSsoSettingsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetUserSsoSettingsResponse(),
            await self.do_request_async('GetUserSsoSettings', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_user_sso_settings(
        self,
        request: ims_20190815_models.GetUserSsoSettingsRequest,
    ) -> ims_20190815_models.GetUserSsoSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_sso_settings_with_options(request, runtime)

    async def get_user_sso_settings_async(
        self,
        request: ims_20190815_models.GetUserSsoSettingsRequest,
    ) -> ims_20190815_models.GetUserSsoSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_sso_settings_with_options_async(request, runtime)

    def set_user_sso_settings_with_options(
        self,
        request: ims_20190815_models.SetUserSsoSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetUserSsoSettingsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.SetUserSsoSettingsResponse(),
            self.do_request('SetUserSsoSettings', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_user_sso_settings_with_options_async(
        self,
        request: ims_20190815_models.SetUserSsoSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetUserSsoSettingsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.SetUserSsoSettingsResponse(),
            await self.do_request_async('SetUserSsoSettings', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_user_sso_settings(
        self,
        request: ims_20190815_models.SetUserSsoSettingsRequest,
    ) -> ims_20190815_models.SetUserSsoSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_user_sso_settings_with_options(request, runtime)

    async def set_user_sso_settings_async(
        self,
        request: ims_20190815_models.SetUserSsoSettingsRequest,
    ) -> ims_20190815_models.SetUserSsoSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_user_sso_settings_with_options_async(request, runtime)

    def set_default_domain_with_options(
        self,
        request: ims_20190815_models.SetDefaultDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetDefaultDomainResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.SetDefaultDomainResponse(),
            self.do_request('SetDefaultDomain', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_default_domain_with_options_async(
        self,
        request: ims_20190815_models.SetDefaultDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetDefaultDomainResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.SetDefaultDomainResponse(),
            await self.do_request_async('SetDefaultDomain', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_default_domain(
        self,
        request: ims_20190815_models.SetDefaultDomainRequest,
    ) -> ims_20190815_models.SetDefaultDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_default_domain_with_options(request, runtime)

    async def set_default_domain_async(
        self,
        request: ims_20190815_models.SetDefaultDomainRequest,
    ) -> ims_20190815_models.SetDefaultDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_default_domain_with_options_async(request, runtime)

    def list_user_basic_infos_with_options(
        self,
        request: ims_20190815_models.ListUserBasicInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListUserBasicInfosResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListUserBasicInfosResponse(),
            self.do_request('ListUserBasicInfos', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_user_basic_infos_with_options_async(
        self,
        request: ims_20190815_models.ListUserBasicInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListUserBasicInfosResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListUserBasicInfosResponse(),
            await self.do_request_async('ListUserBasicInfos', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_user_basic_infos(
        self,
        request: ims_20190815_models.ListUserBasicInfosRequest,
    ) -> ims_20190815_models.ListUserBasicInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_basic_infos_with_options(request, runtime)

    async def list_user_basic_infos_async(
        self,
        request: ims_20190815_models.ListUserBasicInfosRequest,
    ) -> ims_20190815_models.ListUserBasicInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_basic_infos_with_options_async(request, runtime)

    def update_application_with_options(
        self,
        request: ims_20190815_models.UpdateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateApplicationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.UpdateApplicationResponse(),
            self.do_request('UpdateApplication', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_application_with_options_async(
        self,
        request: ims_20190815_models.UpdateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateApplicationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.UpdateApplicationResponse(),
            await self.do_request_async('UpdateApplication', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_application(
        self,
        request: ims_20190815_models.UpdateApplicationRequest,
    ) -> ims_20190815_models.UpdateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_application_with_options(request, runtime)

    async def update_application_async(
        self,
        request: ims_20190815_models.UpdateApplicationRequest,
    ) -> ims_20190815_models.UpdateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_application_with_options_async(request, runtime)

    def list_applications_with_options(
        self,
        request: ims_20190815_models.ListApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListApplicationsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListApplicationsResponse(),
            self.do_request('ListApplications', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_applications_with_options_async(
        self,
        request: ims_20190815_models.ListApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListApplicationsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListApplicationsResponse(),
            await self.do_request_async('ListApplications', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_applications(
        self,
        request: ims_20190815_models.ListApplicationsRequest,
    ) -> ims_20190815_models.ListApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_applications_with_options(request, runtime)

    async def list_applications_async(
        self,
        request: ims_20190815_models.ListApplicationsRequest,
    ) -> ims_20190815_models.ListApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_applications_with_options_async(request, runtime)

    def get_application_with_options(
        self,
        request: ims_20190815_models.GetApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetApplicationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetApplicationResponse(),
            self.do_request('GetApplication', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_application_with_options_async(
        self,
        request: ims_20190815_models.GetApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetApplicationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetApplicationResponse(),
            await self.do_request_async('GetApplication', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_application(
        self,
        request: ims_20190815_models.GetApplicationRequest,
    ) -> ims_20190815_models.GetApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_application_with_options(request, runtime)

    async def get_application_async(
        self,
        request: ims_20190815_models.GetApplicationRequest,
    ) -> ims_20190815_models.GetApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_application_with_options_async(request, runtime)

    def delete_application_with_options(
        self,
        request: ims_20190815_models.DeleteApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteApplicationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.DeleteApplicationResponse(),
            self.do_request('DeleteApplication', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_application_with_options_async(
        self,
        request: ims_20190815_models.DeleteApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteApplicationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.DeleteApplicationResponse(),
            await self.do_request_async('DeleteApplication', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_application(
        self,
        request: ims_20190815_models.DeleteApplicationRequest,
    ) -> ims_20190815_models.DeleteApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_application_with_options(request, runtime)

    async def delete_application_async(
        self,
        request: ims_20190815_models.DeleteApplicationRequest,
    ) -> ims_20190815_models.DeleteApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_application_with_options_async(request, runtime)

    def get_app_secret_with_options(
        self,
        request: ims_20190815_models.GetAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAppSecretResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetAppSecretResponse(),
            self.do_request('GetAppSecret', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_app_secret_with_options_async(
        self,
        request: ims_20190815_models.GetAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAppSecretResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetAppSecretResponse(),
            await self.do_request_async('GetAppSecret', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_app_secret(
        self,
        request: ims_20190815_models.GetAppSecretRequest,
    ) -> ims_20190815_models.GetAppSecretResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_secret_with_options(request, runtime)

    async def get_app_secret_async(
        self,
        request: ims_20190815_models.GetAppSecretRequest,
    ) -> ims_20190815_models.GetAppSecretResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_secret_with_options_async(request, runtime)

    def create_app_secret_with_options(
        self,
        request: ims_20190815_models.CreateAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateAppSecretResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.CreateAppSecretResponse(),
            self.do_request('CreateAppSecret', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_app_secret_with_options_async(
        self,
        request: ims_20190815_models.CreateAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateAppSecretResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.CreateAppSecretResponse(),
            await self.do_request_async('CreateAppSecret', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_app_secret(
        self,
        request: ims_20190815_models.CreateAppSecretRequest,
    ) -> ims_20190815_models.CreateAppSecretResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_secret_with_options(request, runtime)

    async def create_app_secret_async(
        self,
        request: ims_20190815_models.CreateAppSecretRequest,
    ) -> ims_20190815_models.CreateAppSecretResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_secret_with_options_async(request, runtime)

    def list_predefined_scopes_with_options(
        self,
        request: ims_20190815_models.ListPredefinedScopesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListPredefinedScopesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListPredefinedScopesResponse(),
            self.do_request('ListPredefinedScopes', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_predefined_scopes_with_options_async(
        self,
        request: ims_20190815_models.ListPredefinedScopesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListPredefinedScopesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListPredefinedScopesResponse(),
            await self.do_request_async('ListPredefinedScopes', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_predefined_scopes(
        self,
        request: ims_20190815_models.ListPredefinedScopesRequest,
    ) -> ims_20190815_models.ListPredefinedScopesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_predefined_scopes_with_options(request, runtime)

    async def list_predefined_scopes_async(
        self,
        request: ims_20190815_models.ListPredefinedScopesRequest,
    ) -> ims_20190815_models.ListPredefinedScopesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_predefined_scopes_with_options_async(request, runtime)

    def create_application_with_options(
        self,
        request: ims_20190815_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateApplicationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.CreateApplicationResponse(),
            self.do_request('CreateApplication', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_application_with_options_async(
        self,
        request: ims_20190815_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateApplicationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.CreateApplicationResponse(),
            await self.do_request_async('CreateApplication', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_application(
        self,
        request: ims_20190815_models.CreateApplicationRequest,
    ) -> ims_20190815_models.CreateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    async def create_application_async(
        self,
        request: ims_20190815_models.CreateApplicationRequest,
    ) -> ims_20190815_models.CreateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_application_with_options_async(request, runtime)

    def delete_app_secret_with_options(
        self,
        request: ims_20190815_models.DeleteAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteAppSecretResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.DeleteAppSecretResponse(),
            self.do_request('DeleteAppSecret', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_app_secret_with_options_async(
        self,
        request: ims_20190815_models.DeleteAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteAppSecretResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.DeleteAppSecretResponse(),
            await self.do_request_async('DeleteAppSecret', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_app_secret(
        self,
        request: ims_20190815_models.DeleteAppSecretRequest,
    ) -> ims_20190815_models.DeleteAppSecretResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_secret_with_options(request, runtime)

    async def delete_app_secret_async(
        self,
        request: ims_20190815_models.DeleteAppSecretRequest,
    ) -> ims_20190815_models.DeleteAppSecretResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_secret_with_options_async(request, runtime)

    def list_app_secret_ids_with_options(
        self,
        request: ims_20190815_models.ListAppSecretIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListAppSecretIdsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListAppSecretIdsResponse(),
            self.do_request('ListAppSecretIds', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_app_secret_ids_with_options_async(
        self,
        request: ims_20190815_models.ListAppSecretIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListAppSecretIdsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListAppSecretIdsResponse(),
            await self.do_request_async('ListAppSecretIds', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_app_secret_ids(
        self,
        request: ims_20190815_models.ListAppSecretIdsRequest,
    ) -> ims_20190815_models.ListAppSecretIdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_secret_ids_with_options(request, runtime)

    async def list_app_secret_ids_async(
        self,
        request: ims_20190815_models.ListAppSecretIdsRequest,
    ) -> ims_20190815_models.ListAppSecretIdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_secret_ids_with_options_async(request, runtime)

    def generate_credential_report_with_options(
        self,
        request: ims_20190815_models.GenerateCredentialReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GenerateCredentialReportResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GenerateCredentialReportResponse(),
            self.do_request('GenerateCredentialReport', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def generate_credential_report_with_options_async(
        self,
        request: ims_20190815_models.GenerateCredentialReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GenerateCredentialReportResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GenerateCredentialReportResponse(),
            await self.do_request_async('GenerateCredentialReport', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def generate_credential_report(
        self,
        request: ims_20190815_models.GenerateCredentialReportRequest,
    ) -> ims_20190815_models.GenerateCredentialReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_credential_report_with_options(request, runtime)

    async def generate_credential_report_async(
        self,
        request: ims_20190815_models.GenerateCredentialReportRequest,
    ) -> ims_20190815_models.GenerateCredentialReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_credential_report_with_options_async(request, runtime)

    def get_credential_report_with_options(
        self,
        request: ims_20190815_models.GetCredentialReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetCredentialReportResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetCredentialReportResponse(),
            self.do_request('GetCredentialReport', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_credential_report_with_options_async(
        self,
        request: ims_20190815_models.GetCredentialReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetCredentialReportResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetCredentialReportResponse(),
            await self.do_request_async('GetCredentialReport', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_credential_report(
        self,
        request: ims_20190815_models.GetCredentialReportRequest,
    ) -> ims_20190815_models.GetCredentialReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_credential_report_with_options(request, runtime)

    async def get_credential_report_async(
        self,
        request: ims_20190815_models.GetCredentialReportRequest,
    ) -> ims_20190815_models.GetCredentialReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_credential_report_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: ims_20190815_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.UpdateUserResponse(),
            self.do_request('UpdateUser', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_user_with_options_async(
        self,
        request: ims_20190815_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.UpdateUserResponse(),
            await self.do_request_async('UpdateUser', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_user(
        self,
        request: ims_20190815_models.UpdateUserRequest,
    ) -> ims_20190815_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: ims_20190815_models.UpdateUserRequest,
    ) -> ims_20190815_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)

    def update_samlprovider_with_options(
        self,
        request: ims_20190815_models.UpdateSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateSAMLProviderResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.UpdateSAMLProviderResponse(),
            self.do_request('UpdateSAMLProvider', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_samlprovider_with_options_async(
        self,
        request: ims_20190815_models.UpdateSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateSAMLProviderResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.UpdateSAMLProviderResponse(),
            await self.do_request_async('UpdateSAMLProvider', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_samlprovider(
        self,
        request: ims_20190815_models.UpdateSAMLProviderRequest,
    ) -> ims_20190815_models.UpdateSAMLProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_samlprovider_with_options(request, runtime)

    async def update_samlprovider_async(
        self,
        request: ims_20190815_models.UpdateSAMLProviderRequest,
    ) -> ims_20190815_models.UpdateSAMLProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_samlprovider_with_options_async(request, runtime)

    def update_login_profile_with_options(
        self,
        request: ims_20190815_models.UpdateLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateLoginProfileResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.UpdateLoginProfileResponse(),
            self.do_request('UpdateLoginProfile', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_login_profile_with_options_async(
        self,
        request: ims_20190815_models.UpdateLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateLoginProfileResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.UpdateLoginProfileResponse(),
            await self.do_request_async('UpdateLoginProfile', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_login_profile(
        self,
        request: ims_20190815_models.UpdateLoginProfileRequest,
    ) -> ims_20190815_models.UpdateLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_login_profile_with_options(request, runtime)

    async def update_login_profile_async(
        self,
        request: ims_20190815_models.UpdateLoginProfileRequest,
    ) -> ims_20190815_models.UpdateLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_login_profile_with_options_async(request, runtime)

    def update_group_with_options(
        self,
        request: ims_20190815_models.UpdateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.UpdateGroupResponse(),
            self.do_request('UpdateGroup', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_group_with_options_async(
        self,
        request: ims_20190815_models.UpdateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.UpdateGroupResponse(),
            await self.do_request_async('UpdateGroup', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_group(
        self,
        request: ims_20190815_models.UpdateGroupRequest,
    ) -> ims_20190815_models.UpdateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_group_with_options(request, runtime)

    async def update_group_async(
        self,
        request: ims_20190815_models.UpdateGroupRequest,
    ) -> ims_20190815_models.UpdateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_group_with_options_async(request, runtime)

    def update_access_key_with_options(
        self,
        request: ims_20190815_models.UpdateAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateAccessKeyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.UpdateAccessKeyResponse(),
            self.do_request('UpdateAccessKey', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_access_key_with_options_async(
        self,
        request: ims_20190815_models.UpdateAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateAccessKeyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.UpdateAccessKeyResponse(),
            await self.do_request_async('UpdateAccessKey', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_access_key(
        self,
        request: ims_20190815_models.UpdateAccessKeyRequest,
    ) -> ims_20190815_models.UpdateAccessKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_access_key_with_options(request, runtime)

    async def update_access_key_async(
        self,
        request: ims_20190815_models.UpdateAccessKeyRequest,
    ) -> ims_20190815_models.UpdateAccessKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_access_key_with_options_async(request, runtime)

    def unbind_mfadevice_with_options(
        self,
        request: ims_20190815_models.UnbindMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UnbindMFADeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.UnbindMFADeviceResponse(),
            self.do_request('UnbindMFADevice', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def unbind_mfadevice_with_options_async(
        self,
        request: ims_20190815_models.UnbindMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UnbindMFADeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.UnbindMFADeviceResponse(),
            await self.do_request_async('UnbindMFADevice', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def unbind_mfadevice(
        self,
        request: ims_20190815_models.UnbindMFADeviceRequest,
    ) -> ims_20190815_models.UnbindMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_mfadevice_with_options(request, runtime)

    async def unbind_mfadevice_async(
        self,
        request: ims_20190815_models.UnbindMFADeviceRequest,
    ) -> ims_20190815_models.UnbindMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_mfadevice_with_options_async(request, runtime)

    def set_security_preference_with_options(
        self,
        request: ims_20190815_models.SetSecurityPreferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetSecurityPreferenceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.SetSecurityPreferenceResponse(),
            self.do_request('SetSecurityPreference', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_security_preference_with_options_async(
        self,
        request: ims_20190815_models.SetSecurityPreferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetSecurityPreferenceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.SetSecurityPreferenceResponse(),
            await self.do_request_async('SetSecurityPreference', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_security_preference(
        self,
        request: ims_20190815_models.SetSecurityPreferenceRequest,
    ) -> ims_20190815_models.SetSecurityPreferenceResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_security_preference_with_options(request, runtime)

    async def set_security_preference_async(
        self,
        request: ims_20190815_models.SetSecurityPreferenceRequest,
    ) -> ims_20190815_models.SetSecurityPreferenceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_security_preference_with_options_async(request, runtime)

    def set_password_policy_with_options(
        self,
        request: ims_20190815_models.SetPasswordPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetPasswordPolicyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.SetPasswordPolicyResponse(),
            self.do_request('SetPasswordPolicy', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_password_policy_with_options_async(
        self,
        request: ims_20190815_models.SetPasswordPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetPasswordPolicyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.SetPasswordPolicyResponse(),
            await self.do_request_async('SetPasswordPolicy', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_password_policy(
        self,
        request: ims_20190815_models.SetPasswordPolicyRequest,
    ) -> ims_20190815_models.SetPasswordPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_password_policy_with_options(request, runtime)

    async def set_password_policy_async(
        self,
        request: ims_20190815_models.SetPasswordPolicyRequest,
    ) -> ims_20190815_models.SetPasswordPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_password_policy_with_options_async(request, runtime)

    def remove_user_from_group_with_options(
        self,
        request: ims_20190815_models.RemoveUserFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.RemoveUserFromGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.RemoveUserFromGroupResponse(),
            self.do_request('RemoveUserFromGroup', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def remove_user_from_group_with_options_async(
        self,
        request: ims_20190815_models.RemoveUserFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.RemoveUserFromGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.RemoveUserFromGroupResponse(),
            await self.do_request_async('RemoveUserFromGroup', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def remove_user_from_group(
        self,
        request: ims_20190815_models.RemoveUserFromGroupRequest,
    ) -> ims_20190815_models.RemoveUserFromGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_user_from_group_with_options(request, runtime)

    async def remove_user_from_group_async(
        self,
        request: ims_20190815_models.RemoveUserFromGroupRequest,
    ) -> ims_20190815_models.RemoveUserFromGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_user_from_group_with_options_async(request, runtime)

    def list_virtual_mfadevices_with_options(
        self,
        request: ims_20190815_models.ListVirtualMFADevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListVirtualMFADevicesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListVirtualMFADevicesResponse(),
            self.do_request('ListVirtualMFADevices', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_virtual_mfadevices_with_options_async(
        self,
        request: ims_20190815_models.ListVirtualMFADevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListVirtualMFADevicesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListVirtualMFADevicesResponse(),
            await self.do_request_async('ListVirtualMFADevices', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_virtual_mfadevices(
        self,
        request: ims_20190815_models.ListVirtualMFADevicesRequest,
    ) -> ims_20190815_models.ListVirtualMFADevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_virtual_mfadevices_with_options(request, runtime)

    async def list_virtual_mfadevices_async(
        self,
        request: ims_20190815_models.ListVirtualMFADevicesRequest,
    ) -> ims_20190815_models.ListVirtualMFADevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_virtual_mfadevices_with_options_async(request, runtime)

    def list_users_for_group_with_options(
        self,
        request: ims_20190815_models.ListUsersForGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListUsersForGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListUsersForGroupResponse(),
            self.do_request('ListUsersForGroup', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_users_for_group_with_options_async(
        self,
        request: ims_20190815_models.ListUsersForGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListUsersForGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListUsersForGroupResponse(),
            await self.do_request_async('ListUsersForGroup', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_users_for_group(
        self,
        request: ims_20190815_models.ListUsersForGroupRequest,
    ) -> ims_20190815_models.ListUsersForGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_for_group_with_options(request, runtime)

    async def list_users_for_group_async(
        self,
        request: ims_20190815_models.ListUsersForGroupRequest,
    ) -> ims_20190815_models.ListUsersForGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_for_group_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: ims_20190815_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListUsersResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListUsersResponse(),
            self.do_request('ListUsers', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_users_with_options_async(
        self,
        request: ims_20190815_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListUsersResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListUsersResponse(),
            await self.do_request_async('ListUsers', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_users(
        self,
        request: ims_20190815_models.ListUsersRequest,
    ) -> ims_20190815_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: ims_20190815_models.ListUsersRequest,
    ) -> ims_20190815_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def list_samlproviders_with_options(
        self,
        request: ims_20190815_models.ListSAMLProvidersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListSAMLProvidersResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListSAMLProvidersResponse(),
            self.do_request('ListSAMLProviders', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_samlproviders_with_options_async(
        self,
        request: ims_20190815_models.ListSAMLProvidersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListSAMLProvidersResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListSAMLProvidersResponse(),
            await self.do_request_async('ListSAMLProviders', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_samlproviders(
        self,
        request: ims_20190815_models.ListSAMLProvidersRequest,
    ) -> ims_20190815_models.ListSAMLProvidersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_samlproviders_with_options(request, runtime)

    async def list_samlproviders_async(
        self,
        request: ims_20190815_models.ListSAMLProvidersRequest,
    ) -> ims_20190815_models.ListSAMLProvidersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_samlproviders_with_options_async(request, runtime)

    def list_groups_for_user_with_options(
        self,
        request: ims_20190815_models.ListGroupsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListGroupsForUserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListGroupsForUserResponse(),
            self.do_request('ListGroupsForUser', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_groups_for_user_with_options_async(
        self,
        request: ims_20190815_models.ListGroupsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListGroupsForUserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListGroupsForUserResponse(),
            await self.do_request_async('ListGroupsForUser', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_groups_for_user(
        self,
        request: ims_20190815_models.ListGroupsForUserRequest,
    ) -> ims_20190815_models.ListGroupsForUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_groups_for_user_with_options(request, runtime)

    async def list_groups_for_user_async(
        self,
        request: ims_20190815_models.ListGroupsForUserRequest,
    ) -> ims_20190815_models.ListGroupsForUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_groups_for_user_with_options_async(request, runtime)

    def list_groups_with_options(
        self,
        request: ims_20190815_models.ListGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListGroupsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListGroupsResponse(),
            self.do_request('ListGroups', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_groups_with_options_async(
        self,
        request: ims_20190815_models.ListGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListGroupsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListGroupsResponse(),
            await self.do_request_async('ListGroups', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_groups(
        self,
        request: ims_20190815_models.ListGroupsRequest,
    ) -> ims_20190815_models.ListGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_groups_with_options(request, runtime)

    async def list_groups_async(
        self,
        request: ims_20190815_models.ListGroupsRequest,
    ) -> ims_20190815_models.ListGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_groups_with_options_async(request, runtime)

    def list_access_keys_with_options(
        self,
        request: ims_20190815_models.ListAccessKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListAccessKeysResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListAccessKeysResponse(),
            self.do_request('ListAccessKeys', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_access_keys_with_options_async(
        self,
        request: ims_20190815_models.ListAccessKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListAccessKeysResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ListAccessKeysResponse(),
            await self.do_request_async('ListAccessKeys', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_access_keys(
        self,
        request: ims_20190815_models.ListAccessKeysRequest,
    ) -> ims_20190815_models.ListAccessKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_access_keys_with_options(request, runtime)

    async def list_access_keys_async(
        self,
        request: ims_20190815_models.ListAccessKeysRequest,
    ) -> ims_20190815_models.ListAccessKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_access_keys_with_options_async(request, runtime)

    def get_user_mfainfo_with_options(
        self,
        request: ims_20190815_models.GetUserMFAInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetUserMFAInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetUserMFAInfoResponse(),
            self.do_request('GetUserMFAInfo', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_user_mfainfo_with_options_async(
        self,
        request: ims_20190815_models.GetUserMFAInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetUserMFAInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetUserMFAInfoResponse(),
            await self.do_request_async('GetUserMFAInfo', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_user_mfainfo(
        self,
        request: ims_20190815_models.GetUserMFAInfoRequest,
    ) -> ims_20190815_models.GetUserMFAInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_mfainfo_with_options(request, runtime)

    async def get_user_mfainfo_async(
        self,
        request: ims_20190815_models.GetUserMFAInfoRequest,
    ) -> ims_20190815_models.GetUserMFAInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_mfainfo_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: ims_20190815_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetUserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetUserResponse(),
            self.do_request('GetUser', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_user_with_options_async(
        self,
        request: ims_20190815_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetUserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetUserResponse(),
            await self.do_request_async('GetUser', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_user(
        self,
        request: ims_20190815_models.GetUserRequest,
    ) -> ims_20190815_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: ims_20190815_models.GetUserRequest,
    ) -> ims_20190815_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def get_security_preference_with_options(
        self,
        request: ims_20190815_models.GetSecurityPreferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetSecurityPreferenceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetSecurityPreferenceResponse(),
            self.do_request('GetSecurityPreference', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_security_preference_with_options_async(
        self,
        request: ims_20190815_models.GetSecurityPreferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetSecurityPreferenceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetSecurityPreferenceResponse(),
            await self.do_request_async('GetSecurityPreference', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_security_preference(
        self,
        request: ims_20190815_models.GetSecurityPreferenceRequest,
    ) -> ims_20190815_models.GetSecurityPreferenceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_security_preference_with_options(request, runtime)

    async def get_security_preference_async(
        self,
        request: ims_20190815_models.GetSecurityPreferenceRequest,
    ) -> ims_20190815_models.GetSecurityPreferenceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_security_preference_with_options_async(request, runtime)

    def get_samlprovider_with_options(
        self,
        request: ims_20190815_models.GetSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetSAMLProviderResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetSAMLProviderResponse(),
            self.do_request('GetSAMLProvider', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_samlprovider_with_options_async(
        self,
        request: ims_20190815_models.GetSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetSAMLProviderResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetSAMLProviderResponse(),
            await self.do_request_async('GetSAMLProvider', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_samlprovider(
        self,
        request: ims_20190815_models.GetSAMLProviderRequest,
    ) -> ims_20190815_models.GetSAMLProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_samlprovider_with_options(request, runtime)

    async def get_samlprovider_async(
        self,
        request: ims_20190815_models.GetSAMLProviderRequest,
    ) -> ims_20190815_models.GetSAMLProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_samlprovider_with_options_async(request, runtime)

    def get_password_policy_with_options(
        self,
        request: ims_20190815_models.GetPasswordPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetPasswordPolicyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetPasswordPolicyResponse(),
            self.do_request('GetPasswordPolicy', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_password_policy_with_options_async(
        self,
        request: ims_20190815_models.GetPasswordPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetPasswordPolicyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetPasswordPolicyResponse(),
            await self.do_request_async('GetPasswordPolicy', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_password_policy(
        self,
        request: ims_20190815_models.GetPasswordPolicyRequest,
    ) -> ims_20190815_models.GetPasswordPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_password_policy_with_options(request, runtime)

    async def get_password_policy_async(
        self,
        request: ims_20190815_models.GetPasswordPolicyRequest,
    ) -> ims_20190815_models.GetPasswordPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_password_policy_with_options_async(request, runtime)

    def get_login_profile_with_options(
        self,
        request: ims_20190815_models.GetLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetLoginProfileResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetLoginProfileResponse(),
            self.do_request('GetLoginProfile', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_login_profile_with_options_async(
        self,
        request: ims_20190815_models.GetLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetLoginProfileResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetLoginProfileResponse(),
            await self.do_request_async('GetLoginProfile', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_login_profile(
        self,
        request: ims_20190815_models.GetLoginProfileRequest,
    ) -> ims_20190815_models.GetLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_login_profile_with_options(request, runtime)

    async def get_login_profile_async(
        self,
        request: ims_20190815_models.GetLoginProfileRequest,
    ) -> ims_20190815_models.GetLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_login_profile_with_options_async(request, runtime)

    def get_group_with_options(
        self,
        request: ims_20190815_models.GetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetGroupResponse(),
            self.do_request('GetGroup', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_group_with_options_async(
        self,
        request: ims_20190815_models.GetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetGroupResponse(),
            await self.do_request_async('GetGroup', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_group(
        self,
        request: ims_20190815_models.GetGroupRequest,
    ) -> ims_20190815_models.GetGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_group_with_options(request, runtime)

    async def get_group_async(
        self,
        request: ims_20190815_models.GetGroupRequest,
    ) -> ims_20190815_models.GetGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_group_with_options_async(request, runtime)

    def get_default_domain_with_options(
        self,
        request: ims_20190815_models.GetDefaultDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetDefaultDomainResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetDefaultDomainResponse(),
            self.do_request('GetDefaultDomain', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_default_domain_with_options_async(
        self,
        request: ims_20190815_models.GetDefaultDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetDefaultDomainResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetDefaultDomainResponse(),
            await self.do_request_async('GetDefaultDomain', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_default_domain(
        self,
        request: ims_20190815_models.GetDefaultDomainRequest,
    ) -> ims_20190815_models.GetDefaultDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_default_domain_with_options(request, runtime)

    async def get_default_domain_async(
        self,
        request: ims_20190815_models.GetDefaultDomainRequest,
    ) -> ims_20190815_models.GetDefaultDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_default_domain_with_options_async(request, runtime)

    def get_account_summary_with_options(
        self,
        request: ims_20190815_models.GetAccountSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccountSummaryResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetAccountSummaryResponse(),
            self.do_request('GetAccountSummary', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_account_summary_with_options_async(
        self,
        request: ims_20190815_models.GetAccountSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccountSummaryResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetAccountSummaryResponse(),
            await self.do_request_async('GetAccountSummary', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_account_summary(
        self,
        request: ims_20190815_models.GetAccountSummaryRequest,
    ) -> ims_20190815_models.GetAccountSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_account_summary_with_options(request, runtime)

    async def get_account_summary_async(
        self,
        request: ims_20190815_models.GetAccountSummaryRequest,
    ) -> ims_20190815_models.GetAccountSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_account_summary_with_options_async(request, runtime)

    def get_account_security_practice_report_with_options(
        self,
        request: ims_20190815_models.GetAccountSecurityPracticeReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccountSecurityPracticeReportResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetAccountSecurityPracticeReportResponse(),
            self.do_request('GetAccountSecurityPracticeReport', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_account_security_practice_report_with_options_async(
        self,
        request: ims_20190815_models.GetAccountSecurityPracticeReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccountSecurityPracticeReportResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetAccountSecurityPracticeReportResponse(),
            await self.do_request_async('GetAccountSecurityPracticeReport', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_account_security_practice_report(
        self,
        request: ims_20190815_models.GetAccountSecurityPracticeReportRequest,
    ) -> ims_20190815_models.GetAccountSecurityPracticeReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_account_security_practice_report_with_options(request, runtime)

    async def get_account_security_practice_report_async(
        self,
        request: ims_20190815_models.GetAccountSecurityPracticeReportRequest,
    ) -> ims_20190815_models.GetAccountSecurityPracticeReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_account_security_practice_report_with_options_async(request, runtime)

    def get_account_mfainfo_with_options(
        self,
        request: ims_20190815_models.GetAccountMFAInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccountMFAInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetAccountMFAInfoResponse(),
            self.do_request('GetAccountMFAInfo', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_account_mfainfo_with_options_async(
        self,
        request: ims_20190815_models.GetAccountMFAInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccountMFAInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetAccountMFAInfoResponse(),
            await self.do_request_async('GetAccountMFAInfo', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_account_mfainfo(
        self,
        request: ims_20190815_models.GetAccountMFAInfoRequest,
    ) -> ims_20190815_models.GetAccountMFAInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_account_mfainfo_with_options(request, runtime)

    async def get_account_mfainfo_async(
        self,
        request: ims_20190815_models.GetAccountMFAInfoRequest,
    ) -> ims_20190815_models.GetAccountMFAInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_account_mfainfo_with_options_async(request, runtime)

    def get_access_key_last_used_with_options(
        self,
        request: ims_20190815_models.GetAccessKeyLastUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccessKeyLastUsedResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetAccessKeyLastUsedResponse(),
            self.do_request('GetAccessKeyLastUsed', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_access_key_last_used_with_options_async(
        self,
        request: ims_20190815_models.GetAccessKeyLastUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccessKeyLastUsedResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.GetAccessKeyLastUsedResponse(),
            await self.do_request_async('GetAccessKeyLastUsed', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_access_key_last_used(
        self,
        request: ims_20190815_models.GetAccessKeyLastUsedRequest,
    ) -> ims_20190815_models.GetAccessKeyLastUsedResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_access_key_last_used_with_options(request, runtime)

    async def get_access_key_last_used_async(
        self,
        request: ims_20190815_models.GetAccessKeyLastUsedRequest,
    ) -> ims_20190815_models.GetAccessKeyLastUsedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_access_key_last_used_with_options_async(request, runtime)

    def disable_virtual_mfawith_options(
        self,
        request: ims_20190815_models.DisableVirtualMFARequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DisableVirtualMFAResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.DisableVirtualMFAResponse(),
            self.do_request('DisableVirtualMFA', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def disable_virtual_mfawith_options_async(
        self,
        request: ims_20190815_models.DisableVirtualMFARequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DisableVirtualMFAResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.DisableVirtualMFAResponse(),
            await self.do_request_async('DisableVirtualMFA', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def disable_virtual_mfa(
        self,
        request: ims_20190815_models.DisableVirtualMFARequest,
    ) -> ims_20190815_models.DisableVirtualMFAResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_virtual_mfawith_options(request, runtime)

    async def disable_virtual_mfa_async(
        self,
        request: ims_20190815_models.DisableVirtualMFARequest,
    ) -> ims_20190815_models.DisableVirtualMFAResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_virtual_mfawith_options_async(request, runtime)

    def delete_virtual_mfadevice_with_options(
        self,
        request: ims_20190815_models.DeleteVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.DeleteVirtualMFADeviceResponse(),
            self.do_request('DeleteVirtualMFADevice', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_virtual_mfadevice_with_options_async(
        self,
        request: ims_20190815_models.DeleteVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.DeleteVirtualMFADeviceResponse(),
            await self.do_request_async('DeleteVirtualMFADevice', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_virtual_mfadevice(
        self,
        request: ims_20190815_models.DeleteVirtualMFADeviceRequest,
    ) -> ims_20190815_models.DeleteVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_mfadevice_with_options(request, runtime)

    async def delete_virtual_mfadevice_async(
        self,
        request: ims_20190815_models.DeleteVirtualMFADeviceRequest,
    ) -> ims_20190815_models.DeleteVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_virtual_mfadevice_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: ims_20190815_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.DeleteUserResponse(),
            self.do_request('DeleteUser', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: ims_20190815_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.DeleteUserResponse(),
            await self.do_request_async('DeleteUser', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_user(
        self,
        request: ims_20190815_models.DeleteUserRequest,
    ) -> ims_20190815_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: ims_20190815_models.DeleteUserRequest,
    ) -> ims_20190815_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def delete_samlprovider_with_options(
        self,
        request: ims_20190815_models.DeleteSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteSAMLProviderResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.DeleteSAMLProviderResponse(),
            self.do_request('DeleteSAMLProvider', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_samlprovider_with_options_async(
        self,
        request: ims_20190815_models.DeleteSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteSAMLProviderResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.DeleteSAMLProviderResponse(),
            await self.do_request_async('DeleteSAMLProvider', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_samlprovider(
        self,
        request: ims_20190815_models.DeleteSAMLProviderRequest,
    ) -> ims_20190815_models.DeleteSAMLProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_samlprovider_with_options(request, runtime)

    async def delete_samlprovider_async(
        self,
        request: ims_20190815_models.DeleteSAMLProviderRequest,
    ) -> ims_20190815_models.DeleteSAMLProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_samlprovider_with_options_async(request, runtime)

    def delete_login_profile_with_options(
        self,
        request: ims_20190815_models.DeleteLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteLoginProfileResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.DeleteLoginProfileResponse(),
            self.do_request('DeleteLoginProfile', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_login_profile_with_options_async(
        self,
        request: ims_20190815_models.DeleteLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteLoginProfileResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.DeleteLoginProfileResponse(),
            await self.do_request_async('DeleteLoginProfile', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_login_profile(
        self,
        request: ims_20190815_models.DeleteLoginProfileRequest,
    ) -> ims_20190815_models.DeleteLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_login_profile_with_options(request, runtime)

    async def delete_login_profile_async(
        self,
        request: ims_20190815_models.DeleteLoginProfileRequest,
    ) -> ims_20190815_models.DeleteLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_login_profile_with_options_async(request, runtime)

    def delete_group_with_options(
        self,
        request: ims_20190815_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.DeleteGroupResponse(),
            self.do_request('DeleteGroup', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_group_with_options_async(
        self,
        request: ims_20190815_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.DeleteGroupResponse(),
            await self.do_request_async('DeleteGroup', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_group(
        self,
        request: ims_20190815_models.DeleteGroupRequest,
    ) -> ims_20190815_models.DeleteGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    async def delete_group_async(
        self,
        request: ims_20190815_models.DeleteGroupRequest,
    ) -> ims_20190815_models.DeleteGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_group_with_options_async(request, runtime)

    def delete_access_key_with_options(
        self,
        request: ims_20190815_models.DeleteAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteAccessKeyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.DeleteAccessKeyResponse(),
            self.do_request('DeleteAccessKey', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_access_key_with_options_async(
        self,
        request: ims_20190815_models.DeleteAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteAccessKeyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.DeleteAccessKeyResponse(),
            await self.do_request_async('DeleteAccessKey', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_access_key(
        self,
        request: ims_20190815_models.DeleteAccessKeyRequest,
    ) -> ims_20190815_models.DeleteAccessKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_access_key_with_options(request, runtime)

    async def delete_access_key_async(
        self,
        request: ims_20190815_models.DeleteAccessKeyRequest,
    ) -> ims_20190815_models.DeleteAccessKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_access_key_with_options_async(request, runtime)

    def create_virtual_mfadevice_with_options(
        self,
        request: ims_20190815_models.CreateVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.CreateVirtualMFADeviceResponse(),
            self.do_request('CreateVirtualMFADevice', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_virtual_mfadevice_with_options_async(
        self,
        request: ims_20190815_models.CreateVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.CreateVirtualMFADeviceResponse(),
            await self.do_request_async('CreateVirtualMFADevice', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_virtual_mfadevice(
        self,
        request: ims_20190815_models.CreateVirtualMFADeviceRequest,
    ) -> ims_20190815_models.CreateVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_mfadevice_with_options(request, runtime)

    async def create_virtual_mfadevice_async(
        self,
        request: ims_20190815_models.CreateVirtualMFADeviceRequest,
    ) -> ims_20190815_models.CreateVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_virtual_mfadevice_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: ims_20190815_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateUserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.CreateUserResponse(),
            self.do_request('CreateUser', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_user_with_options_async(
        self,
        request: ims_20190815_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateUserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.CreateUserResponse(),
            await self.do_request_async('CreateUser', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_user(
        self,
        request: ims_20190815_models.CreateUserRequest,
    ) -> ims_20190815_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: ims_20190815_models.CreateUserRequest,
    ) -> ims_20190815_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def create_samlprovider_with_options(
        self,
        request: ims_20190815_models.CreateSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateSAMLProviderResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.CreateSAMLProviderResponse(),
            self.do_request('CreateSAMLProvider', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_samlprovider_with_options_async(
        self,
        request: ims_20190815_models.CreateSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateSAMLProviderResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.CreateSAMLProviderResponse(),
            await self.do_request_async('CreateSAMLProvider', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_samlprovider(
        self,
        request: ims_20190815_models.CreateSAMLProviderRequest,
    ) -> ims_20190815_models.CreateSAMLProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_samlprovider_with_options(request, runtime)

    async def create_samlprovider_async(
        self,
        request: ims_20190815_models.CreateSAMLProviderRequest,
    ) -> ims_20190815_models.CreateSAMLProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_samlprovider_with_options_async(request, runtime)

    def create_login_profile_with_options(
        self,
        request: ims_20190815_models.CreateLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateLoginProfileResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.CreateLoginProfileResponse(),
            self.do_request('CreateLoginProfile', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_login_profile_with_options_async(
        self,
        request: ims_20190815_models.CreateLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateLoginProfileResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.CreateLoginProfileResponse(),
            await self.do_request_async('CreateLoginProfile', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_login_profile(
        self,
        request: ims_20190815_models.CreateLoginProfileRequest,
    ) -> ims_20190815_models.CreateLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_login_profile_with_options(request, runtime)

    async def create_login_profile_async(
        self,
        request: ims_20190815_models.CreateLoginProfileRequest,
    ) -> ims_20190815_models.CreateLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_login_profile_with_options_async(request, runtime)

    def create_group_with_options(
        self,
        request: ims_20190815_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.CreateGroupResponse(),
            self.do_request('CreateGroup', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_group_with_options_async(
        self,
        request: ims_20190815_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.CreateGroupResponse(),
            await self.do_request_async('CreateGroup', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_group(
        self,
        request: ims_20190815_models.CreateGroupRequest,
    ) -> ims_20190815_models.CreateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    async def create_group_async(
        self,
        request: ims_20190815_models.CreateGroupRequest,
    ) -> ims_20190815_models.CreateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_group_with_options_async(request, runtime)

    def create_access_key_with_options(
        self,
        request: ims_20190815_models.CreateAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateAccessKeyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.CreateAccessKeyResponse(),
            self.do_request('CreateAccessKey', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_access_key_with_options_async(
        self,
        request: ims_20190815_models.CreateAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateAccessKeyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.CreateAccessKeyResponse(),
            await self.do_request_async('CreateAccessKey', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_access_key(
        self,
        request: ims_20190815_models.CreateAccessKeyRequest,
    ) -> ims_20190815_models.CreateAccessKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_access_key_with_options(request, runtime)

    async def create_access_key_async(
        self,
        request: ims_20190815_models.CreateAccessKeyRequest,
    ) -> ims_20190815_models.CreateAccessKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_access_key_with_options_async(request, runtime)

    def change_password_with_options(
        self,
        request: ims_20190815_models.ChangePasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ChangePasswordResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ChangePasswordResponse(),
            self.do_request('ChangePassword', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def change_password_with_options_async(
        self,
        request: ims_20190815_models.ChangePasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ChangePasswordResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.ChangePasswordResponse(),
            await self.do_request_async('ChangePassword', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def change_password(
        self,
        request: ims_20190815_models.ChangePasswordRequest,
    ) -> ims_20190815_models.ChangePasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_password_with_options(request, runtime)

    async def change_password_async(
        self,
        request: ims_20190815_models.ChangePasswordRequest,
    ) -> ims_20190815_models.ChangePasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_password_with_options_async(request, runtime)

    def bind_mfadevice_with_options(
        self,
        request: ims_20190815_models.BindMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.BindMFADeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.BindMFADeviceResponse(),
            self.do_request('BindMFADevice', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def bind_mfadevice_with_options_async(
        self,
        request: ims_20190815_models.BindMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.BindMFADeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.BindMFADeviceResponse(),
            await self.do_request_async('BindMFADevice', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def bind_mfadevice(
        self,
        request: ims_20190815_models.BindMFADeviceRequest,
    ) -> ims_20190815_models.BindMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_mfadevice_with_options(request, runtime)

    async def bind_mfadevice_async(
        self,
        request: ims_20190815_models.BindMFADeviceRequest,
    ) -> ims_20190815_models.BindMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_mfadevice_with_options_async(request, runtime)

    def add_user_to_group_with_options(
        self,
        request: ims_20190815_models.AddUserToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.AddUserToGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.AddUserToGroupResponse(),
            self.do_request('AddUserToGroup', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def add_user_to_group_with_options_async(
        self,
        request: ims_20190815_models.AddUserToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.AddUserToGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ims_20190815_models.AddUserToGroupResponse(),
            await self.do_request_async('AddUserToGroup', 'HTTPS', 'POST', '2019-08-15', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def add_user_to_group(
        self,
        request: ims_20190815_models.AddUserToGroupRequest,
    ) -> ims_20190815_models.AddUserToGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_group_with_options(request, runtime)

    async def add_user_to_group_async(
        self,
        request: ims_20190815_models.AddUserToGroupRequest,
    ) -> ims_20190815_models.AddUserToGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_user_to_group_with_options_async(request, runtime)

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
