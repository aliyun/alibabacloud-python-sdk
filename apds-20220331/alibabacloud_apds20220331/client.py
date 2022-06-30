# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_apds20220331 import models as apds_20220331_models
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
        self._endpoint = self.get_endpoint('apds', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_file_job(
        self,
        request: apds_20220331_models.CreateFileJobRequest,
    ) -> apds_20220331_models.CreateFileJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_file_job_with_options(request, headers, runtime)

    async def create_file_job_async(
        self,
        request: apds_20220331_models.CreateFileJobRequest,
    ) -> apds_20220331_models.CreateFileJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_file_job_with_options_async(request, headers, runtime)

    def create_file_job_with_options(
        self,
        request: apds_20220331_models.CreateFileJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.CreateFileJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.survey_job_id):
            body['surveyJobId'] = request.survey_job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFileJob',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/file-job/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.CreateFileJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_file_job_with_options_async(
        self,
        request: apds_20220331_models.CreateFileJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.CreateFileJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.survey_job_id):
            body['surveyJobId'] = request.survey_job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFileJob',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/file-job/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.CreateFileJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_migration_group(
        self,
        request: apds_20220331_models.CreateMigrationGroupRequest,
    ) -> apds_20220331_models.CreateMigrationGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_migration_group_with_options(request, headers, runtime)

    async def create_migration_group_async(
        self,
        request: apds_20220331_models.CreateMigrationGroupRequest,
    ) -> apds_20220331_models.CreateMigrationGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_migration_group_with_options_async(request, headers, runtime)

    def create_migration_group_with_options(
        self,
        request: apds_20220331_models.CreateMigrationGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.CreateMigrationGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMigrationGroup',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-group/save-migration-group',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.CreateMigrationGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_migration_group_with_options_async(
        self,
        request: apds_20220331_models.CreateMigrationGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.CreateMigrationGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMigrationGroup',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-group/save-migration-group',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.CreateMigrationGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_migration_job(
        self,
        request: apds_20220331_models.CreateMigrationJobRequest,
    ) -> apds_20220331_models.CreateMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_migration_job_with_options(request, headers, runtime)

    async def create_migration_job_async(
        self,
        request: apds_20220331_models.CreateMigrationJobRequest,
    ) -> apds_20220331_models.CreateMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_migration_job_with_options_async(request, headers, runtime)

    def create_migration_job_with_options(
        self,
        request: apds_20220331_models.CreateMigrationJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.CreateMigrationJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.migration_job_list):
            body['migrationJobList'] = request.migration_job_list
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMigrationJob',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-job/create-migration-jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.CreateMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_migration_job_with_options_async(
        self,
        request: apds_20220331_models.CreateMigrationJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.CreateMigrationJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.migration_job_list):
            body['migrationJobList'] = request.migration_job_list
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMigrationJob',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-job/create-migration-jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.CreateMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_survey_job(
        self,
        request: apds_20220331_models.CreateSurveyJobRequest,
    ) -> apds_20220331_models.CreateSurveyJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_survey_job_with_options(request, headers, runtime)

    async def create_survey_job_async(
        self,
        request: apds_20220331_models.CreateSurveyJobRequest,
    ) -> apds_20220331_models.CreateSurveyJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_survey_job_with_options_async(request, headers, runtime)

    def create_survey_job_with_options(
        self,
        request: apds_20220331_models.CreateSurveyJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.CreateSurveyJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.resource_type_list):
            body['ResourceTypeList'] = request.resource_type_list
        if not UtilClient.is_unset(request.ak):
            body['ak'] = request.ak
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.cloud_type):
            body['cloudType'] = request.cloud_type
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.sk):
            body['sk'] = request.sk
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSurveyJob',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/winback/add-survey-job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.CreateSurveyJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_survey_job_with_options_async(
        self,
        request: apds_20220331_models.CreateSurveyJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.CreateSurveyJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.resource_type_list):
            body['ResourceTypeList'] = request.resource_type_list
        if not UtilClient.is_unset(request.ak):
            body['ak'] = request.ak
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.cloud_type):
            body['cloudType'] = request.cloud_type
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.sk):
            body['sk'] = request.sk
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSurveyJob',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/winback/add-survey-job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.CreateSurveyJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_survey_job_offline(
        self,
        request: apds_20220331_models.CreateSurveyJobOfflineRequest,
    ) -> apds_20220331_models.CreateSurveyJobOfflineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_survey_job_offline_with_options(request, headers, runtime)

    async def create_survey_job_offline_async(
        self,
        request: apds_20220331_models.CreateSurveyJobOfflineRequest,
    ) -> apds_20220331_models.CreateSurveyJobOfflineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_survey_job_offline_with_options_async(request, headers, runtime)

    def create_survey_job_offline_with_options(
        self,
        request: apds_20220331_models.CreateSurveyJobOfflineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.CreateSurveyJobOfflineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.cloud_type):
            body['cloudType'] = request.cloud_type
        if not UtilClient.is_unset(request.file_name):
            body['fileName'] = request.file_name
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.object_name):
            body['objectName'] = request.object_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSurveyJobOffline',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/winback/add-import-survey-job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.CreateSurveyJobOfflineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_survey_job_offline_with_options_async(
        self,
        request: apds_20220331_models.CreateSurveyJobOfflineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.CreateSurveyJobOfflineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.cloud_type):
            body['cloudType'] = request.cloud_type
        if not UtilClient.is_unset(request.file_name):
            body['fileName'] = request.file_name
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.object_name):
            body['objectName'] = request.object_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSurveyJobOffline',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/winback/add-import-survey-job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.CreateSurveyJobOfflineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_migration_group(
        self,
        request: apds_20220331_models.DeleteMigrationGroupRequest,
    ) -> apds_20220331_models.DeleteMigrationGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_migration_group_with_options(request, headers, runtime)

    async def delete_migration_group_async(
        self,
        request: apds_20220331_models.DeleteMigrationGroupRequest,
    ) -> apds_20220331_models.DeleteMigrationGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_migration_group_with_options_async(request, headers, runtime)

    def delete_migration_group_with_options(
        self,
        request: apds_20220331_models.DeleteMigrationGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DeleteMigrationGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMigrationGroup',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-group/remove-migration-group',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DeleteMigrationGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_migration_group_with_options_async(
        self,
        request: apds_20220331_models.DeleteMigrationGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DeleteMigrationGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMigrationGroup',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-group/remove-migration-group',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DeleteMigrationGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_migration_job(
        self,
        request: apds_20220331_models.DeleteMigrationJobRequest,
    ) -> apds_20220331_models.DeleteMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_migration_job_with_options(request, headers, runtime)

    async def delete_migration_job_async(
        self,
        request: apds_20220331_models.DeleteMigrationJobRequest,
    ) -> apds_20220331_models.DeleteMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_migration_job_with_options_async(request, headers, runtime)

    def delete_migration_job_with_options(
        self,
        request: apds_20220331_models.DeleteMigrationJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DeleteMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMigrationJob',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-job/remove-migration-job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DeleteMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_migration_job_with_options_async(
        self,
        request: apds_20220331_models.DeleteMigrationJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DeleteMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMigrationJob',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-job/remove-migration-job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DeleteMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_oss_file(
        self,
        request: apds_20220331_models.DeleteOssFileRequest,
    ) -> apds_20220331_models.DeleteOssFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_oss_file_with_options(request, headers, runtime)

    async def delete_oss_file_async(
        self,
        request: apds_20220331_models.DeleteOssFileRequest,
    ) -> apds_20220331_models.DeleteOssFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_oss_file_with_options_async(request, headers, runtime)

    def delete_oss_file_with_options(
        self,
        request: apds_20220331_models.DeleteOssFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DeleteOssFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_name):
            query['objectName'] = request.object_name
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOssFile',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/file-job/delete-file',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DeleteOssFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_oss_file_with_options_async(
        self,
        request: apds_20220331_models.DeleteOssFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DeleteOssFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_name):
            query['objectName'] = request.object_name
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOssFile',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/file-job/delete-file',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DeleteOssFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_survey_job(
        self,
        request: apds_20220331_models.DeleteSurveyJobRequest,
    ) -> apds_20220331_models.DeleteSurveyJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_survey_job_with_options(request, headers, runtime)

    async def delete_survey_job_async(
        self,
        request: apds_20220331_models.DeleteSurveyJobRequest,
    ) -> apds_20220331_models.DeleteSurveyJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_survey_job_with_options_async(request, headers, runtime)

    def delete_survey_job_with_options(
        self,
        request: apds_20220331_models.DeleteSurveyJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DeleteSurveyJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSurveyJob',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/winback/delete-survey-job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DeleteSurveyJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_survey_job_with_options_async(
        self,
        request: apds_20220331_models.DeleteSurveyJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DeleteSurveyJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSurveyJob',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/winback/delete-survey-job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DeleteSurveyJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_survey_resources(
        self,
        request: apds_20220331_models.DeleteSurveyResourcesRequest,
    ) -> apds_20220331_models.DeleteSurveyResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_survey_resources_with_options(request, headers, runtime)

    async def delete_survey_resources_async(
        self,
        request: apds_20220331_models.DeleteSurveyResourcesRequest,
    ) -> apds_20220331_models.DeleteSurveyResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_survey_resources_with_options_async(request, headers, runtime)

    def delete_survey_resources_with_options(
        self,
        request: apds_20220331_models.DeleteSurveyResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DeleteSurveyResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['ids'] = request.ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSurveyResources',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/confirm-resource/destroy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DeleteSurveyResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_survey_resources_with_options_async(
        self,
        request: apds_20220331_models.DeleteSurveyResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DeleteSurveyResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['ids'] = request.ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSurveyResources',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/confirm-resource/destroy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DeleteSurveyResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_migration_job_config(self) -> apds_20220331_models.DescribeMigrationJobConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_migration_job_config_with_options(headers, runtime)

    async def describe_migration_job_config_async(self) -> apds_20220331_models.DescribeMigrationJobConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_migration_job_config_with_options_async(headers, runtime)

    def describe_migration_job_config_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DescribeMigrationJobConfigResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobConfig',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-job/describe-migration-job-config',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DescribeMigrationJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_migration_job_config_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DescribeMigrationJobConfigResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobConfig',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-job/describe-migration-job-config',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DescribeMigrationJobConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_migration_job_count(
        self,
        request: apds_20220331_models.DescribeMigrationJobCountRequest,
    ) -> apds_20220331_models.DescribeMigrationJobCountResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_migration_job_count_with_options(request, headers, runtime)

    async def describe_migration_job_count_async(
        self,
        request: apds_20220331_models.DescribeMigrationJobCountRequest,
    ) -> apds_20220331_models.DescribeMigrationJobCountResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_migration_job_count_with_options_async(request, headers, runtime)

    def describe_migration_job_count_with_options(
        self,
        request: apds_20220331_models.DescribeMigrationJobCountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DescribeMigrationJobCountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobCount',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-job/count-migration-jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DescribeMigrationJobCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_migration_job_count_with_options_async(
        self,
        request: apds_20220331_models.DescribeMigrationJobCountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DescribeMigrationJobCountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobCount',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-job/count-migration-jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DescribeMigrationJobCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_sts(
        self,
        request: apds_20220331_models.DescribeOssStsRequest,
    ) -> apds_20220331_models.DescribeOssStsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_oss_sts_with_options(request, headers, runtime)

    async def describe_oss_sts_async(
        self,
        request: apds_20220331_models.DescribeOssStsRequest,
    ) -> apds_20220331_models.DescribeOssStsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_oss_sts_with_options_async(request, headers, runtime)

    def describe_oss_sts_with_options(
        self,
        request: apds_20220331_models.DescribeOssStsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DescribeOssStsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak):
            query['ak'] = request.ak
        if not UtilClient.is_unset(request.cloud_type):
            query['cloudType'] = request.cloud_type
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.sk):
            query['sk'] = request.sk
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssSts',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/file-job/sts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DescribeOssStsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_sts_with_options_async(
        self,
        request: apds_20220331_models.DescribeOssStsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DescribeOssStsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak):
            query['ak'] = request.ak
        if not UtilClient.is_unset(request.cloud_type):
            query['cloudType'] = request.cloud_type
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.sk):
            query['sk'] = request.sk
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssSts',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/file-job/sts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DescribeOssStsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_summary_by_status(
        self,
        request: apds_20220331_models.DescribeSummaryByStatusRequest,
    ) -> apds_20220331_models.DescribeSummaryByStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_summary_by_status_with_options(request, headers, runtime)

    async def describe_summary_by_status_async(
        self,
        request: apds_20220331_models.DescribeSummaryByStatusRequest,
    ) -> apds_20220331_models.DescribeSummaryByStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_summary_by_status_with_options_async(request, headers, runtime)

    def describe_summary_by_status_with_options(
        self,
        request: apds_20220331_models.DescribeSummaryByStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DescribeSummaryByStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSummaryByStatus',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/summary/summary-by-status',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DescribeSummaryByStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_summary_by_status_with_options_async(
        self,
        request: apds_20220331_models.DescribeSummaryByStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DescribeSummaryByStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSummaryByStatus',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/summary/summary-by-status',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DescribeSummaryByStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_summary_by_status_and_group(
        self,
        request: apds_20220331_models.DescribeSummaryByStatusAndGroupRequest,
    ) -> apds_20220331_models.DescribeSummaryByStatusAndGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_summary_by_status_and_group_with_options(request, headers, runtime)

    async def describe_summary_by_status_and_group_async(
        self,
        request: apds_20220331_models.DescribeSummaryByStatusAndGroupRequest,
    ) -> apds_20220331_models.DescribeSummaryByStatusAndGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_summary_by_status_and_group_with_options_async(request, headers, runtime)

    def describe_summary_by_status_and_group_with_options(
        self,
        request: apds_20220331_models.DescribeSummaryByStatusAndGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DescribeSummaryByStatusAndGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSummaryByStatusAndGroup',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/summary/summary-by-status-and-region',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DescribeSummaryByStatusAndGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_summary_by_status_and_group_with_options_async(
        self,
        request: apds_20220331_models.DescribeSummaryByStatusAndGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DescribeSummaryByStatusAndGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSummaryByStatusAndGroup',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/summary/summary-by-status-and-region',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DescribeSummaryByStatusAndGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_survey_job(
        self,
        request: apds_20220331_models.DescribeSurveyJobRequest,
    ) -> apds_20220331_models.DescribeSurveyJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_survey_job_with_options(request, headers, runtime)

    async def describe_survey_job_async(
        self,
        request: apds_20220331_models.DescribeSurveyJobRequest,
    ) -> apds_20220331_models.DescribeSurveyJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_survey_job_with_options_async(request, headers, runtime)

    def describe_survey_job_with_options(
        self,
        request: apds_20220331_models.DescribeSurveyJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DescribeSurveyJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSurveyJob',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/winback/query-survey-job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DescribeSurveyJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_survey_job_with_options_async(
        self,
        request: apds_20220331_models.DescribeSurveyJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DescribeSurveyJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSurveyJob',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/winback/query-survey-job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DescribeSurveyJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_survey_job_count(
        self,
        request: apds_20220331_models.DescribeSurveyJobCountRequest,
    ) -> apds_20220331_models.DescribeSurveyJobCountResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_survey_job_count_with_options(request, headers, runtime)

    async def describe_survey_job_count_async(
        self,
        request: apds_20220331_models.DescribeSurveyJobCountRequest,
    ) -> apds_20220331_models.DescribeSurveyJobCountResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_survey_job_count_with_options_async(request, headers, runtime)

    def describe_survey_job_count_with_options(
        self,
        request: apds_20220331_models.DescribeSurveyJobCountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DescribeSurveyJobCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSurveyJobCount',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/winback/count-survey-job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DescribeSurveyJobCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_survey_job_count_with_options_async(
        self,
        request: apds_20220331_models.DescribeSurveyJobCountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DescribeSurveyJobCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSurveyJobCount',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/winback/count-survey-job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DescribeSurveyJobCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_survey_resource_tag(self) -> apds_20220331_models.DescribeSurveyResourceTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_survey_resource_tag_with_options(headers, runtime)

    async def describe_survey_resource_tag_async(self) -> apds_20220331_models.DescribeSurveyResourceTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_survey_resource_tag_with_options_async(headers, runtime)

    def describe_survey_resource_tag_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DescribeSurveyResourceTagResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSurveyResourceTag',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/confirm-resource/get-resource-tag',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DescribeSurveyResourceTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_survey_resource_tag_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DescribeSurveyResourceTagResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSurveyResourceTag',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/confirm-resource/get-resource-tag',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DescribeSurveyResourceTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_survey_template(
        self,
        request: apds_20220331_models.DescribeSurveyTemplateRequest,
    ) -> apds_20220331_models.DescribeSurveyTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_survey_template_with_options(request, headers, runtime)

    async def describe_survey_template_async(
        self,
        request: apds_20220331_models.DescribeSurveyTemplateRequest,
    ) -> apds_20220331_models.DescribeSurveyTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_survey_template_with_options_async(request, headers, runtime)

    def describe_survey_template_with_options(
        self,
        request: apds_20220331_models.DescribeSurveyTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DescribeSurveyTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSurveyTemplate',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/survey-template/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DescribeSurveyTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_survey_template_with_options_async(
        self,
        request: apds_20220331_models.DescribeSurveyTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.DescribeSurveyTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSurveyTemplate',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/survey-template/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.DescribeSurveyTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_migration_jobs(
        self,
        request: apds_20220331_models.ListMigrationJobsRequest,
    ) -> apds_20220331_models.ListMigrationJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_migration_jobs_with_options(request, headers, runtime)

    async def list_migration_jobs_async(
        self,
        request: apds_20220331_models.ListMigrationJobsRequest,
    ) -> apds_20220331_models.ListMigrationJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_migration_jobs_with_options_async(request, headers, runtime)

    def list_migration_jobs_with_options(
        self,
        request: apds_20220331_models.ListMigrationJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.ListMigrationJobsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            body['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_col):
            body['sortCol'] = request.sort_col
        if not UtilClient.is_unset(request.sort_type):
            body['sortType'] = request.sort_type
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMigrationJobs',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-job/describe-migration-jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.ListMigrationJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_migration_jobs_with_options_async(
        self,
        request: apds_20220331_models.ListMigrationJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.ListMigrationJobsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            body['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_col):
            body['sortCol'] = request.sort_col
        if not UtilClient.is_unset(request.sort_type):
            body['sortType'] = request.sort_type
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMigrationJobs',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-job/describe-migration-jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.ListMigrationJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(
        self,
        request: apds_20220331_models.ListRegionsRequest,
    ) -> apds_20220331_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_regions_with_options(request, headers, runtime)

    async def list_regions_async(
        self,
        request: apds_20220331_models.ListRegionsRequest,
    ) -> apds_20220331_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_regions_with_options_async(request, headers, runtime)

    def list_regions_with_options(
        self,
        request: apds_20220331_models.ListRegionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.ListRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak):
            query['ak'] = request.ak
        if not UtilClient.is_unset(request.cloud_type):
            query['cloudType'] = request.cloud_type
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.sk):
            query['sk'] = request.sk
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/winback/query-region',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        request: apds_20220331_models.ListRegionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.ListRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak):
            query['ak'] = request.ak
        if not UtilClient.is_unset(request.cloud_type):
            query['cloudType'] = request.cloud_type
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.sk):
            query['sk'] = request.sk
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/winback/query-region',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_survey_job_down_load_jobs(
        self,
        request: apds_20220331_models.ListSurveyJobDownLoadJobsRequest,
    ) -> apds_20220331_models.ListSurveyJobDownLoadJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_survey_job_down_load_jobs_with_options(request, headers, runtime)

    async def list_survey_job_down_load_jobs_async(
        self,
        request: apds_20220331_models.ListSurveyJobDownLoadJobsRequest,
    ) -> apds_20220331_models.ListSurveyJobDownLoadJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_survey_job_down_load_jobs_with_options_async(request, headers, runtime)

    def list_survey_job_down_load_jobs_with_options(
        self,
        request: apds_20220331_models.ListSurveyJobDownLoadJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.ListSurveyJobDownLoadJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.page_num):
            body['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_col):
            body['sortCol'] = request.sort_col
        if not UtilClient.is_unset(request.sort_type):
            body['sortType'] = request.sort_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSurveyJobDownLoadJobs',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/file-job/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.ListSurveyJobDownLoadJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_survey_job_down_load_jobs_with_options_async(
        self,
        request: apds_20220331_models.ListSurveyJobDownLoadJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.ListSurveyJobDownLoadJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.page_num):
            body['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_col):
            body['sortCol'] = request.sort_col
        if not UtilClient.is_unset(request.sort_type):
            body['sortType'] = request.sort_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSurveyJobDownLoadJobs',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/file-job/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.ListSurveyJobDownLoadJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_survey_jobs(
        self,
        request: apds_20220331_models.ListSurveyJobsRequest,
    ) -> apds_20220331_models.ListSurveyJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_survey_jobs_with_options(request, headers, runtime)

    async def list_survey_jobs_async(
        self,
        request: apds_20220331_models.ListSurveyJobsRequest,
    ) -> apds_20220331_models.ListSurveyJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_survey_jobs_with_options_async(request, headers, runtime)

    def list_survey_jobs_with_options(
        self,
        request: apds_20220331_models.ListSurveyJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.ListSurveyJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.cloud_type):
            body['cloudType'] = request.cloud_type
        if not UtilClient.is_unset(request.file_name):
            body['fileName'] = request.file_name
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.object_name):
            body['objectName'] = request.object_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSurveyJobs',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/winback/query-survey-jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.ListSurveyJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_survey_jobs_with_options_async(
        self,
        request: apds_20220331_models.ListSurveyJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.ListSurveyJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.cloud_type):
            body['cloudType'] = request.cloud_type
        if not UtilClient.is_unset(request.file_name):
            body['fileName'] = request.file_name
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.object_name):
            body['objectName'] = request.object_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSurveyJobs',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/winback/query-survey-jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.ListSurveyJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_survey_resource_by_migration_groups(
        self,
        request: apds_20220331_models.ListSurveyResourceByMigrationGroupsRequest,
    ) -> apds_20220331_models.ListSurveyResourceByMigrationGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_survey_resource_by_migration_groups_with_options(request, headers, runtime)

    async def list_survey_resource_by_migration_groups_async(
        self,
        request: apds_20220331_models.ListSurveyResourceByMigrationGroupsRequest,
    ) -> apds_20220331_models.ListSurveyResourceByMigrationGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_survey_resource_by_migration_groups_with_options_async(request, headers, runtime)

    def list_survey_resource_by_migration_groups_with_options(
        self,
        tmp_req: apds_20220331_models.ListSurveyResourceByMigrationGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.ListSurveyResourceByMigrationGroupsResponse:
        UtilClient.validate_model(tmp_req)
        request = apds_20220331_models.ListSurveyResourceByMigrationGroupsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.body), 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSurveyResourceByMigrationGroups',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-group/get-survey-resource',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.ListSurveyResourceByMigrationGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_survey_resource_by_migration_groups_with_options_async(
        self,
        tmp_req: apds_20220331_models.ListSurveyResourceByMigrationGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.ListSurveyResourceByMigrationGroupsResponse:
        UtilClient.validate_model(tmp_req)
        request = apds_20220331_models.ListSurveyResourceByMigrationGroupsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.body), 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSurveyResourceByMigrationGroups',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-group/get-survey-resource',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.ListSurveyResourceByMigrationGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_survey_resource_connections(
        self,
        request: apds_20220331_models.ListSurveyResourceConnectionsRequest,
    ) -> apds_20220331_models.ListSurveyResourceConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_survey_resource_connections_with_options(request, headers, runtime)

    async def list_survey_resource_connections_async(
        self,
        request: apds_20220331_models.ListSurveyResourceConnectionsRequest,
    ) -> apds_20220331_models.ListSurveyResourceConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_survey_resource_connections_with_options_async(request, headers, runtime)

    def list_survey_resource_connections_with_options(
        self,
        request: apds_20220331_models.ListSurveyResourceConnectionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.ListSurveyResourceConnectionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.ids):
            body['ids'] = request.ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSurveyResourceConnections',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/resource-connects',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.ListSurveyResourceConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_survey_resource_connections_with_options_async(
        self,
        request: apds_20220331_models.ListSurveyResourceConnectionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.ListSurveyResourceConnectionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.ids):
            body['ids'] = request.ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSurveyResourceConnections',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/resource-connects',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.ListSurveyResourceConnectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_survey_resource_types(
        self,
        request: apds_20220331_models.ListSurveyResourceTypesRequest,
    ) -> apds_20220331_models.ListSurveyResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_survey_resource_types_with_options(request, headers, runtime)

    async def list_survey_resource_types_async(
        self,
        request: apds_20220331_models.ListSurveyResourceTypesRequest,
    ) -> apds_20220331_models.ListSurveyResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_survey_resource_types_with_options_async(request, headers, runtime)

    def list_survey_resource_types_with_options(
        self,
        request: apds_20220331_models.ListSurveyResourceTypesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.ListSurveyResourceTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak):
            query['ak'] = request.ak
        if not UtilClient.is_unset(request.cloud_type):
            query['cloudType'] = request.cloud_type
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.sk):
            query['sk'] = request.sk
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSurveyResourceTypes',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/winback/query-resource-type',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.ListSurveyResourceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_survey_resource_types_with_options_async(
        self,
        request: apds_20220331_models.ListSurveyResourceTypesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.ListSurveyResourceTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak):
            query['ak'] = request.ak
        if not UtilClient.is_unset(request.cloud_type):
            query['cloudType'] = request.cloud_type
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.sk):
            query['sk'] = request.sk
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSurveyResourceTypes',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/winback/query-resource-type',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.ListSurveyResourceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_survey_resources_detail(
        self,
        request: apds_20220331_models.ListSurveyResourcesDetailRequest,
    ) -> apds_20220331_models.ListSurveyResourcesDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_survey_resources_detail_with_options(request, headers, runtime)

    async def list_survey_resources_detail_async(
        self,
        request: apds_20220331_models.ListSurveyResourcesDetailRequest,
    ) -> apds_20220331_models.ListSurveyResourcesDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_survey_resources_detail_with_options_async(request, headers, runtime)

    def list_survey_resources_detail_with_options(
        self,
        request: apds_20220331_models.ListSurveyResourcesDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.ListSurveyResourcesDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.ip):
            body['ip'] = request.ip
        if not UtilClient.is_unset(request.job_id):
            body['jobId'] = request.job_id
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sub_project_id):
            body['subProjectId'] = request.sub_project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSurveyResourcesDetail',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/survey-detail/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.ListSurveyResourcesDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_survey_resources_detail_with_options_async(
        self,
        request: apds_20220331_models.ListSurveyResourcesDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.ListSurveyResourcesDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.ip):
            body['ip'] = request.ip
        if not UtilClient.is_unset(request.job_id):
            body['jobId'] = request.job_id
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sub_project_id):
            body['subProjectId'] = request.sub_project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSurveyResourcesDetail',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/survey-detail/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.ListSurveyResourcesDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recover_migration_job(
        self,
        request: apds_20220331_models.RecoverMigrationJobRequest,
    ) -> apds_20220331_models.RecoverMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.recover_migration_job_with_options(request, headers, runtime)

    async def recover_migration_job_async(
        self,
        request: apds_20220331_models.RecoverMigrationJobRequest,
    ) -> apds_20220331_models.RecoverMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.recover_migration_job_with_options_async(request, headers, runtime)

    def recover_migration_job_with_options(
        self,
        request: apds_20220331_models.RecoverMigrationJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.RecoverMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoverMigrationJob',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-job/recover-migration-job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.RecoverMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def recover_migration_job_with_options_async(
        self,
        request: apds_20220331_models.RecoverMigrationJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.RecoverMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoverMigrationJob',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-job/recover-migration-job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.RecoverMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_sync_migration_job(
        self,
        request: apds_20220331_models.StopSyncMigrationJobRequest,
    ) -> apds_20220331_models.StopSyncMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_sync_migration_job_with_options(request, headers, runtime)

    async def stop_sync_migration_job_async(
        self,
        request: apds_20220331_models.StopSyncMigrationJobRequest,
    ) -> apds_20220331_models.StopSyncMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_sync_migration_job_with_options_async(request, headers, runtime)

    def stop_sync_migration_job_with_options(
        self,
        request: apds_20220331_models.StopSyncMigrationJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.StopSyncMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_type):
            query['jobType'] = request.job_type
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopSyncMigrationJob',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-job/unsync-migration-job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.StopSyncMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_sync_migration_job_with_options_async(
        self,
        request: apds_20220331_models.StopSyncMigrationJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.StopSyncMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_type):
            query['jobType'] = request.job_type
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopSyncMigrationJob',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-job/unsync-migration-job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.StopSyncMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_migration_job(
        self,
        request: apds_20220331_models.SyncMigrationJobRequest,
    ) -> apds_20220331_models.SyncMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.sync_migration_job_with_options(request, headers, runtime)

    async def sync_migration_job_async(
        self,
        request: apds_20220331_models.SyncMigrationJobRequest,
    ) -> apds_20220331_models.SyncMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.sync_migration_job_with_options_async(request, headers, runtime)

    def sync_migration_job_with_options(
        self,
        request: apds_20220331_models.SyncMigrationJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.SyncMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_type):
            query['jobType'] = request.job_type
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.regions):
            query['regions'] = request.regions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncMigrationJob',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-job/sync-migration-job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.SyncMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_migration_job_with_options_async(
        self,
        request: apds_20220331_models.SyncMigrationJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apds_20220331_models.SyncMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_type):
            query['jobType'] = request.job_type
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.regions):
            query['regions'] = request.regions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncMigrationJob',
            version='2022-03-31',
            protocol='HTTPS',
            pathname=f'/okss-services/migration-job/sync-migration-job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apds_20220331_models.SyncMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )
