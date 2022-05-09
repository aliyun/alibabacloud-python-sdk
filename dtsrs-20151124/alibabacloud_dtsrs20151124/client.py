# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dtsrs20151124 import models as dtsrs_20151124_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('dtsrs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def configure_migration_job_with_options(
        self,
        request: dtsrs_20151124_models.ConfigureMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.ConfigureMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not UtilClient.is_unset(request.migration_object):
            query['MigrationObject'] = request.migration_object
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.migration_mode):
            query['MigrationMode'] = request.migration_mode
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureMigrationJob',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.ConfigureMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_migration_job_with_options_async(
        self,
        request: dtsrs_20151124_models.ConfigureMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.ConfigureMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not UtilClient.is_unset(request.migration_object):
            query['MigrationObject'] = request.migration_object
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.migration_mode):
            query['MigrationMode'] = request.migration_mode
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureMigrationJob',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.ConfigureMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_migration_job(
        self,
        request: dtsrs_20151124_models.ConfigureMigrationJobRequest,
    ) -> dtsrs_20151124_models.ConfigureMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.configure_migration_job_with_options(request, runtime)

    async def configure_migration_job_async(
        self,
        request: dtsrs_20151124_models.ConfigureMigrationJobRequest,
    ) -> dtsrs_20151124_models.ConfigureMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.configure_migration_job_with_options_async(request, runtime)

    def create_migration_job_with_options(
        self,
        request: dtsrs_20151124_models.CreateMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.CreateMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_class):
            query['MigrationJobClass'] = request.migration_job_class
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMigrationJob',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.CreateMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_migration_job_with_options_async(
        self,
        request: dtsrs_20151124_models.CreateMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.CreateMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_class):
            query['MigrationJobClass'] = request.migration_job_class
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMigrationJob',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.CreateMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_migration_job(
        self,
        request: dtsrs_20151124_models.CreateMigrationJobRequest,
    ) -> dtsrs_20151124_models.CreateMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_migration_job_with_options(request, runtime)

    async def create_migration_job_async(
        self,
        request: dtsrs_20151124_models.CreateMigrationJobRequest,
    ) -> dtsrs_20151124_models.CreateMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_migration_job_with_options_async(request, runtime)

    def create_synchronous_job_with_options(
        self,
        request: dtsrs_20151124_models.CreateSynchronousJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.CreateSynchronousJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_instance_id):
            query['DestinationInstanceId'] = request.destination_instance_id
        if not UtilClient.is_unset(request.full_data_intialization):
            query['FullDataIntialization'] = request.full_data_intialization
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.structure_intialization):
            query['StructureIntialization'] = request.structure_intialization
        if not UtilClient.is_unset(request.synchronous_job_name):
            query['SynchronousJobName'] = request.synchronous_job_name
        if not UtilClient.is_unset(request.synchronous_object_list):
            query['SynchronousObjectList'] = request.synchronous_object_list
        if not UtilClient.is_unset(request.synchronous_speed_limit):
            query['SynchronousSpeedLimit'] = request.synchronous_speed_limit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSynchronousJob',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.CreateSynchronousJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_synchronous_job_with_options_async(
        self,
        request: dtsrs_20151124_models.CreateSynchronousJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.CreateSynchronousJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_instance_id):
            query['DestinationInstanceId'] = request.destination_instance_id
        if not UtilClient.is_unset(request.full_data_intialization):
            query['FullDataIntialization'] = request.full_data_intialization
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.structure_intialization):
            query['StructureIntialization'] = request.structure_intialization
        if not UtilClient.is_unset(request.synchronous_job_name):
            query['SynchronousJobName'] = request.synchronous_job_name
        if not UtilClient.is_unset(request.synchronous_object_list):
            query['SynchronousObjectList'] = request.synchronous_object_list
        if not UtilClient.is_unset(request.synchronous_speed_limit):
            query['SynchronousSpeedLimit'] = request.synchronous_speed_limit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSynchronousJob',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.CreateSynchronousJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_synchronous_job(
        self,
        request: dtsrs_20151124_models.CreateSynchronousJobRequest,
    ) -> dtsrs_20151124_models.CreateSynchronousJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_synchronous_job_with_options(request, runtime)

    async def create_synchronous_job_async(
        self,
        request: dtsrs_20151124_models.CreateSynchronousJobRequest,
    ) -> dtsrs_20151124_models.CreateSynchronousJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_synchronous_job_with_options_async(request, runtime)

    def delete_migration_job_with_options(
        self,
        request: dtsrs_20151124_models.DeleteMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.DeleteMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMigrationJob',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.DeleteMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_migration_job_with_options_async(
        self,
        request: dtsrs_20151124_models.DeleteMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.DeleteMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMigrationJob',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.DeleteMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_migration_job(
        self,
        request: dtsrs_20151124_models.DeleteMigrationJobRequest,
    ) -> dtsrs_20151124_models.DeleteMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_migration_job_with_options(request, runtime)

    async def delete_migration_job_async(
        self,
        request: dtsrs_20151124_models.DeleteMigrationJobRequest,
    ) -> dtsrs_20151124_models.DeleteMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_migration_job_with_options_async(request, runtime)

    def delete_synchronous_job_with_options(
        self,
        request: dtsrs_20151124_models.DeleteSynchronousJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.DeleteSynchronousJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.synchronous_job_id):
            query['SynchronousJobId'] = request.synchronous_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSynchronousJob',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.DeleteSynchronousJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_synchronous_job_with_options_async(
        self,
        request: dtsrs_20151124_models.DeleteSynchronousJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.DeleteSynchronousJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.synchronous_job_id):
            query['SynchronousJobId'] = request.synchronous_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSynchronousJob',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.DeleteSynchronousJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_synchronous_job(
        self,
        request: dtsrs_20151124_models.DeleteSynchronousJobRequest,
    ) -> dtsrs_20151124_models.DeleteSynchronousJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_synchronous_job_with_options(request, runtime)

    async def delete_synchronous_job_async(
        self,
        request: dtsrs_20151124_models.DeleteSynchronousJobRequest,
    ) -> dtsrs_20151124_models.DeleteSynchronousJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_synchronous_job_with_options_async(request, runtime)

    def descirbe_migration_jobs_with_options(
        self,
        request: dtsrs_20151124_models.DescirbeMigrationJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.DescirbeMigrationJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescirbeMigrationJobs',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.DescirbeMigrationJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def descirbe_migration_jobs_with_options_async(
        self,
        request: dtsrs_20151124_models.DescirbeMigrationJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.DescirbeMigrationJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescirbeMigrationJobs',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.DescirbeMigrationJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def descirbe_migration_jobs(
        self,
        request: dtsrs_20151124_models.DescirbeMigrationJobsRequest,
    ) -> dtsrs_20151124_models.DescirbeMigrationJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.descirbe_migration_jobs_with_options(request, runtime)

    async def descirbe_migration_jobs_async(
        self,
        request: dtsrs_20151124_models.DescirbeMigrationJobsRequest,
    ) -> dtsrs_20151124_models.DescirbeMigrationJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.descirbe_migration_jobs_with_options_async(request, runtime)

    def describe_migration_job_status_with_options(
        self,
        request: dtsrs_20151124_models.DescribeMigrationJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.DescribeMigrationJobStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobStatus',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.DescribeMigrationJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_migration_job_status_with_options_async(
        self,
        request: dtsrs_20151124_models.DescribeMigrationJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.DescribeMigrationJobStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobStatus',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.DescribeMigrationJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_migration_job_status(
        self,
        request: dtsrs_20151124_models.DescribeMigrationJobStatusRequest,
    ) -> dtsrs_20151124_models.DescribeMigrationJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_job_status_with_options(request, runtime)

    async def describe_migration_job_status_async(
        self,
        request: dtsrs_20151124_models.DescribeMigrationJobStatusRequest,
    ) -> dtsrs_20151124_models.DescribeMigrationJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_migration_job_status_with_options_async(request, runtime)

    def describe_synchronous_job_configuration_with_options(
        self,
        request: dtsrs_20151124_models.DescribeSynchronousJobConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.DescribeSynchronousJobConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.synchronous_job_id):
            query['SynchronousJobId'] = request.synchronous_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronousJobConfiguration',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.DescribeSynchronousJobConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_synchronous_job_configuration_with_options_async(
        self,
        request: dtsrs_20151124_models.DescribeSynchronousJobConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.DescribeSynchronousJobConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.synchronous_job_id):
            query['SynchronousJobId'] = request.synchronous_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronousJobConfiguration',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.DescribeSynchronousJobConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_synchronous_job_configuration(
        self,
        request: dtsrs_20151124_models.DescribeSynchronousJobConfigurationRequest,
    ) -> dtsrs_20151124_models.DescribeSynchronousJobConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronous_job_configuration_with_options(request, runtime)

    async def describe_synchronous_job_configuration_async(
        self,
        request: dtsrs_20151124_models.DescribeSynchronousJobConfigurationRequest,
    ) -> dtsrs_20151124_models.DescribeSynchronousJobConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronous_job_configuration_with_options_async(request, runtime)

    def describe_synchronous_job_details_with_options(
        self,
        request: dtsrs_20151124_models.DescribeSynchronousJobDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.DescribeSynchronousJobDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.synchronous_job_id):
            query['SynchronousJobId'] = request.synchronous_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronousJobDetails',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.DescribeSynchronousJobDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_synchronous_job_details_with_options_async(
        self,
        request: dtsrs_20151124_models.DescribeSynchronousJobDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.DescribeSynchronousJobDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.synchronous_job_id):
            query['SynchronousJobId'] = request.synchronous_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronousJobDetails',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.DescribeSynchronousJobDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_synchronous_job_details(
        self,
        request: dtsrs_20151124_models.DescribeSynchronousJobDetailsRequest,
    ) -> dtsrs_20151124_models.DescribeSynchronousJobDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronous_job_details_with_options(request, runtime)

    async def describe_synchronous_job_details_async(
        self,
        request: dtsrs_20151124_models.DescribeSynchronousJobDetailsRequest,
    ) -> dtsrs_20151124_models.DescribeSynchronousJobDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronous_job_details_with_options_async(request, runtime)

    def describe_synchronous_job_list_with_options(
        self,
        request: dtsrs_20151124_models.DescribeSynchronousJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.DescribeSynchronousJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.synchronous_job_name):
            query['SynchronousJobName'] = request.synchronous_job_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronousJobList',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.DescribeSynchronousJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_synchronous_job_list_with_options_async(
        self,
        request: dtsrs_20151124_models.DescribeSynchronousJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.DescribeSynchronousJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.synchronous_job_name):
            query['SynchronousJobName'] = request.synchronous_job_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronousJobList',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.DescribeSynchronousJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_synchronous_job_list(
        self,
        request: dtsrs_20151124_models.DescribeSynchronousJobListRequest,
    ) -> dtsrs_20151124_models.DescribeSynchronousJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronous_job_list_with_options(request, runtime)

    async def describe_synchronous_job_list_async(
        self,
        request: dtsrs_20151124_models.DescribeSynchronousJobListRequest,
    ) -> dtsrs_20151124_models.DescribeSynchronousJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronous_job_list_with_options_async(request, runtime)

    def start_migration_job_with_options(
        self,
        request: dtsrs_20151124_models.StartMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.StartMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartMigrationJob',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.StartMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_migration_job_with_options_async(
        self,
        request: dtsrs_20151124_models.StartMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.StartMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartMigrationJob',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.StartMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_migration_job(
        self,
        request: dtsrs_20151124_models.StartMigrationJobRequest,
    ) -> dtsrs_20151124_models.StartMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_migration_job_with_options(request, runtime)

    async def start_migration_job_async(
        self,
        request: dtsrs_20151124_models.StartMigrationJobRequest,
    ) -> dtsrs_20151124_models.StartMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_migration_job_with_options_async(request, runtime)

    def start_synchronous_job_with_options(
        self,
        request: dtsrs_20151124_models.StartSynchronousJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.StartSynchronousJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.synchronous_job_id):
            query['SynchronousJobId'] = request.synchronous_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartSynchronousJob',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.StartSynchronousJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_synchronous_job_with_options_async(
        self,
        request: dtsrs_20151124_models.StartSynchronousJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.StartSynchronousJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.synchronous_job_id):
            query['SynchronousJobId'] = request.synchronous_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartSynchronousJob',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.StartSynchronousJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_synchronous_job(
        self,
        request: dtsrs_20151124_models.StartSynchronousJobRequest,
    ) -> dtsrs_20151124_models.StartSynchronousJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_synchronous_job_with_options(request, runtime)

    async def start_synchronous_job_async(
        self,
        request: dtsrs_20151124_models.StartSynchronousJobRequest,
    ) -> dtsrs_20151124_models.StartSynchronousJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_synchronous_job_with_options_async(request, runtime)

    def stop_migration_job_with_options(
        self,
        request: dtsrs_20151124_models.StopMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.StopMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopMigrationJob',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.StopMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_migration_job_with_options_async(
        self,
        request: dtsrs_20151124_models.StopMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.StopMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopMigrationJob',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.StopMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_migration_job(
        self,
        request: dtsrs_20151124_models.StopMigrationJobRequest,
    ) -> dtsrs_20151124_models.StopMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_migration_job_with_options(request, runtime)

    async def stop_migration_job_async(
        self,
        request: dtsrs_20151124_models.StopMigrationJobRequest,
    ) -> dtsrs_20151124_models.StopMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_migration_job_with_options_async(request, runtime)

    def suspend_migration_job_with_options(
        self,
        request: dtsrs_20151124_models.SuspendMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.SuspendMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendMigrationJob',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.SuspendMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_migration_job_with_options_async(
        self,
        request: dtsrs_20151124_models.SuspendMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.SuspendMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendMigrationJob',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.SuspendMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_migration_job(
        self,
        request: dtsrs_20151124_models.SuspendMigrationJobRequest,
    ) -> dtsrs_20151124_models.SuspendMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_migration_job_with_options(request, runtime)

    async def suspend_migration_job_async(
        self,
        request: dtsrs_20151124_models.SuspendMigrationJobRequest,
    ) -> dtsrs_20151124_models.SuspendMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_migration_job_with_options_async(request, runtime)

    def suspend_synchronous_job_with_options(
        self,
        request: dtsrs_20151124_models.SuspendSynchronousJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.SuspendSynchronousJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.synchronous_job_id):
            query['SynchronousJobId'] = request.synchronous_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendSynchronousJob',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.SuspendSynchronousJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_synchronous_job_with_options_async(
        self,
        request: dtsrs_20151124_models.SuspendSynchronousJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dtsrs_20151124_models.SuspendSynchronousJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.synchronous_job_id):
            query['SynchronousJobId'] = request.synchronous_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendSynchronousJob',
            version='2015-11-24',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            dtsrs_20151124_models.SuspendSynchronousJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_synchronous_job(
        self,
        request: dtsrs_20151124_models.SuspendSynchronousJobRequest,
    ) -> dtsrs_20151124_models.SuspendSynchronousJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_synchronous_job_with_options(request, runtime)

    async def suspend_synchronous_job_async(
        self,
        request: dtsrs_20151124_models.SuspendSynchronousJobRequest,
    ) -> dtsrs_20151124_models.SuspendSynchronousJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_synchronous_job_with_options_async(request, runtime)
