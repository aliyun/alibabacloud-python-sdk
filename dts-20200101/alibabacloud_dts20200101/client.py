# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dts20200101 import models as dts_20200101_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_oss_sdk.client import Client as OSSClient
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models


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

    def configure_dts_job_with_options(
        self,
        request: dts_20200101_models.ConfigureDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureDtsJobResponse:
        """
        @summary Configures a data migration or synchronization task.
        
        @param request: ConfigureDtsJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureDtsJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.data_check_configure):
            query['DataCheckConfigure'] = request.data_check_configure
        if not UtilClient.is_unset(request.data_initialization):
            query['DataInitialization'] = request.data_initialization
        if not UtilClient.is_unset(request.data_synchronization):
            query['DataSynchronization'] = request.data_synchronization
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.delay_notice):
            query['DelayNotice'] = request.delay_notice
        if not UtilClient.is_unset(request.delay_phone):
            query['DelayPhone'] = request.delay_phone
        if not UtilClient.is_unset(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not UtilClient.is_unset(request.dest_ca_certificate_oss_url):
            query['DestCaCertificateOssUrl'] = request.dest_ca_certificate_oss_url
        if not UtilClient.is_unset(request.dest_ca_certificate_password):
            query['DestCaCertificatePassword'] = request.dest_ca_certificate_password
        if not UtilClient.is_unset(request.dest_client_cert_oss_url):
            query['DestClientCertOssUrl'] = request.dest_client_cert_oss_url
        if not UtilClient.is_unset(request.dest_client_key_oss_url):
            query['DestClientKeyOssUrl'] = request.dest_client_key_oss_url
        if not UtilClient.is_unset(request.dest_client_password):
            query['DestClientPassword'] = request.dest_client_password
        if not UtilClient.is_unset(request.dest_primary_vsw_id):
            query['DestPrimaryVswId'] = request.dest_primary_vsw_id
        if not UtilClient.is_unset(request.dest_secondary_vsw_id):
            query['DestSecondaryVswId'] = request.dest_secondary_vsw_id
        if not UtilClient.is_unset(request.destination_endpoint_data_base_name):
            query['DestinationEndpointDataBaseName'] = request.destination_endpoint_data_base_name
        if not UtilClient.is_unset(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not UtilClient.is_unset(request.destination_endpoint_ip):
            query['DestinationEndpointIP'] = request.destination_endpoint_ip
        if not UtilClient.is_unset(request.destination_endpoint_instance_id):
            query['DestinationEndpointInstanceID'] = request.destination_endpoint_instance_id
        if not UtilClient.is_unset(request.destination_endpoint_instance_type):
            query['DestinationEndpointInstanceType'] = request.destination_endpoint_instance_type
        if not UtilClient.is_unset(request.destination_endpoint_oracle_sid):
            query['DestinationEndpointOracleSID'] = request.destination_endpoint_oracle_sid
        if not UtilClient.is_unset(request.destination_endpoint_owner_id):
            query['DestinationEndpointOwnerID'] = request.destination_endpoint_owner_id
        if not UtilClient.is_unset(request.destination_endpoint_password):
            query['DestinationEndpointPassword'] = request.destination_endpoint_password
        if not UtilClient.is_unset(request.destination_endpoint_port):
            query['DestinationEndpointPort'] = request.destination_endpoint_port
        if not UtilClient.is_unset(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not UtilClient.is_unset(request.destination_endpoint_role):
            query['DestinationEndpointRole'] = request.destination_endpoint_role
        if not UtilClient.is_unset(request.destination_endpoint_user_name):
            query['DestinationEndpointUserName'] = request.destination_endpoint_user_name
        if not UtilClient.is_unset(request.disaster_recovery_job):
            query['DisasterRecoveryJob'] = request.disaster_recovery_job
        if not UtilClient.is_unset(request.dts_bis_label):
            query['DtsBisLabel'] = request.dts_bis_label
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not UtilClient.is_unset(request.error_notice):
            query['ErrorNotice'] = request.error_notice
        if not UtilClient.is_unset(request.error_phone):
            query['ErrorPhone'] = request.error_phone
        if not UtilClient.is_unset(request.file_oss_url):
            query['FileOssUrl'] = request.file_oss_url
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.max_du):
            query['MaxDu'] = request.max_du
        if not UtilClient.is_unset(request.min_du):
            query['MinDu'] = request.min_du
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not UtilClient.is_unset(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not UtilClient.is_unset(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not UtilClient.is_unset(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not UtilClient.is_unset(request.source_endpoint_owner_id):
            query['SourceEndpointOwnerID'] = request.source_endpoint_owner_id
        if not UtilClient.is_unset(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.source_endpoint_role):
            query['SourceEndpointRole'] = request.source_endpoint_role
        if not UtilClient.is_unset(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not UtilClient.is_unset(request.source_endpoint_vswitch_id):
            query['SourceEndpointVSwitchID'] = request.source_endpoint_vswitch_id
        if not UtilClient.is_unset(request.src_ca_certificate_oss_url):
            query['SrcCaCertificateOssUrl'] = request.src_ca_certificate_oss_url
        if not UtilClient.is_unset(request.src_ca_certificate_password):
            query['SrcCaCertificatePassword'] = request.src_ca_certificate_password
        if not UtilClient.is_unset(request.src_client_cert_oss_url):
            query['SrcClientCertOssUrl'] = request.src_client_cert_oss_url
        if not UtilClient.is_unset(request.src_client_key_oss_url):
            query['SrcClientKeyOssUrl'] = request.src_client_key_oss_url
        if not UtilClient.is_unset(request.src_client_password):
            query['SrcClientPassword'] = request.src_client_password
        if not UtilClient.is_unset(request.src_primary_vsw_id):
            query['SrcPrimaryVswId'] = request.src_primary_vsw_id
        if not UtilClient.is_unset(request.src_secondary_vsw_id):
            query['SrcSecondaryVswId'] = request.src_secondary_vsw_id
        if not UtilClient.is_unset(request.structure_initialization):
            query['StructureInitialization'] = request.structure_initialization
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        body = {}
        if not UtilClient.is_unset(request.db_list):
            body['DbList'] = request.db_list
        if not UtilClient.is_unset(request.reserve):
            body['Reserve'] = request.reserve
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigureDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ConfigureDtsJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ConfigureDtsJobResponse(),
                self.execute(params, req, runtime)
            )

    async def configure_dts_job_with_options_async(
        self,
        request: dts_20200101_models.ConfigureDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureDtsJobResponse:
        """
        @summary Configures a data migration or synchronization task.
        
        @param request: ConfigureDtsJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureDtsJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.data_check_configure):
            query['DataCheckConfigure'] = request.data_check_configure
        if not UtilClient.is_unset(request.data_initialization):
            query['DataInitialization'] = request.data_initialization
        if not UtilClient.is_unset(request.data_synchronization):
            query['DataSynchronization'] = request.data_synchronization
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.delay_notice):
            query['DelayNotice'] = request.delay_notice
        if not UtilClient.is_unset(request.delay_phone):
            query['DelayPhone'] = request.delay_phone
        if not UtilClient.is_unset(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not UtilClient.is_unset(request.dest_ca_certificate_oss_url):
            query['DestCaCertificateOssUrl'] = request.dest_ca_certificate_oss_url
        if not UtilClient.is_unset(request.dest_ca_certificate_password):
            query['DestCaCertificatePassword'] = request.dest_ca_certificate_password
        if not UtilClient.is_unset(request.dest_client_cert_oss_url):
            query['DestClientCertOssUrl'] = request.dest_client_cert_oss_url
        if not UtilClient.is_unset(request.dest_client_key_oss_url):
            query['DestClientKeyOssUrl'] = request.dest_client_key_oss_url
        if not UtilClient.is_unset(request.dest_client_password):
            query['DestClientPassword'] = request.dest_client_password
        if not UtilClient.is_unset(request.dest_primary_vsw_id):
            query['DestPrimaryVswId'] = request.dest_primary_vsw_id
        if not UtilClient.is_unset(request.dest_secondary_vsw_id):
            query['DestSecondaryVswId'] = request.dest_secondary_vsw_id
        if not UtilClient.is_unset(request.destination_endpoint_data_base_name):
            query['DestinationEndpointDataBaseName'] = request.destination_endpoint_data_base_name
        if not UtilClient.is_unset(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not UtilClient.is_unset(request.destination_endpoint_ip):
            query['DestinationEndpointIP'] = request.destination_endpoint_ip
        if not UtilClient.is_unset(request.destination_endpoint_instance_id):
            query['DestinationEndpointInstanceID'] = request.destination_endpoint_instance_id
        if not UtilClient.is_unset(request.destination_endpoint_instance_type):
            query['DestinationEndpointInstanceType'] = request.destination_endpoint_instance_type
        if not UtilClient.is_unset(request.destination_endpoint_oracle_sid):
            query['DestinationEndpointOracleSID'] = request.destination_endpoint_oracle_sid
        if not UtilClient.is_unset(request.destination_endpoint_owner_id):
            query['DestinationEndpointOwnerID'] = request.destination_endpoint_owner_id
        if not UtilClient.is_unset(request.destination_endpoint_password):
            query['DestinationEndpointPassword'] = request.destination_endpoint_password
        if not UtilClient.is_unset(request.destination_endpoint_port):
            query['DestinationEndpointPort'] = request.destination_endpoint_port
        if not UtilClient.is_unset(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not UtilClient.is_unset(request.destination_endpoint_role):
            query['DestinationEndpointRole'] = request.destination_endpoint_role
        if not UtilClient.is_unset(request.destination_endpoint_user_name):
            query['DestinationEndpointUserName'] = request.destination_endpoint_user_name
        if not UtilClient.is_unset(request.disaster_recovery_job):
            query['DisasterRecoveryJob'] = request.disaster_recovery_job
        if not UtilClient.is_unset(request.dts_bis_label):
            query['DtsBisLabel'] = request.dts_bis_label
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not UtilClient.is_unset(request.error_notice):
            query['ErrorNotice'] = request.error_notice
        if not UtilClient.is_unset(request.error_phone):
            query['ErrorPhone'] = request.error_phone
        if not UtilClient.is_unset(request.file_oss_url):
            query['FileOssUrl'] = request.file_oss_url
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.max_du):
            query['MaxDu'] = request.max_du
        if not UtilClient.is_unset(request.min_du):
            query['MinDu'] = request.min_du
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not UtilClient.is_unset(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not UtilClient.is_unset(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not UtilClient.is_unset(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not UtilClient.is_unset(request.source_endpoint_owner_id):
            query['SourceEndpointOwnerID'] = request.source_endpoint_owner_id
        if not UtilClient.is_unset(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.source_endpoint_role):
            query['SourceEndpointRole'] = request.source_endpoint_role
        if not UtilClient.is_unset(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not UtilClient.is_unset(request.source_endpoint_vswitch_id):
            query['SourceEndpointVSwitchID'] = request.source_endpoint_vswitch_id
        if not UtilClient.is_unset(request.src_ca_certificate_oss_url):
            query['SrcCaCertificateOssUrl'] = request.src_ca_certificate_oss_url
        if not UtilClient.is_unset(request.src_ca_certificate_password):
            query['SrcCaCertificatePassword'] = request.src_ca_certificate_password
        if not UtilClient.is_unset(request.src_client_cert_oss_url):
            query['SrcClientCertOssUrl'] = request.src_client_cert_oss_url
        if not UtilClient.is_unset(request.src_client_key_oss_url):
            query['SrcClientKeyOssUrl'] = request.src_client_key_oss_url
        if not UtilClient.is_unset(request.src_client_password):
            query['SrcClientPassword'] = request.src_client_password
        if not UtilClient.is_unset(request.src_primary_vsw_id):
            query['SrcPrimaryVswId'] = request.src_primary_vsw_id
        if not UtilClient.is_unset(request.src_secondary_vsw_id):
            query['SrcSecondaryVswId'] = request.src_secondary_vsw_id
        if not UtilClient.is_unset(request.structure_initialization):
            query['StructureInitialization'] = request.structure_initialization
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        body = {}
        if not UtilClient.is_unset(request.db_list):
            body['DbList'] = request.db_list
        if not UtilClient.is_unset(request.reserve):
            body['Reserve'] = request.reserve
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigureDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ConfigureDtsJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ConfigureDtsJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def configure_dts_job(
        self,
        request: dts_20200101_models.ConfigureDtsJobRequest,
    ) -> dts_20200101_models.ConfigureDtsJobResponse:
        """
        @summary Configures a data migration or synchronization task.
        
        @param request: ConfigureDtsJobRequest
        @return: ConfigureDtsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.configure_dts_job_with_options(request, runtime)

    async def configure_dts_job_async(
        self,
        request: dts_20200101_models.ConfigureDtsJobRequest,
    ) -> dts_20200101_models.ConfigureDtsJobResponse:
        """
        @summary Configures a data migration or synchronization task.
        
        @param request: ConfigureDtsJobRequest
        @return: ConfigureDtsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.configure_dts_job_with_options_async(request, runtime)

    def configure_dts_job_advance(
        self,
        request: dts_20200101_models.ConfigureDtsJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureDtsJobResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='Dts',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        configure_dts_job_req = dts_20200101_models.ConfigureDtsJobRequest()
        OpenApiUtilClient.convert(request, configure_dts_job_req)
        if not UtilClient.is_unset(request.file_oss_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_oss_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            configure_dts_job_req.file_oss_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        configure_dts_job_resp = self.configure_dts_job_with_options(configure_dts_job_req, runtime)
        return configure_dts_job_resp

    async def configure_dts_job_advance_async(
        self,
        request: dts_20200101_models.ConfigureDtsJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureDtsJobResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='Dts',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        configure_dts_job_req = dts_20200101_models.ConfigureDtsJobRequest()
        OpenApiUtilClient.convert(request, configure_dts_job_req)
        if not UtilClient.is_unset(request.file_oss_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_oss_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            configure_dts_job_req.file_oss_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        configure_dts_job_resp = await self.configure_dts_job_with_options_async(configure_dts_job_req, runtime)
        return configure_dts_job_resp

    def configure_migration_job_with_options(
        self,
        request: dts_20200101_models.ConfigureMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureMigrationJobResponse:
        """
        @summary Configures a data migration task.
        
        @param request: ConfigureMigrationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureMigrationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not UtilClient.is_unset(request.migration_reserved):
            query['MigrationReserved'] = request.migration_reserved
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.migration_mode):
            query['MigrationMode'] = request.migration_mode
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        body = {}
        if not UtilClient.is_unset(request.migration_object):
            body['MigrationObject'] = request.migration_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigureMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ConfigureMigrationJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ConfigureMigrationJobResponse(),
                self.execute(params, req, runtime)
            )

    async def configure_migration_job_with_options_async(
        self,
        request: dts_20200101_models.ConfigureMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureMigrationJobResponse:
        """
        @summary Configures a data migration task.
        
        @param request: ConfigureMigrationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureMigrationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not UtilClient.is_unset(request.migration_reserved):
            query['MigrationReserved'] = request.migration_reserved
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.migration_mode):
            query['MigrationMode'] = request.migration_mode
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        body = {}
        if not UtilClient.is_unset(request.migration_object):
            body['MigrationObject'] = request.migration_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigureMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ConfigureMigrationJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ConfigureMigrationJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def configure_migration_job(
        self,
        request: dts_20200101_models.ConfigureMigrationJobRequest,
    ) -> dts_20200101_models.ConfigureMigrationJobResponse:
        """
        @summary Configures a data migration task.
        
        @param request: ConfigureMigrationJobRequest
        @return: ConfigureMigrationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.configure_migration_job_with_options(request, runtime)

    async def configure_migration_job_async(
        self,
        request: dts_20200101_models.ConfigureMigrationJobRequest,
    ) -> dts_20200101_models.ConfigureMigrationJobResponse:
        """
        @summary Configures a data migration task.
        
        @param request: ConfigureMigrationJobRequest
        @return: ConfigureMigrationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.configure_migration_job_with_options_async(request, runtime)

    def configure_migration_job_alert_with_options(
        self,
        request: dts_20200101_models.ConfigureMigrationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureMigrationJobAlertResponse:
        """
        @summary Configures alert settings to monitor a data migration instance.
        
        @param request: ConfigureMigrationJobAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureMigrationJobAlertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not UtilClient.is_unset(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not UtilClient.is_unset(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not UtilClient.is_unset(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not UtilClient.is_unset(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureMigrationJobAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ConfigureMigrationJobAlertResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ConfigureMigrationJobAlertResponse(),
                self.execute(params, req, runtime)
            )

    async def configure_migration_job_alert_with_options_async(
        self,
        request: dts_20200101_models.ConfigureMigrationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureMigrationJobAlertResponse:
        """
        @summary Configures alert settings to monitor a data migration instance.
        
        @param request: ConfigureMigrationJobAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureMigrationJobAlertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not UtilClient.is_unset(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not UtilClient.is_unset(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not UtilClient.is_unset(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not UtilClient.is_unset(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureMigrationJobAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ConfigureMigrationJobAlertResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ConfigureMigrationJobAlertResponse(),
                await self.execute_async(params, req, runtime)
            )

    def configure_migration_job_alert(
        self,
        request: dts_20200101_models.ConfigureMigrationJobAlertRequest,
    ) -> dts_20200101_models.ConfigureMigrationJobAlertResponse:
        """
        @summary Configures alert settings to monitor a data migration instance.
        
        @param request: ConfigureMigrationJobAlertRequest
        @return: ConfigureMigrationJobAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.configure_migration_job_alert_with_options(request, runtime)

    async def configure_migration_job_alert_async(
        self,
        request: dts_20200101_models.ConfigureMigrationJobAlertRequest,
    ) -> dts_20200101_models.ConfigureMigrationJobAlertResponse:
        """
        @summary Configures alert settings to monitor a data migration instance.
        
        @param request: ConfigureMigrationJobAlertRequest
        @return: ConfigureMigrationJobAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.configure_migration_job_alert_with_options_async(request, runtime)

    def configure_subscription_with_options(
        self,
        request: dts_20200101_models.ConfigureSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSubscriptionResponse:
        """
        @summary Configures a change tracking task.
        
        @description >  You can preview related API operation parameters when you configure a change tracking task in the Data Transmission Service (DTS) console. This helps you configure the request parameters of this API operation. For more information, see [Preview the request parameters of API operations](https://help.aliyun.com/document_detail/2851612.html).
        
        @param request: ConfigureSubscriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureSubscriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.db_list):
            query['DbList'] = request.db_list
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.delay_notice):
            query['DelayNotice'] = request.delay_notice
        if not UtilClient.is_unset(request.delay_phone):
            query['DelayPhone'] = request.delay_phone
        if not UtilClient.is_unset(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not UtilClient.is_unset(request.dts_bis_label):
            query['DtsBisLabel'] = request.dts_bis_label
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not UtilClient.is_unset(request.error_notice):
            query['ErrorNotice'] = request.error_notice
        if not UtilClient.is_unset(request.error_phone):
            query['ErrorPhone'] = request.error_phone
        if not UtilClient.is_unset(request.max_du):
            query['MaxDu'] = request.max_du
        if not UtilClient.is_unset(request.min_du):
            query['MinDu'] = request.min_du
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserve):
            query['Reserve'] = request.reserve
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not UtilClient.is_unset(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not UtilClient.is_unset(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not UtilClient.is_unset(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not UtilClient.is_unset(request.source_endpoint_owner_id):
            query['SourceEndpointOwnerID'] = request.source_endpoint_owner_id
        if not UtilClient.is_unset(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.source_endpoint_role):
            query['SourceEndpointRole'] = request.source_endpoint_role
        if not UtilClient.is_unset(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not UtilClient.is_unset(request.src_ca_certificate_oss_url):
            query['SrcCaCertificateOssUrl'] = request.src_ca_certificate_oss_url
        if not UtilClient.is_unset(request.src_ca_certificate_password):
            query['SrcCaCertificatePassword'] = request.src_ca_certificate_password
        if not UtilClient.is_unset(request.src_client_cert_oss_url):
            query['SrcClientCertOssUrl'] = request.src_client_cert_oss_url
        if not UtilClient.is_unset(request.src_client_key_oss_url):
            query['SrcClientKeyOssUrl'] = request.src_client_key_oss_url
        if not UtilClient.is_unset(request.src_client_password):
            query['SrcClientPassword'] = request.src_client_password
        if not UtilClient.is_unset(request.subscription_data_type_ddl):
            query['SubscriptionDataTypeDDL'] = request.subscription_data_type_ddl
        if not UtilClient.is_unset(request.subscription_data_type_dml):
            query['SubscriptionDataTypeDML'] = request.subscription_data_type_dml
        if not UtilClient.is_unset(request.subscription_instance_network_type):
            query['SubscriptionInstanceNetworkType'] = request.subscription_instance_network_type
        if not UtilClient.is_unset(request.subscription_instance_vpcid):
            query['SubscriptionInstanceVPCId'] = request.subscription_instance_vpcid
        if not UtilClient.is_unset(request.subscription_instance_vswitch_id):
            query['SubscriptionInstanceVSwitchId'] = request.subscription_instance_vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSubscription',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSubscriptionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSubscriptionResponse(),
                self.execute(params, req, runtime)
            )

    async def configure_subscription_with_options_async(
        self,
        request: dts_20200101_models.ConfigureSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSubscriptionResponse:
        """
        @summary Configures a change tracking task.
        
        @description >  You can preview related API operation parameters when you configure a change tracking task in the Data Transmission Service (DTS) console. This helps you configure the request parameters of this API operation. For more information, see [Preview the request parameters of API operations](https://help.aliyun.com/document_detail/2851612.html).
        
        @param request: ConfigureSubscriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureSubscriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.db_list):
            query['DbList'] = request.db_list
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.delay_notice):
            query['DelayNotice'] = request.delay_notice
        if not UtilClient.is_unset(request.delay_phone):
            query['DelayPhone'] = request.delay_phone
        if not UtilClient.is_unset(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not UtilClient.is_unset(request.dts_bis_label):
            query['DtsBisLabel'] = request.dts_bis_label
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not UtilClient.is_unset(request.error_notice):
            query['ErrorNotice'] = request.error_notice
        if not UtilClient.is_unset(request.error_phone):
            query['ErrorPhone'] = request.error_phone
        if not UtilClient.is_unset(request.max_du):
            query['MaxDu'] = request.max_du
        if not UtilClient.is_unset(request.min_du):
            query['MinDu'] = request.min_du
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserve):
            query['Reserve'] = request.reserve
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not UtilClient.is_unset(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not UtilClient.is_unset(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not UtilClient.is_unset(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not UtilClient.is_unset(request.source_endpoint_owner_id):
            query['SourceEndpointOwnerID'] = request.source_endpoint_owner_id
        if not UtilClient.is_unset(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.source_endpoint_role):
            query['SourceEndpointRole'] = request.source_endpoint_role
        if not UtilClient.is_unset(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not UtilClient.is_unset(request.src_ca_certificate_oss_url):
            query['SrcCaCertificateOssUrl'] = request.src_ca_certificate_oss_url
        if not UtilClient.is_unset(request.src_ca_certificate_password):
            query['SrcCaCertificatePassword'] = request.src_ca_certificate_password
        if not UtilClient.is_unset(request.src_client_cert_oss_url):
            query['SrcClientCertOssUrl'] = request.src_client_cert_oss_url
        if not UtilClient.is_unset(request.src_client_key_oss_url):
            query['SrcClientKeyOssUrl'] = request.src_client_key_oss_url
        if not UtilClient.is_unset(request.src_client_password):
            query['SrcClientPassword'] = request.src_client_password
        if not UtilClient.is_unset(request.subscription_data_type_ddl):
            query['SubscriptionDataTypeDDL'] = request.subscription_data_type_ddl
        if not UtilClient.is_unset(request.subscription_data_type_dml):
            query['SubscriptionDataTypeDML'] = request.subscription_data_type_dml
        if not UtilClient.is_unset(request.subscription_instance_network_type):
            query['SubscriptionInstanceNetworkType'] = request.subscription_instance_network_type
        if not UtilClient.is_unset(request.subscription_instance_vpcid):
            query['SubscriptionInstanceVPCId'] = request.subscription_instance_vpcid
        if not UtilClient.is_unset(request.subscription_instance_vswitch_id):
            query['SubscriptionInstanceVSwitchId'] = request.subscription_instance_vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSubscription',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSubscriptionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSubscriptionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def configure_subscription(
        self,
        request: dts_20200101_models.ConfigureSubscriptionRequest,
    ) -> dts_20200101_models.ConfigureSubscriptionResponse:
        """
        @summary Configures a change tracking task.
        
        @description >  You can preview related API operation parameters when you configure a change tracking task in the Data Transmission Service (DTS) console. This helps you configure the request parameters of this API operation. For more information, see [Preview the request parameters of API operations](https://help.aliyun.com/document_detail/2851612.html).
        
        @param request: ConfigureSubscriptionRequest
        @return: ConfigureSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.configure_subscription_with_options(request, runtime)

    async def configure_subscription_async(
        self,
        request: dts_20200101_models.ConfigureSubscriptionRequest,
    ) -> dts_20200101_models.ConfigureSubscriptionResponse:
        """
        @summary Configures a change tracking task.
        
        @description >  You can preview related API operation parameters when you configure a change tracking task in the Data Transmission Service (DTS) console. This helps you configure the request parameters of this API operation. For more information, see [Preview the request parameters of API operations](https://help.aliyun.com/document_detail/2851612.html).
        
        @param request: ConfigureSubscriptionRequest
        @return: ConfigureSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.configure_subscription_with_options_async(request, runtime)

    def configure_subscription_instance_with_options(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceResponse:
        """
        @summary Configures a change tracking instance of the previous version.
        
        @description Before you call this operation, you must call the [CreateSubscriptionInstance](https://help.aliyun.com/document_detail/49436.html) operation to create a change tracking instance.
        
        @param request: ConfigureSubscriptionInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureSubscriptionInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not UtilClient.is_unset(request.subscription_instance_name):
            query['SubscriptionInstanceName'] = request.subscription_instance_name
        if not UtilClient.is_unset(request.subscription_instance_network_type):
            query['SubscriptionInstanceNetworkType'] = request.subscription_instance_network_type
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        if not UtilClient.is_unset(request.subscription_data_type):
            query['SubscriptionDataType'] = request.subscription_data_type
        if not UtilClient.is_unset(request.subscription_instance):
            query['SubscriptionInstance'] = request.subscription_instance
        body = {}
        if not UtilClient.is_unset(request.subscription_object):
            body['SubscriptionObject'] = request.subscription_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigureSubscriptionInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSubscriptionInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSubscriptionInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def configure_subscription_instance_with_options_async(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceResponse:
        """
        @summary Configures a change tracking instance of the previous version.
        
        @description Before you call this operation, you must call the [CreateSubscriptionInstance](https://help.aliyun.com/document_detail/49436.html) operation to create a change tracking instance.
        
        @param request: ConfigureSubscriptionInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureSubscriptionInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not UtilClient.is_unset(request.subscription_instance_name):
            query['SubscriptionInstanceName'] = request.subscription_instance_name
        if not UtilClient.is_unset(request.subscription_instance_network_type):
            query['SubscriptionInstanceNetworkType'] = request.subscription_instance_network_type
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        if not UtilClient.is_unset(request.subscription_data_type):
            query['SubscriptionDataType'] = request.subscription_data_type
        if not UtilClient.is_unset(request.subscription_instance):
            query['SubscriptionInstance'] = request.subscription_instance
        body = {}
        if not UtilClient.is_unset(request.subscription_object):
            body['SubscriptionObject'] = request.subscription_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigureSubscriptionInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSubscriptionInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSubscriptionInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def configure_subscription_instance(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceRequest,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceResponse:
        """
        @summary Configures a change tracking instance of the previous version.
        
        @description Before you call this operation, you must call the [CreateSubscriptionInstance](https://help.aliyun.com/document_detail/49436.html) operation to create a change tracking instance.
        
        @param request: ConfigureSubscriptionInstanceRequest
        @return: ConfigureSubscriptionInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.configure_subscription_instance_with_options(request, runtime)

    async def configure_subscription_instance_async(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceRequest,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceResponse:
        """
        @summary Configures a change tracking instance of the previous version.
        
        @description Before you call this operation, you must call the [CreateSubscriptionInstance](https://help.aliyun.com/document_detail/49436.html) operation to create a change tracking instance.
        
        @param request: ConfigureSubscriptionInstanceRequest
        @return: ConfigureSubscriptionInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.configure_subscription_instance_with_options_async(request, runtime)

    def configure_subscription_instance_alert_with_options(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse:
        """
        @summary Configures alert settings to monitor a change tracking instance.
        
        @param request: ConfigureSubscriptionInstanceAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureSubscriptionInstanceAlertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not UtilClient.is_unset(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not UtilClient.is_unset(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not UtilClient.is_unset(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not UtilClient.is_unset(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSubscriptionInstanceAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse(),
                self.execute(params, req, runtime)
            )

    async def configure_subscription_instance_alert_with_options_async(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse:
        """
        @summary Configures alert settings to monitor a change tracking instance.
        
        @param request: ConfigureSubscriptionInstanceAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureSubscriptionInstanceAlertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not UtilClient.is_unset(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not UtilClient.is_unset(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not UtilClient.is_unset(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not UtilClient.is_unset(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSubscriptionInstanceAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse(),
                await self.execute_async(params, req, runtime)
            )

    def configure_subscription_instance_alert(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceAlertRequest,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse:
        """
        @summary Configures alert settings to monitor a change tracking instance.
        
        @param request: ConfigureSubscriptionInstanceAlertRequest
        @return: ConfigureSubscriptionInstanceAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.configure_subscription_instance_alert_with_options(request, runtime)

    async def configure_subscription_instance_alert_async(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceAlertRequest,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse:
        """
        @summary Configures alert settings to monitor a change tracking instance.
        
        @param request: ConfigureSubscriptionInstanceAlertRequest
        @return: ConfigureSubscriptionInstanceAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.configure_subscription_instance_alert_with_options_async(request, runtime)

    def configure_synchronization_job_with_options(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSynchronizationJobResponse:
        """
        @summary Configures a data synchronization task.
        
        @description Before you call this operation, you must call the [CreateSynchronizationJob](https://help.aliyun.com/document_detail/49446.html) operation to create a data synchronization instance.
        >
        After you call this operation to configure a data synchronization task, the task will be automatically started and prechecked. You do not need to call the [StartSynchronizationJob](https://help.aliyun.com/document_detail/49448.html) operation to start the task.
        A data synchronization task may fail to be started due to precheck failures. You can call the [DescribeSynchronizationJobStatus](https://help.aliyun.com/document_detail/49453.html) operation to query the status of the task. Then, you can change parameter settings based on the error messages about the precheck failures. After you fix the issue, you must call the [StartSynchronizationJob](https://help.aliyun.com/document_detail/49448.html) operation to restart the data synchronization task.
        
        @param request: ConfigureSynchronizationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.data_initialization):
            query['DataInitialization'] = request.data_initialization
        if not UtilClient.is_unset(request.migration_reserved):
            query['MigrationReserved'] = request.migration_reserved
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.structure_initialization):
            query['StructureInitialization'] = request.structure_initialization
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not UtilClient.is_unset(request.synchronization_job_name):
            query['SynchronizationJobName'] = request.synchronization_job_name
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.partition_key):
            query['PartitionKey'] = request.partition_key
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        body = {}
        if not UtilClient.is_unset(request.synchronization_objects):
            body['SynchronizationObjects'] = request.synchronization_objects
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigureSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSynchronizationJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSynchronizationJobResponse(),
                self.execute(params, req, runtime)
            )

    async def configure_synchronization_job_with_options_async(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSynchronizationJobResponse:
        """
        @summary Configures a data synchronization task.
        
        @description Before you call this operation, you must call the [CreateSynchronizationJob](https://help.aliyun.com/document_detail/49446.html) operation to create a data synchronization instance.
        >
        After you call this operation to configure a data synchronization task, the task will be automatically started and prechecked. You do not need to call the [StartSynchronizationJob](https://help.aliyun.com/document_detail/49448.html) operation to start the task.
        A data synchronization task may fail to be started due to precheck failures. You can call the [DescribeSynchronizationJobStatus](https://help.aliyun.com/document_detail/49453.html) operation to query the status of the task. Then, you can change parameter settings based on the error messages about the precheck failures. After you fix the issue, you must call the [StartSynchronizationJob](https://help.aliyun.com/document_detail/49448.html) operation to restart the data synchronization task.
        
        @param request: ConfigureSynchronizationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.data_initialization):
            query['DataInitialization'] = request.data_initialization
        if not UtilClient.is_unset(request.migration_reserved):
            query['MigrationReserved'] = request.migration_reserved
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.structure_initialization):
            query['StructureInitialization'] = request.structure_initialization
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not UtilClient.is_unset(request.synchronization_job_name):
            query['SynchronizationJobName'] = request.synchronization_job_name
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.partition_key):
            query['PartitionKey'] = request.partition_key
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        body = {}
        if not UtilClient.is_unset(request.synchronization_objects):
            body['SynchronizationObjects'] = request.synchronization_objects
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigureSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSynchronizationJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSynchronizationJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def configure_synchronization_job(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobRequest,
    ) -> dts_20200101_models.ConfigureSynchronizationJobResponse:
        """
        @summary Configures a data synchronization task.
        
        @description Before you call this operation, you must call the [CreateSynchronizationJob](https://help.aliyun.com/document_detail/49446.html) operation to create a data synchronization instance.
        >
        After you call this operation to configure a data synchronization task, the task will be automatically started and prechecked. You do not need to call the [StartSynchronizationJob](https://help.aliyun.com/document_detail/49448.html) operation to start the task.
        A data synchronization task may fail to be started due to precheck failures. You can call the [DescribeSynchronizationJobStatus](https://help.aliyun.com/document_detail/49453.html) operation to query the status of the task. Then, you can change parameter settings based on the error messages about the precheck failures. After you fix the issue, you must call the [StartSynchronizationJob](https://help.aliyun.com/document_detail/49448.html) operation to restart the data synchronization task.
        
        @param request: ConfigureSynchronizationJobRequest
        @return: ConfigureSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.configure_synchronization_job_with_options(request, runtime)

    async def configure_synchronization_job_async(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobRequest,
    ) -> dts_20200101_models.ConfigureSynchronizationJobResponse:
        """
        @summary Configures a data synchronization task.
        
        @description Before you call this operation, you must call the [CreateSynchronizationJob](https://help.aliyun.com/document_detail/49446.html) operation to create a data synchronization instance.
        >
        After you call this operation to configure a data synchronization task, the task will be automatically started and prechecked. You do not need to call the [StartSynchronizationJob](https://help.aliyun.com/document_detail/49448.html) operation to start the task.
        A data synchronization task may fail to be started due to precheck failures. You can call the [DescribeSynchronizationJobStatus](https://help.aliyun.com/document_detail/49453.html) operation to query the status of the task. Then, you can change parameter settings based on the error messages about the precheck failures. After you fix the issue, you must call the [StartSynchronizationJob](https://help.aliyun.com/document_detail/49448.html) operation to restart the data synchronization task.
        
        @param request: ConfigureSynchronizationJobRequest
        @return: ConfigureSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.configure_synchronization_job_with_options_async(request, runtime)

    def configure_synchronization_job_alert_with_options(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSynchronizationJobAlertResponse:
        """
        @summary Configures alert settings to monitor a data synchronization instance.
        
        @param request: ConfigureSynchronizationJobAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureSynchronizationJobAlertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not UtilClient.is_unset(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not UtilClient.is_unset(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not UtilClient.is_unset(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not UtilClient.is_unset(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSynchronizationJobAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSynchronizationJobAlertResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSynchronizationJobAlertResponse(),
                self.execute(params, req, runtime)
            )

    async def configure_synchronization_job_alert_with_options_async(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSynchronizationJobAlertResponse:
        """
        @summary Configures alert settings to monitor a data synchronization instance.
        
        @param request: ConfigureSynchronizationJobAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureSynchronizationJobAlertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not UtilClient.is_unset(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not UtilClient.is_unset(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not UtilClient.is_unset(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not UtilClient.is_unset(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSynchronizationJobAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSynchronizationJobAlertResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSynchronizationJobAlertResponse(),
                await self.execute_async(params, req, runtime)
            )

    def configure_synchronization_job_alert(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobAlertRequest,
    ) -> dts_20200101_models.ConfigureSynchronizationJobAlertResponse:
        """
        @summary Configures alert settings to monitor a data synchronization instance.
        
        @param request: ConfigureSynchronizationJobAlertRequest
        @return: ConfigureSynchronizationJobAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.configure_synchronization_job_alert_with_options(request, runtime)

    async def configure_synchronization_job_alert_async(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobAlertRequest,
    ) -> dts_20200101_models.ConfigureSynchronizationJobAlertResponse:
        """
        @summary Configures alert settings to monitor a data synchronization instance.
        
        @param request: ConfigureSynchronizationJobAlertRequest
        @return: ConfigureSynchronizationJobAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.configure_synchronization_job_alert_with_options_async(request, runtime)

    def configure_synchronization_job_replicator_compare_with_options(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse:
        """
        @summary Enables or disables image matching for a data synchronization instance.
        
        @param request: ConfigureSynchronizationJobReplicatorCompareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureSynchronizationJobReplicatorCompareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not UtilClient.is_unset(request.synchronization_replicator_compare_enable):
            query['SynchronizationReplicatorCompareEnable'] = request.synchronization_replicator_compare_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSynchronizationJobReplicatorCompare',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse(),
                self.execute(params, req, runtime)
            )

    async def configure_synchronization_job_replicator_compare_with_options_async(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse:
        """
        @summary Enables or disables image matching for a data synchronization instance.
        
        @param request: ConfigureSynchronizationJobReplicatorCompareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureSynchronizationJobReplicatorCompareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not UtilClient.is_unset(request.synchronization_replicator_compare_enable):
            query['SynchronizationReplicatorCompareEnable'] = request.synchronization_replicator_compare_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSynchronizationJobReplicatorCompare',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse(),
                await self.execute_async(params, req, runtime)
            )

    def configure_synchronization_job_replicator_compare(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareRequest,
    ) -> dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse:
        """
        @summary Enables or disables image matching for a data synchronization instance.
        
        @param request: ConfigureSynchronizationJobReplicatorCompareRequest
        @return: ConfigureSynchronizationJobReplicatorCompareResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.configure_synchronization_job_replicator_compare_with_options(request, runtime)

    async def configure_synchronization_job_replicator_compare_async(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareRequest,
    ) -> dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse:
        """
        @summary Enables or disables image matching for a data synchronization instance.
        
        @param request: ConfigureSynchronizationJobReplicatorCompareRequest
        @return: ConfigureSynchronizationJobReplicatorCompareResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.configure_synchronization_job_replicator_compare_with_options_async(request, runtime)

    def convert_instance_resource_group_with_options(
        self,
        request: dts_20200101_models.ConvertInstanceResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConvertInstanceResourceGroupResponse:
        """
        @summary Transfers resource groups of instance resources.
        
        @param request: ConvertInstanceResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertInstanceResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConvertInstanceResourceGroup',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ConvertInstanceResourceGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ConvertInstanceResourceGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def convert_instance_resource_group_with_options_async(
        self,
        request: dts_20200101_models.ConvertInstanceResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConvertInstanceResourceGroupResponse:
        """
        @summary Transfers resource groups of instance resources.
        
        @param request: ConvertInstanceResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertInstanceResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConvertInstanceResourceGroup',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ConvertInstanceResourceGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ConvertInstanceResourceGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def convert_instance_resource_group(
        self,
        request: dts_20200101_models.ConvertInstanceResourceGroupRequest,
    ) -> dts_20200101_models.ConvertInstanceResourceGroupResponse:
        """
        @summary Transfers resource groups of instance resources.
        
        @param request: ConvertInstanceResourceGroupRequest
        @return: ConvertInstanceResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.convert_instance_resource_group_with_options(request, runtime)

    async def convert_instance_resource_group_async(
        self,
        request: dts_20200101_models.ConvertInstanceResourceGroupRequest,
    ) -> dts_20200101_models.ConvertInstanceResourceGroupResponse:
        """
        @summary Transfers resource groups of instance resources.
        
        @param request: ConvertInstanceResourceGroupRequest
        @return: ConvertInstanceResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.convert_instance_resource_group_with_options_async(request, runtime)

    def count_job_by_condition_with_options(
        self,
        request: dts_20200101_models.CountJobByConditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CountJobByConditionResponse:
        """
        @summary Counts tasks by condition.
        
        @param request: CountJobByConditionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CountJobByConditionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dest_db_type):
            query['DestDbType'] = request.dest_db_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.src_db_type):
            query['SrcDbType'] = request.src_db_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CountJobByCondition',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.CountJobByConditionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.CountJobByConditionResponse(),
                self.execute(params, req, runtime)
            )

    async def count_job_by_condition_with_options_async(
        self,
        request: dts_20200101_models.CountJobByConditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CountJobByConditionResponse:
        """
        @summary Counts tasks by condition.
        
        @param request: CountJobByConditionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CountJobByConditionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dest_db_type):
            query['DestDbType'] = request.dest_db_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.src_db_type):
            query['SrcDbType'] = request.src_db_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CountJobByCondition',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.CountJobByConditionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.CountJobByConditionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def count_job_by_condition(
        self,
        request: dts_20200101_models.CountJobByConditionRequest,
    ) -> dts_20200101_models.CountJobByConditionResponse:
        """
        @summary Counts tasks by condition.
        
        @param request: CountJobByConditionRequest
        @return: CountJobByConditionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.count_job_by_condition_with_options(request, runtime)

    async def count_job_by_condition_async(
        self,
        request: dts_20200101_models.CountJobByConditionRequest,
    ) -> dts_20200101_models.CountJobByConditionResponse:
        """
        @summary Counts tasks by condition.
        
        @param request: CountJobByConditionRequest
        @return: CountJobByConditionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.count_job_by_condition_with_options_async(request, runtime)

    def create_consumer_channel_with_options(
        self,
        request: dts_20200101_models.CreateConsumerChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateConsumerChannelResponse:
        """
        @summary Creates a consumer group for a change tracking task. Downstream clients can use the consumer group to consume tracked data.
        
        @param request: CreateConsumerChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConsumerChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not UtilClient.is_unset(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not UtilClient.is_unset(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsumerChannel',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.CreateConsumerChannelResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.CreateConsumerChannelResponse(),
                self.execute(params, req, runtime)
            )

    async def create_consumer_channel_with_options_async(
        self,
        request: dts_20200101_models.CreateConsumerChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateConsumerChannelResponse:
        """
        @summary Creates a consumer group for a change tracking task. Downstream clients can use the consumer group to consume tracked data.
        
        @param request: CreateConsumerChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConsumerChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not UtilClient.is_unset(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not UtilClient.is_unset(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsumerChannel',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.CreateConsumerChannelResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.CreateConsumerChannelResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_consumer_channel(
        self,
        request: dts_20200101_models.CreateConsumerChannelRequest,
    ) -> dts_20200101_models.CreateConsumerChannelResponse:
        """
        @summary Creates a consumer group for a change tracking task. Downstream clients can use the consumer group to consume tracked data.
        
        @param request: CreateConsumerChannelRequest
        @return: CreateConsumerChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_channel_with_options(request, runtime)

    async def create_consumer_channel_async(
        self,
        request: dts_20200101_models.CreateConsumerChannelRequest,
    ) -> dts_20200101_models.CreateConsumerChannelResponse:
        """
        @summary Creates a consumer group for a change tracking task. Downstream clients can use the consumer group to consume tracked data.
        
        @param request: CreateConsumerChannelRequest
        @return: CreateConsumerChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_consumer_channel_with_options_async(request, runtime)

    def create_consumer_group_with_options(
        self,
        request: dts_20200101_models.CreateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateConsumerGroupResponse:
        """
        @summary Creates a consumer group for a change tracking instance.
        
        @param request: CreateConsumerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not UtilClient.is_unset(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not UtilClient.is_unset(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.CreateConsumerGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.CreateConsumerGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def create_consumer_group_with_options_async(
        self,
        request: dts_20200101_models.CreateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateConsumerGroupResponse:
        """
        @summary Creates a consumer group for a change tracking instance.
        
        @param request: CreateConsumerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not UtilClient.is_unset(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not UtilClient.is_unset(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.CreateConsumerGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.CreateConsumerGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_consumer_group(
        self,
        request: dts_20200101_models.CreateConsumerGroupRequest,
    ) -> dts_20200101_models.CreateConsumerGroupResponse:
        """
        @summary Creates a consumer group for a change tracking instance.
        
        @param request: CreateConsumerGroupRequest
        @return: CreateConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_group_with_options(request, runtime)

    async def create_consumer_group_async(
        self,
        request: dts_20200101_models.CreateConsumerGroupRequest,
    ) -> dts_20200101_models.CreateConsumerGroupResponse:
        """
        @summary Creates a consumer group for a change tracking instance.
        
        @param request: CreateConsumerGroupRequest
        @return: CreateConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_consumer_group_with_options_async(request, runtime)

    def create_dedicated_cluster_monitor_rule_with_options(
        self,
        request: dts_20200101_models.CreateDedicatedClusterMonitorRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateDedicatedClusterMonitorRuleResponse:
        """
        @summary Creates an alert rule.
        
        @param request: CreateDedicatedClusterMonitorRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDedicatedClusterMonitorRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cpu_alarm_threshold):
            query['CpuAlarmThreshold'] = request.cpu_alarm_threshold
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.disk_alarm_threshold):
            query['DiskAlarmThreshold'] = request.disk_alarm_threshold
        if not UtilClient.is_unset(request.du_alarm_threshold):
            query['DuAlarmThreshold'] = request.du_alarm_threshold
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mem_alarm_threshold):
            query['MemAlarmThreshold'] = request.mem_alarm_threshold
        if not UtilClient.is_unset(request.notice_switch):
            query['NoticeSwitch'] = request.notice_switch
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phones):
            query['Phones'] = request.phones
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDedicatedClusterMonitorRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.CreateDedicatedClusterMonitorRuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.CreateDedicatedClusterMonitorRuleResponse(),
                self.execute(params, req, runtime)
            )

    async def create_dedicated_cluster_monitor_rule_with_options_async(
        self,
        request: dts_20200101_models.CreateDedicatedClusterMonitorRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateDedicatedClusterMonitorRuleResponse:
        """
        @summary Creates an alert rule.
        
        @param request: CreateDedicatedClusterMonitorRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDedicatedClusterMonitorRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cpu_alarm_threshold):
            query['CpuAlarmThreshold'] = request.cpu_alarm_threshold
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.disk_alarm_threshold):
            query['DiskAlarmThreshold'] = request.disk_alarm_threshold
        if not UtilClient.is_unset(request.du_alarm_threshold):
            query['DuAlarmThreshold'] = request.du_alarm_threshold
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mem_alarm_threshold):
            query['MemAlarmThreshold'] = request.mem_alarm_threshold
        if not UtilClient.is_unset(request.notice_switch):
            query['NoticeSwitch'] = request.notice_switch
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phones):
            query['Phones'] = request.phones
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDedicatedClusterMonitorRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.CreateDedicatedClusterMonitorRuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.CreateDedicatedClusterMonitorRuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_dedicated_cluster_monitor_rule(
        self,
        request: dts_20200101_models.CreateDedicatedClusterMonitorRuleRequest,
    ) -> dts_20200101_models.CreateDedicatedClusterMonitorRuleResponse:
        """
        @summary Creates an alert rule.
        
        @param request: CreateDedicatedClusterMonitorRuleRequest
        @return: CreateDedicatedClusterMonitorRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_cluster_monitor_rule_with_options(request, runtime)

    async def create_dedicated_cluster_monitor_rule_async(
        self,
        request: dts_20200101_models.CreateDedicatedClusterMonitorRuleRequest,
    ) -> dts_20200101_models.CreateDedicatedClusterMonitorRuleResponse:
        """
        @summary Creates an alert rule.
        
        @param request: CreateDedicatedClusterMonitorRuleRequest
        @return: CreateDedicatedClusterMonitorRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_cluster_monitor_rule_with_options_async(request, runtime)

    def create_dts_instance_with_options(
        self,
        request: dts_20200101_models.CreateDtsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateDtsInstanceResponse:
        """
        @summary Purchases a Data Transmission Service (DTS) instance.
        
        @description    Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of DTS.
        If you want to run a DTS task on a DTS dedicated cluster, you must configure the task before you purchase a DTS instance. You can call the [ConfigureDtsJob](https://help.aliyun.com/document_detail/208399.html) operation to configure a DTS task.
        
        @param request: CreateDtsInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDtsInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not UtilClient.is_unset(request.compute_unit):
            query['ComputeUnit'] = request.compute_unit
        if not UtilClient.is_unset(request.database_count):
            query['DatabaseCount'] = request.database_count
        if not UtilClient.is_unset(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not UtilClient.is_unset(request.destination_region):
            query['DestinationRegion'] = request.destination_region
        if not UtilClient.is_unset(request.dts_region):
            query['DtsRegion'] = request.dts_region
        if not UtilClient.is_unset(request.du):
            query['Du'] = request.du
        if not UtilClient.is_unset(request.fee_type):
            query['FeeType'] = request.fee_type
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.max_du):
            query['MaxDu'] = request.max_du
        if not UtilClient.is_unset(request.min_du):
            query['MinDu'] = request.min_du
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not UtilClient.is_unset(request.source_region):
            query['SourceRegion'] = request.source_region
        if not UtilClient.is_unset(request.sync_architecture):
            query['SyncArchitecture'] = request.sync_architecture
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDtsInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.CreateDtsInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.CreateDtsInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def create_dts_instance_with_options_async(
        self,
        request: dts_20200101_models.CreateDtsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateDtsInstanceResponse:
        """
        @summary Purchases a Data Transmission Service (DTS) instance.
        
        @description    Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of DTS.
        If you want to run a DTS task on a DTS dedicated cluster, you must configure the task before you purchase a DTS instance. You can call the [ConfigureDtsJob](https://help.aliyun.com/document_detail/208399.html) operation to configure a DTS task.
        
        @param request: CreateDtsInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDtsInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not UtilClient.is_unset(request.compute_unit):
            query['ComputeUnit'] = request.compute_unit
        if not UtilClient.is_unset(request.database_count):
            query['DatabaseCount'] = request.database_count
        if not UtilClient.is_unset(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not UtilClient.is_unset(request.destination_region):
            query['DestinationRegion'] = request.destination_region
        if not UtilClient.is_unset(request.dts_region):
            query['DtsRegion'] = request.dts_region
        if not UtilClient.is_unset(request.du):
            query['Du'] = request.du
        if not UtilClient.is_unset(request.fee_type):
            query['FeeType'] = request.fee_type
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.max_du):
            query['MaxDu'] = request.max_du
        if not UtilClient.is_unset(request.min_du):
            query['MinDu'] = request.min_du
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not UtilClient.is_unset(request.source_region):
            query['SourceRegion'] = request.source_region
        if not UtilClient.is_unset(request.sync_architecture):
            query['SyncArchitecture'] = request.sync_architecture
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDtsInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.CreateDtsInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.CreateDtsInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_dts_instance(
        self,
        request: dts_20200101_models.CreateDtsInstanceRequest,
    ) -> dts_20200101_models.CreateDtsInstanceResponse:
        """
        @summary Purchases a Data Transmission Service (DTS) instance.
        
        @description    Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of DTS.
        If you want to run a DTS task on a DTS dedicated cluster, you must configure the task before you purchase a DTS instance. You can call the [ConfigureDtsJob](https://help.aliyun.com/document_detail/208399.html) operation to configure a DTS task.
        
        @param request: CreateDtsInstanceRequest
        @return: CreateDtsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dts_instance_with_options(request, runtime)

    async def create_dts_instance_async(
        self,
        request: dts_20200101_models.CreateDtsInstanceRequest,
    ) -> dts_20200101_models.CreateDtsInstanceResponse:
        """
        @summary Purchases a Data Transmission Service (DTS) instance.
        
        @description    Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of DTS.
        If you want to run a DTS task on a DTS dedicated cluster, you must configure the task before you purchase a DTS instance. You can call the [ConfigureDtsJob](https://help.aliyun.com/document_detail/208399.html) operation to configure a DTS task.
        
        @param request: CreateDtsInstanceRequest
        @return: CreateDtsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dts_instance_with_options_async(request, runtime)

    def create_job_monitor_rule_with_options(
        self,
        request: dts_20200101_models.CreateJobMonitorRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateJobMonitorRuleResponse:
        """
        @summary Creates or modifies an alert rule for a Data Transmission Service (DTS) task.
        
        @description DTS provides the following metrics for DTS tasks:***********\
        **Latency**: DTS monitors the latency of a DTS task. If the latency of the task exceeds the specified threshold, an alert is triggered. The threshold is specified in units of seconds.
        **Status**: DTS monitors the status of a DTS task. If the state of the task changes to **Error** or **Restore**, an alert is triggered.
        **Full Timeout**: DTS monitors the duration of a DTS task. If the duration of the task exceeds the specified threshold, an alert is triggered. The threshold is specified in units of hours.
        
        @param request: CreateJobMonitorRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobMonitorRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.notice_value):
            query['NoticeValue'] = request.notice_value
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.times):
            query['Times'] = request.times
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJobMonitorRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.CreateJobMonitorRuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.CreateJobMonitorRuleResponse(),
                self.execute(params, req, runtime)
            )

    async def create_job_monitor_rule_with_options_async(
        self,
        request: dts_20200101_models.CreateJobMonitorRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateJobMonitorRuleResponse:
        """
        @summary Creates or modifies an alert rule for a Data Transmission Service (DTS) task.
        
        @description DTS provides the following metrics for DTS tasks:***********\
        **Latency**: DTS monitors the latency of a DTS task. If the latency of the task exceeds the specified threshold, an alert is triggered. The threshold is specified in units of seconds.
        **Status**: DTS monitors the status of a DTS task. If the state of the task changes to **Error** or **Restore**, an alert is triggered.
        **Full Timeout**: DTS monitors the duration of a DTS task. If the duration of the task exceeds the specified threshold, an alert is triggered. The threshold is specified in units of hours.
        
        @param request: CreateJobMonitorRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobMonitorRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.notice_value):
            query['NoticeValue'] = request.notice_value
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.times):
            query['Times'] = request.times
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJobMonitorRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.CreateJobMonitorRuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.CreateJobMonitorRuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_job_monitor_rule(
        self,
        request: dts_20200101_models.CreateJobMonitorRuleRequest,
    ) -> dts_20200101_models.CreateJobMonitorRuleResponse:
        """
        @summary Creates or modifies an alert rule for a Data Transmission Service (DTS) task.
        
        @description DTS provides the following metrics for DTS tasks:***********\
        **Latency**: DTS monitors the latency of a DTS task. If the latency of the task exceeds the specified threshold, an alert is triggered. The threshold is specified in units of seconds.
        **Status**: DTS monitors the status of a DTS task. If the state of the task changes to **Error** or **Restore**, an alert is triggered.
        **Full Timeout**: DTS monitors the duration of a DTS task. If the duration of the task exceeds the specified threshold, an alert is triggered. The threshold is specified in units of hours.
        
        @param request: CreateJobMonitorRuleRequest
        @return: CreateJobMonitorRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_job_monitor_rule_with_options(request, runtime)

    async def create_job_monitor_rule_async(
        self,
        request: dts_20200101_models.CreateJobMonitorRuleRequest,
    ) -> dts_20200101_models.CreateJobMonitorRuleResponse:
        """
        @summary Creates or modifies an alert rule for a Data Transmission Service (DTS) task.
        
        @description DTS provides the following metrics for DTS tasks:***********\
        **Latency**: DTS monitors the latency of a DTS task. If the latency of the task exceeds the specified threshold, an alert is triggered. The threshold is specified in units of seconds.
        **Status**: DTS monitors the status of a DTS task. If the state of the task changes to **Error** or **Restore**, an alert is triggered.
        **Full Timeout**: DTS monitors the duration of a DTS task. If the duration of the task exceeds the specified threshold, an alert is triggered. The threshold is specified in units of hours.
        
        @param request: CreateJobMonitorRuleRequest
        @return: CreateJobMonitorRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_job_monitor_rule_with_options_async(request, runtime)

    def create_migration_job_with_options(
        self,
        request: dts_20200101_models.CreateMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateMigrationJobResponse:
        """
        @summary Purchases a data migration instance.
        
        @param request: CreateMigrationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMigrationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_class):
            query['MigrationJobClass'] = request.migration_job_class
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.CreateMigrationJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.CreateMigrationJobResponse(),
                self.execute(params, req, runtime)
            )

    async def create_migration_job_with_options_async(
        self,
        request: dts_20200101_models.CreateMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateMigrationJobResponse:
        """
        @summary Purchases a data migration instance.
        
        @param request: CreateMigrationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMigrationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_class):
            query['MigrationJobClass'] = request.migration_job_class
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.CreateMigrationJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.CreateMigrationJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_migration_job(
        self,
        request: dts_20200101_models.CreateMigrationJobRequest,
    ) -> dts_20200101_models.CreateMigrationJobResponse:
        """
        @summary Purchases a data migration instance.
        
        @param request: CreateMigrationJobRequest
        @return: CreateMigrationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_migration_job_with_options(request, runtime)

    async def create_migration_job_async(
        self,
        request: dts_20200101_models.CreateMigrationJobRequest,
    ) -> dts_20200101_models.CreateMigrationJobResponse:
        """
        @summary Purchases a data migration instance.
        
        @param request: CreateMigrationJobRequest
        @return: CreateMigrationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_migration_job_with_options_async(request, runtime)

    def create_reverse_dts_job_with_options(
        self,
        request: dts_20200101_models.CreateReverseDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateReverseDtsJobResponse:
        """
        @summary Creates a reverse task for a data synchronization or migration task.
        
        @description 调用接口创建的反向任务会立即进行预检查，预检查通过后会进行增量数据采集，增量数据写入模块不会运行（需要调用*StartReverseWriter**接口运行）。
        > 创建的反向任务固定为同步任务，且只有增量写入模块。
        
        @param request: CreateReverseDtsJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateReverseDtsJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.shard_password):
            query['ShardPassword'] = request.shard_password
        if not UtilClient.is_unset(request.shard_username):
            query['ShardUsername'] = request.shard_username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateReverseDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.CreateReverseDtsJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.CreateReverseDtsJobResponse(),
                self.execute(params, req, runtime)
            )

    async def create_reverse_dts_job_with_options_async(
        self,
        request: dts_20200101_models.CreateReverseDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateReverseDtsJobResponse:
        """
        @summary Creates a reverse task for a data synchronization or migration task.
        
        @description 调用接口创建的反向任务会立即进行预检查，预检查通过后会进行增量数据采集，增量数据写入模块不会运行（需要调用*StartReverseWriter**接口运行）。
        > 创建的反向任务固定为同步任务，且只有增量写入模块。
        
        @param request: CreateReverseDtsJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateReverseDtsJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.shard_password):
            query['ShardPassword'] = request.shard_password
        if not UtilClient.is_unset(request.shard_username):
            query['ShardUsername'] = request.shard_username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateReverseDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.CreateReverseDtsJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.CreateReverseDtsJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_reverse_dts_job(
        self,
        request: dts_20200101_models.CreateReverseDtsJobRequest,
    ) -> dts_20200101_models.CreateReverseDtsJobResponse:
        """
        @summary Creates a reverse task for a data synchronization or migration task.
        
        @description 调用接口创建的反向任务会立即进行预检查，预检查通过后会进行增量数据采集，增量数据写入模块不会运行（需要调用*StartReverseWriter**接口运行）。
        > 创建的反向任务固定为同步任务，且只有增量写入模块。
        
        @param request: CreateReverseDtsJobRequest
        @return: CreateReverseDtsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_reverse_dts_job_with_options(request, runtime)

    async def create_reverse_dts_job_async(
        self,
        request: dts_20200101_models.CreateReverseDtsJobRequest,
    ) -> dts_20200101_models.CreateReverseDtsJobResponse:
        """
        @summary Creates a reverse task for a data synchronization or migration task.
        
        @description 调用接口创建的反向任务会立即进行预检查，预检查通过后会进行增量数据采集，增量数据写入模块不会运行（需要调用*StartReverseWriter**接口运行）。
        > 创建的反向任务固定为同步任务，且只有增量写入模块。
        
        @param request: CreateReverseDtsJobRequest
        @return: CreateReverseDtsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_reverse_dts_job_with_options_async(request, runtime)

    def create_subscription_instance_with_options(
        self,
        request: dts_20200101_models.CreateSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateSubscriptionInstanceResponse:
        """
        @summary Purchases a change tracking instance.
        
        @param request: CreateSubscriptionInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSubscriptionInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSubscriptionInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.CreateSubscriptionInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.CreateSubscriptionInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def create_subscription_instance_with_options_async(
        self,
        request: dts_20200101_models.CreateSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateSubscriptionInstanceResponse:
        """
        @summary Purchases a change tracking instance.
        
        @param request: CreateSubscriptionInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSubscriptionInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSubscriptionInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.CreateSubscriptionInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.CreateSubscriptionInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_subscription_instance(
        self,
        request: dts_20200101_models.CreateSubscriptionInstanceRequest,
    ) -> dts_20200101_models.CreateSubscriptionInstanceResponse:
        """
        @summary Purchases a change tracking instance.
        
        @param request: CreateSubscriptionInstanceRequest
        @return: CreateSubscriptionInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_subscription_instance_with_options(request, runtime)

    async def create_subscription_instance_async(
        self,
        request: dts_20200101_models.CreateSubscriptionInstanceRequest,
    ) -> dts_20200101_models.CreateSubscriptionInstanceResponse:
        """
        @summary Purchases a change tracking instance.
        
        @param request: CreateSubscriptionInstanceRequest
        @return: CreateSubscriptionInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_subscription_instance_with_options_async(request, runtime)

    def create_synchronization_job_with_options(
        self,
        request: dts_20200101_models.CreateSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateSynchronizationJobResponse:
        """
        @summary Creates a data synchronization instance.
        
        @param request: CreateSynchronizationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_count):
            query['DBInstanceCount'] = request.dbinstance_count
        if not UtilClient.is_unset(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_region):
            query['SourceRegion'] = request.source_region
        if not UtilClient.is_unset(request.synchronization_job_class):
            query['SynchronizationJobClass'] = request.synchronization_job_class
        if not UtilClient.is_unset(request.topology):
            query['Topology'] = request.topology
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.network_type):
            query['networkType'] = request.network_type
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.CreateSynchronizationJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.CreateSynchronizationJobResponse(),
                self.execute(params, req, runtime)
            )

    async def create_synchronization_job_with_options_async(
        self,
        request: dts_20200101_models.CreateSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateSynchronizationJobResponse:
        """
        @summary Creates a data synchronization instance.
        
        @param request: CreateSynchronizationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_count):
            query['DBInstanceCount'] = request.dbinstance_count
        if not UtilClient.is_unset(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_region):
            query['SourceRegion'] = request.source_region
        if not UtilClient.is_unset(request.synchronization_job_class):
            query['SynchronizationJobClass'] = request.synchronization_job_class
        if not UtilClient.is_unset(request.topology):
            query['Topology'] = request.topology
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.network_type):
            query['networkType'] = request.network_type
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.CreateSynchronizationJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.CreateSynchronizationJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_synchronization_job(
        self,
        request: dts_20200101_models.CreateSynchronizationJobRequest,
    ) -> dts_20200101_models.CreateSynchronizationJobResponse:
        """
        @summary Creates a data synchronization instance.
        
        @param request: CreateSynchronizationJobRequest
        @return: CreateSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_synchronization_job_with_options(request, runtime)

    async def create_synchronization_job_async(
        self,
        request: dts_20200101_models.CreateSynchronizationJobRequest,
    ) -> dts_20200101_models.CreateSynchronizationJobResponse:
        """
        @summary Creates a data synchronization instance.
        
        @param request: CreateSynchronizationJobRequest
        @return: CreateSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_synchronization_job_with_options_async(request, runtime)

    def delete_consumer_channel_with_options(
        self,
        request: dts_20200101_models.DeleteConsumerChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteConsumerChannelResponse:
        """
        @summary Deletes a consumer group.
        
        @param request: DeleteConsumerChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConsumerChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupId'] = request.consumer_group_id
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsumerChannel',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DeleteConsumerChannelResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DeleteConsumerChannelResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_consumer_channel_with_options_async(
        self,
        request: dts_20200101_models.DeleteConsumerChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteConsumerChannelResponse:
        """
        @summary Deletes a consumer group.
        
        @param request: DeleteConsumerChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConsumerChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupId'] = request.consumer_group_id
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsumerChannel',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DeleteConsumerChannelResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DeleteConsumerChannelResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_consumer_channel(
        self,
        request: dts_20200101_models.DeleteConsumerChannelRequest,
    ) -> dts_20200101_models.DeleteConsumerChannelResponse:
        """
        @summary Deletes a consumer group.
        
        @param request: DeleteConsumerChannelRequest
        @return: DeleteConsumerChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_channel_with_options(request, runtime)

    async def delete_consumer_channel_async(
        self,
        request: dts_20200101_models.DeleteConsumerChannelRequest,
    ) -> dts_20200101_models.DeleteConsumerChannelResponse:
        """
        @summary Deletes a consumer group.
        
        @param request: DeleteConsumerChannelRequest
        @return: DeleteConsumerChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_consumer_channel_with_options_async(request, runtime)

    def delete_consumer_group_with_options(
        self,
        request: dts_20200101_models.DeleteConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteConsumerGroupResponse:
        """
        @summary Deletes a consumer group.
        
        @param request: DeleteConsumerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupID'] = request.consumer_group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DeleteConsumerGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DeleteConsumerGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_consumer_group_with_options_async(
        self,
        request: dts_20200101_models.DeleteConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteConsumerGroupResponse:
        """
        @summary Deletes a consumer group.
        
        @param request: DeleteConsumerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupID'] = request.consumer_group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DeleteConsumerGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DeleteConsumerGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_consumer_group(
        self,
        request: dts_20200101_models.DeleteConsumerGroupRequest,
    ) -> dts_20200101_models.DeleteConsumerGroupResponse:
        """
        @summary Deletes a consumer group.
        
        @param request: DeleteConsumerGroupRequest
        @return: DeleteConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_group_with_options(request, runtime)

    async def delete_consumer_group_async(
        self,
        request: dts_20200101_models.DeleteConsumerGroupRequest,
    ) -> dts_20200101_models.DeleteConsumerGroupResponse:
        """
        @summary Deletes a consumer group.
        
        @param request: DeleteConsumerGroupRequest
        @return: DeleteConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_consumer_group_with_options_async(request, runtime)

    def delete_dts_job_with_options(
        self,
        request: dts_20200101_models.DeleteDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteDtsJobResponse:
        """
        @summary Deletes a data migration, data synchronization, or change tracking task.
        
        @param request: DeleteDtsJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDtsJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DeleteDtsJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DeleteDtsJobResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_dts_job_with_options_async(
        self,
        request: dts_20200101_models.DeleteDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteDtsJobResponse:
        """
        @summary Deletes a data migration, data synchronization, or change tracking task.
        
        @param request: DeleteDtsJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDtsJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DeleteDtsJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DeleteDtsJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_dts_job(
        self,
        request: dts_20200101_models.DeleteDtsJobRequest,
    ) -> dts_20200101_models.DeleteDtsJobResponse:
        """
        @summary Deletes a data migration, data synchronization, or change tracking task.
        
        @param request: DeleteDtsJobRequest
        @return: DeleteDtsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dts_job_with_options(request, runtime)

    async def delete_dts_job_async(
        self,
        request: dts_20200101_models.DeleteDtsJobRequest,
    ) -> dts_20200101_models.DeleteDtsJobResponse:
        """
        @summary Deletes a data migration, data synchronization, or change tracking task.
        
        @param request: DeleteDtsJobRequest
        @return: DeleteDtsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dts_job_with_options_async(request, runtime)

    def delete_dts_jobs_with_options(
        self,
        request: dts_20200101_models.DeleteDtsJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteDtsJobsResponse:
        """
        @summary Deletes multiple data migration, data synchronization, or change tracking tasks.
        
        @param request: DeleteDtsJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDtsJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DeleteDtsJobsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DeleteDtsJobsResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_dts_jobs_with_options_async(
        self,
        request: dts_20200101_models.DeleteDtsJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteDtsJobsResponse:
        """
        @summary Deletes multiple data migration, data synchronization, or change tracking tasks.
        
        @param request: DeleteDtsJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDtsJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DeleteDtsJobsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DeleteDtsJobsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_dts_jobs(
        self,
        request: dts_20200101_models.DeleteDtsJobsRequest,
    ) -> dts_20200101_models.DeleteDtsJobsResponse:
        """
        @summary Deletes multiple data migration, data synchronization, or change tracking tasks.
        
        @param request: DeleteDtsJobsRequest
        @return: DeleteDtsJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dts_jobs_with_options(request, runtime)

    async def delete_dts_jobs_async(
        self,
        request: dts_20200101_models.DeleteDtsJobsRequest,
    ) -> dts_20200101_models.DeleteDtsJobsResponse:
        """
        @summary Deletes multiple data migration, data synchronization, or change tracking tasks.
        
        @param request: DeleteDtsJobsRequest
        @return: DeleteDtsJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dts_jobs_with_options_async(request, runtime)

    def delete_migration_job_with_options(
        self,
        request: dts_20200101_models.DeleteMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteMigrationJobResponse:
        """
        @summary Releases a data migration instance.
        
        @param request: DeleteMigrationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMigrationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DeleteMigrationJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DeleteMigrationJobResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_migration_job_with_options_async(
        self,
        request: dts_20200101_models.DeleteMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteMigrationJobResponse:
        """
        @summary Releases a data migration instance.
        
        @param request: DeleteMigrationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMigrationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DeleteMigrationJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DeleteMigrationJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_migration_job(
        self,
        request: dts_20200101_models.DeleteMigrationJobRequest,
    ) -> dts_20200101_models.DeleteMigrationJobResponse:
        """
        @summary Releases a data migration instance.
        
        @param request: DeleteMigrationJobRequest
        @return: DeleteMigrationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_migration_job_with_options(request, runtime)

    async def delete_migration_job_async(
        self,
        request: dts_20200101_models.DeleteMigrationJobRequest,
    ) -> dts_20200101_models.DeleteMigrationJobResponse:
        """
        @summary Releases a data migration instance.
        
        @param request: DeleteMigrationJobRequest
        @return: DeleteMigrationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_migration_job_with_options_async(request, runtime)

    def delete_subscription_instance_with_options(
        self,
        request: dts_20200101_models.DeleteSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteSubscriptionInstanceResponse:
        """
        @summary Releases a change tracking instance.
        
        @param request: DeleteSubscriptionInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSubscriptionInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSubscriptionInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DeleteSubscriptionInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DeleteSubscriptionInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_subscription_instance_with_options_async(
        self,
        request: dts_20200101_models.DeleteSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteSubscriptionInstanceResponse:
        """
        @summary Releases a change tracking instance.
        
        @param request: DeleteSubscriptionInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSubscriptionInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSubscriptionInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DeleteSubscriptionInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DeleteSubscriptionInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_subscription_instance(
        self,
        request: dts_20200101_models.DeleteSubscriptionInstanceRequest,
    ) -> dts_20200101_models.DeleteSubscriptionInstanceResponse:
        """
        @summary Releases a change tracking instance.
        
        @param request: DeleteSubscriptionInstanceRequest
        @return: DeleteSubscriptionInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_subscription_instance_with_options(request, runtime)

    async def delete_subscription_instance_async(
        self,
        request: dts_20200101_models.DeleteSubscriptionInstanceRequest,
    ) -> dts_20200101_models.DeleteSubscriptionInstanceResponse:
        """
        @summary Releases a change tracking instance.
        
        @param request: DeleteSubscriptionInstanceRequest
        @return: DeleteSubscriptionInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_subscription_instance_with_options_async(request, runtime)

    def delete_synchronization_job_with_options(
        self,
        request: dts_20200101_models.DeleteSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteSynchronizationJobResponse:
        """
        @summary Releases a data synchronization instance.
        
        @param request: DeleteSynchronizationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DeleteSynchronizationJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DeleteSynchronizationJobResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_synchronization_job_with_options_async(
        self,
        request: dts_20200101_models.DeleteSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteSynchronizationJobResponse:
        """
        @summary Releases a data synchronization instance.
        
        @param request: DeleteSynchronizationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DeleteSynchronizationJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DeleteSynchronizationJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_synchronization_job(
        self,
        request: dts_20200101_models.DeleteSynchronizationJobRequest,
    ) -> dts_20200101_models.DeleteSynchronizationJobResponse:
        """
        @summary Releases a data synchronization instance.
        
        @param request: DeleteSynchronizationJobRequest
        @return: DeleteSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_synchronization_job_with_options(request, runtime)

    async def delete_synchronization_job_async(
        self,
        request: dts_20200101_models.DeleteSynchronizationJobRequest,
    ) -> dts_20200101_models.DeleteSynchronizationJobResponse:
        """
        @summary Releases a data synchronization instance.
        
        @param request: DeleteSynchronizationJobRequest
        @return: DeleteSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_synchronization_job_with_options_async(request, runtime)

    def describe_channel_account_with_options(
        self,
        request: dts_20200101_models.DescribeChannelAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeChannelAccountResponse:
        """
        @summary 查询数据投递链路store账号
        
        @param request: DescribeChannelAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelAccount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeChannelAccountResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeChannelAccountResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_channel_account_with_options_async(
        self,
        request: dts_20200101_models.DescribeChannelAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeChannelAccountResponse:
        """
        @summary 查询数据投递链路store账号
        
        @param request: DescribeChannelAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelAccount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeChannelAccountResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeChannelAccountResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_channel_account(
        self,
        request: dts_20200101_models.DescribeChannelAccountRequest,
    ) -> dts_20200101_models.DescribeChannelAccountResponse:
        """
        @summary 查询数据投递链路store账号
        
        @param request: DescribeChannelAccountRequest
        @return: DescribeChannelAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_account_with_options(request, runtime)

    async def describe_channel_account_async(
        self,
        request: dts_20200101_models.DescribeChannelAccountRequest,
    ) -> dts_20200101_models.DescribeChannelAccountResponse:
        """
        @summary 查询数据投递链路store账号
        
        @param request: DescribeChannelAccountRequest
        @return: DescribeChannelAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_channel_account_with_options_async(request, runtime)

    def describe_check_jobs_with_options(
        self,
        request: dts_20200101_models.DescribeCheckJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeCheckJobsResponse:
        """
        @summary 请求所有数据校验任务数据
        
        @param request: DescribeCheckJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCheckJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_job_id):
            query['CheckJobId'] = request.check_job_id
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_name):
            query['JobName'] = request.job_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCheckJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeCheckJobsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeCheckJobsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_check_jobs_with_options_async(
        self,
        request: dts_20200101_models.DescribeCheckJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeCheckJobsResponse:
        """
        @summary 请求所有数据校验任务数据
        
        @param request: DescribeCheckJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCheckJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_job_id):
            query['CheckJobId'] = request.check_job_id
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_name):
            query['JobName'] = request.job_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCheckJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeCheckJobsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeCheckJobsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_check_jobs(
        self,
        request: dts_20200101_models.DescribeCheckJobsRequest,
    ) -> dts_20200101_models.DescribeCheckJobsResponse:
        """
        @summary 请求所有数据校验任务数据
        
        @param request: DescribeCheckJobsRequest
        @return: DescribeCheckJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_check_jobs_with_options(request, runtime)

    async def describe_check_jobs_async(
        self,
        request: dts_20200101_models.DescribeCheckJobsRequest,
    ) -> dts_20200101_models.DescribeCheckJobsResponse:
        """
        @summary 请求所有数据校验任务数据
        
        @param request: DescribeCheckJobsRequest
        @return: DescribeCheckJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_check_jobs_with_options_async(request, runtime)

    def describe_cluster_operate_logs_with_options(
        self,
        request: dts_20200101_models.DescribeClusterOperateLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeClusterOperateLogsResponse:
        """
        @summary Queries operation logs of a Data Transmission Service (DTS) dedicated cluster.
        
        @param request: DescribeClusterOperateLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterOperateLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            body['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.dts_job_id):
            body['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerID'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeClusterOperateLogs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeClusterOperateLogsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeClusterOperateLogsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_operate_logs_with_options_async(
        self,
        request: dts_20200101_models.DescribeClusterOperateLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeClusterOperateLogsResponse:
        """
        @summary Queries operation logs of a Data Transmission Service (DTS) dedicated cluster.
        
        @param request: DescribeClusterOperateLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterOperateLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            body['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.dts_job_id):
            body['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerID'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeClusterOperateLogs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeClusterOperateLogsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeClusterOperateLogsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_operate_logs(
        self,
        request: dts_20200101_models.DescribeClusterOperateLogsRequest,
    ) -> dts_20200101_models.DescribeClusterOperateLogsResponse:
        """
        @summary Queries operation logs of a Data Transmission Service (DTS) dedicated cluster.
        
        @param request: DescribeClusterOperateLogsRequest
        @return: DescribeClusterOperateLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_operate_logs_with_options(request, runtime)

    async def describe_cluster_operate_logs_async(
        self,
        request: dts_20200101_models.DescribeClusterOperateLogsRequest,
    ) -> dts_20200101_models.DescribeClusterOperateLogsResponse:
        """
        @summary Queries operation logs of a Data Transmission Service (DTS) dedicated cluster.
        
        @param request: DescribeClusterOperateLogsRequest
        @return: DescribeClusterOperateLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_operate_logs_with_options_async(request, runtime)

    def describe_cluster_used_utilization_with_options(
        self,
        request: dts_20200101_models.DescribeClusterUsedUtilizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeClusterUsedUtilizationResponse:
        """
        @summary Queries the resource usage of a cluster.
        
        @param request: DescribeClusterUsedUtilizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterUsedUtilizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            body['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.dts_job_id):
            body['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.env):
            body['Env'] = request.env
        if not UtilClient.is_unset(request.metric_type):
            body['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerID'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeClusterUsedUtilization',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeClusterUsedUtilizationResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeClusterUsedUtilizationResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_used_utilization_with_options_async(
        self,
        request: dts_20200101_models.DescribeClusterUsedUtilizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeClusterUsedUtilizationResponse:
        """
        @summary Queries the resource usage of a cluster.
        
        @param request: DescribeClusterUsedUtilizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterUsedUtilizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            body['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.dts_job_id):
            body['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.env):
            body['Env'] = request.env
        if not UtilClient.is_unset(request.metric_type):
            body['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerID'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeClusterUsedUtilization',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeClusterUsedUtilizationResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeClusterUsedUtilizationResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_used_utilization(
        self,
        request: dts_20200101_models.DescribeClusterUsedUtilizationRequest,
    ) -> dts_20200101_models.DescribeClusterUsedUtilizationResponse:
        """
        @summary Queries the resource usage of a cluster.
        
        @param request: DescribeClusterUsedUtilizationRequest
        @return: DescribeClusterUsedUtilizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_used_utilization_with_options(request, runtime)

    async def describe_cluster_used_utilization_async(
        self,
        request: dts_20200101_models.DescribeClusterUsedUtilizationRequest,
    ) -> dts_20200101_models.DescribeClusterUsedUtilizationResponse:
        """
        @summary Queries the resource usage of a cluster.
        
        @param request: DescribeClusterUsedUtilizationRequest
        @return: DescribeClusterUsedUtilizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_used_utilization_with_options_async(request, runtime)

    def describe_connection_status_with_options(
        self,
        request: dts_20200101_models.DescribeConnectionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeConnectionStatusResponse:
        """
        @summary Queries the connectivity of Data Transmission Service (DTS) servers to the source and destination databases.
        
        @param request: DescribeConnectionStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConnectionStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_endpoint_architecture):
            query['DestinationEndpointArchitecture'] = request.destination_endpoint_architecture
        if not UtilClient.is_unset(request.destination_endpoint_database_name):
            query['DestinationEndpointDatabaseName'] = request.destination_endpoint_database_name
        if not UtilClient.is_unset(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not UtilClient.is_unset(request.destination_endpoint_ip):
            query['DestinationEndpointIP'] = request.destination_endpoint_ip
        if not UtilClient.is_unset(request.destination_endpoint_instance_id):
            query['DestinationEndpointInstanceID'] = request.destination_endpoint_instance_id
        if not UtilClient.is_unset(request.destination_endpoint_instance_type):
            query['DestinationEndpointInstanceType'] = request.destination_endpoint_instance_type
        if not UtilClient.is_unset(request.destination_endpoint_oracle_sid):
            query['DestinationEndpointOracleSID'] = request.destination_endpoint_oracle_sid
        if not UtilClient.is_unset(request.destination_endpoint_password):
            query['DestinationEndpointPassword'] = request.destination_endpoint_password
        if not UtilClient.is_unset(request.destination_endpoint_port):
            query['DestinationEndpointPort'] = request.destination_endpoint_port
        if not UtilClient.is_unset(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not UtilClient.is_unset(request.destination_endpoint_user_name):
            query['DestinationEndpointUserName'] = request.destination_endpoint_user_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_endpoint_architecture):
            query['SourceEndpointArchitecture'] = request.source_endpoint_architecture
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not UtilClient.is_unset(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not UtilClient.is_unset(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not UtilClient.is_unset(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not UtilClient.is_unset(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConnectionStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeConnectionStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeConnectionStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_connection_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeConnectionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeConnectionStatusResponse:
        """
        @summary Queries the connectivity of Data Transmission Service (DTS) servers to the source and destination databases.
        
        @param request: DescribeConnectionStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConnectionStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_endpoint_architecture):
            query['DestinationEndpointArchitecture'] = request.destination_endpoint_architecture
        if not UtilClient.is_unset(request.destination_endpoint_database_name):
            query['DestinationEndpointDatabaseName'] = request.destination_endpoint_database_name
        if not UtilClient.is_unset(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not UtilClient.is_unset(request.destination_endpoint_ip):
            query['DestinationEndpointIP'] = request.destination_endpoint_ip
        if not UtilClient.is_unset(request.destination_endpoint_instance_id):
            query['DestinationEndpointInstanceID'] = request.destination_endpoint_instance_id
        if not UtilClient.is_unset(request.destination_endpoint_instance_type):
            query['DestinationEndpointInstanceType'] = request.destination_endpoint_instance_type
        if not UtilClient.is_unset(request.destination_endpoint_oracle_sid):
            query['DestinationEndpointOracleSID'] = request.destination_endpoint_oracle_sid
        if not UtilClient.is_unset(request.destination_endpoint_password):
            query['DestinationEndpointPassword'] = request.destination_endpoint_password
        if not UtilClient.is_unset(request.destination_endpoint_port):
            query['DestinationEndpointPort'] = request.destination_endpoint_port
        if not UtilClient.is_unset(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not UtilClient.is_unset(request.destination_endpoint_user_name):
            query['DestinationEndpointUserName'] = request.destination_endpoint_user_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_endpoint_architecture):
            query['SourceEndpointArchitecture'] = request.source_endpoint_architecture
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not UtilClient.is_unset(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not UtilClient.is_unset(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not UtilClient.is_unset(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not UtilClient.is_unset(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConnectionStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeConnectionStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeConnectionStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_connection_status(
        self,
        request: dts_20200101_models.DescribeConnectionStatusRequest,
    ) -> dts_20200101_models.DescribeConnectionStatusResponse:
        """
        @summary Queries the connectivity of Data Transmission Service (DTS) servers to the source and destination databases.
        
        @param request: DescribeConnectionStatusRequest
        @return: DescribeConnectionStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_connection_status_with_options(request, runtime)

    async def describe_connection_status_async(
        self,
        request: dts_20200101_models.DescribeConnectionStatusRequest,
    ) -> dts_20200101_models.DescribeConnectionStatusResponse:
        """
        @summary Queries the connectivity of Data Transmission Service (DTS) servers to the source and destination databases.
        
        @param request: DescribeConnectionStatusRequest
        @return: DescribeConnectionStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_connection_status_with_options_async(request, runtime)

    def describe_consumer_channel_with_options(
        self,
        request: dts_20200101_models.DescribeConsumerChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeConsumerChannelResponse:
        """
        @summary Queries the information of a consumer group, including the consumer group ID, consumer group name, username, and message latency.
        
        @param request: DescribeConsumerChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConsumerChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_channel_id):
            query['ParentChannelId'] = request.parent_channel_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConsumerChannel',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeConsumerChannelResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeConsumerChannelResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_consumer_channel_with_options_async(
        self,
        request: dts_20200101_models.DescribeConsumerChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeConsumerChannelResponse:
        """
        @summary Queries the information of a consumer group, including the consumer group ID, consumer group name, username, and message latency.
        
        @param request: DescribeConsumerChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConsumerChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_channel_id):
            query['ParentChannelId'] = request.parent_channel_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConsumerChannel',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeConsumerChannelResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeConsumerChannelResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_consumer_channel(
        self,
        request: dts_20200101_models.DescribeConsumerChannelRequest,
    ) -> dts_20200101_models.DescribeConsumerChannelResponse:
        """
        @summary Queries the information of a consumer group, including the consumer group ID, consumer group name, username, and message latency.
        
        @param request: DescribeConsumerChannelRequest
        @return: DescribeConsumerChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_consumer_channel_with_options(request, runtime)

    async def describe_consumer_channel_async(
        self,
        request: dts_20200101_models.DescribeConsumerChannelRequest,
    ) -> dts_20200101_models.DescribeConsumerChannelResponse:
        """
        @summary Queries the information of a consumer group, including the consumer group ID, consumer group name, username, and message latency.
        
        @param request: DescribeConsumerChannelRequest
        @return: DescribeConsumerChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_consumer_channel_with_options_async(request, runtime)

    def describe_consumer_group_with_options(
        self,
        request: dts_20200101_models.DescribeConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeConsumerGroupResponse:
        """
        @summary Queries the details of consumer groups in a change tracking instance.
        
        @param request: DescribeConsumerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConsumerGroup',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeConsumerGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeConsumerGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_consumer_group_with_options_async(
        self,
        request: dts_20200101_models.DescribeConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeConsumerGroupResponse:
        """
        @summary Queries the details of consumer groups in a change tracking instance.
        
        @param request: DescribeConsumerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConsumerGroup',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeConsumerGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeConsumerGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_consumer_group(
        self,
        request: dts_20200101_models.DescribeConsumerGroupRequest,
    ) -> dts_20200101_models.DescribeConsumerGroupResponse:
        """
        @summary Queries the details of consumer groups in a change tracking instance.
        
        @param request: DescribeConsumerGroupRequest
        @return: DescribeConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_consumer_group_with_options(request, runtime)

    async def describe_consumer_group_async(
        self,
        request: dts_20200101_models.DescribeConsumerGroupRequest,
    ) -> dts_20200101_models.DescribeConsumerGroupResponse:
        """
        @summary Queries the details of consumer groups in a change tracking instance.
        
        @param request: DescribeConsumerGroupRequest
        @return: DescribeConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_consumer_group_with_options_async(request, runtime)

    def describe_dtsipwith_options(
        self,
        request: dts_20200101_models.DescribeDTSIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDTSIPResponse:
        """
        @summary Queries the CIDR blocks of DTS servers.
        
        @param request: DescribeDTSIPRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDTSIPResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDTSIP',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDTSIPResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDTSIPResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_dtsipwith_options_async(
        self,
        request: dts_20200101_models.DescribeDTSIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDTSIPResponse:
        """
        @summary Queries the CIDR blocks of DTS servers.
        
        @param request: DescribeDTSIPRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDTSIPResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDTSIP',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDTSIPResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDTSIPResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_dtsip(
        self,
        request: dts_20200101_models.DescribeDTSIPRequest,
    ) -> dts_20200101_models.DescribeDTSIPResponse:
        """
        @summary Queries the CIDR blocks of DTS servers.
        
        @param request: DescribeDTSIPRequest
        @return: DescribeDTSIPResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dtsipwith_options(request, runtime)

    async def describe_dtsip_async(
        self,
        request: dts_20200101_models.DescribeDTSIPRequest,
    ) -> dts_20200101_models.DescribeDTSIPResponse:
        """
        @summary Queries the CIDR blocks of DTS servers.
        
        @param request: DescribeDTSIPRequest
        @return: DescribeDTSIPResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dtsipwith_options_async(request, runtime)

    def describe_data_check_report_url_with_options(
        self,
        request: dts_20200101_models.DescribeDataCheckReportUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDataCheckReportUrlResponse:
        """
        @summary Queries the download URL of the data consistency verification report.
        
        @param request: DescribeDataCheckReportUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataCheckReportUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tb_name):
            query['TbName'] = request.tb_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataCheckReportUrl',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDataCheckReportUrlResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDataCheckReportUrlResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_data_check_report_url_with_options_async(
        self,
        request: dts_20200101_models.DescribeDataCheckReportUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDataCheckReportUrlResponse:
        """
        @summary Queries the download URL of the data consistency verification report.
        
        @param request: DescribeDataCheckReportUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataCheckReportUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tb_name):
            query['TbName'] = request.tb_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataCheckReportUrl',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDataCheckReportUrlResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDataCheckReportUrlResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_data_check_report_url(
        self,
        request: dts_20200101_models.DescribeDataCheckReportUrlRequest,
    ) -> dts_20200101_models.DescribeDataCheckReportUrlResponse:
        """
        @summary Queries the download URL of the data consistency verification report.
        
        @param request: DescribeDataCheckReportUrlRequest
        @return: DescribeDataCheckReportUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_check_report_url_with_options(request, runtime)

    async def describe_data_check_report_url_async(
        self,
        request: dts_20200101_models.DescribeDataCheckReportUrlRequest,
    ) -> dts_20200101_models.DescribeDataCheckReportUrlResponse:
        """
        @summary Queries the download URL of the data consistency verification report.
        
        @param request: DescribeDataCheckReportUrlRequest
        @return: DescribeDataCheckReportUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_check_report_url_with_options_async(request, runtime)

    def describe_data_check_table_details_with_options(
        self,
        request: dts_20200101_models.DescribeDataCheckTableDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDataCheckTableDetailsResponse:
        """
        @summary Queries the details of a data verification task.
        
        @param request: DescribeDataCheckTableDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataCheckTableDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataCheckTableDetails',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDataCheckTableDetailsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDataCheckTableDetailsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_data_check_table_details_with_options_async(
        self,
        request: dts_20200101_models.DescribeDataCheckTableDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDataCheckTableDetailsResponse:
        """
        @summary Queries the details of a data verification task.
        
        @param request: DescribeDataCheckTableDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataCheckTableDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataCheckTableDetails',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDataCheckTableDetailsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDataCheckTableDetailsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_data_check_table_details(
        self,
        request: dts_20200101_models.DescribeDataCheckTableDetailsRequest,
    ) -> dts_20200101_models.DescribeDataCheckTableDetailsResponse:
        """
        @summary Queries the details of a data verification task.
        
        @param request: DescribeDataCheckTableDetailsRequest
        @return: DescribeDataCheckTableDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_check_table_details_with_options(request, runtime)

    async def describe_data_check_table_details_async(
        self,
        request: dts_20200101_models.DescribeDataCheckTableDetailsRequest,
    ) -> dts_20200101_models.DescribeDataCheckTableDetailsResponse:
        """
        @summary Queries the details of a data verification task.
        
        @param request: DescribeDataCheckTableDetailsRequest
        @return: DescribeDataCheckTableDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_check_table_details_with_options_async(request, runtime)

    def describe_data_check_table_diff_details_with_options(
        self,
        request: dts_20200101_models.DescribeDataCheckTableDiffDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDataCheckTableDiffDetailsResponse:
        """
        @summary Queries the information about inconsistent data in the data verification task.
        
        @param request: DescribeDataCheckTableDiffDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataCheckTableDiffDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tb_name):
            query['TbName'] = request.tb_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataCheckTableDiffDetails',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDataCheckTableDiffDetailsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDataCheckTableDiffDetailsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_data_check_table_diff_details_with_options_async(
        self,
        request: dts_20200101_models.DescribeDataCheckTableDiffDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDataCheckTableDiffDetailsResponse:
        """
        @summary Queries the information about inconsistent data in the data verification task.
        
        @param request: DescribeDataCheckTableDiffDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataCheckTableDiffDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tb_name):
            query['TbName'] = request.tb_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataCheckTableDiffDetails',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDataCheckTableDiffDetailsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDataCheckTableDiffDetailsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_data_check_table_diff_details(
        self,
        request: dts_20200101_models.DescribeDataCheckTableDiffDetailsRequest,
    ) -> dts_20200101_models.DescribeDataCheckTableDiffDetailsResponse:
        """
        @summary Queries the information about inconsistent data in the data verification task.
        
        @param request: DescribeDataCheckTableDiffDetailsRequest
        @return: DescribeDataCheckTableDiffDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_check_table_diff_details_with_options(request, runtime)

    async def describe_data_check_table_diff_details_async(
        self,
        request: dts_20200101_models.DescribeDataCheckTableDiffDetailsRequest,
    ) -> dts_20200101_models.DescribeDataCheckTableDiffDetailsResponse:
        """
        @summary Queries the information about inconsistent data in the data verification task.
        
        @param request: DescribeDataCheckTableDiffDetailsRequest
        @return: DescribeDataCheckTableDiffDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_check_table_diff_details_with_options_async(request, runtime)

    def describe_dedicated_cluster_with_options(
        self,
        request: dts_20200101_models.DescribeDedicatedClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDedicatedClusterResponse:
        """
        @summary Queries the information about a dedicated cluster.
        
        @param request: DescribeDedicatedClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDedicatedClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedCluster',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDedicatedClusterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDedicatedClusterResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_dedicated_cluster_with_options_async(
        self,
        request: dts_20200101_models.DescribeDedicatedClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDedicatedClusterResponse:
        """
        @summary Queries the information about a dedicated cluster.
        
        @param request: DescribeDedicatedClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDedicatedClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedCluster',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDedicatedClusterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDedicatedClusterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_dedicated_cluster(
        self,
        request: dts_20200101_models.DescribeDedicatedClusterRequest,
    ) -> dts_20200101_models.DescribeDedicatedClusterResponse:
        """
        @summary Queries the information about a dedicated cluster.
        
        @param request: DescribeDedicatedClusterRequest
        @return: DescribeDedicatedClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_cluster_with_options(request, runtime)

    async def describe_dedicated_cluster_async(
        self,
        request: dts_20200101_models.DescribeDedicatedClusterRequest,
    ) -> dts_20200101_models.DescribeDedicatedClusterResponse:
        """
        @summary Queries the information about a dedicated cluster.
        
        @param request: DescribeDedicatedClusterRequest
        @return: DescribeDedicatedClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_cluster_with_options_async(request, runtime)

    def describe_dedicated_cluster_monitor_rule_with_options(
        self,
        request: dts_20200101_models.DescribeDedicatedClusterMonitorRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDedicatedClusterMonitorRuleResponse:
        """
        @summary Queries the information about an alert rule.
        
        @param request: DescribeDedicatedClusterMonitorRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDedicatedClusterMonitorRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedClusterMonitorRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDedicatedClusterMonitorRuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDedicatedClusterMonitorRuleResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_dedicated_cluster_monitor_rule_with_options_async(
        self,
        request: dts_20200101_models.DescribeDedicatedClusterMonitorRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDedicatedClusterMonitorRuleResponse:
        """
        @summary Queries the information about an alert rule.
        
        @param request: DescribeDedicatedClusterMonitorRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDedicatedClusterMonitorRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedClusterMonitorRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDedicatedClusterMonitorRuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDedicatedClusterMonitorRuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_dedicated_cluster_monitor_rule(
        self,
        request: dts_20200101_models.DescribeDedicatedClusterMonitorRuleRequest,
    ) -> dts_20200101_models.DescribeDedicatedClusterMonitorRuleResponse:
        """
        @summary Queries the information about an alert rule.
        
        @param request: DescribeDedicatedClusterMonitorRuleRequest
        @return: DescribeDedicatedClusterMonitorRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_cluster_monitor_rule_with_options(request, runtime)

    async def describe_dedicated_cluster_monitor_rule_async(
        self,
        request: dts_20200101_models.DescribeDedicatedClusterMonitorRuleRequest,
    ) -> dts_20200101_models.DescribeDedicatedClusterMonitorRuleResponse:
        """
        @summary Queries the information about an alert rule.
        
        @param request: DescribeDedicatedClusterMonitorRuleRequest
        @return: DescribeDedicatedClusterMonitorRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_cluster_monitor_rule_with_options_async(request, runtime)

    def describe_dts_etl_job_version_info_with_options(
        self,
        request: dts_20200101_models.DescribeDtsEtlJobVersionInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDtsEtlJobVersionInfoResponse:
        """
        @summary Queries the details of extract, transform, and load (ETL) tasks.
        
        @param request: DescribeDtsEtlJobVersionInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDtsEtlJobVersionInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDtsEtlJobVersionInfo',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDtsEtlJobVersionInfoResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDtsEtlJobVersionInfoResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_dts_etl_job_version_info_with_options_async(
        self,
        request: dts_20200101_models.DescribeDtsEtlJobVersionInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDtsEtlJobVersionInfoResponse:
        """
        @summary Queries the details of extract, transform, and load (ETL) tasks.
        
        @param request: DescribeDtsEtlJobVersionInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDtsEtlJobVersionInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDtsEtlJobVersionInfo',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDtsEtlJobVersionInfoResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDtsEtlJobVersionInfoResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_dts_etl_job_version_info(
        self,
        request: dts_20200101_models.DescribeDtsEtlJobVersionInfoRequest,
    ) -> dts_20200101_models.DescribeDtsEtlJobVersionInfoResponse:
        """
        @summary Queries the details of extract, transform, and load (ETL) tasks.
        
        @param request: DescribeDtsEtlJobVersionInfoRequest
        @return: DescribeDtsEtlJobVersionInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dts_etl_job_version_info_with_options(request, runtime)

    async def describe_dts_etl_job_version_info_async(
        self,
        request: dts_20200101_models.DescribeDtsEtlJobVersionInfoRequest,
    ) -> dts_20200101_models.DescribeDtsEtlJobVersionInfoResponse:
        """
        @summary Queries the details of extract, transform, and load (ETL) tasks.
        
        @param request: DescribeDtsEtlJobVersionInfoRequest
        @return: DescribeDtsEtlJobVersionInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dts_etl_job_version_info_with_options_async(request, runtime)

    def describe_dts_job_config_with_options(
        self,
        request: dts_20200101_models.DescribeDtsJobConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDtsJobConfigResponse:
        """
        @summary 查询DTS任务配置
        
        @param request: DescribeDtsJobConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDtsJobConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.for_acceleration):
            query['ForAcceleration'] = request.for_acceleration
        if not UtilClient.is_unset(request.module):
            query['Module'] = request.module
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDtsJobConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDtsJobConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDtsJobConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_dts_job_config_with_options_async(
        self,
        request: dts_20200101_models.DescribeDtsJobConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDtsJobConfigResponse:
        """
        @summary 查询DTS任务配置
        
        @param request: DescribeDtsJobConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDtsJobConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.for_acceleration):
            query['ForAcceleration'] = request.for_acceleration
        if not UtilClient.is_unset(request.module):
            query['Module'] = request.module
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDtsJobConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDtsJobConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDtsJobConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_dts_job_config(
        self,
        request: dts_20200101_models.DescribeDtsJobConfigRequest,
    ) -> dts_20200101_models.DescribeDtsJobConfigResponse:
        """
        @summary 查询DTS任务配置
        
        @param request: DescribeDtsJobConfigRequest
        @return: DescribeDtsJobConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dts_job_config_with_options(request, runtime)

    async def describe_dts_job_config_async(
        self,
        request: dts_20200101_models.DescribeDtsJobConfigRequest,
    ) -> dts_20200101_models.DescribeDtsJobConfigResponse:
        """
        @summary 查询DTS任务配置
        
        @param request: DescribeDtsJobConfigRequest
        @return: DescribeDtsJobConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dts_job_config_with_options_async(request, runtime)

    def describe_dts_job_detail_with_options(
        self,
        request: dts_20200101_models.DescribeDtsJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDtsJobDetailResponse:
        """
        @summary The latency of incremental data migration or synchronization.
        \\\\\\\\\\>  If you query data migration tasks, the unit of this parameter is milliseconds. If you query data synchronization tasks, the unit of this parameter is seconds.
        
        @param request: DescribeDtsJobDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDtsJobDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceID'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sync_sub_job_history):
            query['SyncSubJobHistory'] = request.sync_sub_job_history
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDtsJobDetail',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDtsJobDetailResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDtsJobDetailResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_dts_job_detail_with_options_async(
        self,
        request: dts_20200101_models.DescribeDtsJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDtsJobDetailResponse:
        """
        @summary The latency of incremental data migration or synchronization.
        \\\\\\\\\\>  If you query data migration tasks, the unit of this parameter is milliseconds. If you query data synchronization tasks, the unit of this parameter is seconds.
        
        @param request: DescribeDtsJobDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDtsJobDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceID'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sync_sub_job_history):
            query['SyncSubJobHistory'] = request.sync_sub_job_history
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDtsJobDetail',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDtsJobDetailResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDtsJobDetailResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_dts_job_detail(
        self,
        request: dts_20200101_models.DescribeDtsJobDetailRequest,
    ) -> dts_20200101_models.DescribeDtsJobDetailResponse:
        """
        @summary The latency of incremental data migration or synchronization.
        \\\\\\\\\\>  If you query data migration tasks, the unit of this parameter is milliseconds. If you query data synchronization tasks, the unit of this parameter is seconds.
        
        @param request: DescribeDtsJobDetailRequest
        @return: DescribeDtsJobDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dts_job_detail_with_options(request, runtime)

    async def describe_dts_job_detail_async(
        self,
        request: dts_20200101_models.DescribeDtsJobDetailRequest,
    ) -> dts_20200101_models.DescribeDtsJobDetailResponse:
        """
        @summary The latency of incremental data migration or synchronization.
        \\\\\\\\\\>  If you query data migration tasks, the unit of this parameter is milliseconds. If you query data synchronization tasks, the unit of this parameter is seconds.
        
        @param request: DescribeDtsJobDetailRequest
        @return: DescribeDtsJobDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dts_job_detail_with_options_async(request, runtime)

    def describe_dts_jobs_with_options(
        self,
        request: dts_20200101_models.DescribeDtsJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDtsJobsResponse:
        """
        @summary Queries the list of Data Transmission Service (DTS) tasks and the details of each task.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=Dts\\&api=DescribeDtsJobs\\&type=RPC\\&version=2020-01-01)
        
        @param request: DescribeDtsJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDtsJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.dest_product_type):
            query['DestProductType'] = request.dest_product_type
        if not UtilClient.is_unset(request.dts_bis_label):
            query['DtsBisLabel'] = request.dts_bis_label
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.order_column):
            query['OrderColumn'] = request.order_column
        if not UtilClient.is_unset(request.order_direction):
            query['OrderDirection'] = request.order_direction
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.src_product_type):
            query['SrcProductType'] = request.src_product_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.without_db_list):
            query['WithoutDbList'] = request.without_db_list
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDtsJobsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDtsJobsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_dts_jobs_with_options_async(
        self,
        request: dts_20200101_models.DescribeDtsJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDtsJobsResponse:
        """
        @summary Queries the list of Data Transmission Service (DTS) tasks and the details of each task.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=Dts\\&api=DescribeDtsJobs\\&type=RPC\\&version=2020-01-01)
        
        @param request: DescribeDtsJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDtsJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.dest_product_type):
            query['DestProductType'] = request.dest_product_type
        if not UtilClient.is_unset(request.dts_bis_label):
            query['DtsBisLabel'] = request.dts_bis_label
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.order_column):
            query['OrderColumn'] = request.order_column
        if not UtilClient.is_unset(request.order_direction):
            query['OrderDirection'] = request.order_direction
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.src_product_type):
            query['SrcProductType'] = request.src_product_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.without_db_list):
            query['WithoutDbList'] = request.without_db_list
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDtsJobsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDtsJobsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_dts_jobs(
        self,
        request: dts_20200101_models.DescribeDtsJobsRequest,
    ) -> dts_20200101_models.DescribeDtsJobsResponse:
        """
        @summary Queries the list of Data Transmission Service (DTS) tasks and the details of each task.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=Dts\\&api=DescribeDtsJobs\\&type=RPC\\&version=2020-01-01)
        
        @param request: DescribeDtsJobsRequest
        @return: DescribeDtsJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dts_jobs_with_options(request, runtime)

    async def describe_dts_jobs_async(
        self,
        request: dts_20200101_models.DescribeDtsJobsRequest,
    ) -> dts_20200101_models.DescribeDtsJobsResponse:
        """
        @summary Queries the list of Data Transmission Service (DTS) tasks and the details of each task.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=Dts\\&api=DescribeDtsJobs\\&type=RPC\\&version=2020-01-01)
        
        @param request: DescribeDtsJobsRequest
        @return: DescribeDtsJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dts_jobs_with_options_async(request, runtime)

    def describe_dts_service_log_with_options(
        self,
        request: dts_20200101_models.DescribeDtsServiceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDtsServiceLogResponse:
        """
        @summary Queries the logs of a data migration or synchronization task.
        
        @param request: DescribeDtsServiceLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDtsServiceLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.sub_job_type):
            query['SubJobType'] = request.sub_job_type
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDtsServiceLog',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDtsServiceLogResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDtsServiceLogResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_dts_service_log_with_options_async(
        self,
        request: dts_20200101_models.DescribeDtsServiceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDtsServiceLogResponse:
        """
        @summary Queries the logs of a data migration or synchronization task.
        
        @param request: DescribeDtsServiceLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDtsServiceLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.sub_job_type):
            query['SubJobType'] = request.sub_job_type
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDtsServiceLog',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeDtsServiceLogResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeDtsServiceLogResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_dts_service_log(
        self,
        request: dts_20200101_models.DescribeDtsServiceLogRequest,
    ) -> dts_20200101_models.DescribeDtsServiceLogResponse:
        """
        @summary Queries the logs of a data migration or synchronization task.
        
        @param request: DescribeDtsServiceLogRequest
        @return: DescribeDtsServiceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dts_service_log_with_options(request, runtime)

    async def describe_dts_service_log_async(
        self,
        request: dts_20200101_models.DescribeDtsServiceLogRequest,
    ) -> dts_20200101_models.DescribeDtsServiceLogResponse:
        """
        @summary Queries the logs of a data migration or synchronization task.
        
        @param request: DescribeDtsServiceLogRequest
        @return: DescribeDtsServiceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dts_service_log_with_options_async(request, runtime)

    def describe_endpoint_switch_status_with_options(
        self,
        request: dts_20200101_models.DescribeEndpointSwitchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeEndpointSwitchStatusResponse:
        """
        @summary Queries the status of the task that changes the database connection settings.
        
        @param request: DescribeEndpointSwitchStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEndpointSwitchStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEndpointSwitchStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeEndpointSwitchStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeEndpointSwitchStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_endpoint_switch_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeEndpointSwitchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeEndpointSwitchStatusResponse:
        """
        @summary Queries the status of the task that changes the database connection settings.
        
        @param request: DescribeEndpointSwitchStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEndpointSwitchStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEndpointSwitchStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeEndpointSwitchStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeEndpointSwitchStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_endpoint_switch_status(
        self,
        request: dts_20200101_models.DescribeEndpointSwitchStatusRequest,
    ) -> dts_20200101_models.DescribeEndpointSwitchStatusResponse:
        """
        @summary Queries the status of the task that changes the database connection settings.
        
        @param request: DescribeEndpointSwitchStatusRequest
        @return: DescribeEndpointSwitchStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_endpoint_switch_status_with_options(request, runtime)

    async def describe_endpoint_switch_status_async(
        self,
        request: dts_20200101_models.DescribeEndpointSwitchStatusRequest,
    ) -> dts_20200101_models.DescribeEndpointSwitchStatusResponse:
        """
        @summary Queries the status of the task that changes the database connection settings.
        
        @param request: DescribeEndpointSwitchStatusRequest
        @return: DescribeEndpointSwitchStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_endpoint_switch_status_with_options_async(request, runtime)

    def describe_etl_job_logs_with_options(
        self,
        request: dts_20200101_models.DescribeEtlJobLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeEtlJobLogsResponse:
        """
        @summary Queries the logs of extract, transform, and load (ETL) tasks.
        
        @param request: DescribeEtlJobLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEtlJobLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEtlJobLogs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeEtlJobLogsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeEtlJobLogsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_etl_job_logs_with_options_async(
        self,
        request: dts_20200101_models.DescribeEtlJobLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeEtlJobLogsResponse:
        """
        @summary Queries the logs of extract, transform, and load (ETL) tasks.
        
        @param request: DescribeEtlJobLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEtlJobLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEtlJobLogs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeEtlJobLogsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeEtlJobLogsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_etl_job_logs(
        self,
        request: dts_20200101_models.DescribeEtlJobLogsRequest,
    ) -> dts_20200101_models.DescribeEtlJobLogsResponse:
        """
        @summary Queries the logs of extract, transform, and load (ETL) tasks.
        
        @param request: DescribeEtlJobLogsRequest
        @return: DescribeEtlJobLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_etl_job_logs_with_options(request, runtime)

    async def describe_etl_job_logs_async(
        self,
        request: dts_20200101_models.DescribeEtlJobLogsRequest,
    ) -> dts_20200101_models.DescribeEtlJobLogsResponse:
        """
        @summary Queries the logs of extract, transform, and load (ETL) tasks.
        
        @param request: DescribeEtlJobLogsRequest
        @return: DescribeEtlJobLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_etl_job_logs_with_options_async(request, runtime)

    def describe_full_process_list_with_options(
        self,
        request: dts_20200101_models.DescribeFullProcessListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeFullProcessListResponse:
        """
        @summary Queries full data migration tasks.
        
        @param request: DescribeFullProcessListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFullProcessListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFullProcessList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeFullProcessListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeFullProcessListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_full_process_list_with_options_async(
        self,
        request: dts_20200101_models.DescribeFullProcessListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeFullProcessListResponse:
        """
        @summary Queries full data migration tasks.
        
        @param request: DescribeFullProcessListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFullProcessListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFullProcessList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeFullProcessListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeFullProcessListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_full_process_list(
        self,
        request: dts_20200101_models.DescribeFullProcessListRequest,
    ) -> dts_20200101_models.DescribeFullProcessListResponse:
        """
        @summary Queries full data migration tasks.
        
        @param request: DescribeFullProcessListRequest
        @return: DescribeFullProcessListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_full_process_list_with_options(request, runtime)

    async def describe_full_process_list_async(
        self,
        request: dts_20200101_models.DescribeFullProcessListRequest,
    ) -> dts_20200101_models.DescribeFullProcessListResponse:
        """
        @summary Queries full data migration tasks.
        
        @param request: DescribeFullProcessListRequest
        @return: DescribeFullProcessListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_full_process_list_with_options_async(request, runtime)

    def describe_gad_instances_with_options(
        self,
        request: dts_20200101_models.DescribeGadInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeGadInstancesResponse:
        """
        @summary 查询GAD实例列表
        
        @param request: DescribeGadInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGadInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.master_db_instance_id):
            query['MasterDbInstanceId'] = request.master_db_instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.slave_db_instance_id):
            query['SlaveDbInstanceId'] = request.slave_db_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGadInstances',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeGadInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeGadInstancesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_gad_instances_with_options_async(
        self,
        request: dts_20200101_models.DescribeGadInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeGadInstancesResponse:
        """
        @summary 查询GAD实例列表
        
        @param request: DescribeGadInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGadInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.master_db_instance_id):
            query['MasterDbInstanceId'] = request.master_db_instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.slave_db_instance_id):
            query['SlaveDbInstanceId'] = request.slave_db_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGadInstances',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeGadInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeGadInstancesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_gad_instances(
        self,
        request: dts_20200101_models.DescribeGadInstancesRequest,
    ) -> dts_20200101_models.DescribeGadInstancesResponse:
        """
        @summary 查询GAD实例列表
        
        @param request: DescribeGadInstancesRequest
        @return: DescribeGadInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_gad_instances_with_options(request, runtime)

    async def describe_gad_instances_async(
        self,
        request: dts_20200101_models.DescribeGadInstancesRequest,
    ) -> dts_20200101_models.DescribeGadInstancesResponse:
        """
        @summary 查询GAD实例列表
        
        @param request: DescribeGadInstancesRequest
        @return: DescribeGadInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_gad_instances_with_options_async(request, runtime)

    def describe_initialization_status_with_options(
        self,
        request: dts_20200101_models.DescribeInitializationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeInitializationStatusResponse:
        """
        @summary Queries the details of initial data synchronization, including the information about the schemas and historical data of the object to be synchronized.
        
        @param request: DescribeInitializationStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInitializationStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInitializationStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeInitializationStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeInitializationStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_initialization_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeInitializationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeInitializationStatusResponse:
        """
        @summary Queries the details of initial data synchronization, including the information about the schemas and historical data of the object to be synchronized.
        
        @param request: DescribeInitializationStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInitializationStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInitializationStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeInitializationStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeInitializationStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_initialization_status(
        self,
        request: dts_20200101_models.DescribeInitializationStatusRequest,
    ) -> dts_20200101_models.DescribeInitializationStatusResponse:
        """
        @summary Queries the details of initial data synchronization, including the information about the schemas and historical data of the object to be synchronized.
        
        @param request: DescribeInitializationStatusRequest
        @return: DescribeInitializationStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_initialization_status_with_options(request, runtime)

    async def describe_initialization_status_async(
        self,
        request: dts_20200101_models.DescribeInitializationStatusRequest,
    ) -> dts_20200101_models.DescribeInitializationStatusResponse:
        """
        @summary Queries the details of initial data synchronization, including the information about the schemas and historical data of the object to be synchronized.
        
        @param request: DescribeInitializationStatusRequest
        @return: DescribeInitializationStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_initialization_status_with_options_async(request, runtime)

    def describe_job_monitor_rule_with_options(
        self,
        request: dts_20200101_models.DescribeJobMonitorRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeJobMonitorRuleResponse:
        """
        @summary Queries the monitoring rules of a Data Transmission Service (DTS) task.
        
        @param request: DescribeJobMonitorRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobMonitorRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobMonitorRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeJobMonitorRuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeJobMonitorRuleResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_job_monitor_rule_with_options_async(
        self,
        request: dts_20200101_models.DescribeJobMonitorRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeJobMonitorRuleResponse:
        """
        @summary Queries the monitoring rules of a Data Transmission Service (DTS) task.
        
        @param request: DescribeJobMonitorRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobMonitorRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobMonitorRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeJobMonitorRuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeJobMonitorRuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_job_monitor_rule(
        self,
        request: dts_20200101_models.DescribeJobMonitorRuleRequest,
    ) -> dts_20200101_models.DescribeJobMonitorRuleResponse:
        """
        @summary Queries the monitoring rules of a Data Transmission Service (DTS) task.
        
        @param request: DescribeJobMonitorRuleRequest
        @return: DescribeJobMonitorRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_job_monitor_rule_with_options(request, runtime)

    async def describe_job_monitor_rule_async(
        self,
        request: dts_20200101_models.DescribeJobMonitorRuleRequest,
    ) -> dts_20200101_models.DescribeJobMonitorRuleResponse:
        """
        @summary Queries the monitoring rules of a Data Transmission Service (DTS) task.
        
        @param request: DescribeJobMonitorRuleRequest
        @return: DescribeJobMonitorRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_job_monitor_rule_with_options_async(request, runtime)

    def describe_metric_list_with_options(
        self,
        request: dts_20200101_models.DescribeMetricListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMetricListResponse:
        """
        @summary Queries the metrics of a cluster.
        
        @param request: DescribeMetricListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dts_job_id):
            body['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.env):
            body['Env'] = request.env
        if not UtilClient.is_unset(request.metric_name):
            body['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.metric_type):
            body['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerID'] = request.owner_id
        if not UtilClient.is_unset(request.param):
            body['Param'] = request.param
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeMetricList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeMetricListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeMetricListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_metric_list_with_options_async(
        self,
        request: dts_20200101_models.DescribeMetricListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMetricListResponse:
        """
        @summary Queries the metrics of a cluster.
        
        @param request: DescribeMetricListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dts_job_id):
            body['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.env):
            body['Env'] = request.env
        if not UtilClient.is_unset(request.metric_name):
            body['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.metric_type):
            body['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerID'] = request.owner_id
        if not UtilClient.is_unset(request.param):
            body['Param'] = request.param
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeMetricList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeMetricListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeMetricListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_metric_list(
        self,
        request: dts_20200101_models.DescribeMetricListRequest,
    ) -> dts_20200101_models.DescribeMetricListResponse:
        """
        @summary Queries the metrics of a cluster.
        
        @param request: DescribeMetricListRequest
        @return: DescribeMetricListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_list_with_options(request, runtime)

    async def describe_metric_list_async(
        self,
        request: dts_20200101_models.DescribeMetricListRequest,
    ) -> dts_20200101_models.DescribeMetricListResponse:
        """
        @summary Queries the metrics of a cluster.
        
        @param request: DescribeMetricListRequest
        @return: DescribeMetricListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_list_with_options_async(request, runtime)

    def describe_migration_job_alert_with_options(
        self,
        request: dts_20200101_models.DescribeMigrationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobAlertResponse:
        """
        @summary Queries the alert settings of a data migration instance.
        
        @param request: DescribeMigrationJobAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMigrationJobAlertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeMigrationJobAlertResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeMigrationJobAlertResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_migration_job_alert_with_options_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobAlertResponse:
        """
        @summary Queries the alert settings of a data migration instance.
        
        @param request: DescribeMigrationJobAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMigrationJobAlertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeMigrationJobAlertResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeMigrationJobAlertResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_migration_job_alert(
        self,
        request: dts_20200101_models.DescribeMigrationJobAlertRequest,
    ) -> dts_20200101_models.DescribeMigrationJobAlertResponse:
        """
        @summary Queries the alert settings of a data migration instance.
        
        @param request: DescribeMigrationJobAlertRequest
        @return: DescribeMigrationJobAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_job_alert_with_options(request, runtime)

    async def describe_migration_job_alert_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobAlertRequest,
    ) -> dts_20200101_models.DescribeMigrationJobAlertResponse:
        """
        @summary Queries the alert settings of a data migration instance.
        
        @param request: DescribeMigrationJobAlertRequest
        @return: DescribeMigrationJobAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_migration_job_alert_with_options_async(request, runtime)

    def describe_migration_job_detail_with_options(
        self,
        request: dts_20200101_models.DescribeMigrationJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobDetailResponse:
        """
        @summary Queries the details of a data migration task.
        
        @param request: DescribeMigrationJobDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMigrationJobDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.migration_mode):
            query['MigrationMode'] = request.migration_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobDetail',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeMigrationJobDetailResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeMigrationJobDetailResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_migration_job_detail_with_options_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobDetailResponse:
        """
        @summary Queries the details of a data migration task.
        
        @param request: DescribeMigrationJobDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMigrationJobDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.migration_mode):
            query['MigrationMode'] = request.migration_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobDetail',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeMigrationJobDetailResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeMigrationJobDetailResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_migration_job_detail(
        self,
        request: dts_20200101_models.DescribeMigrationJobDetailRequest,
    ) -> dts_20200101_models.DescribeMigrationJobDetailResponse:
        """
        @summary Queries the details of a data migration task.
        
        @param request: DescribeMigrationJobDetailRequest
        @return: DescribeMigrationJobDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_job_detail_with_options(request, runtime)

    async def describe_migration_job_detail_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobDetailRequest,
    ) -> dts_20200101_models.DescribeMigrationJobDetailResponse:
        """
        @summary Queries the details of a data migration task.
        
        @param request: DescribeMigrationJobDetailRequest
        @return: DescribeMigrationJobDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_migration_job_detail_with_options_async(request, runtime)

    def describe_migration_job_status_with_options(
        self,
        request: dts_20200101_models.DescribeMigrationJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobStatusResponse:
        """
        @summary Queries the status of a data migration task.
        
        @param request: DescribeMigrationJobStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMigrationJobStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeMigrationJobStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeMigrationJobStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_migration_job_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobStatusResponse:
        """
        @summary Queries the status of a data migration task.
        
        @param request: DescribeMigrationJobStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMigrationJobStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeMigrationJobStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeMigrationJobStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_migration_job_status(
        self,
        request: dts_20200101_models.DescribeMigrationJobStatusRequest,
    ) -> dts_20200101_models.DescribeMigrationJobStatusResponse:
        """
        @summary Queries the status of a data migration task.
        
        @param request: DescribeMigrationJobStatusRequest
        @return: DescribeMigrationJobStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_job_status_with_options(request, runtime)

    async def describe_migration_job_status_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobStatusRequest,
    ) -> dts_20200101_models.DescribeMigrationJobStatusResponse:
        """
        @summary Queries the status of a data migration task.
        
        @param request: DescribeMigrationJobStatusRequest
        @return: DescribeMigrationJobStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_migration_job_status_with_options_async(request, runtime)

    def describe_migration_jobs_with_options(
        self,
        request: dts_20200101_models.DescribeMigrationJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobsResponse:
        """
        @summary Queries the list of data migration instances and the details of each instance.
        
        @param request: DescribeMigrationJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMigrationJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeMigrationJobsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeMigrationJobsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_migration_jobs_with_options_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobsResponse:
        """
        @summary Queries the list of data migration instances and the details of each instance.
        
        @param request: DescribeMigrationJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMigrationJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeMigrationJobsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeMigrationJobsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_migration_jobs(
        self,
        request: dts_20200101_models.DescribeMigrationJobsRequest,
    ) -> dts_20200101_models.DescribeMigrationJobsResponse:
        """
        @summary Queries the list of data migration instances and the details of each instance.
        
        @param request: DescribeMigrationJobsRequest
        @return: DescribeMigrationJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_jobs_with_options(request, runtime)

    async def describe_migration_jobs_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobsRequest,
    ) -> dts_20200101_models.DescribeMigrationJobsResponse:
        """
        @summary Queries the list of data migration instances and the details of each instance.
        
        @param request: DescribeMigrationJobsRequest
        @return: DescribeMigrationJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_migration_jobs_with_options_async(request, runtime)

    def describe_pre_check_create_gad_order_result_with_options(
        self,
        request: dts_20200101_models.DescribePreCheckCreateGadOrderResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribePreCheckCreateGadOrderResultResponse:
        """
        @summary 查询预检查创建GAD订单任务结果
        
        @param request: DescribePreCheckCreateGadOrderResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePreCheckCreateGadOrderResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePreCheckCreateGadOrderResult',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribePreCheckCreateGadOrderResultResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribePreCheckCreateGadOrderResultResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_pre_check_create_gad_order_result_with_options_async(
        self,
        request: dts_20200101_models.DescribePreCheckCreateGadOrderResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribePreCheckCreateGadOrderResultResponse:
        """
        @summary 查询预检查创建GAD订单任务结果
        
        @param request: DescribePreCheckCreateGadOrderResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePreCheckCreateGadOrderResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePreCheckCreateGadOrderResult',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribePreCheckCreateGadOrderResultResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribePreCheckCreateGadOrderResultResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_pre_check_create_gad_order_result(
        self,
        request: dts_20200101_models.DescribePreCheckCreateGadOrderResultRequest,
    ) -> dts_20200101_models.DescribePreCheckCreateGadOrderResultResponse:
        """
        @summary 查询预检查创建GAD订单任务结果
        
        @param request: DescribePreCheckCreateGadOrderResultRequest
        @return: DescribePreCheckCreateGadOrderResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pre_check_create_gad_order_result_with_options(request, runtime)

    async def describe_pre_check_create_gad_order_result_async(
        self,
        request: dts_20200101_models.DescribePreCheckCreateGadOrderResultRequest,
    ) -> dts_20200101_models.DescribePreCheckCreateGadOrderResultResponse:
        """
        @summary 查询预检查创建GAD订单任务结果
        
        @param request: DescribePreCheckCreateGadOrderResultRequest
        @return: DescribePreCheckCreateGadOrderResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pre_check_create_gad_order_result_with_options_async(request, runtime)

    def describe_pre_check_status_with_options(
        self,
        request: dts_20200101_models.DescribePreCheckStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribePreCheckStatusResponse:
        """
        @summary Queries the status of a Data Transmission Service (DTS) subtask that performs precheck, schema migration, initial schema synchronization, full data migration, initial full data synchronization, incremental data migration, or incremental data synchronization.
        
        @param request: DescribePreCheckStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePreCheckStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.job_code):
            query['JobCode'] = request.job_code
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.struct_phase):
            query['StructPhase'] = request.struct_phase
        if not UtilClient.is_unset(request.struct_type):
            query['StructType'] = request.struct_type
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePreCheckStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribePreCheckStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribePreCheckStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_pre_check_status_with_options_async(
        self,
        request: dts_20200101_models.DescribePreCheckStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribePreCheckStatusResponse:
        """
        @summary Queries the status of a Data Transmission Service (DTS) subtask that performs precheck, schema migration, initial schema synchronization, full data migration, initial full data synchronization, incremental data migration, or incremental data synchronization.
        
        @param request: DescribePreCheckStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePreCheckStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.job_code):
            query['JobCode'] = request.job_code
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.struct_phase):
            query['StructPhase'] = request.struct_phase
        if not UtilClient.is_unset(request.struct_type):
            query['StructType'] = request.struct_type
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePreCheckStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribePreCheckStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribePreCheckStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_pre_check_status(
        self,
        request: dts_20200101_models.DescribePreCheckStatusRequest,
    ) -> dts_20200101_models.DescribePreCheckStatusResponse:
        """
        @summary Queries the status of a Data Transmission Service (DTS) subtask that performs precheck, schema migration, initial schema synchronization, full data migration, initial full data synchronization, incremental data migration, or incremental data synchronization.
        
        @param request: DescribePreCheckStatusRequest
        @return: DescribePreCheckStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pre_check_status_with_options(request, runtime)

    async def describe_pre_check_status_async(
        self,
        request: dts_20200101_models.DescribePreCheckStatusRequest,
    ) -> dts_20200101_models.DescribePreCheckStatusResponse:
        """
        @summary Queries the status of a Data Transmission Service (DTS) subtask that performs precheck, schema migration, initial schema synchronization, full data migration, initial full data synchronization, incremental data migration, or incremental data synchronization.
        
        @param request: DescribePreCheckStatusRequest
        @return: DescribePreCheckStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pre_check_status_with_options_async(request, runtime)

    def describe_subscription_instance_alert_with_options(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceAlertResponse:
        """
        @summary Queries the alert settings of a change tracking instance.
        
        @param request: DescribeSubscriptionInstanceAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSubscriptionInstanceAlertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionInstanceAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSubscriptionInstanceAlertResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSubscriptionInstanceAlertResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_subscription_instance_alert_with_options_async(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceAlertResponse:
        """
        @summary Queries the alert settings of a change tracking instance.
        
        @param request: DescribeSubscriptionInstanceAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSubscriptionInstanceAlertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionInstanceAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSubscriptionInstanceAlertResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSubscriptionInstanceAlertResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_subscription_instance_alert(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceAlertRequest,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceAlertResponse:
        """
        @summary Queries the alert settings of a change tracking instance.
        
        @param request: DescribeSubscriptionInstanceAlertRequest
        @return: DescribeSubscriptionInstanceAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_instance_alert_with_options(request, runtime)

    async def describe_subscription_instance_alert_async(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceAlertRequest,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceAlertResponse:
        """
        @summary Queries the alert settings of a change tracking instance.
        
        @param request: DescribeSubscriptionInstanceAlertRequest
        @return: DescribeSubscriptionInstanceAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_subscription_instance_alert_with_options_async(request, runtime)

    def describe_subscription_instance_status_with_options(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceStatusResponse:
        """
        @summary Queries the status of a change tracking instance.
        
        @param request: DescribeSubscriptionInstanceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSubscriptionInstanceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionInstanceStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSubscriptionInstanceStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSubscriptionInstanceStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_subscription_instance_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceStatusResponse:
        """
        @summary Queries the status of a change tracking instance.
        
        @param request: DescribeSubscriptionInstanceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSubscriptionInstanceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionInstanceStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSubscriptionInstanceStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSubscriptionInstanceStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_subscription_instance_status(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceStatusRequest,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceStatusResponse:
        """
        @summary Queries the status of a change tracking instance.
        
        @param request: DescribeSubscriptionInstanceStatusRequest
        @return: DescribeSubscriptionInstanceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_instance_status_with_options(request, runtime)

    async def describe_subscription_instance_status_async(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceStatusRequest,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceStatusResponse:
        """
        @summary Queries the status of a change tracking instance.
        
        @param request: DescribeSubscriptionInstanceStatusRequest
        @return: DescribeSubscriptionInstanceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_subscription_instance_status_with_options_async(request, runtime)

    def describe_subscription_instances_with_options(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionInstancesResponse:
        """
        @summary Queries the list of change tracking instances and the details of each instance.
        
        @param request: DescribeSubscriptionInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSubscriptionInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_name):
            query['SubscriptionInstanceName'] = request.subscription_instance_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionInstances',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSubscriptionInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSubscriptionInstancesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_subscription_instances_with_options_async(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionInstancesResponse:
        """
        @summary Queries the list of change tracking instances and the details of each instance.
        
        @param request: DescribeSubscriptionInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSubscriptionInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_name):
            query['SubscriptionInstanceName'] = request.subscription_instance_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionInstances',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSubscriptionInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSubscriptionInstancesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_subscription_instances(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstancesRequest,
    ) -> dts_20200101_models.DescribeSubscriptionInstancesResponse:
        """
        @summary Queries the list of change tracking instances and the details of each instance.
        
        @param request: DescribeSubscriptionInstancesRequest
        @return: DescribeSubscriptionInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_instances_with_options(request, runtime)

    async def describe_subscription_instances_async(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstancesRequest,
    ) -> dts_20200101_models.DescribeSubscriptionInstancesResponse:
        """
        @summary Queries the list of change tracking instances and the details of each instance.
        
        @param request: DescribeSubscriptionInstancesRequest
        @return: DescribeSubscriptionInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_subscription_instances_with_options_async(request, runtime)

    def describe_subscription_meta_with_options(
        self,
        tmp_req: dts_20200101_models.DescribeSubscriptionMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionMetaResponse:
        """
        @summary Queries the details of the subtasks in a distributed change tracking task for a PolarDB-X 1.0 instance.
        
        @description    When Data Transmission Service (DTS) tracks data changes from a PolarDB-X 1.0 instance, data is distributed across the attached ApsaraDB RDS for MySQL instances. DTS runs a subtask for each ApsaraDB RDS for MySQL instance. You can call this operation to query the details of the subtasks in a distributed change tracking task.
        You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the ID of the change tracking instance and the ID of the consumer group.
        
        @param tmp_req: DescribeSubscriptionMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSubscriptionMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dts_20200101_models.DescribeSubscriptionMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_migration_job_ids):
            request.sub_migration_job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_migration_job_ids, 'SubMigrationJobIds', 'json')
        if not UtilClient.is_unset(tmp_req.topics):
            request.topics_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.sub_migration_job_ids_shrink):
            query['SubMigrationJobIds'] = request.sub_migration_job_ids_shrink
        if not UtilClient.is_unset(request.topics_shrink):
            query['Topics'] = request.topics_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionMeta',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSubscriptionMetaResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSubscriptionMetaResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_subscription_meta_with_options_async(
        self,
        tmp_req: dts_20200101_models.DescribeSubscriptionMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionMetaResponse:
        """
        @summary Queries the details of the subtasks in a distributed change tracking task for a PolarDB-X 1.0 instance.
        
        @description    When Data Transmission Service (DTS) tracks data changes from a PolarDB-X 1.0 instance, data is distributed across the attached ApsaraDB RDS for MySQL instances. DTS runs a subtask for each ApsaraDB RDS for MySQL instance. You can call this operation to query the details of the subtasks in a distributed change tracking task.
        You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the ID of the change tracking instance and the ID of the consumer group.
        
        @param tmp_req: DescribeSubscriptionMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSubscriptionMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dts_20200101_models.DescribeSubscriptionMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_migration_job_ids):
            request.sub_migration_job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_migration_job_ids, 'SubMigrationJobIds', 'json')
        if not UtilClient.is_unset(tmp_req.topics):
            request.topics_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.sub_migration_job_ids_shrink):
            query['SubMigrationJobIds'] = request.sub_migration_job_ids_shrink
        if not UtilClient.is_unset(request.topics_shrink):
            query['Topics'] = request.topics_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionMeta',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSubscriptionMetaResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSubscriptionMetaResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_subscription_meta(
        self,
        request: dts_20200101_models.DescribeSubscriptionMetaRequest,
    ) -> dts_20200101_models.DescribeSubscriptionMetaResponse:
        """
        @summary Queries the details of the subtasks in a distributed change tracking task for a PolarDB-X 1.0 instance.
        
        @description    When Data Transmission Service (DTS) tracks data changes from a PolarDB-X 1.0 instance, data is distributed across the attached ApsaraDB RDS for MySQL instances. DTS runs a subtask for each ApsaraDB RDS for MySQL instance. You can call this operation to query the details of the subtasks in a distributed change tracking task.
        You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the ID of the change tracking instance and the ID of the consumer group.
        
        @param request: DescribeSubscriptionMetaRequest
        @return: DescribeSubscriptionMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_meta_with_options(request, runtime)

    async def describe_subscription_meta_async(
        self,
        request: dts_20200101_models.DescribeSubscriptionMetaRequest,
    ) -> dts_20200101_models.DescribeSubscriptionMetaResponse:
        """
        @summary Queries the details of the subtasks in a distributed change tracking task for a PolarDB-X 1.0 instance.
        
        @description    When Data Transmission Service (DTS) tracks data changes from a PolarDB-X 1.0 instance, data is distributed across the attached ApsaraDB RDS for MySQL instances. DTS runs a subtask for each ApsaraDB RDS for MySQL instance. You can call this operation to query the details of the subtasks in a distributed change tracking task.
        You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the ID of the change tracking instance and the ID of the consumer group.
        
        @param request: DescribeSubscriptionMetaRequest
        @return: DescribeSubscriptionMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_subscription_meta_with_options_async(request, runtime)

    def describe_sync_status_with_options(
        self,
        request: dts_20200101_models.DescribeSyncStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSyncStatusResponse:
        """
        @summary 查看同步和迁移任务的增量写入延迟信息
        
        @param request: DescribeSyncStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSyncStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSyncStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSyncStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSyncStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_sync_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeSyncStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSyncStatusResponse:
        """
        @summary 查看同步和迁移任务的增量写入延迟信息
        
        @param request: DescribeSyncStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSyncStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSyncStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSyncStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSyncStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_sync_status(
        self,
        request: dts_20200101_models.DescribeSyncStatusRequest,
    ) -> dts_20200101_models.DescribeSyncStatusResponse:
        """
        @summary 查看同步和迁移任务的增量写入延迟信息
        
        @param request: DescribeSyncStatusRequest
        @return: DescribeSyncStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sync_status_with_options(request, runtime)

    async def describe_sync_status_async(
        self,
        request: dts_20200101_models.DescribeSyncStatusRequest,
    ) -> dts_20200101_models.DescribeSyncStatusResponse:
        """
        @summary 查看同步和迁移任务的增量写入延迟信息
        
        @param request: DescribeSyncStatusRequest
        @return: DescribeSyncStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sync_status_with_options_async(request, runtime)

    def describe_synchronization_job_alert_with_options(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobAlertResponse:
        """
        @summary Queries the alert settings of a data synchronization instance.
        
        @param request: DescribeSynchronizationJobAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSynchronizationJobAlertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationJobAlertResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationJobAlertResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_synchronization_job_alert_with_options_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobAlertResponse:
        """
        @summary Queries the alert settings of a data synchronization instance.
        
        @param request: DescribeSynchronizationJobAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSynchronizationJobAlertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationJobAlertResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationJobAlertResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_synchronization_job_alert(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobAlertRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobAlertResponse:
        """
        @summary Queries the alert settings of a data synchronization instance.
        
        @param request: DescribeSynchronizationJobAlertRequest
        @return: DescribeSynchronizationJobAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_job_alert_with_options(request, runtime)

    async def describe_synchronization_job_alert_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobAlertRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobAlertResponse:
        """
        @summary Queries the alert settings of a data synchronization instance.
        
        @param request: DescribeSynchronizationJobAlertRequest
        @return: DescribeSynchronizationJobAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronization_job_alert_with_options_async(request, runtime)

    def describe_synchronization_job_replicator_compare_with_options(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobReplicatorCompareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse:
        """
        @summary Queries whether image matching is enabled for a data synchronization instance.
        
        @param request: DescribeSynchronizationJobReplicatorCompareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSynchronizationJobReplicatorCompareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobReplicatorCompare',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_synchronization_job_replicator_compare_with_options_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobReplicatorCompareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse:
        """
        @summary Queries whether image matching is enabled for a data synchronization instance.
        
        @param request: DescribeSynchronizationJobReplicatorCompareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSynchronizationJobReplicatorCompareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobReplicatorCompare',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_synchronization_job_replicator_compare(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobReplicatorCompareRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse:
        """
        @summary Queries whether image matching is enabled for a data synchronization instance.
        
        @param request: DescribeSynchronizationJobReplicatorCompareRequest
        @return: DescribeSynchronizationJobReplicatorCompareResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_job_replicator_compare_with_options(request, runtime)

    async def describe_synchronization_job_replicator_compare_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobReplicatorCompareRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse:
        """
        @summary Queries whether image matching is enabled for a data synchronization instance.
        
        @param request: DescribeSynchronizationJobReplicatorCompareRequest
        @return: DescribeSynchronizationJobReplicatorCompareResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronization_job_replicator_compare_with_options_async(request, runtime)

    def describe_synchronization_job_status_with_options(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusResponse:
        """
        @summary Queries the status of a data synchronization instance.
        
        @param request: DescribeSynchronizationJobStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSynchronizationJobStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationJobStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationJobStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_synchronization_job_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusResponse:
        """
        @summary Queries the status of a data synchronization instance.
        
        @param request: DescribeSynchronizationJobStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSynchronizationJobStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationJobStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationJobStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_synchronization_job_status(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusResponse:
        """
        @summary Queries the status of a data synchronization instance.
        
        @param request: DescribeSynchronizationJobStatusRequest
        @return: DescribeSynchronizationJobStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_job_status_with_options(request, runtime)

    async def describe_synchronization_job_status_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusResponse:
        """
        @summary Queries the status of a data synchronization instance.
        
        @param request: DescribeSynchronizationJobStatusRequest
        @return: DescribeSynchronizationJobStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronization_job_status_with_options_async(request, runtime)

    def describe_synchronization_job_status_list_with_options(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusListResponse:
        """
        @summary Queries the status of one or more data synchronization instances.
        
        @param request: DescribeSynchronizationJobStatusListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSynchronizationJobStatusListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_job_id_list_json_str):
            query['SynchronizationJobIdListJsonStr'] = request.synchronization_job_id_list_json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobStatusList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationJobStatusListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationJobStatusListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_synchronization_job_status_list_with_options_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusListResponse:
        """
        @summary Queries the status of one or more data synchronization instances.
        
        @param request: DescribeSynchronizationJobStatusListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSynchronizationJobStatusListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_job_id_list_json_str):
            query['SynchronizationJobIdListJsonStr'] = request.synchronization_job_id_list_json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobStatusList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationJobStatusListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationJobStatusListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_synchronization_job_status_list(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusListRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusListResponse:
        """
        @summary Queries the status of one or more data synchronization instances.
        
        @param request: DescribeSynchronizationJobStatusListRequest
        @return: DescribeSynchronizationJobStatusListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_job_status_list_with_options(request, runtime)

    async def describe_synchronization_job_status_list_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusListRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusListResponse:
        """
        @summary Queries the status of one or more data synchronization instances.
        
        @param request: DescribeSynchronizationJobStatusListRequest
        @return: DescribeSynchronizationJobStatusListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronization_job_status_list_with_options_async(request, runtime)

    def describe_synchronization_jobs_with_options(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobsResponse:
        """
        @summary Queries the list of data synchronization instances and the details of each instance.
        
        @param request: DescribeSynchronizationJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSynchronizationJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_job_name):
            query['SynchronizationJobName'] = request.synchronization_job_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationJobsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationJobsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_synchronization_jobs_with_options_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobsResponse:
        """
        @summary Queries the list of data synchronization instances and the details of each instance.
        
        @param request: DescribeSynchronizationJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSynchronizationJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_job_name):
            query['SynchronizationJobName'] = request.synchronization_job_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationJobsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationJobsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_synchronization_jobs(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobsRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobsResponse:
        """
        @summary Queries the list of data synchronization instances and the details of each instance.
        
        @param request: DescribeSynchronizationJobsRequest
        @return: DescribeSynchronizationJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_jobs_with_options(request, runtime)

    async def describe_synchronization_jobs_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobsRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobsResponse:
        """
        @summary Queries the list of data synchronization instances and the details of each instance.
        
        @param request: DescribeSynchronizationJobsRequest
        @return: DescribeSynchronizationJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronization_jobs_with_options_async(request, runtime)

    def describe_synchronization_object_modify_status_with_options(
        self,
        request: dts_20200101_models.DescribeSynchronizationObjectModifyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse:
        """
        @summary Queries the status of the task that changes the objects to be synchronized.
        
        @param request: DescribeSynchronizationObjectModifyStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSynchronizationObjectModifyStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationObjectModifyStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_synchronization_object_modify_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationObjectModifyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse:
        """
        @summary Queries the status of the task that changes the objects to be synchronized.
        
        @param request: DescribeSynchronizationObjectModifyStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSynchronizationObjectModifyStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationObjectModifyStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_synchronization_object_modify_status(
        self,
        request: dts_20200101_models.DescribeSynchronizationObjectModifyStatusRequest,
    ) -> dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse:
        """
        @summary Queries the status of the task that changes the objects to be synchronized.
        
        @param request: DescribeSynchronizationObjectModifyStatusRequest
        @return: DescribeSynchronizationObjectModifyStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_object_modify_status_with_options(request, runtime)

    async def describe_synchronization_object_modify_status_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationObjectModifyStatusRequest,
    ) -> dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse:
        """
        @summary Queries the status of the task that changes the objects to be synchronized.
        
        @param request: DescribeSynchronizationObjectModifyStatusRequest
        @return: DescribeSynchronizationObjectModifyStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronization_object_modify_status_with_options_async(request, runtime)

    def describe_tag_keys_with_options(
        self,
        request: dts_20200101_models.DescribeTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeTagKeysResponse:
        """
        @summary Queries all the tags added to a data migration, data synchronization, or change tracking instance.
        
        @param request: DescribeTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagKeys',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeTagKeysResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeTagKeysResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_tag_keys_with_options_async(
        self,
        request: dts_20200101_models.DescribeTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeTagKeysResponse:
        """
        @summary Queries all the tags added to a data migration, data synchronization, or change tracking instance.
        
        @param request: DescribeTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagKeys',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeTagKeysResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeTagKeysResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_tag_keys(
        self,
        request: dts_20200101_models.DescribeTagKeysRequest,
    ) -> dts_20200101_models.DescribeTagKeysResponse:
        """
        @summary Queries all the tags added to a data migration, data synchronization, or change tracking instance.
        
        @param request: DescribeTagKeysRequest
        @return: DescribeTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_keys_with_options(request, runtime)

    async def describe_tag_keys_async(
        self,
        request: dts_20200101_models.DescribeTagKeysRequest,
    ) -> dts_20200101_models.DescribeTagKeysResponse:
        """
        @summary Queries all the tags added to a data migration, data synchronization, or change tracking instance.
        
        @param request: DescribeTagKeysRequest
        @return: DescribeTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tag_keys_with_options_async(request, runtime)

    def describe_tag_values_with_options(
        self,
        request: dts_20200101_models.DescribeTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeTagValuesResponse:
        """
        @summary Queries all the tag values of a tag bound to a data migration, data synchronization, or change tracking instance.
        
        @param request: DescribeTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagValues',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeTagValuesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeTagValuesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_tag_values_with_options_async(
        self,
        request: dts_20200101_models.DescribeTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeTagValuesResponse:
        """
        @summary Queries all the tag values of a tag bound to a data migration, data synchronization, or change tracking instance.
        
        @param request: DescribeTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagValues',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DescribeTagValuesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DescribeTagValuesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_tag_values(
        self,
        request: dts_20200101_models.DescribeTagValuesRequest,
    ) -> dts_20200101_models.DescribeTagValuesResponse:
        """
        @summary Queries all the tag values of a tag bound to a data migration, data synchronization, or change tracking instance.
        
        @param request: DescribeTagValuesRequest
        @return: DescribeTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_values_with_options(request, runtime)

    async def describe_tag_values_async(
        self,
        request: dts_20200101_models.DescribeTagValuesRequest,
    ) -> dts_20200101_models.DescribeTagValuesResponse:
        """
        @summary Queries all the tag values of a tag bound to a data migration, data synchronization, or change tracking instance.
        
        @param request: DescribeTagValuesRequest
        @return: DescribeTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tag_values_with_options_async(request, runtime)

    def detach_gad_instance_db_member_with_options(
        self,
        request: dts_20200101_models.DetachGadInstanceDbMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DetachGadInstanceDbMemberResponse:
        """
        @summary 移除从角色
        
        @param request: DetachGadInstanceDbMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachGadInstanceDbMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.slave_db_instance_id):
            query['SlaveDbInstanceId'] = request.slave_db_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachGadInstanceDbMember',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DetachGadInstanceDbMemberResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DetachGadInstanceDbMemberResponse(),
                self.execute(params, req, runtime)
            )

    async def detach_gad_instance_db_member_with_options_async(
        self,
        request: dts_20200101_models.DetachGadInstanceDbMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DetachGadInstanceDbMemberResponse:
        """
        @summary 移除从角色
        
        @param request: DetachGadInstanceDbMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachGadInstanceDbMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.slave_db_instance_id):
            query['SlaveDbInstanceId'] = request.slave_db_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachGadInstanceDbMember',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.DetachGadInstanceDbMemberResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.DetachGadInstanceDbMemberResponse(),
                await self.execute_async(params, req, runtime)
            )

    def detach_gad_instance_db_member(
        self,
        request: dts_20200101_models.DetachGadInstanceDbMemberRequest,
    ) -> dts_20200101_models.DetachGadInstanceDbMemberResponse:
        """
        @summary 移除从角色
        
        @param request: DetachGadInstanceDbMemberRequest
        @return: DetachGadInstanceDbMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_gad_instance_db_member_with_options(request, runtime)

    async def detach_gad_instance_db_member_async(
        self,
        request: dts_20200101_models.DetachGadInstanceDbMemberRequest,
    ) -> dts_20200101_models.DetachGadInstanceDbMemberResponse:
        """
        @summary 移除从角色
        
        @param request: DetachGadInstanceDbMemberRequest
        @return: DetachGadInstanceDbMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_gad_instance_db_member_with_options_async(request, runtime)

    def init_dts_rds_instance_with_options(
        self,
        request: dts_20200101_models.InitDtsRdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.InitDtsRdsInstanceResponse:
        """
        @summary Initializes a built-in account on a node of an active geo-redundancy database cluster. Data Transmission Service (DTS) uses the built-in account to connect to the node and perform data synchronization tasks.
        
        @description    The node must be an ApsaraDB RDS for MySQL instance or a self-managed MySQL database that is connected over Cloud Enterprise Network (CEN).
        This operation is used to initialize the built-in account named rdsdt_dtsacct on a node of an active geo-redundancy database cluster. DTS uses this account to connect to the node and perform data synchronization tasks.
        
        @param request: InitDtsRdsInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitDtsRdsInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.endpoint_cen_id):
            query['EndpointCenId'] = request.endpoint_cen_id
        if not UtilClient.is_unset(request.endpoint_instance_id):
            query['EndpointInstanceId'] = request.endpoint_instance_id
        if not UtilClient.is_unset(request.endpoint_instance_type):
            query['EndpointInstanceType'] = request.endpoint_instance_type
        if not UtilClient.is_unset(request.endpoint_region):
            query['EndpointRegion'] = request.endpoint_region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitDtsRdsInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.InitDtsRdsInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.InitDtsRdsInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def init_dts_rds_instance_with_options_async(
        self,
        request: dts_20200101_models.InitDtsRdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.InitDtsRdsInstanceResponse:
        """
        @summary Initializes a built-in account on a node of an active geo-redundancy database cluster. Data Transmission Service (DTS) uses the built-in account to connect to the node and perform data synchronization tasks.
        
        @description    The node must be an ApsaraDB RDS for MySQL instance or a self-managed MySQL database that is connected over Cloud Enterprise Network (CEN).
        This operation is used to initialize the built-in account named rdsdt_dtsacct on a node of an active geo-redundancy database cluster. DTS uses this account to connect to the node and perform data synchronization tasks.
        
        @param request: InitDtsRdsInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitDtsRdsInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.endpoint_cen_id):
            query['EndpointCenId'] = request.endpoint_cen_id
        if not UtilClient.is_unset(request.endpoint_instance_id):
            query['EndpointInstanceId'] = request.endpoint_instance_id
        if not UtilClient.is_unset(request.endpoint_instance_type):
            query['EndpointInstanceType'] = request.endpoint_instance_type
        if not UtilClient.is_unset(request.endpoint_region):
            query['EndpointRegion'] = request.endpoint_region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitDtsRdsInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.InitDtsRdsInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.InitDtsRdsInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def init_dts_rds_instance(
        self,
        request: dts_20200101_models.InitDtsRdsInstanceRequest,
    ) -> dts_20200101_models.InitDtsRdsInstanceResponse:
        """
        @summary Initializes a built-in account on a node of an active geo-redundancy database cluster. Data Transmission Service (DTS) uses the built-in account to connect to the node and perform data synchronization tasks.
        
        @description    The node must be an ApsaraDB RDS for MySQL instance or a self-managed MySQL database that is connected over Cloud Enterprise Network (CEN).
        This operation is used to initialize the built-in account named rdsdt_dtsacct on a node of an active geo-redundancy database cluster. DTS uses this account to connect to the node and perform data synchronization tasks.
        
        @param request: InitDtsRdsInstanceRequest
        @return: InitDtsRdsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.init_dts_rds_instance_with_options(request, runtime)

    async def init_dts_rds_instance_async(
        self,
        request: dts_20200101_models.InitDtsRdsInstanceRequest,
    ) -> dts_20200101_models.InitDtsRdsInstanceResponse:
        """
        @summary Initializes a built-in account on a node of an active geo-redundancy database cluster. Data Transmission Service (DTS) uses the built-in account to connect to the node and perform data synchronization tasks.
        
        @description    The node must be an ApsaraDB RDS for MySQL instance or a self-managed MySQL database that is connected over Cloud Enterprise Network (CEN).
        This operation is used to initialize the built-in account named rdsdt_dtsacct on a node of an active geo-redundancy database cluster. DTS uses this account to connect to the node and perform data synchronization tasks.
        
        @param request: InitDtsRdsInstanceRequest
        @return: InitDtsRdsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.init_dts_rds_instance_with_options_async(request, runtime)

    def list_dedicated_cluster_with_options(
        self,
        request: dts_20200101_models.ListDedicatedClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ListDedicatedClusterResponse:
        """
        @summary Queries all clusters that are created within an Alibaba Cloud account. You can also query clusters based on the specified conditions.
        
        @param request: ListDedicatedClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDedicatedClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_column):
            query['OrderColumn'] = request.order_column
        if not UtilClient.is_unset(request.order_direction):
            query['OrderDirection'] = request.order_direction
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDedicatedCluster',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ListDedicatedClusterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ListDedicatedClusterResponse(),
                self.execute(params, req, runtime)
            )

    async def list_dedicated_cluster_with_options_async(
        self,
        request: dts_20200101_models.ListDedicatedClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ListDedicatedClusterResponse:
        """
        @summary Queries all clusters that are created within an Alibaba Cloud account. You can also query clusters based on the specified conditions.
        
        @param request: ListDedicatedClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDedicatedClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_column):
            query['OrderColumn'] = request.order_column
        if not UtilClient.is_unset(request.order_direction):
            query['OrderDirection'] = request.order_direction
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDedicatedCluster',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ListDedicatedClusterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ListDedicatedClusterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_dedicated_cluster(
        self,
        request: dts_20200101_models.ListDedicatedClusterRequest,
    ) -> dts_20200101_models.ListDedicatedClusterResponse:
        """
        @summary Queries all clusters that are created within an Alibaba Cloud account. You can also query clusters based on the specified conditions.
        
        @param request: ListDedicatedClusterRequest
        @return: ListDedicatedClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dedicated_cluster_with_options(request, runtime)

    async def list_dedicated_cluster_async(
        self,
        request: dts_20200101_models.ListDedicatedClusterRequest,
    ) -> dts_20200101_models.ListDedicatedClusterResponse:
        """
        @summary Queries all clusters that are created within an Alibaba Cloud account. You can also query clusters based on the specified conditions.
        
        @param request: ListDedicatedClusterRequest
        @return: ListDedicatedClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_dedicated_cluster_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: dts_20200101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are bound to specific data migration, data synchronization, or change tracking instances, or queries the instances to which specific tags are bound.
        
        @description ***\
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ListTagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ListTagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_tag_resources_with_options_async(
        self,
        request: dts_20200101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are bound to specific data migration, data synchronization, or change tracking instances, or queries the instances to which specific tags are bound.
        
        @description ***\
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ListTagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ListTagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_tag_resources(
        self,
        request: dts_20200101_models.ListTagResourcesRequest,
    ) -> dts_20200101_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are bound to specific data migration, data synchronization, or change tracking instances, or queries the instances to which specific tags are bound.
        
        @description ***\
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: dts_20200101_models.ListTagResourcesRequest,
    ) -> dts_20200101_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are bound to specific data migration, data synchronization, or change tracking instances, or queries the instances to which specific tags are bound.
        
        @description ***\
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_consumer_channel_with_options(
        self,
        request: dts_20200101_models.ModifyConsumerChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyConsumerChannelResponse:
        """
        @summary Modifies the information of a consumer group, including the consumer group name, username, and password.
        
        @param request: ModifyConsumerChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyConsumerChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupId'] = request.consumer_group_id
        if not UtilClient.is_unset(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not UtilClient.is_unset(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not UtilClient.is_unset(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyConsumerChannel',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyConsumerChannelResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyConsumerChannelResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_consumer_channel_with_options_async(
        self,
        request: dts_20200101_models.ModifyConsumerChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyConsumerChannelResponse:
        """
        @summary Modifies the information of a consumer group, including the consumer group name, username, and password.
        
        @param request: ModifyConsumerChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyConsumerChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupId'] = request.consumer_group_id
        if not UtilClient.is_unset(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not UtilClient.is_unset(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not UtilClient.is_unset(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyConsumerChannel',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyConsumerChannelResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyConsumerChannelResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_consumer_channel(
        self,
        request: dts_20200101_models.ModifyConsumerChannelRequest,
    ) -> dts_20200101_models.ModifyConsumerChannelResponse:
        """
        @summary Modifies the information of a consumer group, including the consumer group name, username, and password.
        
        @param request: ModifyConsumerChannelRequest
        @return: ModifyConsumerChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_consumer_channel_with_options(request, runtime)

    async def modify_consumer_channel_async(
        self,
        request: dts_20200101_models.ModifyConsumerChannelRequest,
    ) -> dts_20200101_models.ModifyConsumerChannelResponse:
        """
        @summary Modifies the information of a consumer group, including the consumer group name, username, and password.
        
        @param request: ModifyConsumerChannelRequest
        @return: ModifyConsumerChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_consumer_channel_with_options_async(request, runtime)

    def modify_consumer_group_password_with_options(
        self,
        request: dts_20200101_models.ModifyConsumerGroupPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyConsumerGroupPasswordResponse:
        """
        @summary Modifies the password of a consumer group
        
        @param request: ModifyConsumerGroupPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyConsumerGroupPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupID'] = request.consumer_group_id
        if not UtilClient.is_unset(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not UtilClient.is_unset(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not UtilClient.is_unset(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not UtilClient.is_unset(request.consumer_group_new_password):
            query['consumerGroupNewPassword'] = request.consumer_group_new_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyConsumerGroupPassword',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyConsumerGroupPasswordResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyConsumerGroupPasswordResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_consumer_group_password_with_options_async(
        self,
        request: dts_20200101_models.ModifyConsumerGroupPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyConsumerGroupPasswordResponse:
        """
        @summary Modifies the password of a consumer group
        
        @param request: ModifyConsumerGroupPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyConsumerGroupPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupID'] = request.consumer_group_id
        if not UtilClient.is_unset(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not UtilClient.is_unset(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not UtilClient.is_unset(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not UtilClient.is_unset(request.consumer_group_new_password):
            query['consumerGroupNewPassword'] = request.consumer_group_new_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyConsumerGroupPassword',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyConsumerGroupPasswordResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyConsumerGroupPasswordResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_consumer_group_password(
        self,
        request: dts_20200101_models.ModifyConsumerGroupPasswordRequest,
    ) -> dts_20200101_models.ModifyConsumerGroupPasswordResponse:
        """
        @summary Modifies the password of a consumer group
        
        @param request: ModifyConsumerGroupPasswordRequest
        @return: ModifyConsumerGroupPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_consumer_group_password_with_options(request, runtime)

    async def modify_consumer_group_password_async(
        self,
        request: dts_20200101_models.ModifyConsumerGroupPasswordRequest,
    ) -> dts_20200101_models.ModifyConsumerGroupPasswordResponse:
        """
        @summary Modifies the password of a consumer group
        
        @param request: ModifyConsumerGroupPasswordRequest
        @return: ModifyConsumerGroupPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_consumer_group_password_with_options_async(request, runtime)

    def modify_consumption_timestamp_with_options(
        self,
        request: dts_20200101_models.ModifyConsumptionTimestampRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyConsumptionTimestampResponse:
        """
        @summary Modifies the consumption checkpoint of a change tracking instance.
        
        @param request: ModifyConsumptionTimestampRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyConsumptionTimestampResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.consumption_timestamp):
            query['ConsumptionTimestamp'] = request.consumption_timestamp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyConsumptionTimestamp',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyConsumptionTimestampResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyConsumptionTimestampResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_consumption_timestamp_with_options_async(
        self,
        request: dts_20200101_models.ModifyConsumptionTimestampRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyConsumptionTimestampResponse:
        """
        @summary Modifies the consumption checkpoint of a change tracking instance.
        
        @param request: ModifyConsumptionTimestampRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyConsumptionTimestampResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.consumption_timestamp):
            query['ConsumptionTimestamp'] = request.consumption_timestamp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyConsumptionTimestamp',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyConsumptionTimestampResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyConsumptionTimestampResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_consumption_timestamp(
        self,
        request: dts_20200101_models.ModifyConsumptionTimestampRequest,
    ) -> dts_20200101_models.ModifyConsumptionTimestampResponse:
        """
        @summary Modifies the consumption checkpoint of a change tracking instance.
        
        @param request: ModifyConsumptionTimestampRequest
        @return: ModifyConsumptionTimestampResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_consumption_timestamp_with_options(request, runtime)

    async def modify_consumption_timestamp_async(
        self,
        request: dts_20200101_models.ModifyConsumptionTimestampRequest,
    ) -> dts_20200101_models.ModifyConsumptionTimestampResponse:
        """
        @summary Modifies the consumption checkpoint of a change tracking instance.
        
        @param request: ModifyConsumptionTimestampRequest
        @return: ModifyConsumptionTimestampResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_consumption_timestamp_with_options_async(request, runtime)

    def modify_dedicated_cluster_with_options(
        self,
        request: dts_20200101_models.ModifyDedicatedClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDedicatedClusterResponse:
        """
        @summary Modifies the configuration of a cluster.
        
        @description You can modify only the overcommit ratio.
        
        @param request: ModifyDedicatedClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDedicatedClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.dedicated_cluster_name):
            query['DedicatedClusterName'] = request.dedicated_cluster_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.oversold_ratio):
            query['OversoldRatio'] = request.oversold_ratio
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedCluster',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyDedicatedClusterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyDedicatedClusterResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_dedicated_cluster_with_options_async(
        self,
        request: dts_20200101_models.ModifyDedicatedClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDedicatedClusterResponse:
        """
        @summary Modifies the configuration of a cluster.
        
        @description You can modify only the overcommit ratio.
        
        @param request: ModifyDedicatedClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDedicatedClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.dedicated_cluster_name):
            query['DedicatedClusterName'] = request.dedicated_cluster_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.oversold_ratio):
            query['OversoldRatio'] = request.oversold_ratio
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedCluster',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyDedicatedClusterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyDedicatedClusterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_dedicated_cluster(
        self,
        request: dts_20200101_models.ModifyDedicatedClusterRequest,
    ) -> dts_20200101_models.ModifyDedicatedClusterResponse:
        """
        @summary Modifies the configuration of a cluster.
        
        @description You can modify only the overcommit ratio.
        
        @param request: ModifyDedicatedClusterRequest
        @return: ModifyDedicatedClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_cluster_with_options(request, runtime)

    async def modify_dedicated_cluster_async(
        self,
        request: dts_20200101_models.ModifyDedicatedClusterRequest,
    ) -> dts_20200101_models.ModifyDedicatedClusterResponse:
        """
        @summary Modifies the configuration of a cluster.
        
        @description You can modify only the overcommit ratio.
        
        @param request: ModifyDedicatedClusterRequest
        @return: ModifyDedicatedClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_cluster_with_options_async(request, runtime)

    def modify_dts_job_with_options(
        self,
        tmp_req: dts_20200101_models.ModifyDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobResponse:
        """
        @summary Modifies the configurations of a data synchronization task.
        
        @description When you configure a data synchronization task in the Data Transmission Service (DTS) console, you can move the pointer over *Next: Save Task Settings and Precheck** in the **Advanced Settings** step and click **Preview OpenAPI parameters** to view the parameters that are used to configure the task by calling an API operation.
        
        @param tmp_req: ModifyDtsJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDtsJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dts_20200101_models.ModifyDtsJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.db_list):
            request.db_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.db_list, 'DbList', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_initialization):
            query['DataInitialization'] = request.data_initialization
        if not UtilClient.is_unset(request.data_synchronization):
            query['DataSynchronization'] = request.data_synchronization
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.file_oss_url):
            query['FileOssUrl'] = request.file_oss_url
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.structure_initialization):
            query['StructureInitialization'] = request.structure_initialization
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        body = {}
        if not UtilClient.is_unset(request.db_list_shrink):
            body['DbList'] = request.db_list_shrink
        if not UtilClient.is_unset(request.etl_operator_column_reference):
            body['EtlOperatorColumnReference'] = request.etl_operator_column_reference
        if not UtilClient.is_unset(request.filter_table_name):
            body['FilterTableName'] = request.filter_table_name
        if not UtilClient.is_unset(request.modify_type_enum):
            body['ModifyTypeEnum'] = request.modify_type_enum
        if not UtilClient.is_unset(request.reserved):
            body['Reserved'] = request.reserved
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_dts_job_with_options_async(
        self,
        tmp_req: dts_20200101_models.ModifyDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobResponse:
        """
        @summary Modifies the configurations of a data synchronization task.
        
        @description When you configure a data synchronization task in the Data Transmission Service (DTS) console, you can move the pointer over *Next: Save Task Settings and Precheck** in the **Advanced Settings** step and click **Preview OpenAPI parameters** to view the parameters that are used to configure the task by calling an API operation.
        
        @param tmp_req: ModifyDtsJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDtsJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dts_20200101_models.ModifyDtsJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.db_list):
            request.db_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.db_list, 'DbList', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_initialization):
            query['DataInitialization'] = request.data_initialization
        if not UtilClient.is_unset(request.data_synchronization):
            query['DataSynchronization'] = request.data_synchronization
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.file_oss_url):
            query['FileOssUrl'] = request.file_oss_url
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.structure_initialization):
            query['StructureInitialization'] = request.structure_initialization
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        body = {}
        if not UtilClient.is_unset(request.db_list_shrink):
            body['DbList'] = request.db_list_shrink
        if not UtilClient.is_unset(request.etl_operator_column_reference):
            body['EtlOperatorColumnReference'] = request.etl_operator_column_reference
        if not UtilClient.is_unset(request.filter_table_name):
            body['FilterTableName'] = request.filter_table_name
        if not UtilClient.is_unset(request.modify_type_enum):
            body['ModifyTypeEnum'] = request.modify_type_enum
        if not UtilClient.is_unset(request.reserved):
            body['Reserved'] = request.reserved
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_dts_job(
        self,
        request: dts_20200101_models.ModifyDtsJobRequest,
    ) -> dts_20200101_models.ModifyDtsJobResponse:
        """
        @summary Modifies the configurations of a data synchronization task.
        
        @description When you configure a data synchronization task in the Data Transmission Service (DTS) console, you can move the pointer over *Next: Save Task Settings and Precheck** in the **Advanced Settings** step and click **Preview OpenAPI parameters** to view the parameters that are used to configure the task by calling an API operation.
        
        @param request: ModifyDtsJobRequest
        @return: ModifyDtsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dts_job_with_options(request, runtime)

    async def modify_dts_job_async(
        self,
        request: dts_20200101_models.ModifyDtsJobRequest,
    ) -> dts_20200101_models.ModifyDtsJobResponse:
        """
        @summary Modifies the configurations of a data synchronization task.
        
        @description When you configure a data synchronization task in the Data Transmission Service (DTS) console, you can move the pointer over *Next: Save Task Settings and Precheck** in the **Advanced Settings** step and click **Preview OpenAPI parameters** to view the parameters that are used to configure the task by calling an API operation.
        
        @param request: ModifyDtsJobRequest
        @return: ModifyDtsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dts_job_with_options_async(request, runtime)

    def modify_dts_job_advance(
        self,
        request: dts_20200101_models.ModifyDtsJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='Dts',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        modify_dts_job_req = dts_20200101_models.ModifyDtsJobRequest()
        OpenApiUtilClient.convert(request, modify_dts_job_req)
        if not UtilClient.is_unset(request.file_oss_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_oss_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            modify_dts_job_req.file_oss_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        modify_dts_job_resp = self.modify_dts_job_with_options(modify_dts_job_req, runtime)
        return modify_dts_job_resp

    async def modify_dts_job_advance_async(
        self,
        request: dts_20200101_models.ModifyDtsJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='Dts',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        modify_dts_job_req = dts_20200101_models.ModifyDtsJobRequest()
        OpenApiUtilClient.convert(request, modify_dts_job_req)
        if not UtilClient.is_unset(request.file_oss_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_oss_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            modify_dts_job_req.file_oss_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        modify_dts_job_resp = await self.modify_dts_job_with_options_async(modify_dts_job_req, runtime)
        return modify_dts_job_resp

    def modify_dts_job_config_with_options(
        self,
        request: dts_20200101_models.ModifyDtsJobConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobConfigResponse:
        """
        @summary Modifies the parameters of a Data Transmission Service (DTS) task.
        
        @param request: ModifyDtsJobConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDtsJobConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_dts_job_config_with_options_async(
        self,
        request: dts_20200101_models.ModifyDtsJobConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobConfigResponse:
        """
        @summary Modifies the parameters of a Data Transmission Service (DTS) task.
        
        @param request: ModifyDtsJobConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDtsJobConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_dts_job_config(
        self,
        request: dts_20200101_models.ModifyDtsJobConfigRequest,
    ) -> dts_20200101_models.ModifyDtsJobConfigResponse:
        """
        @summary Modifies the parameters of a Data Transmission Service (DTS) task.
        
        @param request: ModifyDtsJobConfigRequest
        @return: ModifyDtsJobConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dts_job_config_with_options(request, runtime)

    async def modify_dts_job_config_async(
        self,
        request: dts_20200101_models.ModifyDtsJobConfigRequest,
    ) -> dts_20200101_models.ModifyDtsJobConfigResponse:
        """
        @summary Modifies the parameters of a Data Transmission Service (DTS) task.
        
        @param request: ModifyDtsJobConfigRequest
        @return: ModifyDtsJobConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dts_job_config_with_options_async(request, runtime)

    def modify_dts_job_dedicated_cluster_with_options(
        self,
        request: dts_20200101_models.ModifyDtsJobDedicatedClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobDedicatedClusterResponse:
        """
        @summary Changes the dedicated cluster on which a Data Transmission Service (DTS) task runs.
        
        @description > After a DTS task is migrated from a dedicated cluster to a shared cluster, the task is billed on a pay-as-you-go basis.
        
        @param request: ModifyDtsJobDedicatedClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDtsJobDedicatedClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobDedicatedCluster',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobDedicatedClusterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobDedicatedClusterResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_dts_job_dedicated_cluster_with_options_async(
        self,
        request: dts_20200101_models.ModifyDtsJobDedicatedClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobDedicatedClusterResponse:
        """
        @summary Changes the dedicated cluster on which a Data Transmission Service (DTS) task runs.
        
        @description > After a DTS task is migrated from a dedicated cluster to a shared cluster, the task is billed on a pay-as-you-go basis.
        
        @param request: ModifyDtsJobDedicatedClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDtsJobDedicatedClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobDedicatedCluster',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobDedicatedClusterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobDedicatedClusterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_dts_job_dedicated_cluster(
        self,
        request: dts_20200101_models.ModifyDtsJobDedicatedClusterRequest,
    ) -> dts_20200101_models.ModifyDtsJobDedicatedClusterResponse:
        """
        @summary Changes the dedicated cluster on which a Data Transmission Service (DTS) task runs.
        
        @description > After a DTS task is migrated from a dedicated cluster to a shared cluster, the task is billed on a pay-as-you-go basis.
        
        @param request: ModifyDtsJobDedicatedClusterRequest
        @return: ModifyDtsJobDedicatedClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dts_job_dedicated_cluster_with_options(request, runtime)

    async def modify_dts_job_dedicated_cluster_async(
        self,
        request: dts_20200101_models.ModifyDtsJobDedicatedClusterRequest,
    ) -> dts_20200101_models.ModifyDtsJobDedicatedClusterResponse:
        """
        @summary Changes the dedicated cluster on which a Data Transmission Service (DTS) task runs.
        
        @description > After a DTS task is migrated from a dedicated cluster to a shared cluster, the task is billed on a pay-as-you-go basis.
        
        @param request: ModifyDtsJobDedicatedClusterRequest
        @return: ModifyDtsJobDedicatedClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dts_job_dedicated_cluster_with_options_async(request, runtime)

    def modify_dts_job_du_limit_with_options(
        self,
        request: dts_20200101_models.ModifyDtsJobDuLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobDuLimitResponse:
        """
        @summary Modifies the upper limit of DTS units (DUs) for a Data Transmission Service (DTS) task.
        
        @description    DTS allows you to upgrade or downgrade the configurations of DTS instances in a dedicated cluster. You can adjust the resources that are occupied for task execution to dynamically adjust the number of tasks that can be scheduled in the cluster. This way, you can reduce the total number of DUs required for the cluster or release DUs.
        Before you modify the upper limit of DUs for a DTS task, make sure that sufficient DUs are available.
        
        @param request: ModifyDtsJobDuLimitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDtsJobDuLimitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.du_limit):
            query['DuLimit'] = request.du_limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobDuLimit',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobDuLimitResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobDuLimitResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_dts_job_du_limit_with_options_async(
        self,
        request: dts_20200101_models.ModifyDtsJobDuLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobDuLimitResponse:
        """
        @summary Modifies the upper limit of DTS units (DUs) for a Data Transmission Service (DTS) task.
        
        @description    DTS allows you to upgrade or downgrade the configurations of DTS instances in a dedicated cluster. You can adjust the resources that are occupied for task execution to dynamically adjust the number of tasks that can be scheduled in the cluster. This way, you can reduce the total number of DUs required for the cluster or release DUs.
        Before you modify the upper limit of DUs for a DTS task, make sure that sufficient DUs are available.
        
        @param request: ModifyDtsJobDuLimitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDtsJobDuLimitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.du_limit):
            query['DuLimit'] = request.du_limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobDuLimit',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobDuLimitResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobDuLimitResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_dts_job_du_limit(
        self,
        request: dts_20200101_models.ModifyDtsJobDuLimitRequest,
    ) -> dts_20200101_models.ModifyDtsJobDuLimitResponse:
        """
        @summary Modifies the upper limit of DTS units (DUs) for a Data Transmission Service (DTS) task.
        
        @description    DTS allows you to upgrade or downgrade the configurations of DTS instances in a dedicated cluster. You can adjust the resources that are occupied for task execution to dynamically adjust the number of tasks that can be scheduled in the cluster. This way, you can reduce the total number of DUs required for the cluster or release DUs.
        Before you modify the upper limit of DUs for a DTS task, make sure that sufficient DUs are available.
        
        @param request: ModifyDtsJobDuLimitRequest
        @return: ModifyDtsJobDuLimitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dts_job_du_limit_with_options(request, runtime)

    async def modify_dts_job_du_limit_async(
        self,
        request: dts_20200101_models.ModifyDtsJobDuLimitRequest,
    ) -> dts_20200101_models.ModifyDtsJobDuLimitResponse:
        """
        @summary Modifies the upper limit of DTS units (DUs) for a Data Transmission Service (DTS) task.
        
        @description    DTS allows you to upgrade or downgrade the configurations of DTS instances in a dedicated cluster. You can adjust the resources that are occupied for task execution to dynamically adjust the number of tasks that can be scheduled in the cluster. This way, you can reduce the total number of DUs required for the cluster or release DUs.
        Before you modify the upper limit of DUs for a DTS task, make sure that sufficient DUs are available.
        
        @param request: ModifyDtsJobDuLimitRequest
        @return: ModifyDtsJobDuLimitResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dts_job_du_limit_with_options_async(request, runtime)

    def modify_dts_job_endpoint_with_options(
        self,
        request: dts_20200101_models.ModifyDtsJobEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobEndpointResponse:
        """
        @summary Changes the source or destination database instance of a data synchronization or migration task in Data Transmission Service (DTS).
        
        @description >  After the database is changed, Data Transmission Service (DTS) rolls back the incremental write offset for 10 seconds. If the synchronized or migrated data does not have a primary key, make sure that no data is written to the source database while the source or destination database is being replaced. Otherwise, duplicate data may exist.
        
        @param request: ModifyDtsJobEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDtsJobEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.endpoint_instance_id):
            query['EndpointInstanceId'] = request.endpoint_instance_id
        if not UtilClient.is_unset(request.endpoint_instance_type):
            query['EndpointInstanceType'] = request.endpoint_instance_type
        if not UtilClient.is_unset(request.endpoint_ip):
            query['EndpointIp'] = request.endpoint_ip
        if not UtilClient.is_unset(request.endpoint_port):
            query['EndpointPort'] = request.endpoint_port
        if not UtilClient.is_unset(request.endpoint_region_id):
            query['EndpointRegionId'] = request.endpoint_region_id
        if not UtilClient.is_unset(request.modify_account):
            query['ModifyAccount'] = request.modify_account
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.shard_password):
            query['ShardPassword'] = request.shard_password
        if not UtilClient.is_unset(request.shard_username):
            query['ShardUsername'] = request.shard_username
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobEndpoint',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobEndpointResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobEndpointResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_dts_job_endpoint_with_options_async(
        self,
        request: dts_20200101_models.ModifyDtsJobEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobEndpointResponse:
        """
        @summary Changes the source or destination database instance of a data synchronization or migration task in Data Transmission Service (DTS).
        
        @description >  After the database is changed, Data Transmission Service (DTS) rolls back the incremental write offset for 10 seconds. If the synchronized or migrated data does not have a primary key, make sure that no data is written to the source database while the source or destination database is being replaced. Otherwise, duplicate data may exist.
        
        @param request: ModifyDtsJobEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDtsJobEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.endpoint_instance_id):
            query['EndpointInstanceId'] = request.endpoint_instance_id
        if not UtilClient.is_unset(request.endpoint_instance_type):
            query['EndpointInstanceType'] = request.endpoint_instance_type
        if not UtilClient.is_unset(request.endpoint_ip):
            query['EndpointIp'] = request.endpoint_ip
        if not UtilClient.is_unset(request.endpoint_port):
            query['EndpointPort'] = request.endpoint_port
        if not UtilClient.is_unset(request.endpoint_region_id):
            query['EndpointRegionId'] = request.endpoint_region_id
        if not UtilClient.is_unset(request.modify_account):
            query['ModifyAccount'] = request.modify_account
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.shard_password):
            query['ShardPassword'] = request.shard_password
        if not UtilClient.is_unset(request.shard_username):
            query['ShardUsername'] = request.shard_username
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobEndpoint',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobEndpointResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobEndpointResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_dts_job_endpoint(
        self,
        request: dts_20200101_models.ModifyDtsJobEndpointRequest,
    ) -> dts_20200101_models.ModifyDtsJobEndpointResponse:
        """
        @summary Changes the source or destination database instance of a data synchronization or migration task in Data Transmission Service (DTS).
        
        @description >  After the database is changed, Data Transmission Service (DTS) rolls back the incremental write offset for 10 seconds. If the synchronized or migrated data does not have a primary key, make sure that no data is written to the source database while the source or destination database is being replaced. Otherwise, duplicate data may exist.
        
        @param request: ModifyDtsJobEndpointRequest
        @return: ModifyDtsJobEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dts_job_endpoint_with_options(request, runtime)

    async def modify_dts_job_endpoint_async(
        self,
        request: dts_20200101_models.ModifyDtsJobEndpointRequest,
    ) -> dts_20200101_models.ModifyDtsJobEndpointResponse:
        """
        @summary Changes the source or destination database instance of a data synchronization or migration task in Data Transmission Service (DTS).
        
        @description >  After the database is changed, Data Transmission Service (DTS) rolls back the incremental write offset for 10 seconds. If the synchronized or migrated data does not have a primary key, make sure that no data is written to the source database while the source or destination database is being replaced. Otherwise, duplicate data may exist.
        
        @param request: ModifyDtsJobEndpointRequest
        @return: ModifyDtsJobEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dts_job_endpoint_with_options_async(request, runtime)

    def modify_dts_job_name_with_options(
        self,
        request: dts_20200101_models.ModifyDtsJobNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobNameResponse:
        """
        @summary Changes the name of a Data Transmission Service (DTS) task.
        
        @param request: ModifyDtsJobNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDtsJobNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobName',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobNameResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobNameResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_dts_job_name_with_options_async(
        self,
        request: dts_20200101_models.ModifyDtsJobNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobNameResponse:
        """
        @summary Changes the name of a Data Transmission Service (DTS) task.
        
        @param request: ModifyDtsJobNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDtsJobNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobName',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobNameResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobNameResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_dts_job_name(
        self,
        request: dts_20200101_models.ModifyDtsJobNameRequest,
    ) -> dts_20200101_models.ModifyDtsJobNameResponse:
        """
        @summary Changes the name of a Data Transmission Service (DTS) task.
        
        @param request: ModifyDtsJobNameRequest
        @return: ModifyDtsJobNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dts_job_name_with_options(request, runtime)

    async def modify_dts_job_name_async(
        self,
        request: dts_20200101_models.ModifyDtsJobNameRequest,
    ) -> dts_20200101_models.ModifyDtsJobNameResponse:
        """
        @summary Changes the name of a Data Transmission Service (DTS) task.
        
        @param request: ModifyDtsJobNameRequest
        @return: ModifyDtsJobNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dts_job_name_with_options_async(request, runtime)

    def modify_dts_job_password_with_options(
        self,
        request: dts_20200101_models.ModifyDtsJobPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobPasswordResponse:
        """
        @summary Changes the password of the account used to log on to the source or destination database in a Data Transmission Service (DTS) task.
        
        @param request: ModifyDtsJobPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDtsJobPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobPassword',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobPasswordResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobPasswordResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_dts_job_password_with_options_async(
        self,
        request: dts_20200101_models.ModifyDtsJobPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobPasswordResponse:
        """
        @summary Changes the password of the account used to log on to the source or destination database in a Data Transmission Service (DTS) task.
        
        @param request: ModifyDtsJobPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDtsJobPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobPassword',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobPasswordResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyDtsJobPasswordResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_dts_job_password(
        self,
        request: dts_20200101_models.ModifyDtsJobPasswordRequest,
    ) -> dts_20200101_models.ModifyDtsJobPasswordResponse:
        """
        @summary Changes the password of the account used to log on to the source or destination database in a Data Transmission Service (DTS) task.
        
        @param request: ModifyDtsJobPasswordRequest
        @return: ModifyDtsJobPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dts_job_password_with_options(request, runtime)

    async def modify_dts_job_password_async(
        self,
        request: dts_20200101_models.ModifyDtsJobPasswordRequest,
    ) -> dts_20200101_models.ModifyDtsJobPasswordResponse:
        """
        @summary Changes the password of the account used to log on to the source or destination database in a Data Transmission Service (DTS) task.
        
        @param request: ModifyDtsJobPasswordRequest
        @return: ModifyDtsJobPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dts_job_password_with_options_async(request, runtime)

    def modify_dynamic_config_with_options(
        self,
        request: dts_20200101_models.ModifyDynamicConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDynamicConfigResponse:
        """
        @summary Enables throttling for data synchronization and data migration.
        
        @param request: ModifyDynamicConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDynamicConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_list):
            query['ConfigList'] = request.config_list
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.enable_limit):
            query['EnableLimit'] = request.enable_limit
        if not UtilClient.is_unset(request.job_code):
            query['JobCode'] = request.job_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDynamicConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyDynamicConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyDynamicConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_dynamic_config_with_options_async(
        self,
        request: dts_20200101_models.ModifyDynamicConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDynamicConfigResponse:
        """
        @summary Enables throttling for data synchronization and data migration.
        
        @param request: ModifyDynamicConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDynamicConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_list):
            query['ConfigList'] = request.config_list
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.enable_limit):
            query['EnableLimit'] = request.enable_limit
        if not UtilClient.is_unset(request.job_code):
            query['JobCode'] = request.job_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDynamicConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyDynamicConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyDynamicConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_dynamic_config(
        self,
        request: dts_20200101_models.ModifyDynamicConfigRequest,
    ) -> dts_20200101_models.ModifyDynamicConfigResponse:
        """
        @summary Enables throttling for data synchronization and data migration.
        
        @param request: ModifyDynamicConfigRequest
        @return: ModifyDynamicConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dynamic_config_with_options(request, runtime)

    async def modify_dynamic_config_async(
        self,
        request: dts_20200101_models.ModifyDynamicConfigRequest,
    ) -> dts_20200101_models.ModifyDynamicConfigResponse:
        """
        @summary Enables throttling for data synchronization and data migration.
        
        @param request: ModifyDynamicConfigRequest
        @return: ModifyDynamicConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dynamic_config_with_options_async(request, runtime)

    def modify_gad_instance_name_with_options(
        self,
        request: dts_20200101_models.ModifyGadInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyGadInstanceNameResponse:
        """
        @summary 修改GAD实例名称
        
        @param request: ModifyGadInstanceNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGadInstanceNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGadInstanceName',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyGadInstanceNameResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyGadInstanceNameResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_gad_instance_name_with_options_async(
        self,
        request: dts_20200101_models.ModifyGadInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyGadInstanceNameResponse:
        """
        @summary 修改GAD实例名称
        
        @param request: ModifyGadInstanceNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGadInstanceNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGadInstanceName',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifyGadInstanceNameResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifyGadInstanceNameResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_gad_instance_name(
        self,
        request: dts_20200101_models.ModifyGadInstanceNameRequest,
    ) -> dts_20200101_models.ModifyGadInstanceNameResponse:
        """
        @summary 修改GAD实例名称
        
        @param request: ModifyGadInstanceNameRequest
        @return: ModifyGadInstanceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_gad_instance_name_with_options(request, runtime)

    async def modify_gad_instance_name_async(
        self,
        request: dts_20200101_models.ModifyGadInstanceNameRequest,
    ) -> dts_20200101_models.ModifyGadInstanceNameResponse:
        """
        @summary 修改GAD实例名称
        
        @param request: ModifyGadInstanceNameRequest
        @return: ModifyGadInstanceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_gad_instance_name_with_options_async(request, runtime)

    def modify_subscription_with_options(
        self,
        request: dts_20200101_models.ModifySubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifySubscriptionResponse:
        """
        @summary Modifies the information about a change tracking task.
        
        @description >  You can preview related API operation parameters when you modify the information about a change tracking task in the Data Transmission Service (DTS) console. This helps you configure the request parameters of this API operation. For more information, see [Preview the request parameters of API operations](https://help.aliyun.com/document_detail/2851612.html).
        
        @param request: ModifySubscriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySubscriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_list):
            query['DbList'] = request.db_list
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_data_type_ddl):
            query['SubscriptionDataTypeDDL'] = request.subscription_data_type_ddl
        if not UtilClient.is_unset(request.subscription_data_type_dml):
            query['SubscriptionDataTypeDML'] = request.subscription_data_type_dml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySubscription',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifySubscriptionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifySubscriptionResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_subscription_with_options_async(
        self,
        request: dts_20200101_models.ModifySubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifySubscriptionResponse:
        """
        @summary Modifies the information about a change tracking task.
        
        @description >  You can preview related API operation parameters when you modify the information about a change tracking task in the Data Transmission Service (DTS) console. This helps you configure the request parameters of this API operation. For more information, see [Preview the request parameters of API operations](https://help.aliyun.com/document_detail/2851612.html).
        
        @param request: ModifySubscriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySubscriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_list):
            query['DbList'] = request.db_list
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_data_type_ddl):
            query['SubscriptionDataTypeDDL'] = request.subscription_data_type_ddl
        if not UtilClient.is_unset(request.subscription_data_type_dml):
            query['SubscriptionDataTypeDML'] = request.subscription_data_type_dml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySubscription',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifySubscriptionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifySubscriptionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_subscription(
        self,
        request: dts_20200101_models.ModifySubscriptionRequest,
    ) -> dts_20200101_models.ModifySubscriptionResponse:
        """
        @summary Modifies the information about a change tracking task.
        
        @description >  You can preview related API operation parameters when you modify the information about a change tracking task in the Data Transmission Service (DTS) console. This helps you configure the request parameters of this API operation. For more information, see [Preview the request parameters of API operations](https://help.aliyun.com/document_detail/2851612.html).
        
        @param request: ModifySubscriptionRequest
        @return: ModifySubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_subscription_with_options(request, runtime)

    async def modify_subscription_async(
        self,
        request: dts_20200101_models.ModifySubscriptionRequest,
    ) -> dts_20200101_models.ModifySubscriptionResponse:
        """
        @summary Modifies the information about a change tracking task.
        
        @description >  You can preview related API operation parameters when you modify the information about a change tracking task in the Data Transmission Service (DTS) console. This helps you configure the request parameters of this API operation. For more information, see [Preview the request parameters of API operations](https://help.aliyun.com/document_detail/2851612.html).
        
        @param request: ModifySubscriptionRequest
        @return: ModifySubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_subscription_with_options_async(request, runtime)

    def modify_subscription_object_with_options(
        self,
        request: dts_20200101_models.ModifySubscriptionObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifySubscriptionObjectResponse:
        """
        @summary Modifies the objects for change tracking.
        
        @param request: ModifySubscriptionObjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySubscriptionObjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not UtilClient.is_unset(request.subscription_object):
            query['SubscriptionObject'] = request.subscription_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySubscriptionObject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifySubscriptionObjectResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifySubscriptionObjectResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_subscription_object_with_options_async(
        self,
        request: dts_20200101_models.ModifySubscriptionObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifySubscriptionObjectResponse:
        """
        @summary Modifies the objects for change tracking.
        
        @param request: ModifySubscriptionObjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySubscriptionObjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not UtilClient.is_unset(request.subscription_object):
            query['SubscriptionObject'] = request.subscription_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySubscriptionObject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifySubscriptionObjectResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifySubscriptionObjectResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_subscription_object(
        self,
        request: dts_20200101_models.ModifySubscriptionObjectRequest,
    ) -> dts_20200101_models.ModifySubscriptionObjectResponse:
        """
        @summary Modifies the objects for change tracking.
        
        @param request: ModifySubscriptionObjectRequest
        @return: ModifySubscriptionObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_subscription_object_with_options(request, runtime)

    async def modify_subscription_object_async(
        self,
        request: dts_20200101_models.ModifySubscriptionObjectRequest,
    ) -> dts_20200101_models.ModifySubscriptionObjectResponse:
        """
        @summary Modifies the objects for change tracking.
        
        @param request: ModifySubscriptionObjectRequest
        @return: ModifySubscriptionObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_subscription_object_with_options_async(request, runtime)

    def modify_synchronization_object_with_options(
        self,
        request: dts_20200101_models.ModifySynchronizationObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifySynchronizationObjectResponse:
        """
        @summary Modifies the objects to be synchronized.
        
        @param request: ModifySynchronizationObjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySynchronizationObjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        body = {}
        if not UtilClient.is_unset(request.synchronization_objects):
            body['SynchronizationObjects'] = request.synchronization_objects
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifySynchronizationObject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifySynchronizationObjectResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifySynchronizationObjectResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_synchronization_object_with_options_async(
        self,
        request: dts_20200101_models.ModifySynchronizationObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifySynchronizationObjectResponse:
        """
        @summary Modifies the objects to be synchronized.
        
        @param request: ModifySynchronizationObjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySynchronizationObjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        body = {}
        if not UtilClient.is_unset(request.synchronization_objects):
            body['SynchronizationObjects'] = request.synchronization_objects
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifySynchronizationObject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ModifySynchronizationObjectResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ModifySynchronizationObjectResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_synchronization_object(
        self,
        request: dts_20200101_models.ModifySynchronizationObjectRequest,
    ) -> dts_20200101_models.ModifySynchronizationObjectResponse:
        """
        @summary Modifies the objects to be synchronized.
        
        @param request: ModifySynchronizationObjectRequest
        @return: ModifySynchronizationObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_synchronization_object_with_options(request, runtime)

    async def modify_synchronization_object_async(
        self,
        request: dts_20200101_models.ModifySynchronizationObjectRequest,
    ) -> dts_20200101_models.ModifySynchronizationObjectResponse:
        """
        @summary Modifies the objects to be synchronized.
        
        @param request: ModifySynchronizationObjectRequest
        @return: ModifySynchronizationObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_synchronization_object_with_options_async(request, runtime)

    def pre_check_create_gad_order_with_options(
        self,
        request: dts_20200101_models.PreCheckCreateGadOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.PreCheckCreateGadOrderResponse:
        """
        @summary 预检查创建GAD订单
        
        @param request: PreCheckCreateGadOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreCheckCreateGadOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.slave_db_instance_id):
            query['SlaveDbInstanceId'] = request.slave_db_instance_id
        if not UtilClient.is_unset(request.slave_db_instance_region):
            query['SlaveDbInstanceRegion'] = request.slave_db_instance_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PreCheckCreateGadOrder',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.PreCheckCreateGadOrderResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.PreCheckCreateGadOrderResponse(),
                self.execute(params, req, runtime)
            )

    async def pre_check_create_gad_order_with_options_async(
        self,
        request: dts_20200101_models.PreCheckCreateGadOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.PreCheckCreateGadOrderResponse:
        """
        @summary 预检查创建GAD订单
        
        @param request: PreCheckCreateGadOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreCheckCreateGadOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.slave_db_instance_id):
            query['SlaveDbInstanceId'] = request.slave_db_instance_id
        if not UtilClient.is_unset(request.slave_db_instance_region):
            query['SlaveDbInstanceRegion'] = request.slave_db_instance_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PreCheckCreateGadOrder',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.PreCheckCreateGadOrderResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.PreCheckCreateGadOrderResponse(),
                await self.execute_async(params, req, runtime)
            )

    def pre_check_create_gad_order(
        self,
        request: dts_20200101_models.PreCheckCreateGadOrderRequest,
    ) -> dts_20200101_models.PreCheckCreateGadOrderResponse:
        """
        @summary 预检查创建GAD订单
        
        @param request: PreCheckCreateGadOrderRequest
        @return: PreCheckCreateGadOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.pre_check_create_gad_order_with_options(request, runtime)

    async def pre_check_create_gad_order_async(
        self,
        request: dts_20200101_models.PreCheckCreateGadOrderRequest,
    ) -> dts_20200101_models.PreCheckCreateGadOrderResponse:
        """
        @summary 预检查创建GAD订单
        
        @param request: PreCheckCreateGadOrderRequest
        @return: PreCheckCreateGadOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.pre_check_create_gad_order_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: dts_20200101_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.RenewInstanceResponse:
        """
        @summary Renews a Data Transmission Service (DTS) instance. This API operation is available only for subscription instances.
        
        @param request: RenewInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.buy_count):
            query['BuyCount'] = request.buy_count
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.RenewInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.RenewInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def renew_instance_with_options_async(
        self,
        request: dts_20200101_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.RenewInstanceResponse:
        """
        @summary Renews a Data Transmission Service (DTS) instance. This API operation is available only for subscription instances.
        
        @param request: RenewInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.buy_count):
            query['BuyCount'] = request.buy_count
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.RenewInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.RenewInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def renew_instance(
        self,
        request: dts_20200101_models.RenewInstanceRequest,
    ) -> dts_20200101_models.RenewInstanceResponse:
        """
        @summary Renews a Data Transmission Service (DTS) instance. This API operation is available only for subscription instances.
        
        @param request: RenewInstanceRequest
        @return: RenewInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: dts_20200101_models.RenewInstanceRequest,
    ) -> dts_20200101_models.RenewInstanceResponse:
        """
        @summary Renews a Data Transmission Service (DTS) instance. This API operation is available only for subscription instances.
        
        @param request: RenewInstanceRequest
        @return: RenewInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def reset_dts_job_with_options(
        self,
        request: dts_20200101_models.ResetDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ResetDtsJobResponse:
        """
        @summary Resets a data synchronization or change tracking task.
        
        @description >  If you clear the configurations of a data synchronization or change tracking task, DTS deletes the task. Then, DTS creates another task. The task is in the Not Configured state. You must call the [ConfigureDtsJob](https://help.aliyun.com/document_detail/208399.html) operation reconfigure the task.
        
        @param request: ResetDtsJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetDtsJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ResetDtsJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ResetDtsJobResponse(),
                self.execute(params, req, runtime)
            )

    async def reset_dts_job_with_options_async(
        self,
        request: dts_20200101_models.ResetDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ResetDtsJobResponse:
        """
        @summary Resets a data synchronization or change tracking task.
        
        @description >  If you clear the configurations of a data synchronization or change tracking task, DTS deletes the task. Then, DTS creates another task. The task is in the Not Configured state. You must call the [ConfigureDtsJob](https://help.aliyun.com/document_detail/208399.html) operation reconfigure the task.
        
        @param request: ResetDtsJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetDtsJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ResetDtsJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ResetDtsJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def reset_dts_job(
        self,
        request: dts_20200101_models.ResetDtsJobRequest,
    ) -> dts_20200101_models.ResetDtsJobResponse:
        """
        @summary Resets a data synchronization or change tracking task.
        
        @description >  If you clear the configurations of a data synchronization or change tracking task, DTS deletes the task. Then, DTS creates another task. The task is in the Not Configured state. You must call the [ConfigureDtsJob](https://help.aliyun.com/document_detail/208399.html) operation reconfigure the task.
        
        @param request: ResetDtsJobRequest
        @return: ResetDtsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_dts_job_with_options(request, runtime)

    async def reset_dts_job_async(
        self,
        request: dts_20200101_models.ResetDtsJobRequest,
    ) -> dts_20200101_models.ResetDtsJobResponse:
        """
        @summary Resets a data synchronization or change tracking task.
        
        @description >  If you clear the configurations of a data synchronization or change tracking task, DTS deletes the task. Then, DTS creates another task. The task is in the Not Configured state. You must call the [ConfigureDtsJob](https://help.aliyun.com/document_detail/208399.html) operation reconfigure the task.
        
        @param request: ResetDtsJobRequest
        @return: ResetDtsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_dts_job_with_options_async(request, runtime)

    def reset_synchronization_job_with_options(
        self,
        request: dts_20200101_models.ResetSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ResetSynchronizationJobResponse:
        """
        @summary Clears the configurations of a data synchronization task.
        
        @description >  If you clear the configurations of a data synchronization task, the task will be released. To start the task again, you must call the *ConfigureSynchronizationJob** operation to reconfigure the task.
        
        @param request: ResetSynchronizationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ResetSynchronizationJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ResetSynchronizationJobResponse(),
                self.execute(params, req, runtime)
            )

    async def reset_synchronization_job_with_options_async(
        self,
        request: dts_20200101_models.ResetSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ResetSynchronizationJobResponse:
        """
        @summary Clears the configurations of a data synchronization task.
        
        @description >  If you clear the configurations of a data synchronization task, the task will be released. To start the task again, you must call the *ConfigureSynchronizationJob** operation to reconfigure the task.
        
        @param request: ResetSynchronizationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ResetSynchronizationJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ResetSynchronizationJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def reset_synchronization_job(
        self,
        request: dts_20200101_models.ResetSynchronizationJobRequest,
    ) -> dts_20200101_models.ResetSynchronizationJobResponse:
        """
        @summary Clears the configurations of a data synchronization task.
        
        @description >  If you clear the configurations of a data synchronization task, the task will be released. To start the task again, you must call the *ConfigureSynchronizationJob** operation to reconfigure the task.
        
        @param request: ResetSynchronizationJobRequest
        @return: ResetSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_synchronization_job_with_options(request, runtime)

    async def reset_synchronization_job_async(
        self,
        request: dts_20200101_models.ResetSynchronizationJobRequest,
    ) -> dts_20200101_models.ResetSynchronizationJobResponse:
        """
        @summary Clears the configurations of a data synchronization task.
        
        @description >  If you clear the configurations of a data synchronization task, the task will be released. To start the task again, you must call the *ConfigureSynchronizationJob** operation to reconfigure the task.
        
        @param request: ResetSynchronizationJobRequest
        @return: ResetSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_synchronization_job_with_options_async(request, runtime)

    def reverse_two_way_direction_with_options(
        self,
        request: dts_20200101_models.ReverseTwoWayDirectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ReverseTwoWayDirectionResponse:
        """
        @summary 调转双向任务的方向
        
        @param request: ReverseTwoWayDirectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReverseTwoWayDirectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.ignore_error_sub_job):
            query['IgnoreErrorSubJob'] = request.ignore_error_sub_job
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReverseTwoWayDirection',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ReverseTwoWayDirectionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ReverseTwoWayDirectionResponse(),
                self.execute(params, req, runtime)
            )

    async def reverse_two_way_direction_with_options_async(
        self,
        request: dts_20200101_models.ReverseTwoWayDirectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ReverseTwoWayDirectionResponse:
        """
        @summary 调转双向任务的方向
        
        @param request: ReverseTwoWayDirectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReverseTwoWayDirectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.ignore_error_sub_job):
            query['IgnoreErrorSubJob'] = request.ignore_error_sub_job
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReverseTwoWayDirection',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ReverseTwoWayDirectionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ReverseTwoWayDirectionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def reverse_two_way_direction(
        self,
        request: dts_20200101_models.ReverseTwoWayDirectionRequest,
    ) -> dts_20200101_models.ReverseTwoWayDirectionResponse:
        """
        @summary 调转双向任务的方向
        
        @param request: ReverseTwoWayDirectionRequest
        @return: ReverseTwoWayDirectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reverse_two_way_direction_with_options(request, runtime)

    async def reverse_two_way_direction_async(
        self,
        request: dts_20200101_models.ReverseTwoWayDirectionRequest,
    ) -> dts_20200101_models.ReverseTwoWayDirectionResponse:
        """
        @summary 调转双向任务的方向
        
        @param request: ReverseTwoWayDirectionRequest
        @return: ReverseTwoWayDirectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reverse_two_way_direction_with_options_async(request, runtime)

    def shield_precheck_with_options(
        self,
        request: dts_20200101_models.ShieldPrecheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ShieldPrecheckResponse:
        """
        @summary Ignores the precheck items that a data migration or synchronization task may fail to pass.
        
        @param request: ShieldPrecheckRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ShieldPrecheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.precheck_items):
            query['PrecheckItems'] = request.precheck_items
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ShieldPrecheck',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ShieldPrecheckResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ShieldPrecheckResponse(),
                self.execute(params, req, runtime)
            )

    async def shield_precheck_with_options_async(
        self,
        request: dts_20200101_models.ShieldPrecheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ShieldPrecheckResponse:
        """
        @summary Ignores the precheck items that a data migration or synchronization task may fail to pass.
        
        @param request: ShieldPrecheckRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ShieldPrecheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.precheck_items):
            query['PrecheckItems'] = request.precheck_items
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ShieldPrecheck',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.ShieldPrecheckResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.ShieldPrecheckResponse(),
                await self.execute_async(params, req, runtime)
            )

    def shield_precheck(
        self,
        request: dts_20200101_models.ShieldPrecheckRequest,
    ) -> dts_20200101_models.ShieldPrecheckResponse:
        """
        @summary Ignores the precheck items that a data migration or synchronization task may fail to pass.
        
        @param request: ShieldPrecheckRequest
        @return: ShieldPrecheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.shield_precheck_with_options(request, runtime)

    async def shield_precheck_async(
        self,
        request: dts_20200101_models.ShieldPrecheckRequest,
    ) -> dts_20200101_models.ShieldPrecheckResponse:
        """
        @summary Ignores the precheck items that a data migration or synchronization task may fail to pass.
        
        @param request: ShieldPrecheckRequest
        @return: ShieldPrecheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.shield_precheck_with_options_async(request, runtime)

    def skip_full_job_table_with_options(
        self,
        request: dts_20200101_models.SkipFullJobTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SkipFullJobTableResponse:
        """
        @summary The tables that do not need to be synchronized in a full data synchronization are skipped.
        
        @param request: SkipFullJobTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SkipFullJobTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.job_progress_id):
            query['JobProgressId'] = request.job_progress_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SkipFullJobTable',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.SkipFullJobTableResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.SkipFullJobTableResponse(),
                self.execute(params, req, runtime)
            )

    async def skip_full_job_table_with_options_async(
        self,
        request: dts_20200101_models.SkipFullJobTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SkipFullJobTableResponse:
        """
        @summary The tables that do not need to be synchronized in a full data synchronization are skipped.
        
        @param request: SkipFullJobTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SkipFullJobTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.job_progress_id):
            query['JobProgressId'] = request.job_progress_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SkipFullJobTable',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.SkipFullJobTableResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.SkipFullJobTableResponse(),
                await self.execute_async(params, req, runtime)
            )

    def skip_full_job_table(
        self,
        request: dts_20200101_models.SkipFullJobTableRequest,
    ) -> dts_20200101_models.SkipFullJobTableResponse:
        """
        @summary The tables that do not need to be synchronized in a full data synchronization are skipped.
        
        @param request: SkipFullJobTableRequest
        @return: SkipFullJobTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.skip_full_job_table_with_options(request, runtime)

    async def skip_full_job_table_async(
        self,
        request: dts_20200101_models.SkipFullJobTableRequest,
    ) -> dts_20200101_models.SkipFullJobTableResponse:
        """
        @summary The tables that do not need to be synchronized in a full data synchronization are skipped.
        
        @param request: SkipFullJobTableRequest
        @return: SkipFullJobTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.skip_full_job_table_with_options_async(request, runtime)

    def skip_pre_check_with_options(
        self,
        request: dts_20200101_models.SkipPreCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SkipPreCheckResponse:
        """
        @summary Skips one or more precheck items.
        
        @param request: SkipPreCheckRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SkipPreCheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.skip):
            query['Skip'] = request.skip
        if not UtilClient.is_unset(request.skip_pre_check_items):
            query['SkipPreCheckItems'] = request.skip_pre_check_items
        if not UtilClient.is_unset(request.skip_pre_check_names):
            query['SkipPreCheckNames'] = request.skip_pre_check_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SkipPreCheck',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.SkipPreCheckResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.SkipPreCheckResponse(),
                self.execute(params, req, runtime)
            )

    async def skip_pre_check_with_options_async(
        self,
        request: dts_20200101_models.SkipPreCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SkipPreCheckResponse:
        """
        @summary Skips one or more precheck items.
        
        @param request: SkipPreCheckRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SkipPreCheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.skip):
            query['Skip'] = request.skip
        if not UtilClient.is_unset(request.skip_pre_check_items):
            query['SkipPreCheckItems'] = request.skip_pre_check_items
        if not UtilClient.is_unset(request.skip_pre_check_names):
            query['SkipPreCheckNames'] = request.skip_pre_check_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SkipPreCheck',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.SkipPreCheckResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.SkipPreCheckResponse(),
                await self.execute_async(params, req, runtime)
            )

    def skip_pre_check(
        self,
        request: dts_20200101_models.SkipPreCheckRequest,
    ) -> dts_20200101_models.SkipPreCheckResponse:
        """
        @summary Skips one or more precheck items.
        
        @param request: SkipPreCheckRequest
        @return: SkipPreCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.skip_pre_check_with_options(request, runtime)

    async def skip_pre_check_async(
        self,
        request: dts_20200101_models.SkipPreCheckRequest,
    ) -> dts_20200101_models.SkipPreCheckResponse:
        """
        @summary Skips one or more precheck items.
        
        @param request: SkipPreCheckRequest
        @return: SkipPreCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.skip_pre_check_with_options_async(request, runtime)

    def start_dts_job_with_options(
        self,
        request: dts_20200101_models.StartDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartDtsJobResponse:
        """
        @summary Starts a data migration, data synchronization, or change tracking task.
        
        @param request: StartDtsJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDtsJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.StartDtsJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.StartDtsJobResponse(),
                self.execute(params, req, runtime)
            )

    async def start_dts_job_with_options_async(
        self,
        request: dts_20200101_models.StartDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartDtsJobResponse:
        """
        @summary Starts a data migration, data synchronization, or change tracking task.
        
        @param request: StartDtsJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDtsJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.StartDtsJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.StartDtsJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def start_dts_job(
        self,
        request: dts_20200101_models.StartDtsJobRequest,
    ) -> dts_20200101_models.StartDtsJobResponse:
        """
        @summary Starts a data migration, data synchronization, or change tracking task.
        
        @param request: StartDtsJobRequest
        @return: StartDtsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_dts_job_with_options(request, runtime)

    async def start_dts_job_async(
        self,
        request: dts_20200101_models.StartDtsJobRequest,
    ) -> dts_20200101_models.StartDtsJobResponse:
        """
        @summary Starts a data migration, data synchronization, or change tracking task.
        
        @param request: StartDtsJobRequest
        @return: StartDtsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_dts_job_with_options_async(request, runtime)

    def start_dts_jobs_with_options(
        self,
        request: dts_20200101_models.StartDtsJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartDtsJobsResponse:
        """
        @summary Starts multiple data migration or data synchronization tasks.
        
        @param request: StartDtsJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDtsJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.StartDtsJobsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.StartDtsJobsResponse(),
                self.execute(params, req, runtime)
            )

    async def start_dts_jobs_with_options_async(
        self,
        request: dts_20200101_models.StartDtsJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartDtsJobsResponse:
        """
        @summary Starts multiple data migration or data synchronization tasks.
        
        @param request: StartDtsJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDtsJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.StartDtsJobsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.StartDtsJobsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def start_dts_jobs(
        self,
        request: dts_20200101_models.StartDtsJobsRequest,
    ) -> dts_20200101_models.StartDtsJobsResponse:
        """
        @summary Starts multiple data migration or data synchronization tasks.
        
        @param request: StartDtsJobsRequest
        @return: StartDtsJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_dts_jobs_with_options(request, runtime)

    async def start_dts_jobs_async(
        self,
        request: dts_20200101_models.StartDtsJobsRequest,
    ) -> dts_20200101_models.StartDtsJobsResponse:
        """
        @summary Starts multiple data migration or data synchronization tasks.
        
        @param request: StartDtsJobsRequest
        @return: StartDtsJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_dts_jobs_with_options_async(request, runtime)

    def start_migration_job_with_options(
        self,
        request: dts_20200101_models.StartMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartMigrationJobResponse:
        """
        @summary Starts a data migration task.
        
        @param request: StartMigrationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartMigrationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.StartMigrationJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.StartMigrationJobResponse(),
                self.execute(params, req, runtime)
            )

    async def start_migration_job_with_options_async(
        self,
        request: dts_20200101_models.StartMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartMigrationJobResponse:
        """
        @summary Starts a data migration task.
        
        @param request: StartMigrationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartMigrationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.StartMigrationJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.StartMigrationJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def start_migration_job(
        self,
        request: dts_20200101_models.StartMigrationJobRequest,
    ) -> dts_20200101_models.StartMigrationJobResponse:
        """
        @summary Starts a data migration task.
        
        @param request: StartMigrationJobRequest
        @return: StartMigrationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_migration_job_with_options(request, runtime)

    async def start_migration_job_async(
        self,
        request: dts_20200101_models.StartMigrationJobRequest,
    ) -> dts_20200101_models.StartMigrationJobResponse:
        """
        @summary Starts a data migration task.
        
        @param request: StartMigrationJobRequest
        @return: StartMigrationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_migration_job_with_options_async(request, runtime)

    def start_reverse_writer_with_options(
        self,
        request: dts_20200101_models.StartReverseWriterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartReverseWriterResponse:
        """
        @summary Starts the reverse task that is created by calling the CreateReverseDtsJob operation.
        
        @description Before you call this operation, make sure that your instance is not released and is paused. You can check the status of the instance in the Data Transmission Service (DTS) console or by calling the [DescribeDtsJobDetail](https://help.aliyun.com/document_detail/208925.html) operation.
        
        @param request: StartReverseWriterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartReverseWriterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_point):
            query['CheckPoint'] = request.check_point
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartReverseWriter',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.StartReverseWriterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.StartReverseWriterResponse(),
                self.execute(params, req, runtime)
            )

    async def start_reverse_writer_with_options_async(
        self,
        request: dts_20200101_models.StartReverseWriterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartReverseWriterResponse:
        """
        @summary Starts the reverse task that is created by calling the CreateReverseDtsJob operation.
        
        @description Before you call this operation, make sure that your instance is not released and is paused. You can check the status of the instance in the Data Transmission Service (DTS) console or by calling the [DescribeDtsJobDetail](https://help.aliyun.com/document_detail/208925.html) operation.
        
        @param request: StartReverseWriterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartReverseWriterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_point):
            query['CheckPoint'] = request.check_point
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartReverseWriter',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.StartReverseWriterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.StartReverseWriterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def start_reverse_writer(
        self,
        request: dts_20200101_models.StartReverseWriterRequest,
    ) -> dts_20200101_models.StartReverseWriterResponse:
        """
        @summary Starts the reverse task that is created by calling the CreateReverseDtsJob operation.
        
        @description Before you call this operation, make sure that your instance is not released and is paused. You can check the status of the instance in the Data Transmission Service (DTS) console or by calling the [DescribeDtsJobDetail](https://help.aliyun.com/document_detail/208925.html) operation.
        
        @param request: StartReverseWriterRequest
        @return: StartReverseWriterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_reverse_writer_with_options(request, runtime)

    async def start_reverse_writer_async(
        self,
        request: dts_20200101_models.StartReverseWriterRequest,
    ) -> dts_20200101_models.StartReverseWriterResponse:
        """
        @summary Starts the reverse task that is created by calling the CreateReverseDtsJob operation.
        
        @description Before you call this operation, make sure that your instance is not released and is paused. You can check the status of the instance in the Data Transmission Service (DTS) console or by calling the [DescribeDtsJobDetail](https://help.aliyun.com/document_detail/208925.html) operation.
        
        @param request: StartReverseWriterRequest
        @return: StartReverseWriterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_reverse_writer_with_options_async(request, runtime)

    def start_subscription_instance_with_options(
        self,
        request: dts_20200101_models.StartSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartSubscriptionInstanceResponse:
        """
        @summary Starts a change tracking task.
        
        @param request: StartSubscriptionInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartSubscriptionInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartSubscriptionInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.StartSubscriptionInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.StartSubscriptionInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def start_subscription_instance_with_options_async(
        self,
        request: dts_20200101_models.StartSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartSubscriptionInstanceResponse:
        """
        @summary Starts a change tracking task.
        
        @param request: StartSubscriptionInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartSubscriptionInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartSubscriptionInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.StartSubscriptionInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.StartSubscriptionInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def start_subscription_instance(
        self,
        request: dts_20200101_models.StartSubscriptionInstanceRequest,
    ) -> dts_20200101_models.StartSubscriptionInstanceResponse:
        """
        @summary Starts a change tracking task.
        
        @param request: StartSubscriptionInstanceRequest
        @return: StartSubscriptionInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_subscription_instance_with_options(request, runtime)

    async def start_subscription_instance_async(
        self,
        request: dts_20200101_models.StartSubscriptionInstanceRequest,
    ) -> dts_20200101_models.StartSubscriptionInstanceResponse:
        """
        @summary Starts a change tracking task.
        
        @param request: StartSubscriptionInstanceRequest
        @return: StartSubscriptionInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_subscription_instance_with_options_async(request, runtime)

    def start_synchronization_job_with_options(
        self,
        request: dts_20200101_models.StartSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartSynchronizationJobResponse:
        """
        @summary Starts a data synchronization task.
        
        @param request: StartSynchronizationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.StartSynchronizationJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.StartSynchronizationJobResponse(),
                self.execute(params, req, runtime)
            )

    async def start_synchronization_job_with_options_async(
        self,
        request: dts_20200101_models.StartSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartSynchronizationJobResponse:
        """
        @summary Starts a data synchronization task.
        
        @param request: StartSynchronizationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.StartSynchronizationJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.StartSynchronizationJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def start_synchronization_job(
        self,
        request: dts_20200101_models.StartSynchronizationJobRequest,
    ) -> dts_20200101_models.StartSynchronizationJobResponse:
        """
        @summary Starts a data synchronization task.
        
        @param request: StartSynchronizationJobRequest
        @return: StartSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_synchronization_job_with_options(request, runtime)

    async def start_synchronization_job_async(
        self,
        request: dts_20200101_models.StartSynchronizationJobRequest,
    ) -> dts_20200101_models.StartSynchronizationJobResponse:
        """
        @summary Starts a data synchronization task.
        
        @param request: StartSynchronizationJobRequest
        @return: StartSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_synchronization_job_with_options_async(request, runtime)

    def stop_dedicated_cluster_with_options(
        self,
        request: dts_20200101_models.StopDedicatedClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StopDedicatedClusterResponse:
        """
        @summary Releases a cluster.
        
        @param request: StopDedicatedClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDedicatedClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.dedicated_cluster_name):
            query['DedicatedClusterName'] = request.dedicated_cluster_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDedicatedCluster',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.StopDedicatedClusterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.StopDedicatedClusterResponse(),
                self.execute(params, req, runtime)
            )

    async def stop_dedicated_cluster_with_options_async(
        self,
        request: dts_20200101_models.StopDedicatedClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StopDedicatedClusterResponse:
        """
        @summary Releases a cluster.
        
        @param request: StopDedicatedClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDedicatedClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.dedicated_cluster_name):
            query['DedicatedClusterName'] = request.dedicated_cluster_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDedicatedCluster',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.StopDedicatedClusterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.StopDedicatedClusterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def stop_dedicated_cluster(
        self,
        request: dts_20200101_models.StopDedicatedClusterRequest,
    ) -> dts_20200101_models.StopDedicatedClusterResponse:
        """
        @summary Releases a cluster.
        
        @param request: StopDedicatedClusterRequest
        @return: StopDedicatedClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_dedicated_cluster_with_options(request, runtime)

    async def stop_dedicated_cluster_async(
        self,
        request: dts_20200101_models.StopDedicatedClusterRequest,
    ) -> dts_20200101_models.StopDedicatedClusterResponse:
        """
        @summary Releases a cluster.
        
        @param request: StopDedicatedClusterRequest
        @return: StopDedicatedClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_dedicated_cluster_with_options_async(request, runtime)

    def stop_dts_job_with_options(
        self,
        request: dts_20200101_models.StopDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StopDtsJobResponse:
        """
        @summary Stops a data migration, data synchronization, or change tracking task.
        
        @param request: StopDtsJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDtsJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.StopDtsJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.StopDtsJobResponse(),
                self.execute(params, req, runtime)
            )

    async def stop_dts_job_with_options_async(
        self,
        request: dts_20200101_models.StopDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StopDtsJobResponse:
        """
        @summary Stops a data migration, data synchronization, or change tracking task.
        
        @param request: StopDtsJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDtsJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.StopDtsJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.StopDtsJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def stop_dts_job(
        self,
        request: dts_20200101_models.StopDtsJobRequest,
    ) -> dts_20200101_models.StopDtsJobResponse:
        """
        @summary Stops a data migration, data synchronization, or change tracking task.
        
        @param request: StopDtsJobRequest
        @return: StopDtsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_dts_job_with_options(request, runtime)

    async def stop_dts_job_async(
        self,
        request: dts_20200101_models.StopDtsJobRequest,
    ) -> dts_20200101_models.StopDtsJobResponse:
        """
        @summary Stops a data migration, data synchronization, or change tracking task.
        
        @param request: StopDtsJobRequest
        @return: StopDtsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_dts_job_with_options_async(request, runtime)

    def stop_dts_jobs_with_options(
        self,
        request: dts_20200101_models.StopDtsJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StopDtsJobsResponse:
        """
        @summary Stops multiple data migration or data synchronization tasks.
        
        @param request: StopDtsJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDtsJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.StopDtsJobsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.StopDtsJobsResponse(),
                self.execute(params, req, runtime)
            )

    async def stop_dts_jobs_with_options_async(
        self,
        request: dts_20200101_models.StopDtsJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StopDtsJobsResponse:
        """
        @summary Stops multiple data migration or data synchronization tasks.
        
        @param request: StopDtsJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDtsJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.StopDtsJobsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.StopDtsJobsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def stop_dts_jobs(
        self,
        request: dts_20200101_models.StopDtsJobsRequest,
    ) -> dts_20200101_models.StopDtsJobsResponse:
        """
        @summary Stops multiple data migration or data synchronization tasks.
        
        @param request: StopDtsJobsRequest
        @return: StopDtsJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_dts_jobs_with_options(request, runtime)

    async def stop_dts_jobs_async(
        self,
        request: dts_20200101_models.StopDtsJobsRequest,
    ) -> dts_20200101_models.StopDtsJobsResponse:
        """
        @summary Stops multiple data migration or data synchronization tasks.
        
        @param request: StopDtsJobsRequest
        @return: StopDtsJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_dts_jobs_with_options_async(request, runtime)

    def stop_migration_job_with_options(
        self,
        request: dts_20200101_models.StopMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StopMigrationJobResponse:
        """
        @summary Stops a data migration task that is in the Migrating state.
        
        @param request: StopMigrationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopMigrationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.StopMigrationJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.StopMigrationJobResponse(),
                self.execute(params, req, runtime)
            )

    async def stop_migration_job_with_options_async(
        self,
        request: dts_20200101_models.StopMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StopMigrationJobResponse:
        """
        @summary Stops a data migration task that is in the Migrating state.
        
        @param request: StopMigrationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopMigrationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.StopMigrationJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.StopMigrationJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def stop_migration_job(
        self,
        request: dts_20200101_models.StopMigrationJobRequest,
    ) -> dts_20200101_models.StopMigrationJobResponse:
        """
        @summary Stops a data migration task that is in the Migrating state.
        
        @param request: StopMigrationJobRequest
        @return: StopMigrationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_migration_job_with_options(request, runtime)

    async def stop_migration_job_async(
        self,
        request: dts_20200101_models.StopMigrationJobRequest,
    ) -> dts_20200101_models.StopMigrationJobResponse:
        """
        @summary Stops a data migration task that is in the Migrating state.
        
        @param request: StopMigrationJobRequest
        @return: StopMigrationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_migration_job_with_options_async(request, runtime)

    def summary_job_detail_with_options(
        self,
        request: dts_20200101_models.SummaryJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SummaryJobDetailResponse:
        """
        @summary Queries the number of migrated or synchronized objects in a Data Transmission Service (DTS) task.
        
        @param request: SummaryJobDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SummaryJobDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.job_code):
            query['JobCode'] = request.job_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.struct_type):
            query['StructType'] = request.struct_type
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SummaryJobDetail',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.SummaryJobDetailResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.SummaryJobDetailResponse(),
                self.execute(params, req, runtime)
            )

    async def summary_job_detail_with_options_async(
        self,
        request: dts_20200101_models.SummaryJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SummaryJobDetailResponse:
        """
        @summary Queries the number of migrated or synchronized objects in a Data Transmission Service (DTS) task.
        
        @param request: SummaryJobDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SummaryJobDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.job_code):
            query['JobCode'] = request.job_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.struct_type):
            query['StructType'] = request.struct_type
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SummaryJobDetail',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.SummaryJobDetailResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.SummaryJobDetailResponse(),
                await self.execute_async(params, req, runtime)
            )

    def summary_job_detail(
        self,
        request: dts_20200101_models.SummaryJobDetailRequest,
    ) -> dts_20200101_models.SummaryJobDetailResponse:
        """
        @summary Queries the number of migrated or synchronized objects in a Data Transmission Service (DTS) task.
        
        @param request: SummaryJobDetailRequest
        @return: SummaryJobDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.summary_job_detail_with_options(request, runtime)

    async def summary_job_detail_async(
        self,
        request: dts_20200101_models.SummaryJobDetailRequest,
    ) -> dts_20200101_models.SummaryJobDetailResponse:
        """
        @summary Queries the number of migrated or synchronized objects in a Data Transmission Service (DTS) task.
        
        @param request: SummaryJobDetailRequest
        @return: SummaryJobDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.summary_job_detail_with_options_async(request, runtime)

    def suspend_dts_job_with_options(
        self,
        request: dts_20200101_models.SuspendDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SuspendDtsJobResponse:
        """
        @summary Pauses a data migration, data synchronization, or change tracking task.
        
        @description ***\
        
        @param request: SuspendDtsJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendDtsJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.SuspendDtsJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.SuspendDtsJobResponse(),
                self.execute(params, req, runtime)
            )

    async def suspend_dts_job_with_options_async(
        self,
        request: dts_20200101_models.SuspendDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SuspendDtsJobResponse:
        """
        @summary Pauses a data migration, data synchronization, or change tracking task.
        
        @description ***\
        
        @param request: SuspendDtsJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendDtsJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.SuspendDtsJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.SuspendDtsJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def suspend_dts_job(
        self,
        request: dts_20200101_models.SuspendDtsJobRequest,
    ) -> dts_20200101_models.SuspendDtsJobResponse:
        """
        @summary Pauses a data migration, data synchronization, or change tracking task.
        
        @description ***\
        
        @param request: SuspendDtsJobRequest
        @return: SuspendDtsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.suspend_dts_job_with_options(request, runtime)

    async def suspend_dts_job_async(
        self,
        request: dts_20200101_models.SuspendDtsJobRequest,
    ) -> dts_20200101_models.SuspendDtsJobResponse:
        """
        @summary Pauses a data migration, data synchronization, or change tracking task.
        
        @description ***\
        
        @param request: SuspendDtsJobRequest
        @return: SuspendDtsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.suspend_dts_job_with_options_async(request, runtime)

    def suspend_dts_jobs_with_options(
        self,
        request: dts_20200101_models.SuspendDtsJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SuspendDtsJobsResponse:
        """
        @summary Suspends multiple Data Transmission Service (DTS) tasks.
        
        @param request: SuspendDtsJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendDtsJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.SuspendDtsJobsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.SuspendDtsJobsResponse(),
                self.execute(params, req, runtime)
            )

    async def suspend_dts_jobs_with_options_async(
        self,
        request: dts_20200101_models.SuspendDtsJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SuspendDtsJobsResponse:
        """
        @summary Suspends multiple Data Transmission Service (DTS) tasks.
        
        @param request: SuspendDtsJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendDtsJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.SuspendDtsJobsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.SuspendDtsJobsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def suspend_dts_jobs(
        self,
        request: dts_20200101_models.SuspendDtsJobsRequest,
    ) -> dts_20200101_models.SuspendDtsJobsResponse:
        """
        @summary Suspends multiple Data Transmission Service (DTS) tasks.
        
        @param request: SuspendDtsJobsRequest
        @return: SuspendDtsJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.suspend_dts_jobs_with_options(request, runtime)

    async def suspend_dts_jobs_async(
        self,
        request: dts_20200101_models.SuspendDtsJobsRequest,
    ) -> dts_20200101_models.SuspendDtsJobsResponse:
        """
        @summary Suspends multiple Data Transmission Service (DTS) tasks.
        
        @param request: SuspendDtsJobsRequest
        @return: SuspendDtsJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.suspend_dts_jobs_with_options_async(request, runtime)

    def suspend_migration_job_with_options(
        self,
        request: dts_20200101_models.SuspendMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SuspendMigrationJobResponse:
        """
        @summary Pauses a data migration task.
        
        @param request: SuspendMigrationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendMigrationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.SuspendMigrationJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.SuspendMigrationJobResponse(),
                self.execute(params, req, runtime)
            )

    async def suspend_migration_job_with_options_async(
        self,
        request: dts_20200101_models.SuspendMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SuspendMigrationJobResponse:
        """
        @summary Pauses a data migration task.
        
        @param request: SuspendMigrationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendMigrationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.SuspendMigrationJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.SuspendMigrationJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def suspend_migration_job(
        self,
        request: dts_20200101_models.SuspendMigrationJobRequest,
    ) -> dts_20200101_models.SuspendMigrationJobResponse:
        """
        @summary Pauses a data migration task.
        
        @param request: SuspendMigrationJobRequest
        @return: SuspendMigrationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.suspend_migration_job_with_options(request, runtime)

    async def suspend_migration_job_async(
        self,
        request: dts_20200101_models.SuspendMigrationJobRequest,
    ) -> dts_20200101_models.SuspendMigrationJobResponse:
        """
        @summary Pauses a data migration task.
        
        @param request: SuspendMigrationJobRequest
        @return: SuspendMigrationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.suspend_migration_job_with_options_async(request, runtime)

    def suspend_synchronization_job_with_options(
        self,
        request: dts_20200101_models.SuspendSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SuspendSynchronizationJobResponse:
        """
        @summary Pauses a data synchronization task.
        
        @description >
        When you call this operation, the data synchronization task must be in the Synchronizing state.
        We recommend that you do not pause a data synchronization task for more than 6 hours. Otherwise, the task cannot be started again.
        If the billing method is pay-as-you-go, DTS charges a fee even when the task is paused. This is because DTS only stops writing data to the destination database. DTS continues to pull the logs of the source database so that the task can resume quickly after it is restarted. Therefore, data synchronization consumes resources such as the bandwidth of the source database.
        
        @param request: SuspendSynchronizationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.SuspendSynchronizationJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.SuspendSynchronizationJobResponse(),
                self.execute(params, req, runtime)
            )

    async def suspend_synchronization_job_with_options_async(
        self,
        request: dts_20200101_models.SuspendSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SuspendSynchronizationJobResponse:
        """
        @summary Pauses a data synchronization task.
        
        @description >
        When you call this operation, the data synchronization task must be in the Synchronizing state.
        We recommend that you do not pause a data synchronization task for more than 6 hours. Otherwise, the task cannot be started again.
        If the billing method is pay-as-you-go, DTS charges a fee even when the task is paused. This is because DTS only stops writing data to the destination database. DTS continues to pull the logs of the source database so that the task can resume quickly after it is restarted. Therefore, data synchronization consumes resources such as the bandwidth of the source database.
        
        @param request: SuspendSynchronizationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.SuspendSynchronizationJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.SuspendSynchronizationJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def suspend_synchronization_job(
        self,
        request: dts_20200101_models.SuspendSynchronizationJobRequest,
    ) -> dts_20200101_models.SuspendSynchronizationJobResponse:
        """
        @summary Pauses a data synchronization task.
        
        @description >
        When you call this operation, the data synchronization task must be in the Synchronizing state.
        We recommend that you do not pause a data synchronization task for more than 6 hours. Otherwise, the task cannot be started again.
        If the billing method is pay-as-you-go, DTS charges a fee even when the task is paused. This is because DTS only stops writing data to the destination database. DTS continues to pull the logs of the source database so that the task can resume quickly after it is restarted. Therefore, data synchronization consumes resources such as the bandwidth of the source database.
        
        @param request: SuspendSynchronizationJobRequest
        @return: SuspendSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.suspend_synchronization_job_with_options(request, runtime)

    async def suspend_synchronization_job_async(
        self,
        request: dts_20200101_models.SuspendSynchronizationJobRequest,
    ) -> dts_20200101_models.SuspendSynchronizationJobResponse:
        """
        @summary Pauses a data synchronization task.
        
        @description >
        When you call this operation, the data synchronization task must be in the Synchronizing state.
        We recommend that you do not pause a data synchronization task for more than 6 hours. Otherwise, the task cannot be started again.
        If the billing method is pay-as-you-go, DTS charges a fee even when the task is paused. This is because DTS only stops writing data to the destination database. DTS continues to pull the logs of the source database so that the task can resume quickly after it is restarted. Therefore, data synchronization consumes resources such as the bandwidth of the source database.
        
        @param request: SuspendSynchronizationJobRequest
        @return: SuspendSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.suspend_synchronization_job_with_options_async(request, runtime)

    def switch_physical_dts_job_to_cloud_with_options(
        self,
        request: dts_20200101_models.SwitchPhysicalDtsJobToCloudRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SwitchPhysicalDtsJobToCloudResponse:
        """
        @summary 物理迁移任务切换上云
        
        @param request: SwitchPhysicalDtsJobToCloudRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchPhysicalDtsJobToCloudResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchPhysicalDtsJobToCloud',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.SwitchPhysicalDtsJobToCloudResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.SwitchPhysicalDtsJobToCloudResponse(),
                self.execute(params, req, runtime)
            )

    async def switch_physical_dts_job_to_cloud_with_options_async(
        self,
        request: dts_20200101_models.SwitchPhysicalDtsJobToCloudRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SwitchPhysicalDtsJobToCloudResponse:
        """
        @summary 物理迁移任务切换上云
        
        @param request: SwitchPhysicalDtsJobToCloudRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchPhysicalDtsJobToCloudResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchPhysicalDtsJobToCloud',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.SwitchPhysicalDtsJobToCloudResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.SwitchPhysicalDtsJobToCloudResponse(),
                await self.execute_async(params, req, runtime)
            )

    def switch_physical_dts_job_to_cloud(
        self,
        request: dts_20200101_models.SwitchPhysicalDtsJobToCloudRequest,
    ) -> dts_20200101_models.SwitchPhysicalDtsJobToCloudResponse:
        """
        @summary 物理迁移任务切换上云
        
        @param request: SwitchPhysicalDtsJobToCloudRequest
        @return: SwitchPhysicalDtsJobToCloudResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_physical_dts_job_to_cloud_with_options(request, runtime)

    async def switch_physical_dts_job_to_cloud_async(
        self,
        request: dts_20200101_models.SwitchPhysicalDtsJobToCloudRequest,
    ) -> dts_20200101_models.SwitchPhysicalDtsJobToCloudResponse:
        """
        @summary 物理迁移任务切换上云
        
        @param request: SwitchPhysicalDtsJobToCloudRequest
        @return: SwitchPhysicalDtsJobToCloudResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.switch_physical_dts_job_to_cloud_with_options_async(request, runtime)

    def switch_synchronization_endpoint_with_options(
        self,
        request: dts_20200101_models.SwitchSynchronizationEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SwitchSynchronizationEndpointResponse:
        """
        @summary After you perform a primary/secondary switchover on the source or destination database, you can call the SwitchSynchronizationEndpoint operation to transfer the connection settings to Data Transmission Service (DTS). DTS will restart the data synchronization task from the breakpoint.
        
        @param request: SwitchSynchronizationEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchSynchronizationEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchSynchronizationEndpoint',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.SwitchSynchronizationEndpointResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.SwitchSynchronizationEndpointResponse(),
                self.execute(params, req, runtime)
            )

    async def switch_synchronization_endpoint_with_options_async(
        self,
        request: dts_20200101_models.SwitchSynchronizationEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SwitchSynchronizationEndpointResponse:
        """
        @summary After you perform a primary/secondary switchover on the source or destination database, you can call the SwitchSynchronizationEndpoint operation to transfer the connection settings to Data Transmission Service (DTS). DTS will restart the data synchronization task from the breakpoint.
        
        @param request: SwitchSynchronizationEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchSynchronizationEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchSynchronizationEndpoint',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.SwitchSynchronizationEndpointResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.SwitchSynchronizationEndpointResponse(),
                await self.execute_async(params, req, runtime)
            )

    def switch_synchronization_endpoint(
        self,
        request: dts_20200101_models.SwitchSynchronizationEndpointRequest,
    ) -> dts_20200101_models.SwitchSynchronizationEndpointResponse:
        """
        @summary After you perform a primary/secondary switchover on the source or destination database, you can call the SwitchSynchronizationEndpoint operation to transfer the connection settings to Data Transmission Service (DTS). DTS will restart the data synchronization task from the breakpoint.
        
        @param request: SwitchSynchronizationEndpointRequest
        @return: SwitchSynchronizationEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_synchronization_endpoint_with_options(request, runtime)

    async def switch_synchronization_endpoint_async(
        self,
        request: dts_20200101_models.SwitchSynchronizationEndpointRequest,
    ) -> dts_20200101_models.SwitchSynchronizationEndpointResponse:
        """
        @summary After you perform a primary/secondary switchover on the source or destination database, you can call the SwitchSynchronizationEndpoint operation to transfer the connection settings to Data Transmission Service (DTS). DTS will restart the data synchronization task from the breakpoint.
        
        @param request: SwitchSynchronizationEndpointRequest
        @return: SwitchSynchronizationEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.switch_synchronization_endpoint_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: dts_20200101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.TagResourcesResponse:
        """
        @summary Adds tags to data migration, data synchronization, or change tracking instances.
        
        @description If you have a large number of instances, you can create multiple tags and add these tags to the instances. Then, you can query instances by tag.
        A tag consists of a key and a value. Each key must be unique in a region within an Alibaba Cloud account. Different keys can be mapped to the same value.
        If the tag that you specify does not exist, this tag is automatically created and added to the specified instance.
        If the key of the specified tag is the same as that of an existing tag, the specified tag overwrites the existing tag.
        You can add up to 20 tags to an instance.
        You can add tags to up to 50 instances in each request.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.TagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.TagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def tag_resources_with_options_async(
        self,
        request: dts_20200101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.TagResourcesResponse:
        """
        @summary Adds tags to data migration, data synchronization, or change tracking instances.
        
        @description If you have a large number of instances, you can create multiple tags and add these tags to the instances. Then, you can query instances by tag.
        A tag consists of a key and a value. Each key must be unique in a region within an Alibaba Cloud account. Different keys can be mapped to the same value.
        If the tag that you specify does not exist, this tag is automatically created and added to the specified instance.
        If the key of the specified tag is the same as that of an existing tag, the specified tag overwrites the existing tag.
        You can add up to 20 tags to an instance.
        You can add tags to up to 50 instances in each request.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.TagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.TagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def tag_resources(
        self,
        request: dts_20200101_models.TagResourcesRequest,
    ) -> dts_20200101_models.TagResourcesResponse:
        """
        @summary Adds tags to data migration, data synchronization, or change tracking instances.
        
        @description If you have a large number of instances, you can create multiple tags and add these tags to the instances. Then, you can query instances by tag.
        A tag consists of a key and a value. Each key must be unique in a region within an Alibaba Cloud account. Different keys can be mapped to the same value.
        If the tag that you specify does not exist, this tag is automatically created and added to the specified instance.
        If the key of the specified tag is the same as that of an existing tag, the specified tag overwrites the existing tag.
        You can add up to 20 tags to an instance.
        You can add tags to up to 50 instances in each request.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: dts_20200101_models.TagResourcesRequest,
    ) -> dts_20200101_models.TagResourcesResponse:
        """
        @summary Adds tags to data migration, data synchronization, or change tracking instances.
        
        @description If you have a large number of instances, you can create multiple tags and add these tags to the instances. Then, you can query instances by tag.
        A tag consists of a key and a value. Each key must be unique in a region within an Alibaba Cloud account. Different keys can be mapped to the same value.
        If the tag that you specify does not exist, this tag is automatically created and added to the specified instance.
        If the key of the specified tag is the same as that of an existing tag, the specified tag overwrites the existing tag.
        You can add up to 20 tags to an instance.
        You can add tags to up to 50 instances in each request.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def transfer_instance_class_with_options(
        self,
        request: dts_20200101_models.TransferInstanceClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.TransferInstanceClassResponse:
        """
        @summary Upgrades or downgrades a Data Transmission Service (DTS) instance.
        
        @param request: TransferInstanceClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferInstanceClassResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferInstanceClass',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.TransferInstanceClassResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.TransferInstanceClassResponse(),
                self.execute(params, req, runtime)
            )

    async def transfer_instance_class_with_options_async(
        self,
        request: dts_20200101_models.TransferInstanceClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.TransferInstanceClassResponse:
        """
        @summary Upgrades or downgrades a Data Transmission Service (DTS) instance.
        
        @param request: TransferInstanceClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferInstanceClassResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferInstanceClass',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.TransferInstanceClassResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.TransferInstanceClassResponse(),
                await self.execute_async(params, req, runtime)
            )

    def transfer_instance_class(
        self,
        request: dts_20200101_models.TransferInstanceClassRequest,
    ) -> dts_20200101_models.TransferInstanceClassResponse:
        """
        @summary Upgrades or downgrades a Data Transmission Service (DTS) instance.
        
        @param request: TransferInstanceClassRequest
        @return: TransferInstanceClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transfer_instance_class_with_options(request, runtime)

    async def transfer_instance_class_async(
        self,
        request: dts_20200101_models.TransferInstanceClassRequest,
    ) -> dts_20200101_models.TransferInstanceClassResponse:
        """
        @summary Upgrades or downgrades a Data Transmission Service (DTS) instance.
        
        @param request: TransferInstanceClassRequest
        @return: TransferInstanceClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.transfer_instance_class_with_options_async(request, runtime)

    def transfer_pay_type_with_options(
        self,
        request: dts_20200101_models.TransferPayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.TransferPayTypeResponse:
        """
        @summary Changes the billing method of a Data Transmission Service (DTS) instance.
        
        @description Before you call this operation, make sure that you fully understand the [billing](https://www.alibabacloud.com/zh/product/data-transmission-service/pricing) of DTS.
        To prevent resource waste, make sure that the billing method of your DTS instances has to be changed.
        Data migration instances only support the pay-as-you-go billing method.
        
        @param request: TransferPayTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferPayTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.buy_count):
            query['BuyCount'] = request.buy_count
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.max_du):
            query['MaxDu'] = request.max_du
        if not UtilClient.is_unset(request.min_du):
            query['MinDu'] = request.min_du
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferPayType',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.TransferPayTypeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.TransferPayTypeResponse(),
                self.execute(params, req, runtime)
            )

    async def transfer_pay_type_with_options_async(
        self,
        request: dts_20200101_models.TransferPayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.TransferPayTypeResponse:
        """
        @summary Changes the billing method of a Data Transmission Service (DTS) instance.
        
        @description Before you call this operation, make sure that you fully understand the [billing](https://www.alibabacloud.com/zh/product/data-transmission-service/pricing) of DTS.
        To prevent resource waste, make sure that the billing method of your DTS instances has to be changed.
        Data migration instances only support the pay-as-you-go billing method.
        
        @param request: TransferPayTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferPayTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.buy_count):
            query['BuyCount'] = request.buy_count
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.max_du):
            query['MaxDu'] = request.max_du
        if not UtilClient.is_unset(request.min_du):
            query['MinDu'] = request.min_du
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferPayType',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.TransferPayTypeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.TransferPayTypeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def transfer_pay_type(
        self,
        request: dts_20200101_models.TransferPayTypeRequest,
    ) -> dts_20200101_models.TransferPayTypeResponse:
        """
        @summary Changes the billing method of a Data Transmission Service (DTS) instance.
        
        @description Before you call this operation, make sure that you fully understand the [billing](https://www.alibabacloud.com/zh/product/data-transmission-service/pricing) of DTS.
        To prevent resource waste, make sure that the billing method of your DTS instances has to be changed.
        Data migration instances only support the pay-as-you-go billing method.
        
        @param request: TransferPayTypeRequest
        @return: TransferPayTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transfer_pay_type_with_options(request, runtime)

    async def transfer_pay_type_async(
        self,
        request: dts_20200101_models.TransferPayTypeRequest,
    ) -> dts_20200101_models.TransferPayTypeResponse:
        """
        @summary Changes the billing method of a Data Transmission Service (DTS) instance.
        
        @description Before you call this operation, make sure that you fully understand the [billing](https://www.alibabacloud.com/zh/product/data-transmission-service/pricing) of DTS.
        To prevent resource waste, make sure that the billing method of your DTS instances has to be changed.
        Data migration instances only support the pay-as-you-go billing method.
        
        @param request: TransferPayTypeRequest
        @return: TransferPayTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.transfer_pay_type_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: dts_20200101_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.UntagResourcesResponse:
        """
        @summary Unbinds tags from one or more data migration, data synchronization, or change tracking instances.
        
        @description >  If a tag is unbound from an instance and is not bound to other instances, the tag is deleted.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.UntagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.UntagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def untag_resources_with_options_async(
        self,
        request: dts_20200101_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.UntagResourcesResponse:
        """
        @summary Unbinds tags from one or more data migration, data synchronization, or change tracking instances.
        
        @description >  If a tag is unbound from an instance and is not bound to other instances, the tag is deleted.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.UntagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.UntagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def untag_resources(
        self,
        request: dts_20200101_models.UntagResourcesRequest,
    ) -> dts_20200101_models.UntagResourcesResponse:
        """
        @summary Unbinds tags from one or more data migration, data synchronization, or change tracking instances.
        
        @description >  If a tag is unbound from an instance and is not bound to other instances, the tag is deleted.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: dts_20200101_models.UntagResourcesRequest,
    ) -> dts_20200101_models.UntagResourcesResponse:
        """
        @summary Unbinds tags from one or more data migration, data synchronization, or change tracking instances.
        
        @description >  If a tag is unbound from an instance and is not bound to other instances, the tag is deleted.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def upgrade_two_way_with_options(
        self,
        request: dts_20200101_models.UpgradeTwoWayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.UpgradeTwoWayResponse:
        """
        @summary Upgrades the synchronization topology of a data synchronization instance from one-way synchronization to two-way synchronization. This operation is supported only for pay-as-you-go synchronization instances.
        
        @description Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/data-transmission-service/pricing) of Data Transmission Service (DTS)
        When you call this operation, take note of the following information:
        The source and destination databases of the data synchronization task are both **MySQL** databases.
        The synchronization topology of the data synchronization task is **one-way synchronization**.
        The data synchronization task is in the **Synchronizing** state.
        The upgrade operation causes data synchronization latency of about 5 seconds. We recommend that you perform this operation during off-peak hours.
        
        @param request: UpgradeTwoWayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeTwoWayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeTwoWay',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.UpgradeTwoWayResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.UpgradeTwoWayResponse(),
                self.execute(params, req, runtime)
            )

    async def upgrade_two_way_with_options_async(
        self,
        request: dts_20200101_models.UpgradeTwoWayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.UpgradeTwoWayResponse:
        """
        @summary Upgrades the synchronization topology of a data synchronization instance from one-way synchronization to two-way synchronization. This operation is supported only for pay-as-you-go synchronization instances.
        
        @description Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/data-transmission-service/pricing) of Data Transmission Service (DTS)
        When you call this operation, take note of the following information:
        The source and destination databases of the data synchronization task are both **MySQL** databases.
        The synchronization topology of the data synchronization task is **one-way synchronization**.
        The data synchronization task is in the **Synchronizing** state.
        The upgrade operation causes data synchronization latency of about 5 seconds. We recommend that you perform this operation during off-peak hours.
        
        @param request: UpgradeTwoWayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeTwoWayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeTwoWay',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.UpgradeTwoWayResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.UpgradeTwoWayResponse(),
                await self.execute_async(params, req, runtime)
            )

    def upgrade_two_way(
        self,
        request: dts_20200101_models.UpgradeTwoWayRequest,
    ) -> dts_20200101_models.UpgradeTwoWayResponse:
        """
        @summary Upgrades the synchronization topology of a data synchronization instance from one-way synchronization to two-way synchronization. This operation is supported only for pay-as-you-go synchronization instances.
        
        @description Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/data-transmission-service/pricing) of Data Transmission Service (DTS)
        When you call this operation, take note of the following information:
        The source and destination databases of the data synchronization task are both **MySQL** databases.
        The synchronization topology of the data synchronization task is **one-way synchronization**.
        The data synchronization task is in the **Synchronizing** state.
        The upgrade operation causes data synchronization latency of about 5 seconds. We recommend that you perform this operation during off-peak hours.
        
        @param request: UpgradeTwoWayRequest
        @return: UpgradeTwoWayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_two_way_with_options(request, runtime)

    async def upgrade_two_way_async(
        self,
        request: dts_20200101_models.UpgradeTwoWayRequest,
    ) -> dts_20200101_models.UpgradeTwoWayResponse:
        """
        @summary Upgrades the synchronization topology of a data synchronization instance from one-way synchronization to two-way synchronization. This operation is supported only for pay-as-you-go synchronization instances.
        
        @description Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/data-transmission-service/pricing) of Data Transmission Service (DTS)
        When you call this operation, take note of the following information:
        The source and destination databases of the data synchronization task are both **MySQL** databases.
        The synchronization topology of the data synchronization task is **one-way synchronization**.
        The data synchronization task is in the **Synchronizing** state.
        The upgrade operation causes data synchronization latency of about 5 seconds. We recommend that you perform this operation during off-peak hours.
        
        @param request: UpgradeTwoWayRequest
        @return: UpgradeTwoWayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_two_way_with_options_async(request, runtime)

    def white_ip_list_with_options(
        self,
        request: dts_20200101_models.WhiteIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.WhiteIpListResponse:
        """
        @summary If the \\\\\\\\*source or destination instance\\\\*\\\\* is a \\\\*\\\\*self-managed database\\\\*\\\\* or a \\\\*\\\\*third-party cloud database\\\\*\\\\*, you need to call this operation to query the CIDR blocks of DTS servers. Then, you need to add the CIDR blocks of DTS servers to the security settings of the source or destination instance, for example, the firewall of your database. For more information, see \\[Add the CIDR blocks of DTS servers to the security settings of on-premises databases]\\\\(~~176627~~).
        \\\\>  If the \\\\\\\\*source or destination database\\\\*\\\\* is an \\\\*\\\\*ApsaraDB database instance\\\\*\\\\* (such as RDS instance and ApsaraDB for MongoDB instance) or a \\\\*\\\\*self-managed database hosted on Elastic Compute Service (ECS)\\\\*\\\\*, you do not need to add the CIDR blocks. When you click \\\\*\\\\*Set Whitelist and Next\\\\*\\\\* in the DTS console, DTS automatically adds the CIDR blocks of DTS servers to the security settings of the source or destination instance.
        
        @description The operation that you want to perform. Set the value to *WhiteIpList**.
        
        @param request: WhiteIpListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: WhiteIpListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dest_aliyun_uid):
            query['DestAliyunUid'] = request.dest_aliyun_uid
        if not UtilClient.is_unset(request.dest_primary_vsw_id):
            query['DestPrimaryVswId'] = request.dest_primary_vsw_id
        if not UtilClient.is_unset(request.dest_role_name):
            query['DestRoleName'] = request.dest_role_name
        if not UtilClient.is_unset(request.dest_secondary_vsw_id):
            query['DestSecondaryVswId'] = request.dest_secondary_vsw_id
        if not UtilClient.is_unset(request.dest_vpc_id):
            query['DestVpcId'] = request.dest_vpc_id
        if not UtilClient.is_unset(request.destination_region):
            query['DestinationRegion'] = request.destination_region
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.src_aliyun_uid):
            query['SrcAliyunUid'] = request.src_aliyun_uid
        if not UtilClient.is_unset(request.src_primary_vsw_id):
            query['SrcPrimaryVswId'] = request.src_primary_vsw_id
        if not UtilClient.is_unset(request.src_role_name):
            query['SrcRoleName'] = request.src_role_name
        if not UtilClient.is_unset(request.src_secondary_vsw_id):
            query['SrcSecondaryVswId'] = request.src_secondary_vsw_id
        if not UtilClient.is_unset(request.src_vpc_id):
            query['SrcVpcId'] = request.src_vpc_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WhiteIpList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.WhiteIpListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.WhiteIpListResponse(),
                self.execute(params, req, runtime)
            )

    async def white_ip_list_with_options_async(
        self,
        request: dts_20200101_models.WhiteIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.WhiteIpListResponse:
        """
        @summary If the \\\\\\\\*source or destination instance\\\\*\\\\* is a \\\\*\\\\*self-managed database\\\\*\\\\* or a \\\\*\\\\*third-party cloud database\\\\*\\\\*, you need to call this operation to query the CIDR blocks of DTS servers. Then, you need to add the CIDR blocks of DTS servers to the security settings of the source or destination instance, for example, the firewall of your database. For more information, see \\[Add the CIDR blocks of DTS servers to the security settings of on-premises databases]\\\\(~~176627~~).
        \\\\>  If the \\\\\\\\*source or destination database\\\\*\\\\* is an \\\\*\\\\*ApsaraDB database instance\\\\*\\\\* (such as RDS instance and ApsaraDB for MongoDB instance) or a \\\\*\\\\*self-managed database hosted on Elastic Compute Service (ECS)\\\\*\\\\*, you do not need to add the CIDR blocks. When you click \\\\*\\\\*Set Whitelist and Next\\\\*\\\\* in the DTS console, DTS automatically adds the CIDR blocks of DTS servers to the security settings of the source or destination instance.
        
        @description The operation that you want to perform. Set the value to *WhiteIpList**.
        
        @param request: WhiteIpListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: WhiteIpListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dest_aliyun_uid):
            query['DestAliyunUid'] = request.dest_aliyun_uid
        if not UtilClient.is_unset(request.dest_primary_vsw_id):
            query['DestPrimaryVswId'] = request.dest_primary_vsw_id
        if not UtilClient.is_unset(request.dest_role_name):
            query['DestRoleName'] = request.dest_role_name
        if not UtilClient.is_unset(request.dest_secondary_vsw_id):
            query['DestSecondaryVswId'] = request.dest_secondary_vsw_id
        if not UtilClient.is_unset(request.dest_vpc_id):
            query['DestVpcId'] = request.dest_vpc_id
        if not UtilClient.is_unset(request.destination_region):
            query['DestinationRegion'] = request.destination_region
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.src_aliyun_uid):
            query['SrcAliyunUid'] = request.src_aliyun_uid
        if not UtilClient.is_unset(request.src_primary_vsw_id):
            query['SrcPrimaryVswId'] = request.src_primary_vsw_id
        if not UtilClient.is_unset(request.src_role_name):
            query['SrcRoleName'] = request.src_role_name
        if not UtilClient.is_unset(request.src_secondary_vsw_id):
            query['SrcSecondaryVswId'] = request.src_secondary_vsw_id
        if not UtilClient.is_unset(request.src_vpc_id):
            query['SrcVpcId'] = request.src_vpc_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.zero_etl_job):
            query['ZeroEtlJob'] = request.zero_etl_job
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WhiteIpList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dts_20200101_models.WhiteIpListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dts_20200101_models.WhiteIpListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def white_ip_list(
        self,
        request: dts_20200101_models.WhiteIpListRequest,
    ) -> dts_20200101_models.WhiteIpListResponse:
        """
        @summary If the \\\\\\\\*source or destination instance\\\\*\\\\* is a \\\\*\\\\*self-managed database\\\\*\\\\* or a \\\\*\\\\*third-party cloud database\\\\*\\\\*, you need to call this operation to query the CIDR blocks of DTS servers. Then, you need to add the CIDR blocks of DTS servers to the security settings of the source or destination instance, for example, the firewall of your database. For more information, see \\[Add the CIDR blocks of DTS servers to the security settings of on-premises databases]\\\\(~~176627~~).
        \\\\>  If the \\\\\\\\*source or destination database\\\\*\\\\* is an \\\\*\\\\*ApsaraDB database instance\\\\*\\\\* (such as RDS instance and ApsaraDB for MongoDB instance) or a \\\\*\\\\*self-managed database hosted on Elastic Compute Service (ECS)\\\\*\\\\*, you do not need to add the CIDR blocks. When you click \\\\*\\\\*Set Whitelist and Next\\\\*\\\\* in the DTS console, DTS automatically adds the CIDR blocks of DTS servers to the security settings of the source or destination instance.
        
        @description The operation that you want to perform. Set the value to *WhiteIpList**.
        
        @param request: WhiteIpListRequest
        @return: WhiteIpListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.white_ip_list_with_options(request, runtime)

    async def white_ip_list_async(
        self,
        request: dts_20200101_models.WhiteIpListRequest,
    ) -> dts_20200101_models.WhiteIpListResponse:
        """
        @summary If the \\\\\\\\*source or destination instance\\\\*\\\\* is a \\\\*\\\\*self-managed database\\\\*\\\\* or a \\\\*\\\\*third-party cloud database\\\\*\\\\*, you need to call this operation to query the CIDR blocks of DTS servers. Then, you need to add the CIDR blocks of DTS servers to the security settings of the source or destination instance, for example, the firewall of your database. For more information, see \\[Add the CIDR blocks of DTS servers to the security settings of on-premises databases]\\\\(~~176627~~).
        \\\\>  If the \\\\\\\\*source or destination database\\\\*\\\\* is an \\\\*\\\\*ApsaraDB database instance\\\\*\\\\* (such as RDS instance and ApsaraDB for MongoDB instance) or a \\\\*\\\\*self-managed database hosted on Elastic Compute Service (ECS)\\\\*\\\\*, you do not need to add the CIDR blocks. When you click \\\\*\\\\*Set Whitelist and Next\\\\*\\\\* in the DTS console, DTS automatically adds the CIDR blocks of DTS servers to the security settings of the source or destination instance.
        
        @description The operation that you want to perform. Set the value to *WhiteIpList**.
        
        @param request: WhiteIpListRequest
        @return: WhiteIpListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.white_ip_list_with_options_async(request, runtime)
