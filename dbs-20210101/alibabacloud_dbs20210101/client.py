# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dbs20210101 import models as dbs_20210101_models
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
            'cn-qingdao': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-beijing': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-chengdu': 'dbs-api.cn-chengdu.aliyuncs.com',
            'cn-zhangjiakou': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-huhehaote': 'dbs-api.cn-huhehaote.aliyuncs.com',
            'cn-hangzhou': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-hongkong': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'ap-southeast-1': 'dbs-api.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'dbs-api.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'dbs-api.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'dbs-api.ap-southeast-5.aliyuncs.com',
            'ap-northeast-1': 'dbs-api.ap-northeast-1.aliyuncs.com',
            'us-west-1': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'us-east-1': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'eu-central-1': 'dbs-api.eu-central-1.aliyuncs.com',
            'cn-hangzhou-finance': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-shanghai-finance-1': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'ap-south-1': 'dbs-api.ap-south-1.aliyuncs.com',
            'eu-west-1': 'dbs-api.eu-west-1.aliyuncs.com',
            'me-east-1': 'dbs-api.me-east-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dbs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_sandbox_instance_with_options(
        self,
        request: dbs_20210101_models.CreateSandboxInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20210101_models.CreateSandboxInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.sandbox_instance_name):
            query['SandboxInstanceName'] = request.sandbox_instance_name
        if not UtilClient.is_unset(request.sandbox_password):
            query['SandboxPassword'] = request.sandbox_password
        if not UtilClient.is_unset(request.sandbox_specification):
            query['SandboxSpecification'] = request.sandbox_specification
        if not UtilClient.is_unset(request.sandbox_type):
            query['SandboxType'] = request.sandbox_type
        if not UtilClient.is_unset(request.sandbox_user):
            query['SandboxUser'] = request.sandbox_user
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_switch_id):
            query['VpcSwitchId'] = request.vpc_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSandboxInstance',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.CreateSandboxInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sandbox_instance_with_options_async(
        self,
        request: dbs_20210101_models.CreateSandboxInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20210101_models.CreateSandboxInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.sandbox_instance_name):
            query['SandboxInstanceName'] = request.sandbox_instance_name
        if not UtilClient.is_unset(request.sandbox_password):
            query['SandboxPassword'] = request.sandbox_password
        if not UtilClient.is_unset(request.sandbox_specification):
            query['SandboxSpecification'] = request.sandbox_specification
        if not UtilClient.is_unset(request.sandbox_type):
            query['SandboxType'] = request.sandbox_type
        if not UtilClient.is_unset(request.sandbox_user):
            query['SandboxUser'] = request.sandbox_user
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_switch_id):
            query['VpcSwitchId'] = request.vpc_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSandboxInstance',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.CreateSandboxInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sandbox_instance(
        self,
        request: dbs_20210101_models.CreateSandboxInstanceRequest,
    ) -> dbs_20210101_models.CreateSandboxInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sandbox_instance_with_options(request, runtime)

    async def create_sandbox_instance_async(
        self,
        request: dbs_20210101_models.CreateSandboxInstanceRequest,
    ) -> dbs_20210101_models.CreateSandboxInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sandbox_instance_with_options_async(request, runtime)

    def delete_sandbox_instance_with_options(
        self,
        request: dbs_20210101_models.DeleteSandboxInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20210101_models.DeleteSandboxInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSandboxInstance',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.DeleteSandboxInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sandbox_instance_with_options_async(
        self,
        request: dbs_20210101_models.DeleteSandboxInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20210101_models.DeleteSandboxInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSandboxInstance',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.DeleteSandboxInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sandbox_instance(
        self,
        request: dbs_20210101_models.DeleteSandboxInstanceRequest,
    ) -> dbs_20210101_models.DeleteSandboxInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sandbox_instance_with_options(request, runtime)

    async def delete_sandbox_instance_async(
        self,
        request: dbs_20210101_models.DeleteSandboxInstanceRequest,
    ) -> dbs_20210101_models.DeleteSandboxInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sandbox_instance_with_options_async(request, runtime)

    def describe_sandbox_backup_sets_with_options(
        self,
        request: dbs_20210101_models.DescribeSandboxBackupSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20210101_models.DescribeSandboxBackupSetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSandboxBackupSets',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.DescribeSandboxBackupSetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sandbox_backup_sets_with_options_async(
        self,
        request: dbs_20210101_models.DescribeSandboxBackupSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20210101_models.DescribeSandboxBackupSetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSandboxBackupSets',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.DescribeSandboxBackupSetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sandbox_backup_sets(
        self,
        request: dbs_20210101_models.DescribeSandboxBackupSetsRequest,
    ) -> dbs_20210101_models.DescribeSandboxBackupSetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sandbox_backup_sets_with_options(request, runtime)

    async def describe_sandbox_backup_sets_async(
        self,
        request: dbs_20210101_models.DescribeSandboxBackupSetsRequest,
    ) -> dbs_20210101_models.DescribeSandboxBackupSetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sandbox_backup_sets_with_options_async(request, runtime)

    def describe_sandbox_instances_with_options(
        self,
        request: dbs_20210101_models.DescribeSandboxInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20210101_models.DescribeSandboxInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSandboxInstances',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.DescribeSandboxInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sandbox_instances_with_options_async(
        self,
        request: dbs_20210101_models.DescribeSandboxInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20210101_models.DescribeSandboxInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSandboxInstances',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.DescribeSandboxInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sandbox_instances(
        self,
        request: dbs_20210101_models.DescribeSandboxInstancesRequest,
    ) -> dbs_20210101_models.DescribeSandboxInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sandbox_instances_with_options(request, runtime)

    async def describe_sandbox_instances_async(
        self,
        request: dbs_20210101_models.DescribeSandboxInstancesRequest,
    ) -> dbs_20210101_models.DescribeSandboxInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sandbox_instances_with_options_async(request, runtime)

    def describe_sandbox_recovery_time_with_options(
        self,
        request: dbs_20210101_models.DescribeSandboxRecoveryTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20210101_models.DescribeSandboxRecoveryTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSandboxRecoveryTime',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.DescribeSandboxRecoveryTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sandbox_recovery_time_with_options_async(
        self,
        request: dbs_20210101_models.DescribeSandboxRecoveryTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20210101_models.DescribeSandboxRecoveryTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSandboxRecoveryTime',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.DescribeSandboxRecoveryTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sandbox_recovery_time(
        self,
        request: dbs_20210101_models.DescribeSandboxRecoveryTimeRequest,
    ) -> dbs_20210101_models.DescribeSandboxRecoveryTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sandbox_recovery_time_with_options(request, runtime)

    async def describe_sandbox_recovery_time_async(
        self,
        request: dbs_20210101_models.DescribeSandboxRecoveryTimeRequest,
    ) -> dbs_20210101_models.DescribeSandboxRecoveryTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sandbox_recovery_time_with_options_async(request, runtime)
