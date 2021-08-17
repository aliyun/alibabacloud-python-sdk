# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_hcs_mgw20171024 import models as hcs_mgw_20171024_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('hcs-mgw', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def check_import_data_address_with_options(
        self,
        request: hcs_mgw_20171024_models.CheckImportDataAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CheckImportDataAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CheckImportDataAddressResponse(),
            self.do_rpcrequest('CheckImportDataAddress', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_import_data_address_with_options_async(
        self,
        request: hcs_mgw_20171024_models.CheckImportDataAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CheckImportDataAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CheckImportDataAddressResponse(),
            await self.do_rpcrequest_async('CheckImportDataAddress', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_import_data_address(
        self,
        request: hcs_mgw_20171024_models.CheckImportDataAddressRequest,
    ) -> hcs_mgw_20171024_models.CheckImportDataAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_import_data_address_with_options(request, runtime)

    async def check_import_data_address_async(
        self,
        request: hcs_mgw_20171024_models.CheckImportDataAddressRequest,
    ) -> hcs_mgw_20171024_models.CheckImportDataAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_import_data_address_with_options_async(request, runtime)

    def check_import_data_address_ex_with_options(
        self,
        request: hcs_mgw_20171024_models.CheckImportDataAddressExRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CheckImportDataAddressExResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CheckImportDataAddressExResponse(),
            self.do_rpcrequest('CheckImportDataAddressEx', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_import_data_address_ex_with_options_async(
        self,
        request: hcs_mgw_20171024_models.CheckImportDataAddressExRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CheckImportDataAddressExResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CheckImportDataAddressExResponse(),
            await self.do_rpcrequest_async('CheckImportDataAddressEx', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_import_data_address_ex(
        self,
        request: hcs_mgw_20171024_models.CheckImportDataAddressExRequest,
    ) -> hcs_mgw_20171024_models.CheckImportDataAddressExResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_import_data_address_ex_with_options(request, runtime)

    async def check_import_data_address_ex_async(
        self,
        request: hcs_mgw_20171024_models.CheckImportDataAddressExRequest,
    ) -> hcs_mgw_20171024_models.CheckImportDataAddressExResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_import_data_address_ex_with_options_async(request, runtime)

    def check_migration_license_with_options(
        self,
        request: hcs_mgw_20171024_models.CheckMigrationLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CheckMigrationLicenseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CheckMigrationLicenseResponse(),
            self.do_rpcrequest('CheckMigrationLicense', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_migration_license_with_options_async(
        self,
        request: hcs_mgw_20171024_models.CheckMigrationLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CheckMigrationLicenseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CheckMigrationLicenseResponse(),
            await self.do_rpcrequest_async('CheckMigrationLicense', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_migration_license(
        self,
        request: hcs_mgw_20171024_models.CheckMigrationLicenseRequest,
    ) -> hcs_mgw_20171024_models.CheckMigrationLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_migration_license_with_options(request, runtime)

    async def check_migration_license_async(
        self,
        request: hcs_mgw_20171024_models.CheckMigrationLicenseRequest,
    ) -> hcs_mgw_20171024_models.CheckMigrationLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_migration_license_with_options_async(request, runtime)

    def check_role_with_options(
        self,
        request: hcs_mgw_20171024_models.CheckRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CheckRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CheckRoleResponse(),
            self.do_rpcrequest('CheckRole', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_role_with_options_async(
        self,
        request: hcs_mgw_20171024_models.CheckRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CheckRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CheckRoleResponse(),
            await self.do_rpcrequest_async('CheckRole', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_role(
        self,
        request: hcs_mgw_20171024_models.CheckRoleRequest,
    ) -> hcs_mgw_20171024_models.CheckRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_role_with_options(request, runtime)

    async def check_role_async(
        self,
        request: hcs_mgw_20171024_models.CheckRoleRequest,
    ) -> hcs_mgw_20171024_models.CheckRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_role_with_options_async(request, runtime)

    def create_data_address_with_options(
        self,
        request: hcs_mgw_20171024_models.CreateDataAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CreateDataAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CreateDataAddressResponse(),
            self.do_rpcrequest('CreateDataAddress', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_data_address_with_options_async(
        self,
        request: hcs_mgw_20171024_models.CreateDataAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CreateDataAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CreateDataAddressResponse(),
            await self.do_rpcrequest_async('CreateDataAddress', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_data_address(
        self,
        request: hcs_mgw_20171024_models.CreateDataAddressRequest,
    ) -> hcs_mgw_20171024_models.CreateDataAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_data_address_with_options(request, runtime)

    async def create_data_address_async(
        self,
        request: hcs_mgw_20171024_models.CreateDataAddressRequest,
    ) -> hcs_mgw_20171024_models.CreateDataAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_data_address_with_options_async(request, runtime)

    def create_import_job_with_options(
        self,
        request: hcs_mgw_20171024_models.CreateImportJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CreateImportJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CreateImportJobResponse(),
            self.do_rpcrequest('CreateImportJob', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_import_job_with_options_async(
        self,
        request: hcs_mgw_20171024_models.CreateImportJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CreateImportJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CreateImportJobResponse(),
            await self.do_rpcrequest_async('CreateImportJob', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_import_job(
        self,
        request: hcs_mgw_20171024_models.CreateImportJobRequest,
    ) -> hcs_mgw_20171024_models.CreateImportJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_import_job_with_options(request, runtime)

    async def create_import_job_async(
        self,
        request: hcs_mgw_20171024_models.CreateImportJobRequest,
    ) -> hcs_mgw_20171024_models.CreateImportJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_import_job_with_options_async(request, runtime)

    def create_import_job_ex_with_options(
        self,
        request: hcs_mgw_20171024_models.CreateImportJobExRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CreateImportJobExResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CreateImportJobExResponse(),
            self.do_rpcrequest('CreateImportJobEx', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_import_job_ex_with_options_async(
        self,
        request: hcs_mgw_20171024_models.CreateImportJobExRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CreateImportJobExResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CreateImportJobExResponse(),
            await self.do_rpcrequest_async('CreateImportJobEx', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_import_job_ex(
        self,
        request: hcs_mgw_20171024_models.CreateImportJobExRequest,
    ) -> hcs_mgw_20171024_models.CreateImportJobExResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_import_job_ex_with_options(request, runtime)

    async def create_import_job_ex_async(
        self,
        request: hcs_mgw_20171024_models.CreateImportJobExRequest,
    ) -> hcs_mgw_20171024_models.CreateImportJobExResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_import_job_ex_with_options_async(request, runtime)

    def create_import_report_with_options(
        self,
        request: hcs_mgw_20171024_models.CreateImportReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CreateImportReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CreateImportReportResponse(),
            self.do_rpcrequest('CreateImportReport', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_import_report_with_options_async(
        self,
        request: hcs_mgw_20171024_models.CreateImportReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CreateImportReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CreateImportReportResponse(),
            await self.do_rpcrequest_async('CreateImportReport', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_import_report(
        self,
        request: hcs_mgw_20171024_models.CreateImportReportRequest,
    ) -> hcs_mgw_20171024_models.CreateImportReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_import_report_with_options(request, runtime)

    async def create_import_report_async(
        self,
        request: hcs_mgw_20171024_models.CreateImportReportRequest,
    ) -> hcs_mgw_20171024_models.CreateImportReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_import_report_with_options_async(request, runtime)

    def create_job_with_options(
        self,
        request: hcs_mgw_20171024_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CreateJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CreateJobResponse(),
            self.do_rpcrequest('CreateJob', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_job_with_options_async(
        self,
        request: hcs_mgw_20171024_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CreateJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CreateJobResponse(),
            await self.do_rpcrequest_async('CreateJob', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_job(
        self,
        request: hcs_mgw_20171024_models.CreateJobRequest,
    ) -> hcs_mgw_20171024_models.CreateJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_job_with_options(request, runtime)

    async def create_job_async(
        self,
        request: hcs_mgw_20171024_models.CreateJobRequest,
    ) -> hcs_mgw_20171024_models.CreateJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_job_with_options_async(request, runtime)

    def create_migration_license_with_options(
        self,
        request: hcs_mgw_20171024_models.CreateMigrationLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CreateMigrationLicenseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CreateMigrationLicenseResponse(),
            self.do_rpcrequest('CreateMigrationLicense', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_migration_license_with_options_async(
        self,
        request: hcs_mgw_20171024_models.CreateMigrationLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CreateMigrationLicenseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CreateMigrationLicenseResponse(),
            await self.do_rpcrequest_async('CreateMigrationLicense', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_migration_license(
        self,
        request: hcs_mgw_20171024_models.CreateMigrationLicenseRequest,
    ) -> hcs_mgw_20171024_models.CreateMigrationLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_migration_license_with_options(request, runtime)

    async def create_migration_license_async(
        self,
        request: hcs_mgw_20171024_models.CreateMigrationLicenseRequest,
    ) -> hcs_mgw_20171024_models.CreateMigrationLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_migration_license_with_options_async(request, runtime)

    def create_mover_with_options(
        self,
        request: hcs_mgw_20171024_models.CreateMoverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CreateMoverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CreateMoverResponse(),
            self.do_rpcrequest('CreateMover', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_mover_with_options_async(
        self,
        request: hcs_mgw_20171024_models.CreateMoverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CreateMoverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CreateMoverResponse(),
            await self.do_rpcrequest_async('CreateMover', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_mover(
        self,
        request: hcs_mgw_20171024_models.CreateMoverRequest,
    ) -> hcs_mgw_20171024_models.CreateMoverResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_mover_with_options(request, runtime)

    async def create_mover_async(
        self,
        request: hcs_mgw_20171024_models.CreateMoverRequest,
    ) -> hcs_mgw_20171024_models.CreateMoverResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_mover_with_options_async(request, runtime)

    def create_order_with_options(
        self,
        request: hcs_mgw_20171024_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CreateOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CreateOrderResponse(),
            self.do_rpcrequest('CreateOrder', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_order_with_options_async(
        self,
        request: hcs_mgw_20171024_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CreateOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CreateOrderResponse(),
            await self.do_rpcrequest_async('CreateOrder', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_order(
        self,
        request: hcs_mgw_20171024_models.CreateOrderRequest,
    ) -> hcs_mgw_20171024_models.CreateOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_order_with_options(request, runtime)

    async def create_order_async(
        self,
        request: hcs_mgw_20171024_models.CreateOrderRequest,
    ) -> hcs_mgw_20171024_models.CreateOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_order_with_options_async(request, runtime)

    def create_remote_with_options(
        self,
        request: hcs_mgw_20171024_models.CreateRemoteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CreateRemoteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CreateRemoteResponse(),
            self.do_rpcrequest('CreateRemote', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_remote_with_options_async(
        self,
        request: hcs_mgw_20171024_models.CreateRemoteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CreateRemoteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CreateRemoteResponse(),
            await self.do_rpcrequest_async('CreateRemote', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_remote(
        self,
        request: hcs_mgw_20171024_models.CreateRemoteRequest,
    ) -> hcs_mgw_20171024_models.CreateRemoteResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_remote_with_options(request, runtime)

    async def create_remote_async(
        self,
        request: hcs_mgw_20171024_models.CreateRemoteRequest,
    ) -> hcs_mgw_20171024_models.CreateRemoteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_remote_with_options_async(request, runtime)

    def create_virtual_cluster_with_options(
        self,
        request: hcs_mgw_20171024_models.CreateVirtualClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CreateVirtualClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CreateVirtualClusterResponse(),
            self.do_rpcrequest('CreateVirtualCluster', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_virtual_cluster_with_options_async(
        self,
        request: hcs_mgw_20171024_models.CreateVirtualClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.CreateVirtualClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.CreateVirtualClusterResponse(),
            await self.do_rpcrequest_async('CreateVirtualCluster', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_virtual_cluster(
        self,
        request: hcs_mgw_20171024_models.CreateVirtualClusterRequest,
    ) -> hcs_mgw_20171024_models.CreateVirtualClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_cluster_with_options(request, runtime)

    async def create_virtual_cluster_async(
        self,
        request: hcs_mgw_20171024_models.CreateVirtualClusterRequest,
    ) -> hcs_mgw_20171024_models.CreateVirtualClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_virtual_cluster_with_options_async(request, runtime)

    def delete_data_address_with_options(
        self,
        request: hcs_mgw_20171024_models.DeleteDataAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DeleteDataAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DeleteDataAddressResponse(),
            self.do_rpcrequest('DeleteDataAddress', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_data_address_with_options_async(
        self,
        request: hcs_mgw_20171024_models.DeleteDataAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DeleteDataAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DeleteDataAddressResponse(),
            await self.do_rpcrequest_async('DeleteDataAddress', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_data_address(
        self,
        request: hcs_mgw_20171024_models.DeleteDataAddressRequest,
    ) -> hcs_mgw_20171024_models.DeleteDataAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_data_address_with_options(request, runtime)

    async def delete_data_address_async(
        self,
        request: hcs_mgw_20171024_models.DeleteDataAddressRequest,
    ) -> hcs_mgw_20171024_models.DeleteDataAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_address_with_options_async(request, runtime)

    def delete_import_job_with_options(
        self,
        request: hcs_mgw_20171024_models.DeleteImportJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DeleteImportJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DeleteImportJobResponse(),
            self.do_rpcrequest('DeleteImportJob', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_import_job_with_options_async(
        self,
        request: hcs_mgw_20171024_models.DeleteImportJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DeleteImportJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DeleteImportJobResponse(),
            await self.do_rpcrequest_async('DeleteImportJob', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_import_job(
        self,
        request: hcs_mgw_20171024_models.DeleteImportJobRequest,
    ) -> hcs_mgw_20171024_models.DeleteImportJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_import_job_with_options(request, runtime)

    async def delete_import_job_async(
        self,
        request: hcs_mgw_20171024_models.DeleteImportJobRequest,
    ) -> hcs_mgw_20171024_models.DeleteImportJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_import_job_with_options_async(request, runtime)

    def delete_job_with_options(
        self,
        request: hcs_mgw_20171024_models.DeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DeleteJobResponse(),
            self.do_rpcrequest('DeleteJob', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_job_with_options_async(
        self,
        request: hcs_mgw_20171024_models.DeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DeleteJobResponse(),
            await self.do_rpcrequest_async('DeleteJob', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_job(
        self,
        request: hcs_mgw_20171024_models.DeleteJobRequest,
    ) -> hcs_mgw_20171024_models.DeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_job_with_options(request, runtime)

    async def delete_job_async(
        self,
        request: hcs_mgw_20171024_models.DeleteJobRequest,
    ) -> hcs_mgw_20171024_models.DeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_job_with_options_async(request, runtime)

    def delete_mover_with_options(
        self,
        request: hcs_mgw_20171024_models.DeleteMoverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DeleteMoverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DeleteMoverResponse(),
            self.do_rpcrequest('DeleteMover', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_mover_with_options_async(
        self,
        request: hcs_mgw_20171024_models.DeleteMoverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DeleteMoverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DeleteMoverResponse(),
            await self.do_rpcrequest_async('DeleteMover', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_mover(
        self,
        request: hcs_mgw_20171024_models.DeleteMoverRequest,
    ) -> hcs_mgw_20171024_models.DeleteMoverResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_mover_with_options(request, runtime)

    async def delete_mover_async(
        self,
        request: hcs_mgw_20171024_models.DeleteMoverRequest,
    ) -> hcs_mgw_20171024_models.DeleteMoverResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_mover_with_options_async(request, runtime)

    def describe_bucket_folders_with_options(
        self,
        request: hcs_mgw_20171024_models.DescribeBucketFoldersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeBucketFoldersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeBucketFoldersResponse(),
            self.do_rpcrequest('DescribeBucketFolders', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_bucket_folders_with_options_async(
        self,
        request: hcs_mgw_20171024_models.DescribeBucketFoldersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeBucketFoldersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeBucketFoldersResponse(),
            await self.do_rpcrequest_async('DescribeBucketFolders', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_bucket_folders(
        self,
        request: hcs_mgw_20171024_models.DescribeBucketFoldersRequest,
    ) -> hcs_mgw_20171024_models.DescribeBucketFoldersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_bucket_folders_with_options(request, runtime)

    async def describe_bucket_folders_async(
        self,
        request: hcs_mgw_20171024_models.DescribeBucketFoldersRequest,
    ) -> hcs_mgw_20171024_models.DescribeBucketFoldersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_bucket_folders_with_options_async(request, runtime)

    def describe_buckets_with_options(
        self,
        request: hcs_mgw_20171024_models.DescribeBucketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeBucketsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeBucketsResponse(),
            self.do_rpcrequest('DescribeBuckets', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_buckets_with_options_async(
        self,
        request: hcs_mgw_20171024_models.DescribeBucketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeBucketsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeBucketsResponse(),
            await self.do_rpcrequest_async('DescribeBuckets', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_buckets(
        self,
        request: hcs_mgw_20171024_models.DescribeBucketsRequest,
    ) -> hcs_mgw_20171024_models.DescribeBucketsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_buckets_with_options(request, runtime)

    async def describe_buckets_async(
        self,
        request: hcs_mgw_20171024_models.DescribeBucketsRequest,
    ) -> hcs_mgw_20171024_models.DescribeBucketsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_buckets_with_options_async(request, runtime)

    def describe_data_addresses_with_options(
        self,
        request: hcs_mgw_20171024_models.DescribeDataAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeDataAddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeDataAddressesResponse(),
            self.do_rpcrequest('DescribeDataAddresses', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_data_addresses_with_options_async(
        self,
        request: hcs_mgw_20171024_models.DescribeDataAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeDataAddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeDataAddressesResponse(),
            await self.do_rpcrequest_async('DescribeDataAddresses', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_addresses(
        self,
        request: hcs_mgw_20171024_models.DescribeDataAddressesRequest,
    ) -> hcs_mgw_20171024_models.DescribeDataAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_addresses_with_options(request, runtime)

    async def describe_data_addresses_async(
        self,
        request: hcs_mgw_20171024_models.DescribeDataAddressesRequest,
    ) -> hcs_mgw_20171024_models.DescribeDataAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_addresses_with_options_async(request, runtime)

    def describe_import_jobs_with_options(
        self,
        request: hcs_mgw_20171024_models.DescribeImportJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeImportJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeImportJobsResponse(),
            self.do_rpcrequest('DescribeImportJobs', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_import_jobs_with_options_async(
        self,
        request: hcs_mgw_20171024_models.DescribeImportJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeImportJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeImportJobsResponse(),
            await self.do_rpcrequest_async('DescribeImportJobs', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_import_jobs(
        self,
        request: hcs_mgw_20171024_models.DescribeImportJobsRequest,
    ) -> hcs_mgw_20171024_models.DescribeImportJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_import_jobs_with_options(request, runtime)

    async def describe_import_jobs_async(
        self,
        request: hcs_mgw_20171024_models.DescribeImportJobsRequest,
    ) -> hcs_mgw_20171024_models.DescribeImportJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_import_jobs_with_options_async(request, runtime)

    def describe_import_report_with_options(
        self,
        request: hcs_mgw_20171024_models.DescribeImportReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeImportReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeImportReportResponse(),
            self.do_rpcrequest('DescribeImportReport', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_import_report_with_options_async(
        self,
        request: hcs_mgw_20171024_models.DescribeImportReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeImportReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeImportReportResponse(),
            await self.do_rpcrequest_async('DescribeImportReport', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_import_report(
        self,
        request: hcs_mgw_20171024_models.DescribeImportReportRequest,
    ) -> hcs_mgw_20171024_models.DescribeImportReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_import_report_with_options(request, runtime)

    async def describe_import_report_async(
        self,
        request: hcs_mgw_20171024_models.DescribeImportReportRequest,
    ) -> hcs_mgw_20171024_models.DescribeImportReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_import_report_with_options_async(request, runtime)

    def describe_jobs_with_options(
        self,
        request: hcs_mgw_20171024_models.DescribeJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeJobsResponse(),
            self.do_rpcrequest('DescribeJobs', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_jobs_with_options_async(
        self,
        request: hcs_mgw_20171024_models.DescribeJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeJobsResponse(),
            await self.do_rpcrequest_async('DescribeJobs', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_jobs(
        self,
        request: hcs_mgw_20171024_models.DescribeJobsRequest,
    ) -> hcs_mgw_20171024_models.DescribeJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_jobs_with_options(request, runtime)

    async def describe_jobs_async(
        self,
        request: hcs_mgw_20171024_models.DescribeJobsRequest,
    ) -> hcs_mgw_20171024_models.DescribeJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_jobs_with_options_async(request, runtime)

    def describe_migration_orders_with_options(
        self,
        request: hcs_mgw_20171024_models.DescribeMigrationOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeMigrationOrdersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeMigrationOrdersResponse(),
            self.do_rpcrequest('DescribeMigrationOrders', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_migration_orders_with_options_async(
        self,
        request: hcs_mgw_20171024_models.DescribeMigrationOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeMigrationOrdersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeMigrationOrdersResponse(),
            await self.do_rpcrequest_async('DescribeMigrationOrders', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_migration_orders(
        self,
        request: hcs_mgw_20171024_models.DescribeMigrationOrdersRequest,
    ) -> hcs_mgw_20171024_models.DescribeMigrationOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_orders_with_options(request, runtime)

    async def describe_migration_orders_async(
        self,
        request: hcs_mgw_20171024_models.DescribeMigrationOrdersRequest,
    ) -> hcs_mgw_20171024_models.DescribeMigrationOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_migration_orders_with_options_async(request, runtime)

    def describe_mover_attribute_with_options(
        self,
        request: hcs_mgw_20171024_models.DescribeMoverAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeMoverAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeMoverAttributeResponse(),
            self.do_rpcrequest('DescribeMoverAttribute', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_mover_attribute_with_options_async(
        self,
        request: hcs_mgw_20171024_models.DescribeMoverAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeMoverAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeMoverAttributeResponse(),
            await self.do_rpcrequest_async('DescribeMoverAttribute', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_mover_attribute(
        self,
        request: hcs_mgw_20171024_models.DescribeMoverAttributeRequest,
    ) -> hcs_mgw_20171024_models.DescribeMoverAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mover_attribute_with_options(request, runtime)

    async def describe_mover_attribute_async(
        self,
        request: hcs_mgw_20171024_models.DescribeMoverAttributeRequest,
    ) -> hcs_mgw_20171024_models.DescribeMoverAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mover_attribute_with_options_async(request, runtime)

    def describe_movers_with_options(
        self,
        request: hcs_mgw_20171024_models.DescribeMoversRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeMoversResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeMoversResponse(),
            self.do_rpcrequest('DescribeMovers', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_movers_with_options_async(
        self,
        request: hcs_mgw_20171024_models.DescribeMoversRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeMoversResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeMoversResponse(),
            await self.do_rpcrequest_async('DescribeMovers', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_movers(
        self,
        request: hcs_mgw_20171024_models.DescribeMoversRequest,
    ) -> hcs_mgw_20171024_models.DescribeMoversResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_movers_with_options(request, runtime)

    async def describe_movers_async(
        self,
        request: hcs_mgw_20171024_models.DescribeMoversRequest,
    ) -> hcs_mgw_20171024_models.DescribeMoversResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_movers_with_options_async(request, runtime)

    def describe_offline_cluster_with_options(
        self,
        request: hcs_mgw_20171024_models.DescribeOfflineClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeOfflineClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeOfflineClusterResponse(),
            self.do_rpcrequest('DescribeOfflineCluster', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_offline_cluster_with_options_async(
        self,
        request: hcs_mgw_20171024_models.DescribeOfflineClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeOfflineClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeOfflineClusterResponse(),
            await self.do_rpcrequest_async('DescribeOfflineCluster', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_offline_cluster(
        self,
        request: hcs_mgw_20171024_models.DescribeOfflineClusterRequest,
    ) -> hcs_mgw_20171024_models.DescribeOfflineClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_offline_cluster_with_options(request, runtime)

    async def describe_offline_cluster_async(
        self,
        request: hcs_mgw_20171024_models.DescribeOfflineClusterRequest,
    ) -> hcs_mgw_20171024_models.DescribeOfflineClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_offline_cluster_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeRegionsResponse(),
            await self.do_rpcrequest_async('DescribeRegions', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self) -> hcs_mgw_20171024_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    async def describe_regions_async(self) -> hcs_mgw_20171024_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(runtime)

    def describe_remotes_with_options(
        self,
        request: hcs_mgw_20171024_models.DescribeRemotesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeRemotesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeRemotesResponse(),
            self.do_rpcrequest('DescribeRemotes', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_remotes_with_options_async(
        self,
        request: hcs_mgw_20171024_models.DescribeRemotesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeRemotesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeRemotesResponse(),
            await self.do_rpcrequest_async('DescribeRemotes', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_remotes(
        self,
        request: hcs_mgw_20171024_models.DescribeRemotesRequest,
    ) -> hcs_mgw_20171024_models.DescribeRemotesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_remotes_with_options(request, runtime)

    async def describe_remotes_async(
        self,
        request: hcs_mgw_20171024_models.DescribeRemotesRequest,
    ) -> hcs_mgw_20171024_models.DescribeRemotesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_remotes_with_options_async(request, runtime)

    def describe_user_business_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeUserBusinessStatusResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeUserBusinessStatusResponse(),
            self.do_rpcrequest('DescribeUserBusinessStatus', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_business_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeUserBusinessStatusResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeUserBusinessStatusResponse(),
            await self.do_rpcrequest_async('DescribeUserBusinessStatus', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_business_status(self) -> hcs_mgw_20171024_models.DescribeUserBusinessStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_business_status_with_options(runtime)

    async def describe_user_business_status_async(self) -> hcs_mgw_20171024_models.DescribeUserBusinessStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_business_status_with_options_async(runtime)

    def describe_user_options_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeUserOptionsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeUserOptionsResponse(),
            self.do_rpcrequest('DescribeUserOptions', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_options_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.DescribeUserOptionsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            hcs_mgw_20171024_models.DescribeUserOptionsResponse(),
            await self.do_rpcrequest_async('DescribeUserOptions', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_options(self) -> hcs_mgw_20171024_models.DescribeUserOptionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_options_with_options(runtime)

    async def describe_user_options_async(self) -> hcs_mgw_20171024_models.DescribeUserOptionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_options_with_options_async(runtime)

    def get_data_address_with_options(
        self,
        request: hcs_mgw_20171024_models.GetDataAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.GetDataAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.GetDataAddressResponse(),
            self.do_rpcrequest('GetDataAddress', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_data_address_with_options_async(
        self,
        request: hcs_mgw_20171024_models.GetDataAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.GetDataAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.GetDataAddressResponse(),
            await self.do_rpcrequest_async('GetDataAddress', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_address(
        self,
        request: hcs_mgw_20171024_models.GetDataAddressRequest,
    ) -> hcs_mgw_20171024_models.GetDataAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_data_address_with_options(request, runtime)

    async def get_data_address_async(
        self,
        request: hcs_mgw_20171024_models.GetDataAddressRequest,
    ) -> hcs_mgw_20171024_models.GetDataAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_data_address_with_options_async(request, runtime)

    def get_import_job_detailed_status_with_options(
        self,
        request: hcs_mgw_20171024_models.GetImportJobDetailedStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.GetImportJobDetailedStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.GetImportJobDetailedStatusResponse(),
            self.do_rpcrequest('GetImportJobDetailedStatus', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_import_job_detailed_status_with_options_async(
        self,
        request: hcs_mgw_20171024_models.GetImportJobDetailedStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.GetImportJobDetailedStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.GetImportJobDetailedStatusResponse(),
            await self.do_rpcrequest_async('GetImportJobDetailedStatus', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_import_job_detailed_status(
        self,
        request: hcs_mgw_20171024_models.GetImportJobDetailedStatusRequest,
    ) -> hcs_mgw_20171024_models.GetImportJobDetailedStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_import_job_detailed_status_with_options(request, runtime)

    async def get_import_job_detailed_status_async(
        self,
        request: hcs_mgw_20171024_models.GetImportJobDetailedStatusRequest,
    ) -> hcs_mgw_20171024_models.GetImportJobDetailedStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_import_job_detailed_status_with_options_async(request, runtime)

    def get_import_job_status_with_options(
        self,
        request: hcs_mgw_20171024_models.GetImportJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.GetImportJobStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.GetImportJobStatusResponse(),
            self.do_rpcrequest('GetImportJobStatus', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_import_job_status_with_options_async(
        self,
        request: hcs_mgw_20171024_models.GetImportJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.GetImportJobStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.GetImportJobStatusResponse(),
            await self.do_rpcrequest_async('GetImportJobStatus', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_import_job_status(
        self,
        request: hcs_mgw_20171024_models.GetImportJobStatusRequest,
    ) -> hcs_mgw_20171024_models.GetImportJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_import_job_status_with_options(request, runtime)

    async def get_import_job_status_async(
        self,
        request: hcs_mgw_20171024_models.GetImportJobStatusRequest,
    ) -> hcs_mgw_20171024_models.GetImportJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_import_job_status_with_options_async(request, runtime)

    def get_import_report_status_with_options(
        self,
        request: hcs_mgw_20171024_models.GetImportReportStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.GetImportReportStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.GetImportReportStatusResponse(),
            self.do_rpcrequest('GetImportReportStatus', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_import_report_status_with_options_async(
        self,
        request: hcs_mgw_20171024_models.GetImportReportStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.GetImportReportStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.GetImportReportStatusResponse(),
            await self.do_rpcrequest_async('GetImportReportStatus', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_import_report_status(
        self,
        request: hcs_mgw_20171024_models.GetImportReportStatusRequest,
    ) -> hcs_mgw_20171024_models.GetImportReportStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_import_report_status_with_options(request, runtime)

    async def get_import_report_status_async(
        self,
        request: hcs_mgw_20171024_models.GetImportReportStatusRequest,
    ) -> hcs_mgw_20171024_models.GetImportReportStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_import_report_status_with_options_async(request, runtime)

    def get_lightning_cube_installer_url_with_options(
        self,
        request: hcs_mgw_20171024_models.GetLightningCubeInstallerUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.GetLightningCubeInstallerUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.GetLightningCubeInstallerUrlResponse(),
            self.do_rpcrequest('GetLightningCubeInstallerUrl', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_lightning_cube_installer_url_with_options_async(
        self,
        request: hcs_mgw_20171024_models.GetLightningCubeInstallerUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.GetLightningCubeInstallerUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.GetLightningCubeInstallerUrlResponse(),
            await self.do_rpcrequest_async('GetLightningCubeInstallerUrl', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_lightning_cube_installer_url(
        self,
        request: hcs_mgw_20171024_models.GetLightningCubeInstallerUrlRequest,
    ) -> hcs_mgw_20171024_models.GetLightningCubeInstallerUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_lightning_cube_installer_url_with_options(request, runtime)

    async def get_lightning_cube_installer_url_async(
        self,
        request: hcs_mgw_20171024_models.GetLightningCubeInstallerUrlRequest,
    ) -> hcs_mgw_20171024_models.GetLightningCubeInstallerUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_lightning_cube_installer_url_with_options_async(request, runtime)

    def get_sls_token_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.GetSlsTokenResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            hcs_mgw_20171024_models.GetSlsTokenResponse(),
            self.do_rpcrequest('GetSlsToken', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_sls_token_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.GetSlsTokenResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            hcs_mgw_20171024_models.GetSlsTokenResponse(),
            await self.do_rpcrequest_async('GetSlsToken', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_sls_token(self) -> hcs_mgw_20171024_models.GetSlsTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sls_token_with_options(runtime)

    async def get_sls_token_async(self) -> hcs_mgw_20171024_models.GetSlsTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sls_token_with_options_async(runtime)

    def get_support_import_data_address_type_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.GetSupportImportDataAddressTypeResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            hcs_mgw_20171024_models.GetSupportImportDataAddressTypeResponse(),
            self.do_rpcrequest('GetSupportImportDataAddressType', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_support_import_data_address_type_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.GetSupportImportDataAddressTypeResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            hcs_mgw_20171024_models.GetSupportImportDataAddressTypeResponse(),
            await self.do_rpcrequest_async('GetSupportImportDataAddressType', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_support_import_data_address_type(self) -> hcs_mgw_20171024_models.GetSupportImportDataAddressTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_support_import_data_address_type_with_options(runtime)

    async def get_support_import_data_address_type_async(self) -> hcs_mgw_20171024_models.GetSupportImportDataAddressTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_support_import_data_address_type_with_options_async(runtime)

    def pay_order_callback_with_options(
        self,
        request: hcs_mgw_20171024_models.PayOrderCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.PayOrderCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.PayOrderCallbackResponse(),
            self.do_rpcrequest('PayOrderCallback', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def pay_order_callback_with_options_async(
        self,
        request: hcs_mgw_20171024_models.PayOrderCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.PayOrderCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.PayOrderCallbackResponse(),
            await self.do_rpcrequest_async('PayOrderCallback', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pay_order_callback(
        self,
        request: hcs_mgw_20171024_models.PayOrderCallbackRequest,
    ) -> hcs_mgw_20171024_models.PayOrderCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.pay_order_callback_with_options(request, runtime)

    async def pay_order_callback_async(
        self,
        request: hcs_mgw_20171024_models.PayOrderCallbackRequest,
    ) -> hcs_mgw_20171024_models.PayOrderCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pay_order_callback_with_options_async(request, runtime)

    def refund_with_options(
        self,
        request: hcs_mgw_20171024_models.RefundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.RefundResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.RefundResponse(),
            self.do_rpcrequest('Refund', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refund_with_options_async(
        self,
        request: hcs_mgw_20171024_models.RefundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.RefundResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.RefundResponse(),
            await self.do_rpcrequest_async('Refund', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refund(
        self,
        request: hcs_mgw_20171024_models.RefundRequest,
    ) -> hcs_mgw_20171024_models.RefundResponse:
        runtime = util_models.RuntimeOptions()
        return self.refund_with_options(request, runtime)

    async def refund_async(
        self,
        request: hcs_mgw_20171024_models.RefundRequest,
    ) -> hcs_mgw_20171024_models.RefundResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refund_with_options_async(request, runtime)

    def retry_data_address_with_options(
        self,
        request: hcs_mgw_20171024_models.RetryDataAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.RetryDataAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.RetryDataAddressResponse(),
            self.do_rpcrequest('RetryDataAddress', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def retry_data_address_with_options_async(
        self,
        request: hcs_mgw_20171024_models.RetryDataAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.RetryDataAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.RetryDataAddressResponse(),
            await self.do_rpcrequest_async('RetryDataAddress', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def retry_data_address(
        self,
        request: hcs_mgw_20171024_models.RetryDataAddressRequest,
    ) -> hcs_mgw_20171024_models.RetryDataAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.retry_data_address_with_options(request, runtime)

    async def retry_data_address_async(
        self,
        request: hcs_mgw_20171024_models.RetryDataAddressRequest,
    ) -> hcs_mgw_20171024_models.RetryDataAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retry_data_address_with_options_async(request, runtime)

    def retry_import_job_with_options(
        self,
        request: hcs_mgw_20171024_models.RetryImportJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.RetryImportJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.RetryImportJobResponse(),
            self.do_rpcrequest('RetryImportJob', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def retry_import_job_with_options_async(
        self,
        request: hcs_mgw_20171024_models.RetryImportJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.RetryImportJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.RetryImportJobResponse(),
            await self.do_rpcrequest_async('RetryImportJob', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def retry_import_job(
        self,
        request: hcs_mgw_20171024_models.RetryImportJobRequest,
    ) -> hcs_mgw_20171024_models.RetryImportJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.retry_import_job_with_options(request, runtime)

    async def retry_import_job_async(
        self,
        request: hcs_mgw_20171024_models.RetryImportJobRequest,
    ) -> hcs_mgw_20171024_models.RetryImportJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retry_import_job_with_options_async(request, runtime)

    def start_import_job_with_options(
        self,
        request: hcs_mgw_20171024_models.StartImportJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.StartImportJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.StartImportJobResponse(),
            self.do_rpcrequest('StartImportJob', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_import_job_with_options_async(
        self,
        request: hcs_mgw_20171024_models.StartImportJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.StartImportJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.StartImportJobResponse(),
            await self.do_rpcrequest_async('StartImportJob', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_import_job(
        self,
        request: hcs_mgw_20171024_models.StartImportJobRequest,
    ) -> hcs_mgw_20171024_models.StartImportJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_import_job_with_options(request, runtime)

    async def start_import_job_async(
        self,
        request: hcs_mgw_20171024_models.StartImportJobRequest,
    ) -> hcs_mgw_20171024_models.StartImportJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_import_job_with_options_async(request, runtime)

    def start_job_with_options(
        self,
        request: hcs_mgw_20171024_models.StartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.StartJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.StartJobResponse(),
            self.do_rpcrequest('StartJob', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_job_with_options_async(
        self,
        request: hcs_mgw_20171024_models.StartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.StartJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.StartJobResponse(),
            await self.do_rpcrequest_async('StartJob', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_job(
        self,
        request: hcs_mgw_20171024_models.StartJobRequest,
    ) -> hcs_mgw_20171024_models.StartJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_job_with_options(request, runtime)

    async def start_job_async(
        self,
        request: hcs_mgw_20171024_models.StartJobRequest,
    ) -> hcs_mgw_20171024_models.StartJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_job_with_options_async(request, runtime)

    def stop_import_job_with_options(
        self,
        request: hcs_mgw_20171024_models.StopImportJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.StopImportJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.StopImportJobResponse(),
            self.do_rpcrequest('StopImportJob', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_import_job_with_options_async(
        self,
        request: hcs_mgw_20171024_models.StopImportJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.StopImportJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.StopImportJobResponse(),
            await self.do_rpcrequest_async('StopImportJob', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_import_job(
        self,
        request: hcs_mgw_20171024_models.StopImportJobRequest,
    ) -> hcs_mgw_20171024_models.StopImportJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_import_job_with_options(request, runtime)

    async def stop_import_job_async(
        self,
        request: hcs_mgw_20171024_models.StopImportJobRequest,
    ) -> hcs_mgw_20171024_models.StopImportJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_import_job_with_options_async(request, runtime)

    def stop_job_with_options(
        self,
        request: hcs_mgw_20171024_models.StopJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.StopJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.StopJobResponse(),
            self.do_rpcrequest('StopJob', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_job_with_options_async(
        self,
        request: hcs_mgw_20171024_models.StopJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.StopJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.StopJobResponse(),
            await self.do_rpcrequest_async('StopJob', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_job(
        self,
        request: hcs_mgw_20171024_models.StopJobRequest,
    ) -> hcs_mgw_20171024_models.StopJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_job_with_options(request, runtime)

    async def stop_job_async(
        self,
        request: hcs_mgw_20171024_models.StopJobRequest,
    ) -> hcs_mgw_20171024_models.StopJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_job_with_options_async(request, runtime)

    def update_data_address_with_options(
        self,
        request: hcs_mgw_20171024_models.UpdateDataAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.UpdateDataAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.UpdateDataAddressResponse(),
            self.do_rpcrequest('UpdateDataAddress', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_data_address_with_options_async(
        self,
        request: hcs_mgw_20171024_models.UpdateDataAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.UpdateDataAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.UpdateDataAddressResponse(),
            await self.do_rpcrequest_async('UpdateDataAddress', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_data_address(
        self,
        request: hcs_mgw_20171024_models.UpdateDataAddressRequest,
    ) -> hcs_mgw_20171024_models.UpdateDataAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_data_address_with_options(request, runtime)

    async def update_data_address_async(
        self,
        request: hcs_mgw_20171024_models.UpdateDataAddressRequest,
    ) -> hcs_mgw_20171024_models.UpdateDataAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_data_address_with_options_async(request, runtime)

    def update_import_job_with_options(
        self,
        request: hcs_mgw_20171024_models.UpdateImportJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.UpdateImportJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.UpdateImportJobResponse(),
            self.do_rpcrequest('UpdateImportJob', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_import_job_with_options_async(
        self,
        request: hcs_mgw_20171024_models.UpdateImportJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.UpdateImportJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.UpdateImportJobResponse(),
            await self.do_rpcrequest_async('UpdateImportJob', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_import_job(
        self,
        request: hcs_mgw_20171024_models.UpdateImportJobRequest,
    ) -> hcs_mgw_20171024_models.UpdateImportJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_import_job_with_options(request, runtime)

    async def update_import_job_async(
        self,
        request: hcs_mgw_20171024_models.UpdateImportJobRequest,
    ) -> hcs_mgw_20171024_models.UpdateImportJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_import_job_with_options_async(request, runtime)

    def update_migration_status_with_options(
        self,
        request: hcs_mgw_20171024_models.UpdateMigrationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.UpdateMigrationStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.UpdateMigrationStatusResponse(),
            self.do_rpcrequest('UpdateMigrationStatus', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_migration_status_with_options_async(
        self,
        request: hcs_mgw_20171024_models.UpdateMigrationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.UpdateMigrationStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.UpdateMigrationStatusResponse(),
            await self.do_rpcrequest_async('UpdateMigrationStatus', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_migration_status(
        self,
        request: hcs_mgw_20171024_models.UpdateMigrationStatusRequest,
    ) -> hcs_mgw_20171024_models.UpdateMigrationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_migration_status_with_options(request, runtime)

    async def update_migration_status_async(
        self,
        request: hcs_mgw_20171024_models.UpdateMigrationStatusRequest,
    ) -> hcs_mgw_20171024_models.UpdateMigrationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_migration_status_with_options_async(request, runtime)

    def verify_css_create_order_param_with_options(
        self,
        request: hcs_mgw_20171024_models.VerifyCssCreateOrderParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.VerifyCssCreateOrderParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.VerifyCssCreateOrderParamResponse(),
            self.do_rpcrequest('VerifyCssCreateOrderParam', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_css_create_order_param_with_options_async(
        self,
        request: hcs_mgw_20171024_models.VerifyCssCreateOrderParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20171024_models.VerifyCssCreateOrderParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            hcs_mgw_20171024_models.VerifyCssCreateOrderParamResponse(),
            await self.do_rpcrequest_async('VerifyCssCreateOrderParam', '2017-10-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_css_create_order_param(
        self,
        request: hcs_mgw_20171024_models.VerifyCssCreateOrderParamRequest,
    ) -> hcs_mgw_20171024_models.VerifyCssCreateOrderParamResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_css_create_order_param_with_options(request, runtime)

    async def verify_css_create_order_param_async(
        self,
        request: hcs_mgw_20171024_models.VerifyCssCreateOrderParamRequest,
    ) -> hcs_mgw_20171024_models.VerifyCssCreateOrderParamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_css_create_order_param_with_options_async(request, runtime)
