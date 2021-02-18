# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dts20200101 import models as dts_20200101_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'dts.aliyuncs.com',
            'cn-beijing': 'dts.aliyuncs.com',
            'cn-zhangjiakou': 'dts.aliyuncs.com',
            'cn-huhehaote': 'dts.aliyuncs.com',
            'cn-hangzhou': 'dts.aliyuncs.com',
            'cn-shanghai': 'dts.aliyuncs.com',
            'cn-shenzhen': 'dts.aliyuncs.com',
            'cn-hongkong': 'dts.aliyuncs.com',
            'ap-southeast-1': 'dts.aliyuncs.com',
            'ap-southeast-2': 'dts.aliyuncs.com',
            'ap-southeast-3': 'dts.aliyuncs.com',
            'ap-southeast-5': 'dts.aliyuncs.com',
            'eu-west-1': 'dts.aliyuncs.com',
            'us-west-1': 'dts.aliyuncs.com',
            'us-east-1': 'dts.aliyuncs.com',
            'eu-central-1': 'dts.aliyuncs.com',
            'me-east-1': 'dts.aliyuncs.com',
            'ap-south-1': 'dts.aliyuncs.com',
            'cn-hangzhou-finance': 'dts.aliyuncs.com',
            'cn-shanghai-finance-1': 'dts.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dts.aliyuncs.com',
            'cn-north-2-gov-1': 'dts.aliyuncs.com',
            'ap-northeast-2-pop': 'dts.aliyuncs.com',
            'cn-beijing-finance-1': 'dts.aliyuncs.com',
            'cn-beijing-finance-pop': 'dts.aliyuncs.com',
            'cn-beijing-gov-1': 'dts.aliyuncs.com',
            'cn-beijing-nu16-b01': 'dts.aliyuncs.com',
            'cn-chengdu': 'dts.aliyuncs.com',
            'cn-edge-1': 'dts.aliyuncs.com',
            'cn-fujian': 'dts.aliyuncs.com',
            'cn-haidian-cm12-c01': 'dts.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'dts.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'dts.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'dts.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'dts.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'dts.aliyuncs.com',
            'cn-hangzhou-test-306': 'dts.aliyuncs.com',
            'cn-hongkong-finance-pop': 'dts.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'dts.aliyuncs.com',
            'cn-qingdao-nebula': 'dts.aliyuncs.com',
            'cn-shanghai-et15-b01': 'dts.aliyuncs.com',
            'cn-shanghai-et2-b01': 'dts.aliyuncs.com',
            'cn-shanghai-inner': 'dts.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'dts.aliyuncs.com',
            'cn-shenzhen-inner': 'dts.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'dts.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'dts.aliyuncs.com',
            'cn-wuhan': 'dts.aliyuncs.com',
            'cn-wulanchabu': 'dts.aliyuncs.com',
            'cn-yushanfang': 'dts.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'dts.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'dts.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'dts.aliyuncs.com',
            'eu-west-1-oxs': 'dts.aliyuncs.com',
            'rus-west-1-pop': 'dts.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dts', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        request: dts_20200101_models.ConfigureMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureMigrationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ConfigureMigrationJobResponse().from_map(
            self.do_rpcrequest('ConfigureMigrationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def configure_migration_job_with_options_async(
        self,
        request: dts_20200101_models.ConfigureMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureMigrationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ConfigureMigrationJobResponse().from_map(
            await self.do_rpcrequest_async('ConfigureMigrationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def configure_migration_job(
        self,
        request: dts_20200101_models.ConfigureMigrationJobRequest,
    ) -> dts_20200101_models.ConfigureMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.configure_migration_job_with_options(request, runtime)

    async def configure_migration_job_async(
        self,
        request: dts_20200101_models.ConfigureMigrationJobRequest,
    ) -> dts_20200101_models.ConfigureMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.configure_migration_job_with_options_async(request, runtime)

    def configure_migration_job_alert_with_options(
        self,
        request: dts_20200101_models.ConfigureMigrationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureMigrationJobAlertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ConfigureMigrationJobAlertResponse().from_map(
            self.do_rpcrequest('ConfigureMigrationJobAlert', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def configure_migration_job_alert_with_options_async(
        self,
        request: dts_20200101_models.ConfigureMigrationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureMigrationJobAlertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ConfigureMigrationJobAlertResponse().from_map(
            await self.do_rpcrequest_async('ConfigureMigrationJobAlert', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def configure_migration_job_alert(
        self,
        request: dts_20200101_models.ConfigureMigrationJobAlertRequest,
    ) -> dts_20200101_models.ConfigureMigrationJobAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.configure_migration_job_alert_with_options(request, runtime)

    async def configure_migration_job_alert_async(
        self,
        request: dts_20200101_models.ConfigureMigrationJobAlertRequest,
    ) -> dts_20200101_models.ConfigureMigrationJobAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.configure_migration_job_alert_with_options_async(request, runtime)

    def configure_subscription_instance_with_options(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ConfigureSubscriptionInstanceResponse().from_map(
            self.do_rpcrequest('ConfigureSubscriptionInstance', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def configure_subscription_instance_with_options_async(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ConfigureSubscriptionInstanceResponse().from_map(
            await self.do_rpcrequest_async('ConfigureSubscriptionInstance', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def configure_subscription_instance(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceRequest,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.configure_subscription_instance_with_options(request, runtime)

    async def configure_subscription_instance_async(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceRequest,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.configure_subscription_instance_with_options_async(request, runtime)

    def configure_subscription_instance_alert_with_options(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse().from_map(
            self.do_rpcrequest('ConfigureSubscriptionInstanceAlert', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def configure_subscription_instance_alert_with_options_async(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse().from_map(
            await self.do_rpcrequest_async('ConfigureSubscriptionInstanceAlert', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def configure_subscription_instance_alert(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceAlertRequest,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.configure_subscription_instance_alert_with_options(request, runtime)

    async def configure_subscription_instance_alert_async(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceAlertRequest,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.configure_subscription_instance_alert_with_options_async(request, runtime)

    def configure_synchronization_job_with_options(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSynchronizationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ConfigureSynchronizationJobResponse().from_map(
            self.do_rpcrequest('ConfigureSynchronizationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def configure_synchronization_job_with_options_async(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSynchronizationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ConfigureSynchronizationJobResponse().from_map(
            await self.do_rpcrequest_async('ConfigureSynchronizationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def configure_synchronization_job(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobRequest,
    ) -> dts_20200101_models.ConfigureSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.configure_synchronization_job_with_options(request, runtime)

    async def configure_synchronization_job_async(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobRequest,
    ) -> dts_20200101_models.ConfigureSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.configure_synchronization_job_with_options_async(request, runtime)

    def configure_synchronization_job_alert_with_options(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSynchronizationJobAlertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ConfigureSynchronizationJobAlertResponse().from_map(
            self.do_rpcrequest('ConfigureSynchronizationJobAlert', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def configure_synchronization_job_alert_with_options_async(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSynchronizationJobAlertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ConfigureSynchronizationJobAlertResponse().from_map(
            await self.do_rpcrequest_async('ConfigureSynchronizationJobAlert', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def configure_synchronization_job_alert(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobAlertRequest,
    ) -> dts_20200101_models.ConfigureSynchronizationJobAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.configure_synchronization_job_alert_with_options(request, runtime)

    async def configure_synchronization_job_alert_async(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobAlertRequest,
    ) -> dts_20200101_models.ConfigureSynchronizationJobAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.configure_synchronization_job_alert_with_options_async(request, runtime)

    def configure_synchronization_job_replicator_compare_with_options(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse().from_map(
            self.do_rpcrequest('ConfigureSynchronizationJobReplicatorCompare', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def configure_synchronization_job_replicator_compare_with_options_async(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse().from_map(
            await self.do_rpcrequest_async('ConfigureSynchronizationJobReplicatorCompare', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def configure_synchronization_job_replicator_compare(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareRequest,
    ) -> dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse:
        runtime = util_models.RuntimeOptions()
        return self.configure_synchronization_job_replicator_compare_with_options(request, runtime)

    async def configure_synchronization_job_replicator_compare_async(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareRequest,
    ) -> dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.configure_synchronization_job_replicator_compare_with_options_async(request, runtime)

    def create_consumer_group_with_options(
        self,
        request: dts_20200101_models.CreateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateConsumerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.CreateConsumerGroupResponse().from_map(
            self.do_rpcrequest('CreateConsumerGroup', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_consumer_group_with_options_async(
        self,
        request: dts_20200101_models.CreateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateConsumerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.CreateConsumerGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateConsumerGroup', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_consumer_group(
        self,
        request: dts_20200101_models.CreateConsumerGroupRequest,
    ) -> dts_20200101_models.CreateConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_group_with_options(request, runtime)

    async def create_consumer_group_async(
        self,
        request: dts_20200101_models.CreateConsumerGroupRequest,
    ) -> dts_20200101_models.CreateConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_consumer_group_with_options_async(request, runtime)

    def create_migration_job_with_options(
        self,
        request: dts_20200101_models.CreateMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateMigrationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.CreateMigrationJobResponse().from_map(
            self.do_rpcrequest('CreateMigrationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_migration_job_with_options_async(
        self,
        request: dts_20200101_models.CreateMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateMigrationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.CreateMigrationJobResponse().from_map(
            await self.do_rpcrequest_async('CreateMigrationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_migration_job(
        self,
        request: dts_20200101_models.CreateMigrationJobRequest,
    ) -> dts_20200101_models.CreateMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_migration_job_with_options(request, runtime)

    async def create_migration_job_async(
        self,
        request: dts_20200101_models.CreateMigrationJobRequest,
    ) -> dts_20200101_models.CreateMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_migration_job_with_options_async(request, runtime)

    def create_subscription_instance_with_options(
        self,
        request: dts_20200101_models.CreateSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateSubscriptionInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.CreateSubscriptionInstanceResponse().from_map(
            self.do_rpcrequest('CreateSubscriptionInstance', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_subscription_instance_with_options_async(
        self,
        request: dts_20200101_models.CreateSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateSubscriptionInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.CreateSubscriptionInstanceResponse().from_map(
            await self.do_rpcrequest_async('CreateSubscriptionInstance', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_subscription_instance(
        self,
        request: dts_20200101_models.CreateSubscriptionInstanceRequest,
    ) -> dts_20200101_models.CreateSubscriptionInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_subscription_instance_with_options(request, runtime)

    async def create_subscription_instance_async(
        self,
        request: dts_20200101_models.CreateSubscriptionInstanceRequest,
    ) -> dts_20200101_models.CreateSubscriptionInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_subscription_instance_with_options_async(request, runtime)

    def create_synchronization_job_with_options(
        self,
        request: dts_20200101_models.CreateSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateSynchronizationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.CreateSynchronizationJobResponse().from_map(
            self.do_rpcrequest('CreateSynchronizationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_synchronization_job_with_options_async(
        self,
        request: dts_20200101_models.CreateSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateSynchronizationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.CreateSynchronizationJobResponse().from_map(
            await self.do_rpcrequest_async('CreateSynchronizationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_synchronization_job(
        self,
        request: dts_20200101_models.CreateSynchronizationJobRequest,
    ) -> dts_20200101_models.CreateSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_synchronization_job_with_options(request, runtime)

    async def create_synchronization_job_async(
        self,
        request: dts_20200101_models.CreateSynchronizationJobRequest,
    ) -> dts_20200101_models.CreateSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_synchronization_job_with_options_async(request, runtime)

    def delete_consumer_group_with_options(
        self,
        request: dts_20200101_models.DeleteConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteConsumerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DeleteConsumerGroupResponse().from_map(
            self.do_rpcrequest('DeleteConsumerGroup', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_consumer_group_with_options_async(
        self,
        request: dts_20200101_models.DeleteConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteConsumerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DeleteConsumerGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteConsumerGroup', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_consumer_group(
        self,
        request: dts_20200101_models.DeleteConsumerGroupRequest,
    ) -> dts_20200101_models.DeleteConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_group_with_options(request, runtime)

    async def delete_consumer_group_async(
        self,
        request: dts_20200101_models.DeleteConsumerGroupRequest,
    ) -> dts_20200101_models.DeleteConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_consumer_group_with_options_async(request, runtime)

    def delete_migration_job_with_options(
        self,
        request: dts_20200101_models.DeleteMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteMigrationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DeleteMigrationJobResponse().from_map(
            self.do_rpcrequest('DeleteMigrationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_migration_job_with_options_async(
        self,
        request: dts_20200101_models.DeleteMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteMigrationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DeleteMigrationJobResponse().from_map(
            await self.do_rpcrequest_async('DeleteMigrationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_migration_job(
        self,
        request: dts_20200101_models.DeleteMigrationJobRequest,
    ) -> dts_20200101_models.DeleteMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_migration_job_with_options(request, runtime)

    async def delete_migration_job_async(
        self,
        request: dts_20200101_models.DeleteMigrationJobRequest,
    ) -> dts_20200101_models.DeleteMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_migration_job_with_options_async(request, runtime)

    def delete_subscription_instance_with_options(
        self,
        request: dts_20200101_models.DeleteSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteSubscriptionInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DeleteSubscriptionInstanceResponse().from_map(
            self.do_rpcrequest('DeleteSubscriptionInstance', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_subscription_instance_with_options_async(
        self,
        request: dts_20200101_models.DeleteSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteSubscriptionInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DeleteSubscriptionInstanceResponse().from_map(
            await self.do_rpcrequest_async('DeleteSubscriptionInstance', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_subscription_instance(
        self,
        request: dts_20200101_models.DeleteSubscriptionInstanceRequest,
    ) -> dts_20200101_models.DeleteSubscriptionInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_subscription_instance_with_options(request, runtime)

    async def delete_subscription_instance_async(
        self,
        request: dts_20200101_models.DeleteSubscriptionInstanceRequest,
    ) -> dts_20200101_models.DeleteSubscriptionInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_subscription_instance_with_options_async(request, runtime)

    def delete_synchronization_job_with_options(
        self,
        request: dts_20200101_models.DeleteSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteSynchronizationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DeleteSynchronizationJobResponse().from_map(
            self.do_rpcrequest('DeleteSynchronizationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_synchronization_job_with_options_async(
        self,
        request: dts_20200101_models.DeleteSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteSynchronizationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DeleteSynchronizationJobResponse().from_map(
            await self.do_rpcrequest_async('DeleteSynchronizationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_synchronization_job(
        self,
        request: dts_20200101_models.DeleteSynchronizationJobRequest,
    ) -> dts_20200101_models.DeleteSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_synchronization_job_with_options(request, runtime)

    async def delete_synchronization_job_async(
        self,
        request: dts_20200101_models.DeleteSynchronizationJobRequest,
    ) -> dts_20200101_models.DeleteSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_synchronization_job_with_options_async(request, runtime)

    def describe_connection_status_with_options(
        self,
        request: dts_20200101_models.DescribeConnectionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeConnectionStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeConnectionStatusResponse().from_map(
            self.do_rpcrequest('DescribeConnectionStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_connection_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeConnectionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeConnectionStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeConnectionStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeConnectionStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_connection_status(
        self,
        request: dts_20200101_models.DescribeConnectionStatusRequest,
    ) -> dts_20200101_models.DescribeConnectionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_connection_status_with_options(request, runtime)

    async def describe_connection_status_async(
        self,
        request: dts_20200101_models.DescribeConnectionStatusRequest,
    ) -> dts_20200101_models.DescribeConnectionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_connection_status_with_options_async(request, runtime)

    def describe_consumer_group_with_options(
        self,
        request: dts_20200101_models.DescribeConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeConsumerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeConsumerGroupResponse().from_map(
            self.do_rpcrequest('DescribeConsumerGroup', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_consumer_group_with_options_async(
        self,
        request: dts_20200101_models.DescribeConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeConsumerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeConsumerGroupResponse().from_map(
            await self.do_rpcrequest_async('DescribeConsumerGroup', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_consumer_group(
        self,
        request: dts_20200101_models.DescribeConsumerGroupRequest,
    ) -> dts_20200101_models.DescribeConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_consumer_group_with_options(request, runtime)

    async def describe_consumer_group_async(
        self,
        request: dts_20200101_models.DescribeConsumerGroupRequest,
    ) -> dts_20200101_models.DescribeConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_consumer_group_with_options_async(request, runtime)

    def describe_dtsipwith_options(
        self,
        request: dts_20200101_models.DescribeDTSIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDTSIPResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeDTSIPResponse().from_map(
            self.do_rpcrequest('DescribeDTSIP', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dtsipwith_options_async(
        self,
        request: dts_20200101_models.DescribeDTSIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDTSIPResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeDTSIPResponse().from_map(
            await self.do_rpcrequest_async('DescribeDTSIP', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dtsip(
        self,
        request: dts_20200101_models.DescribeDTSIPRequest,
    ) -> dts_20200101_models.DescribeDTSIPResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dtsipwith_options(request, runtime)

    async def describe_dtsip_async(
        self,
        request: dts_20200101_models.DescribeDTSIPRequest,
    ) -> dts_20200101_models.DescribeDTSIPResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dtsipwith_options_async(request, runtime)

    def describe_endpoint_switch_status_with_options(
        self,
        request: dts_20200101_models.DescribeEndpointSwitchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeEndpointSwitchStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeEndpointSwitchStatusResponse().from_map(
            self.do_rpcrequest('DescribeEndpointSwitchStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_endpoint_switch_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeEndpointSwitchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeEndpointSwitchStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeEndpointSwitchStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeEndpointSwitchStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_endpoint_switch_status(
        self,
        request: dts_20200101_models.DescribeEndpointSwitchStatusRequest,
    ) -> dts_20200101_models.DescribeEndpointSwitchStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_endpoint_switch_status_with_options(request, runtime)

    async def describe_endpoint_switch_status_async(
        self,
        request: dts_20200101_models.DescribeEndpointSwitchStatusRequest,
    ) -> dts_20200101_models.DescribeEndpointSwitchStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_endpoint_switch_status_with_options_async(request, runtime)

    def describe_initialization_status_with_options(
        self,
        request: dts_20200101_models.DescribeInitializationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeInitializationStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeInitializationStatusResponse().from_map(
            self.do_rpcrequest('DescribeInitializationStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_initialization_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeInitializationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeInitializationStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeInitializationStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeInitializationStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_initialization_status(
        self,
        request: dts_20200101_models.DescribeInitializationStatusRequest,
    ) -> dts_20200101_models.DescribeInitializationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_initialization_status_with_options(request, runtime)

    async def describe_initialization_status_async(
        self,
        request: dts_20200101_models.DescribeInitializationStatusRequest,
    ) -> dts_20200101_models.DescribeInitializationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_initialization_status_with_options_async(request, runtime)

    def describe_migration_job_alert_with_options(
        self,
        request: dts_20200101_models.DescribeMigrationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobAlertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeMigrationJobAlertResponse().from_map(
            self.do_rpcrequest('DescribeMigrationJobAlert', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_migration_job_alert_with_options_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobAlertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeMigrationJobAlertResponse().from_map(
            await self.do_rpcrequest_async('DescribeMigrationJobAlert', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_migration_job_alert(
        self,
        request: dts_20200101_models.DescribeMigrationJobAlertRequest,
    ) -> dts_20200101_models.DescribeMigrationJobAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_job_alert_with_options(request, runtime)

    async def describe_migration_job_alert_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobAlertRequest,
    ) -> dts_20200101_models.DescribeMigrationJobAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_migration_job_alert_with_options_async(request, runtime)

    def describe_migration_job_detail_with_options(
        self,
        request: dts_20200101_models.DescribeMigrationJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeMigrationJobDetailResponse().from_map(
            self.do_rpcrequest('DescribeMigrationJobDetail', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_migration_job_detail_with_options_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeMigrationJobDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeMigrationJobDetail', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_migration_job_detail(
        self,
        request: dts_20200101_models.DescribeMigrationJobDetailRequest,
    ) -> dts_20200101_models.DescribeMigrationJobDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_job_detail_with_options(request, runtime)

    async def describe_migration_job_detail_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobDetailRequest,
    ) -> dts_20200101_models.DescribeMigrationJobDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_migration_job_detail_with_options_async(request, runtime)

    def describe_migration_jobs_with_options(
        self,
        request: dts_20200101_models.DescribeMigrationJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeMigrationJobsResponse().from_map(
            self.do_rpcrequest('DescribeMigrationJobs', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_migration_jobs_with_options_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeMigrationJobsResponse().from_map(
            await self.do_rpcrequest_async('DescribeMigrationJobs', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_migration_jobs(
        self,
        request: dts_20200101_models.DescribeMigrationJobsRequest,
    ) -> dts_20200101_models.DescribeMigrationJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_jobs_with_options(request, runtime)

    async def describe_migration_jobs_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobsRequest,
    ) -> dts_20200101_models.DescribeMigrationJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_migration_jobs_with_options_async(request, runtime)

    def describe_migration_job_status_with_options(
        self,
        request: dts_20200101_models.DescribeMigrationJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeMigrationJobStatusResponse().from_map(
            self.do_rpcrequest('DescribeMigrationJobStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_migration_job_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeMigrationJobStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeMigrationJobStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_migration_job_status(
        self,
        request: dts_20200101_models.DescribeMigrationJobStatusRequest,
    ) -> dts_20200101_models.DescribeMigrationJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_job_status_with_options(request, runtime)

    async def describe_migration_job_status_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobStatusRequest,
    ) -> dts_20200101_models.DescribeMigrationJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_migration_job_status_with_options_async(request, runtime)

    def describe_subscription_instance_alert_with_options(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceAlertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeSubscriptionInstanceAlertResponse().from_map(
            self.do_rpcrequest('DescribeSubscriptionInstanceAlert', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_subscription_instance_alert_with_options_async(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceAlertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeSubscriptionInstanceAlertResponse().from_map(
            await self.do_rpcrequest_async('DescribeSubscriptionInstanceAlert', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_subscription_instance_alert(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceAlertRequest,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_instance_alert_with_options(request, runtime)

    async def describe_subscription_instance_alert_async(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceAlertRequest,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_subscription_instance_alert_with_options_async(request, runtime)

    def describe_subscription_instances_with_options(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeSubscriptionInstancesResponse().from_map(
            self.do_rpcrequest('DescribeSubscriptionInstances', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_subscription_instances_with_options_async(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeSubscriptionInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeSubscriptionInstances', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_subscription_instances(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstancesRequest,
    ) -> dts_20200101_models.DescribeSubscriptionInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_instances_with_options(request, runtime)

    async def describe_subscription_instances_async(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstancesRequest,
    ) -> dts_20200101_models.DescribeSubscriptionInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_subscription_instances_with_options_async(request, runtime)

    def describe_subscription_instance_status_with_options(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeSubscriptionInstanceStatusResponse().from_map(
            self.do_rpcrequest('DescribeSubscriptionInstanceStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_subscription_instance_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeSubscriptionInstanceStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeSubscriptionInstanceStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_subscription_instance_status(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceStatusRequest,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_instance_status_with_options(request, runtime)

    async def describe_subscription_instance_status_async(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceStatusRequest,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_subscription_instance_status_with_options_async(request, runtime)

    def describe_synchronization_job_alert_with_options(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobAlertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeSynchronizationJobAlertResponse().from_map(
            self.do_rpcrequest('DescribeSynchronizationJobAlert', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_synchronization_job_alert_with_options_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobAlertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeSynchronizationJobAlertResponse().from_map(
            await self.do_rpcrequest_async('DescribeSynchronizationJobAlert', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_synchronization_job_alert(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobAlertRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_job_alert_with_options(request, runtime)

    async def describe_synchronization_job_alert_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobAlertRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronization_job_alert_with_options_async(request, runtime)

    def describe_synchronization_job_replicator_compare_with_options(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobReplicatorCompareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse().from_map(
            self.do_rpcrequest('DescribeSynchronizationJobReplicatorCompare', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_synchronization_job_replicator_compare_with_options_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobReplicatorCompareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse().from_map(
            await self.do_rpcrequest_async('DescribeSynchronizationJobReplicatorCompare', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_synchronization_job_replicator_compare(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobReplicatorCompareRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_job_replicator_compare_with_options(request, runtime)

    async def describe_synchronization_job_replicator_compare_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobReplicatorCompareRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronization_job_replicator_compare_with_options_async(request, runtime)

    def describe_synchronization_jobs_with_options(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeSynchronizationJobsResponse().from_map(
            self.do_rpcrequest('DescribeSynchronizationJobs', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_synchronization_jobs_with_options_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeSynchronizationJobsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSynchronizationJobs', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_synchronization_jobs(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobsRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_jobs_with_options(request, runtime)

    async def describe_synchronization_jobs_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobsRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronization_jobs_with_options_async(request, runtime)

    def describe_synchronization_job_status_with_options(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeSynchronizationJobStatusResponse().from_map(
            self.do_rpcrequest('DescribeSynchronizationJobStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_synchronization_job_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeSynchronizationJobStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeSynchronizationJobStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_synchronization_job_status(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_job_status_with_options(request, runtime)

    async def describe_synchronization_job_status_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronization_job_status_with_options_async(request, runtime)

    def describe_synchronization_job_status_list_with_options(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeSynchronizationJobStatusListResponse().from_map(
            self.do_rpcrequest('DescribeSynchronizationJobStatusList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_synchronization_job_status_list_with_options_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeSynchronizationJobStatusListResponse().from_map(
            await self.do_rpcrequest_async('DescribeSynchronizationJobStatusList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_synchronization_job_status_list(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusListRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_job_status_list_with_options(request, runtime)

    async def describe_synchronization_job_status_list_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusListRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronization_job_status_list_with_options_async(request, runtime)

    def describe_synchronization_object_modify_status_with_options(
        self,
        request: dts_20200101_models.DescribeSynchronizationObjectModifyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse().from_map(
            self.do_rpcrequest('DescribeSynchronizationObjectModifyStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_synchronization_object_modify_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationObjectModifyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeSynchronizationObjectModifyStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_synchronization_object_modify_status(
        self,
        request: dts_20200101_models.DescribeSynchronizationObjectModifyStatusRequest,
    ) -> dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_object_modify_status_with_options(request, runtime)

    async def describe_synchronization_object_modify_status_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationObjectModifyStatusRequest,
    ) -> dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronization_object_modify_status_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: dts_20200101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: dts_20200101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: dts_20200101_models.ListTagResourcesRequest,
    ) -> dts_20200101_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: dts_20200101_models.ListTagResourcesRequest,
    ) -> dts_20200101_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_consumer_group_password_with_options(
        self,
        request: dts_20200101_models.ModifyConsumerGroupPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyConsumerGroupPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ModifyConsumerGroupPasswordResponse().from_map(
            self.do_rpcrequest('ModifyConsumerGroupPassword', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_consumer_group_password_with_options_async(
        self,
        request: dts_20200101_models.ModifyConsumerGroupPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyConsumerGroupPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ModifyConsumerGroupPasswordResponse().from_map(
            await self.do_rpcrequest_async('ModifyConsumerGroupPassword', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_consumer_group_password(
        self,
        request: dts_20200101_models.ModifyConsumerGroupPasswordRequest,
    ) -> dts_20200101_models.ModifyConsumerGroupPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_consumer_group_password_with_options(request, runtime)

    async def modify_consumer_group_password_async(
        self,
        request: dts_20200101_models.ModifyConsumerGroupPasswordRequest,
    ) -> dts_20200101_models.ModifyConsumerGroupPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_consumer_group_password_with_options_async(request, runtime)

    def modify_consumption_timestamp_with_options(
        self,
        request: dts_20200101_models.ModifyConsumptionTimestampRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyConsumptionTimestampResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ModifyConsumptionTimestampResponse().from_map(
            self.do_rpcrequest('ModifyConsumptionTimestamp', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_consumption_timestamp_with_options_async(
        self,
        request: dts_20200101_models.ModifyConsumptionTimestampRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyConsumptionTimestampResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ModifyConsumptionTimestampResponse().from_map(
            await self.do_rpcrequest_async('ModifyConsumptionTimestamp', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_consumption_timestamp(
        self,
        request: dts_20200101_models.ModifyConsumptionTimestampRequest,
    ) -> dts_20200101_models.ModifyConsumptionTimestampResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_consumption_timestamp_with_options(request, runtime)

    async def modify_consumption_timestamp_async(
        self,
        request: dts_20200101_models.ModifyConsumptionTimestampRequest,
    ) -> dts_20200101_models.ModifyConsumptionTimestampResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_consumption_timestamp_with_options_async(request, runtime)

    def modify_subscription_object_with_options(
        self,
        request: dts_20200101_models.ModifySubscriptionObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifySubscriptionObjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ModifySubscriptionObjectResponse().from_map(
            self.do_rpcrequest('ModifySubscriptionObject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_subscription_object_with_options_async(
        self,
        request: dts_20200101_models.ModifySubscriptionObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifySubscriptionObjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ModifySubscriptionObjectResponse().from_map(
            await self.do_rpcrequest_async('ModifySubscriptionObject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_subscription_object(
        self,
        request: dts_20200101_models.ModifySubscriptionObjectRequest,
    ) -> dts_20200101_models.ModifySubscriptionObjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_subscription_object_with_options(request, runtime)

    async def modify_subscription_object_async(
        self,
        request: dts_20200101_models.ModifySubscriptionObjectRequest,
    ) -> dts_20200101_models.ModifySubscriptionObjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_subscription_object_with_options_async(request, runtime)

    def modify_synchronization_object_with_options(
        self,
        request: dts_20200101_models.ModifySynchronizationObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifySynchronizationObjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ModifySynchronizationObjectResponse().from_map(
            self.do_rpcrequest('ModifySynchronizationObject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_synchronization_object_with_options_async(
        self,
        request: dts_20200101_models.ModifySynchronizationObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifySynchronizationObjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ModifySynchronizationObjectResponse().from_map(
            await self.do_rpcrequest_async('ModifySynchronizationObject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_synchronization_object(
        self,
        request: dts_20200101_models.ModifySynchronizationObjectRequest,
    ) -> dts_20200101_models.ModifySynchronizationObjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_synchronization_object_with_options(request, runtime)

    async def modify_synchronization_object_async(
        self,
        request: dts_20200101_models.ModifySynchronizationObjectRequest,
    ) -> dts_20200101_models.ModifySynchronizationObjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_synchronization_object_with_options_async(request, runtime)

    def reset_synchronization_job_with_options(
        self,
        request: dts_20200101_models.ResetSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ResetSynchronizationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ResetSynchronizationJobResponse().from_map(
            self.do_rpcrequest('ResetSynchronizationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_synchronization_job_with_options_async(
        self,
        request: dts_20200101_models.ResetSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ResetSynchronizationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ResetSynchronizationJobResponse().from_map(
            await self.do_rpcrequest_async('ResetSynchronizationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_synchronization_job(
        self,
        request: dts_20200101_models.ResetSynchronizationJobRequest,
    ) -> dts_20200101_models.ResetSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_synchronization_job_with_options(request, runtime)

    async def reset_synchronization_job_async(
        self,
        request: dts_20200101_models.ResetSynchronizationJobRequest,
    ) -> dts_20200101_models.ResetSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_synchronization_job_with_options_async(request, runtime)

    def shield_precheck_with_options(
        self,
        request: dts_20200101_models.ShieldPrecheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ShieldPrecheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ShieldPrecheckResponse().from_map(
            self.do_rpcrequest('ShieldPrecheck', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def shield_precheck_with_options_async(
        self,
        request: dts_20200101_models.ShieldPrecheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ShieldPrecheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.ShieldPrecheckResponse().from_map(
            await self.do_rpcrequest_async('ShieldPrecheck', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def shield_precheck(
        self,
        request: dts_20200101_models.ShieldPrecheckRequest,
    ) -> dts_20200101_models.ShieldPrecheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.shield_precheck_with_options(request, runtime)

    async def shield_precheck_async(
        self,
        request: dts_20200101_models.ShieldPrecheckRequest,
    ) -> dts_20200101_models.ShieldPrecheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.shield_precheck_with_options_async(request, runtime)

    def start_migration_job_with_options(
        self,
        request: dts_20200101_models.StartMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartMigrationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.StartMigrationJobResponse().from_map(
            self.do_rpcrequest('StartMigrationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_migration_job_with_options_async(
        self,
        request: dts_20200101_models.StartMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartMigrationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.StartMigrationJobResponse().from_map(
            await self.do_rpcrequest_async('StartMigrationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_migration_job(
        self,
        request: dts_20200101_models.StartMigrationJobRequest,
    ) -> dts_20200101_models.StartMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_migration_job_with_options(request, runtime)

    async def start_migration_job_async(
        self,
        request: dts_20200101_models.StartMigrationJobRequest,
    ) -> dts_20200101_models.StartMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_migration_job_with_options_async(request, runtime)

    def start_subscription_instance_with_options(
        self,
        request: dts_20200101_models.StartSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartSubscriptionInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.StartSubscriptionInstanceResponse().from_map(
            self.do_rpcrequest('StartSubscriptionInstance', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_subscription_instance_with_options_async(
        self,
        request: dts_20200101_models.StartSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartSubscriptionInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.StartSubscriptionInstanceResponse().from_map(
            await self.do_rpcrequest_async('StartSubscriptionInstance', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_subscription_instance(
        self,
        request: dts_20200101_models.StartSubscriptionInstanceRequest,
    ) -> dts_20200101_models.StartSubscriptionInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_subscription_instance_with_options(request, runtime)

    async def start_subscription_instance_async(
        self,
        request: dts_20200101_models.StartSubscriptionInstanceRequest,
    ) -> dts_20200101_models.StartSubscriptionInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_subscription_instance_with_options_async(request, runtime)

    def start_synchronization_job_with_options(
        self,
        request: dts_20200101_models.StartSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartSynchronizationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.StartSynchronizationJobResponse().from_map(
            self.do_rpcrequest('StartSynchronizationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_synchronization_job_with_options_async(
        self,
        request: dts_20200101_models.StartSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartSynchronizationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.StartSynchronizationJobResponse().from_map(
            await self.do_rpcrequest_async('StartSynchronizationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_synchronization_job(
        self,
        request: dts_20200101_models.StartSynchronizationJobRequest,
    ) -> dts_20200101_models.StartSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_synchronization_job_with_options(request, runtime)

    async def start_synchronization_job_async(
        self,
        request: dts_20200101_models.StartSynchronizationJobRequest,
    ) -> dts_20200101_models.StartSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_synchronization_job_with_options_async(request, runtime)

    def stop_migration_job_with_options(
        self,
        request: dts_20200101_models.StopMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StopMigrationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.StopMigrationJobResponse().from_map(
            self.do_rpcrequest('StopMigrationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_migration_job_with_options_async(
        self,
        request: dts_20200101_models.StopMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StopMigrationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.StopMigrationJobResponse().from_map(
            await self.do_rpcrequest_async('StopMigrationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_migration_job(
        self,
        request: dts_20200101_models.StopMigrationJobRequest,
    ) -> dts_20200101_models.StopMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_migration_job_with_options(request, runtime)

    async def stop_migration_job_async(
        self,
        request: dts_20200101_models.StopMigrationJobRequest,
    ) -> dts_20200101_models.StopMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_migration_job_with_options_async(request, runtime)

    def suspend_migration_job_with_options(
        self,
        request: dts_20200101_models.SuspendMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SuspendMigrationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.SuspendMigrationJobResponse().from_map(
            self.do_rpcrequest('SuspendMigrationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def suspend_migration_job_with_options_async(
        self,
        request: dts_20200101_models.SuspendMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SuspendMigrationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.SuspendMigrationJobResponse().from_map(
            await self.do_rpcrequest_async('SuspendMigrationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def suspend_migration_job(
        self,
        request: dts_20200101_models.SuspendMigrationJobRequest,
    ) -> dts_20200101_models.SuspendMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_migration_job_with_options(request, runtime)

    async def suspend_migration_job_async(
        self,
        request: dts_20200101_models.SuspendMigrationJobRequest,
    ) -> dts_20200101_models.SuspendMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_migration_job_with_options_async(request, runtime)

    def suspend_synchronization_job_with_options(
        self,
        request: dts_20200101_models.SuspendSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SuspendSynchronizationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.SuspendSynchronizationJobResponse().from_map(
            self.do_rpcrequest('SuspendSynchronizationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def suspend_synchronization_job_with_options_async(
        self,
        request: dts_20200101_models.SuspendSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SuspendSynchronizationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.SuspendSynchronizationJobResponse().from_map(
            await self.do_rpcrequest_async('SuspendSynchronizationJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def suspend_synchronization_job(
        self,
        request: dts_20200101_models.SuspendSynchronizationJobRequest,
    ) -> dts_20200101_models.SuspendSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_synchronization_job_with_options(request, runtime)

    async def suspend_synchronization_job_async(
        self,
        request: dts_20200101_models.SuspendSynchronizationJobRequest,
    ) -> dts_20200101_models.SuspendSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_synchronization_job_with_options_async(request, runtime)

    def switch_synchronization_endpoint_with_options(
        self,
        request: dts_20200101_models.SwitchSynchronizationEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SwitchSynchronizationEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.SwitchSynchronizationEndpointResponse().from_map(
            self.do_rpcrequest('SwitchSynchronizationEndpoint', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def switch_synchronization_endpoint_with_options_async(
        self,
        request: dts_20200101_models.SwitchSynchronizationEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SwitchSynchronizationEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.SwitchSynchronizationEndpointResponse().from_map(
            await self.do_rpcrequest_async('SwitchSynchronizationEndpoint', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_synchronization_endpoint(
        self,
        request: dts_20200101_models.SwitchSynchronizationEndpointRequest,
    ) -> dts_20200101_models.SwitchSynchronizationEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_synchronization_endpoint_with_options(request, runtime)

    async def switch_synchronization_endpoint_async(
        self,
        request: dts_20200101_models.SwitchSynchronizationEndpointRequest,
    ) -> dts_20200101_models.SwitchSynchronizationEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_synchronization_endpoint_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: dts_20200101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: dts_20200101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: dts_20200101_models.TagResourcesRequest,
    ) -> dts_20200101_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: dts_20200101_models.TagResourcesRequest,
    ) -> dts_20200101_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: dts_20200101_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: dts_20200101_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dts_20200101_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: dts_20200101_models.UntagResourcesRequest,
    ) -> dts_20200101_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: dts_20200101_models.UntagResourcesRequest,
    ) -> dts_20200101_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
