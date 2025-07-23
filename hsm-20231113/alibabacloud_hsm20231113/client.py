# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_hsm20231113 import models as hsm_20231113_models
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
        self._endpoint = self.get_endpoint('hsm', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def config_audit_log_with_options(
        self,
        request: hsm_20231113_models.ConfigAuditLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigAuditLogResponse:
        """
        @summary Enables or disables the audit log feature and delivers audit logs to buckets.
        
        @description    The region of the bucket must be the same as the region where the security audit feature is enabled.
        If the security audit feature is enabled, do not delete Object Storage Service (OSS) buckets. If you delete OSS buckets, audit logs fail to be delivered.
        Only electronic virtual security modules (EVSMs) and general virtual security modules (GVSMs) within the Chinese mainland support the security audit feature.
        
        @param request: ConfigAuditLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigAuditLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_action):
            query['AuditAction'] = request.audit_action
        if not UtilClient.is_unset(request.audit_oss_bucket):
            query['AuditOssBucket'] = request.audit_oss_bucket
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigAuditLog',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigAuditLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_audit_log_with_options_async(
        self,
        request: hsm_20231113_models.ConfigAuditLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigAuditLogResponse:
        """
        @summary Enables or disables the audit log feature and delivers audit logs to buckets.
        
        @description    The region of the bucket must be the same as the region where the security audit feature is enabled.
        If the security audit feature is enabled, do not delete Object Storage Service (OSS) buckets. If you delete OSS buckets, audit logs fail to be delivered.
        Only electronic virtual security modules (EVSMs) and general virtual security modules (GVSMs) within the Chinese mainland support the security audit feature.
        
        @param request: ConfigAuditLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigAuditLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_action):
            query['AuditAction'] = request.audit_action
        if not UtilClient.is_unset(request.audit_oss_bucket):
            query['AuditOssBucket'] = request.audit_oss_bucket
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigAuditLog',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigAuditLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_audit_log(
        self,
        request: hsm_20231113_models.ConfigAuditLogRequest,
    ) -> hsm_20231113_models.ConfigAuditLogResponse:
        """
        @summary Enables or disables the audit log feature and delivers audit logs to buckets.
        
        @description    The region of the bucket must be the same as the region where the security audit feature is enabled.
        If the security audit feature is enabled, do not delete Object Storage Service (OSS) buckets. If you delete OSS buckets, audit logs fail to be delivered.
        Only electronic virtual security modules (EVSMs) and general virtual security modules (GVSMs) within the Chinese mainland support the security audit feature.
        
        @param request: ConfigAuditLogRequest
        @return: ConfigAuditLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_audit_log_with_options(request, runtime)

    async def config_audit_log_async(
        self,
        request: hsm_20231113_models.ConfigAuditLogRequest,
    ) -> hsm_20231113_models.ConfigAuditLogResponse:
        """
        @summary Enables or disables the audit log feature and delivers audit logs to buckets.
        
        @description    The region of the bucket must be the same as the region where the security audit feature is enabled.
        If the security audit feature is enabled, do not delete Object Storage Service (OSS) buckets. If you delete OSS buckets, audit logs fail to be delivered.
        Only electronic virtual security modules (EVSMs) and general virtual security modules (GVSMs) within the Chinese mainland support the security audit feature.
        
        @param request: ConfigAuditLogRequest
        @return: ConfigAuditLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_audit_log_with_options_async(request, runtime)

    def config_backup_remark_with_options(
        self,
        request: hsm_20231113_models.ConfigBackupRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigBackupRemarkResponse:
        """
        @summary Configures the name and description of a backup.
        
        @param request: ConfigBackupRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigBackupRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigBackupRemark',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigBackupRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_backup_remark_with_options_async(
        self,
        request: hsm_20231113_models.ConfigBackupRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigBackupRemarkResponse:
        """
        @summary Configures the name and description of a backup.
        
        @param request: ConfigBackupRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigBackupRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigBackupRemark',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigBackupRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_backup_remark(
        self,
        request: hsm_20231113_models.ConfigBackupRemarkRequest,
    ) -> hsm_20231113_models.ConfigBackupRemarkResponse:
        """
        @summary Configures the name and description of a backup.
        
        @param request: ConfigBackupRemarkRequest
        @return: ConfigBackupRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_backup_remark_with_options(request, runtime)

    async def config_backup_remark_async(
        self,
        request: hsm_20231113_models.ConfigBackupRemarkRequest,
    ) -> hsm_20231113_models.ConfigBackupRemarkResponse:
        """
        @summary Configures the name and description of a backup.
        
        @param request: ConfigBackupRemarkRequest
        @return: ConfigBackupRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_backup_remark_with_options_async(request, runtime)

    def config_backup_task_with_options(
        self,
        request: hsm_20231113_models.ConfigBackupTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigBackupTaskResponse:
        """
        @summary Modifies the execution mode of a backup task.
        
        @description Only hardware security modules (HSMs) in the Chinese mainland support the operation.
        
        @param request: ConfigBackupTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigBackupTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_hour_in_day):
            query['BackupHourInDay'] = request.backup_hour_in_day
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not UtilClient.is_unset(request.manual_2periodic_list):
            query['Manual2PeriodicList'] = request.manual_2periodic_list
        if not UtilClient.is_unset(request.periodic_2manual_list):
            query['Periodic2ManualList'] = request.periodic_2manual_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigBackupTask',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigBackupTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_backup_task_with_options_async(
        self,
        request: hsm_20231113_models.ConfigBackupTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigBackupTaskResponse:
        """
        @summary Modifies the execution mode of a backup task.
        
        @description Only hardware security modules (HSMs) in the Chinese mainland support the operation.
        
        @param request: ConfigBackupTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigBackupTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_hour_in_day):
            query['BackupHourInDay'] = request.backup_hour_in_day
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not UtilClient.is_unset(request.manual_2periodic_list):
            query['Manual2PeriodicList'] = request.manual_2periodic_list
        if not UtilClient.is_unset(request.periodic_2manual_list):
            query['Periodic2ManualList'] = request.periodic_2manual_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigBackupTask',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigBackupTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_backup_task(
        self,
        request: hsm_20231113_models.ConfigBackupTaskRequest,
    ) -> hsm_20231113_models.ConfigBackupTaskResponse:
        """
        @summary Modifies the execution mode of a backup task.
        
        @description Only hardware security modules (HSMs) in the Chinese mainland support the operation.
        
        @param request: ConfigBackupTaskRequest
        @return: ConfigBackupTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_backup_task_with_options(request, runtime)

    async def config_backup_task_async(
        self,
        request: hsm_20231113_models.ConfigBackupTaskRequest,
    ) -> hsm_20231113_models.ConfigBackupTaskResponse:
        """
        @summary Modifies the execution mode of a backup task.
        
        @description Only hardware security modules (HSMs) in the Chinese mainland support the operation.
        
        @param request: ConfigBackupTaskRequest
        @return: ConfigBackupTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_backup_task_with_options_async(request, runtime)

    def config_cluster_certificate_with_options(
        self,
        request: hsm_20231113_models.ConfigClusterCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigClusterCertificateResponse:
        """
        @summary Configures a certificate for a cluster of hardware security modules (HSMs) outside the Chinese mainland.
        
        @description For more information about how to create a self-signed certificate and a cluster certificate on an Elastic Compute Service (ECS) instance, see [Create a NIST FIPS-validated GVSM cluster](https://help.aliyun.com/document_detail/293585.html).
        
        @param request: ConfigClusterCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigClusterCertificateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_certificate):
            body['ClusterCertificate'] = request.cluster_certificate
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.issuer_certificate):
            body['IssuerCertificate'] = request.issuer_certificate
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigClusterCertificate',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigClusterCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_cluster_certificate_with_options_async(
        self,
        request: hsm_20231113_models.ConfigClusterCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigClusterCertificateResponse:
        """
        @summary Configures a certificate for a cluster of hardware security modules (HSMs) outside the Chinese mainland.
        
        @description For more information about how to create a self-signed certificate and a cluster certificate on an Elastic Compute Service (ECS) instance, see [Create a NIST FIPS-validated GVSM cluster](https://help.aliyun.com/document_detail/293585.html).
        
        @param request: ConfigClusterCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigClusterCertificateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_certificate):
            body['ClusterCertificate'] = request.cluster_certificate
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.issuer_certificate):
            body['IssuerCertificate'] = request.issuer_certificate
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigClusterCertificate',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigClusterCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_cluster_certificate(
        self,
        request: hsm_20231113_models.ConfigClusterCertificateRequest,
    ) -> hsm_20231113_models.ConfigClusterCertificateResponse:
        """
        @summary Configures a certificate for a cluster of hardware security modules (HSMs) outside the Chinese mainland.
        
        @description For more information about how to create a self-signed certificate and a cluster certificate on an Elastic Compute Service (ECS) instance, see [Create a NIST FIPS-validated GVSM cluster](https://help.aliyun.com/document_detail/293585.html).
        
        @param request: ConfigClusterCertificateRequest
        @return: ConfigClusterCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_cluster_certificate_with_options(request, runtime)

    async def config_cluster_certificate_async(
        self,
        request: hsm_20231113_models.ConfigClusterCertificateRequest,
    ) -> hsm_20231113_models.ConfigClusterCertificateResponse:
        """
        @summary Configures a certificate for a cluster of hardware security modules (HSMs) outside the Chinese mainland.
        
        @description For more information about how to create a self-signed certificate and a cluster certificate on an Elastic Compute Service (ECS) instance, see [Create a NIST FIPS-validated GVSM cluster](https://help.aliyun.com/document_detail/293585.html).
        
        @param request: ConfigClusterCertificateRequest
        @return: ConfigClusterCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_cluster_certificate_with_options_async(request, runtime)

    def config_cluster_name_with_options(
        self,
        request: hsm_20231113_models.ConfigClusterNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigClusterNameResponse:
        """
        @summary Changes the name of a cluster.
        
        @param request: ConfigClusterNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigClusterNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigClusterName',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigClusterNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_cluster_name_with_options_async(
        self,
        request: hsm_20231113_models.ConfigClusterNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigClusterNameResponse:
        """
        @summary Changes the name of a cluster.
        
        @param request: ConfigClusterNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigClusterNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigClusterName',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigClusterNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_cluster_name(
        self,
        request: hsm_20231113_models.ConfigClusterNameRequest,
    ) -> hsm_20231113_models.ConfigClusterNameResponse:
        """
        @summary Changes the name of a cluster.
        
        @param request: ConfigClusterNameRequest
        @return: ConfigClusterNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_cluster_name_with_options(request, runtime)

    async def config_cluster_name_async(
        self,
        request: hsm_20231113_models.ConfigClusterNameRequest,
    ) -> hsm_20231113_models.ConfigClusterNameResponse:
        """
        @summary Changes the name of a cluster.
        
        @param request: ConfigClusterNameRequest
        @return: ConfigClusterNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_cluster_name_with_options_async(request, runtime)

    def config_cluster_subnet_with_options(
        self,
        tmp_req: hsm_20231113_models.ConfigClusterSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigClusterSubnetResponse:
        """
        @summary Modifies a list of vSwitches that are associated with a hardware security module (HSM) cluster.
        
        @description You can call the operation to configure all vSwitches that are associated with a HSM cluster. You can only add new vSwitches. You cannot delete vSwitches.
        
        @param tmp_req: ConfigClusterSubnetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigClusterSubnetResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hsm_20231113_models.ConfigClusterSubnetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.v_switch_ids):
            request.v_switch_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.v_switch_ids, 'VSwitchIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_ids_shrink):
            body['VSwitchIds'] = request.v_switch_ids_shrink
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigClusterSubnet',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigClusterSubnetResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_cluster_subnet_with_options_async(
        self,
        tmp_req: hsm_20231113_models.ConfigClusterSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigClusterSubnetResponse:
        """
        @summary Modifies a list of vSwitches that are associated with a hardware security module (HSM) cluster.
        
        @description You can call the operation to configure all vSwitches that are associated with a HSM cluster. You can only add new vSwitches. You cannot delete vSwitches.
        
        @param tmp_req: ConfigClusterSubnetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigClusterSubnetResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hsm_20231113_models.ConfigClusterSubnetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.v_switch_ids):
            request.v_switch_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.v_switch_ids, 'VSwitchIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_ids_shrink):
            body['VSwitchIds'] = request.v_switch_ids_shrink
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigClusterSubnet',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigClusterSubnetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_cluster_subnet(
        self,
        request: hsm_20231113_models.ConfigClusterSubnetRequest,
    ) -> hsm_20231113_models.ConfigClusterSubnetResponse:
        """
        @summary Modifies a list of vSwitches that are associated with a hardware security module (HSM) cluster.
        
        @description You can call the operation to configure all vSwitches that are associated with a HSM cluster. You can only add new vSwitches. You cannot delete vSwitches.
        
        @param request: ConfigClusterSubnetRequest
        @return: ConfigClusterSubnetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_cluster_subnet_with_options(request, runtime)

    async def config_cluster_subnet_async(
        self,
        request: hsm_20231113_models.ConfigClusterSubnetRequest,
    ) -> hsm_20231113_models.ConfigClusterSubnetResponse:
        """
        @summary Modifies a list of vSwitches that are associated with a hardware security module (HSM) cluster.
        
        @description You can call the operation to configure all vSwitches that are associated with a HSM cluster. You can only add new vSwitches. You cannot delete vSwitches.
        
        @param request: ConfigClusterSubnetRequest
        @return: ConfigClusterSubnetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_cluster_subnet_with_options_async(request, runtime)

    def config_cluster_whitelist_with_options(
        self,
        request: hsm_20231113_models.ConfigClusterWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigClusterWhitelistResponse:
        """
        @summary Modifies the IP address whitelist of a cluster.
        
        @description The IP address whitelist of a cluster has a higher priority than the IP address whitelist of a hardware security module (HSM) in the cluster. In cluster mode, we recommend that you create an IP address whitelist for your cluster. You do not need to create an IP address for the HSM in the cluster.
        
        @param request: ConfigClusterWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigClusterWhitelistResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.whitelist):
            body['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigClusterWhitelist',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigClusterWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_cluster_whitelist_with_options_async(
        self,
        request: hsm_20231113_models.ConfigClusterWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigClusterWhitelistResponse:
        """
        @summary Modifies the IP address whitelist of a cluster.
        
        @description The IP address whitelist of a cluster has a higher priority than the IP address whitelist of a hardware security module (HSM) in the cluster. In cluster mode, we recommend that you create an IP address whitelist for your cluster. You do not need to create an IP address for the HSM in the cluster.
        
        @param request: ConfigClusterWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigClusterWhitelistResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.whitelist):
            body['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigClusterWhitelist',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigClusterWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_cluster_whitelist(
        self,
        request: hsm_20231113_models.ConfigClusterWhitelistRequest,
    ) -> hsm_20231113_models.ConfigClusterWhitelistResponse:
        """
        @summary Modifies the IP address whitelist of a cluster.
        
        @description The IP address whitelist of a cluster has a higher priority than the IP address whitelist of a hardware security module (HSM) in the cluster. In cluster mode, we recommend that you create an IP address whitelist for your cluster. You do not need to create an IP address for the HSM in the cluster.
        
        @param request: ConfigClusterWhitelistRequest
        @return: ConfigClusterWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_cluster_whitelist_with_options(request, runtime)

    async def config_cluster_whitelist_async(
        self,
        request: hsm_20231113_models.ConfigClusterWhitelistRequest,
    ) -> hsm_20231113_models.ConfigClusterWhitelistResponse:
        """
        @summary Modifies the IP address whitelist of a cluster.
        
        @description The IP address whitelist of a cluster has a higher priority than the IP address whitelist of a hardware security module (HSM) in the cluster. In cluster mode, we recommend that you create an IP address whitelist for your cluster. You do not need to create an IP address for the HSM in the cluster.
        
        @param request: ConfigClusterWhitelistRequest
        @return: ConfigClusterWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_cluster_whitelist_with_options_async(request, runtime)

    def config_image_remark_with_options(
        self,
        request: hsm_20231113_models.ConfigImageRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigImageRemarkResponse:
        """
        @summary Modifies the description of an image.
        
        @param request: ConfigImageRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigImageRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigImageRemark',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigImageRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_image_remark_with_options_async(
        self,
        request: hsm_20231113_models.ConfigImageRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigImageRemarkResponse:
        """
        @summary Modifies the description of an image.
        
        @param request: ConfigImageRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigImageRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigImageRemark',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigImageRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_image_remark(
        self,
        request: hsm_20231113_models.ConfigImageRemarkRequest,
    ) -> hsm_20231113_models.ConfigImageRemarkResponse:
        """
        @summary Modifies the description of an image.
        
        @param request: ConfigImageRemarkRequest
        @return: ConfigImageRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_image_remark_with_options(request, runtime)

    async def config_image_remark_async(
        self,
        request: hsm_20231113_models.ConfigImageRemarkRequest,
    ) -> hsm_20231113_models.ConfigImageRemarkResponse:
        """
        @summary Modifies the description of an image.
        
        @param request: ConfigImageRemarkRequest
        @return: ConfigImageRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_image_remark_with_options_async(request, runtime)

    def config_instance_ip_address_with_options(
        self,
        request: hsm_20231113_models.ConfigInstanceIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigInstanceIpAddressResponse:
        """
        @summary Modifies the virtual private cloud (VPC) endpoint of a hardware security module (HSM).
        
        @description After you add an HSM to a cluster, you cannot modify the VPC endpoint of the HSM.
        
        @param request: ConfigInstanceIpAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigInstanceIpAddressResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigInstanceIpAddress',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigInstanceIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_instance_ip_address_with_options_async(
        self,
        request: hsm_20231113_models.ConfigInstanceIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigInstanceIpAddressResponse:
        """
        @summary Modifies the virtual private cloud (VPC) endpoint of a hardware security module (HSM).
        
        @description After you add an HSM to a cluster, you cannot modify the VPC endpoint of the HSM.
        
        @param request: ConfigInstanceIpAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigInstanceIpAddressResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigInstanceIpAddress',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigInstanceIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_instance_ip_address(
        self,
        request: hsm_20231113_models.ConfigInstanceIpAddressRequest,
    ) -> hsm_20231113_models.ConfigInstanceIpAddressResponse:
        """
        @summary Modifies the virtual private cloud (VPC) endpoint of a hardware security module (HSM).
        
        @description After you add an HSM to a cluster, you cannot modify the VPC endpoint of the HSM.
        
        @param request: ConfigInstanceIpAddressRequest
        @return: ConfigInstanceIpAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_instance_ip_address_with_options(request, runtime)

    async def config_instance_ip_address_async(
        self,
        request: hsm_20231113_models.ConfigInstanceIpAddressRequest,
    ) -> hsm_20231113_models.ConfigInstanceIpAddressResponse:
        """
        @summary Modifies the virtual private cloud (VPC) endpoint of a hardware security module (HSM).
        
        @description After you add an HSM to a cluster, you cannot modify the VPC endpoint of the HSM.
        
        @param request: ConfigInstanceIpAddressRequest
        @return: ConfigInstanceIpAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_instance_ip_address_with_options_async(request, runtime)

    def config_instance_remark_with_options(
        self,
        request: hsm_20231113_models.ConfigInstanceRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigInstanceRemarkResponse:
        """
        @summary Modifies the description of a hardware security module (HSM).
        
        @param request: ConfigInstanceRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigInstanceRemarkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigInstanceRemark',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigInstanceRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_instance_remark_with_options_async(
        self,
        request: hsm_20231113_models.ConfigInstanceRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigInstanceRemarkResponse:
        """
        @summary Modifies the description of a hardware security module (HSM).
        
        @param request: ConfigInstanceRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigInstanceRemarkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigInstanceRemark',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigInstanceRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_instance_remark(
        self,
        request: hsm_20231113_models.ConfigInstanceRemarkRequest,
    ) -> hsm_20231113_models.ConfigInstanceRemarkResponse:
        """
        @summary Modifies the description of a hardware security module (HSM).
        
        @param request: ConfigInstanceRemarkRequest
        @return: ConfigInstanceRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_instance_remark_with_options(request, runtime)

    async def config_instance_remark_async(
        self,
        request: hsm_20231113_models.ConfigInstanceRemarkRequest,
    ) -> hsm_20231113_models.ConfigInstanceRemarkResponse:
        """
        @summary Modifies the description of a hardware security module (HSM).
        
        @param request: ConfigInstanceRemarkRequest
        @return: ConfigInstanceRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_instance_remark_with_options_async(request, runtime)

    def config_instance_whitelist_with_options(
        self,
        request: hsm_20231113_models.ConfigInstanceWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigInstanceWhitelistResponse:
        """
        @summary Modifies the IP address whitelist of a hardware security module (HSM).
        
        @description You can configure the IP address whitelist for HSMs that are not added to a cluster and are in the ACTIVE state.
        
        @param request: ConfigInstanceWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigInstanceWhitelistResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.whitelist):
            body['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigInstanceWhitelist',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigInstanceWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_instance_whitelist_with_options_async(
        self,
        request: hsm_20231113_models.ConfigInstanceWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigInstanceWhitelistResponse:
        """
        @summary Modifies the IP address whitelist of a hardware security module (HSM).
        
        @description You can configure the IP address whitelist for HSMs that are not added to a cluster and are in the ACTIVE state.
        
        @param request: ConfigInstanceWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigInstanceWhitelistResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.whitelist):
            body['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigInstanceWhitelist',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigInstanceWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_instance_whitelist(
        self,
        request: hsm_20231113_models.ConfigInstanceWhitelistRequest,
    ) -> hsm_20231113_models.ConfigInstanceWhitelistResponse:
        """
        @summary Modifies the IP address whitelist of a hardware security module (HSM).
        
        @description You can configure the IP address whitelist for HSMs that are not added to a cluster and are in the ACTIVE state.
        
        @param request: ConfigInstanceWhitelistRequest
        @return: ConfigInstanceWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_instance_whitelist_with_options(request, runtime)

    async def config_instance_whitelist_async(
        self,
        request: hsm_20231113_models.ConfigInstanceWhitelistRequest,
    ) -> hsm_20231113_models.ConfigInstanceWhitelistResponse:
        """
        @summary Modifies the IP address whitelist of a hardware security module (HSM).
        
        @description You can configure the IP address whitelist for HSMs that are not added to a cluster and are in the ACTIVE state.
        
        @param request: ConfigInstanceWhitelistRequest
        @return: ConfigInstanceWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_instance_whitelist_with_options_async(request, runtime)

    def copy_image_with_options(
        self,
        request: hsm_20231113_models.CopyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.CopyImageResponse:
        """
        @summary Copies an image to another region.
        
        @description This operation requires that the destination region does not have the same image. This operation is available only for hardware security modules (HSMs) outside the Chinese mainland.
        
        @param request: CopyImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_uid):
            body['ImageUid'] = request.image_uid
        if not UtilClient.is_unset(request.target_region_id):
            body['TargetRegionId'] = request.target_region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CopyImage',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.CopyImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_image_with_options_async(
        self,
        request: hsm_20231113_models.CopyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.CopyImageResponse:
        """
        @summary Copies an image to another region.
        
        @description This operation requires that the destination region does not have the same image. This operation is available only for hardware security modules (HSMs) outside the Chinese mainland.
        
        @param request: CopyImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_uid):
            body['ImageUid'] = request.image_uid
        if not UtilClient.is_unset(request.target_region_id):
            body['TargetRegionId'] = request.target_region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CopyImage',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.CopyImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_image(
        self,
        request: hsm_20231113_models.CopyImageRequest,
    ) -> hsm_20231113_models.CopyImageResponse:
        """
        @summary Copies an image to another region.
        
        @description This operation requires that the destination region does not have the same image. This operation is available only for hardware security modules (HSMs) outside the Chinese mainland.
        
        @param request: CopyImageRequest
        @return: CopyImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.copy_image_with_options(request, runtime)

    async def copy_image_async(
        self,
        request: hsm_20231113_models.CopyImageRequest,
    ) -> hsm_20231113_models.CopyImageResponse:
        """
        @summary Copies an image to another region.
        
        @description This operation requires that the destination region does not have the same image. This operation is available only for hardware security modules (HSMs) outside the Chinese mainland.
        
        @param request: CopyImageRequest
        @return: CopyImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.copy_image_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        request: hsm_20231113_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.CreateClusterResponse:
        """
        @summary Creates a cluster by specifying a hardware security module (HSM) as the master HSM.
        
        @description The master HSM that you specify to create a cluster must be in the ACTIVE state.
        
        @param request: CreateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.master_instance_id):
            body['MasterInstanceId'] = request.master_instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: hsm_20231113_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.CreateClusterResponse:
        """
        @summary Creates a cluster by specifying a hardware security module (HSM) as the master HSM.
        
        @description The master HSM that you specify to create a cluster must be in the ACTIVE state.
        
        @param request: CreateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.master_instance_id):
            body['MasterInstanceId'] = request.master_instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: hsm_20231113_models.CreateClusterRequest,
    ) -> hsm_20231113_models.CreateClusterResponse:
        """
        @summary Creates a cluster by specifying a hardware security module (HSM) as the master HSM.
        
        @description The master HSM that you specify to create a cluster must be in the ACTIVE state.
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: hsm_20231113_models.CreateClusterRequest,
    ) -> hsm_20231113_models.CreateClusterResponse:
        """
        @summary Creates a cluster by specifying a hardware security module (HSM) as the master HSM.
        
        @description The master HSM that you specify to create a cluster must be in the ACTIVE state.
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: hsm_20231113_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.DeleteClusterResponse:
        """
        @summary Deletes a hardware security module (HSM) cluster.
        
        @description You can delete an HSM only if the cluster does not contain HSMs.
        
        @param request: DeleteClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: hsm_20231113_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.DeleteClusterResponse:
        """
        @summary Deletes a hardware security module (HSM) cluster.
        
        @description You can delete an HSM only if the cluster does not contain HSMs.
        
        @param request: DeleteClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.DeleteClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster(
        self,
        request: hsm_20231113_models.DeleteClusterRequest,
    ) -> hsm_20231113_models.DeleteClusterResponse:
        """
        @summary Deletes a hardware security module (HSM) cluster.
        
        @description You can delete an HSM only if the cluster does not contain HSMs.
        
        @param request: DeleteClusterRequest
        @return: DeleteClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: hsm_20231113_models.DeleteClusterRequest,
    ) -> hsm_20231113_models.DeleteClusterResponse:
        """
        @summary Deletes a hardware security module (HSM) cluster.
        
        @description You can delete an HSM only if the cluster does not contain HSMs.
        
        @param request: DeleteClusterRequest
        @return: DeleteClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: hsm_20231113_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.DescribeRegionsResponse:
        """
        @summary Queries the regions that are supported by Cloud Hardware Security Module.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: hsm_20231113_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.DescribeRegionsResponse:
        """
        @summary Queries the regions that are supported by Cloud Hardware Security Module.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: hsm_20231113_models.DescribeRegionsRequest,
    ) -> hsm_20231113_models.DescribeRegionsResponse:
        """
        @summary Queries the regions that are supported by Cloud Hardware Security Module.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: hsm_20231113_models.DescribeRegionsRequest,
    ) -> hsm_20231113_models.DescribeRegionsResponse:
        """
        @summary Queries the regions that are supported by Cloud Hardware Security Module.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def enable_backup_with_options(
        self,
        request: hsm_20231113_models.EnableBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.EnableBackupResponse:
        """
        @summary Binds a backup to a specified hardware security module (HSM).
        
        @description This operation is available only for backups in the Chinese mainland.
        
        @param request: EnableBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableBackup',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.EnableBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_backup_with_options_async(
        self,
        request: hsm_20231113_models.EnableBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.EnableBackupResponse:
        """
        @summary Binds a backup to a specified hardware security module (HSM).
        
        @description This operation is available only for backups in the Chinese mainland.
        
        @param request: EnableBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableBackup',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.EnableBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_backup(
        self,
        request: hsm_20231113_models.EnableBackupRequest,
    ) -> hsm_20231113_models.EnableBackupResponse:
        """
        @summary Binds a backup to a specified hardware security module (HSM).
        
        @description This operation is available only for backups in the Chinese mainland.
        
        @param request: EnableBackupRequest
        @return: EnableBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_backup_with_options(request, runtime)

    async def enable_backup_async(
        self,
        request: hsm_20231113_models.EnableBackupRequest,
    ) -> hsm_20231113_models.EnableBackupResponse:
        """
        @summary Binds a backup to a specified hardware security module (HSM).
        
        @description This operation is available only for backups in the Chinese mainland.
        
        @param request: EnableBackupRequest
        @return: EnableBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_backup_with_options_async(request, runtime)

    def export_image_with_options(
        self,
        request: hsm_20231113_models.ExportImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ExportImageResponse:
        """
        @summary Exports the image for a specified hardware security module (HSM).
        
        @param request: ExportImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportImage',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ExportImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_image_with_options_async(
        self,
        request: hsm_20231113_models.ExportImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ExportImageResponse:
        """
        @summary Exports the image for a specified hardware security module (HSM).
        
        @param request: ExportImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportImage',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ExportImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_image(
        self,
        request: hsm_20231113_models.ExportImageRequest,
    ) -> hsm_20231113_models.ExportImageResponse:
        """
        @summary Exports the image for a specified hardware security module (HSM).
        
        @param request: ExportImageRequest
        @return: ExportImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_image_with_options(request, runtime)

    async def export_image_async(
        self,
        request: hsm_20231113_models.ExportImageRequest,
    ) -> hsm_20231113_models.ExportImageResponse:
        """
        @summary Exports the image for a specified hardware security module (HSM).
        
        @param request: ExportImageRequest
        @return: ExportImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_image_with_options_async(request, runtime)

    def get_audit_log_status_with_options(
        self,
        request: hsm_20231113_models.GetAuditLogStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.GetAuditLogStatusResponse:
        """
        @summary Queries the status of the audit log feature in the current region.
        
        @param request: GetAuditLogStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAuditLogStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.get_oss_bucket):
            query['GetOssBucket'] = request.get_oss_bucket
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuditLogStatus',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.GetAuditLogStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_audit_log_status_with_options_async(
        self,
        request: hsm_20231113_models.GetAuditLogStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.GetAuditLogStatusResponse:
        """
        @summary Queries the status of the audit log feature in the current region.
        
        @param request: GetAuditLogStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAuditLogStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.get_oss_bucket):
            query['GetOssBucket'] = request.get_oss_bucket
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuditLogStatus',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.GetAuditLogStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_audit_log_status(
        self,
        request: hsm_20231113_models.GetAuditLogStatusRequest,
    ) -> hsm_20231113_models.GetAuditLogStatusResponse:
        """
        @summary Queries the status of the audit log feature in the current region.
        
        @param request: GetAuditLogStatusRequest
        @return: GetAuditLogStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_audit_log_status_with_options(request, runtime)

    async def get_audit_log_status_async(
        self,
        request: hsm_20231113_models.GetAuditLogStatusRequest,
    ) -> hsm_20231113_models.GetAuditLogStatusResponse:
        """
        @summary Queries the status of the audit log feature in the current region.
        
        @param request: GetAuditLogStatusRequest
        @return: GetAuditLogStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_audit_log_status_with_options_async(request, runtime)

    def get_backup_with_options(
        self,
        request: hsm_20231113_models.GetBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.GetBackupResponse:
        """
        @summary Queries the information about a specified backup.
        
        @param request: GetBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBackup',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.GetBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_backup_with_options_async(
        self,
        request: hsm_20231113_models.GetBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.GetBackupResponse:
        """
        @summary Queries the information about a specified backup.
        
        @param request: GetBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBackup',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.GetBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_backup(
        self,
        request: hsm_20231113_models.GetBackupRequest,
    ) -> hsm_20231113_models.GetBackupResponse:
        """
        @summary Queries the information about a specified backup.
        
        @param request: GetBackupRequest
        @return: GetBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_backup_with_options(request, runtime)

    async def get_backup_async(
        self,
        request: hsm_20231113_models.GetBackupRequest,
    ) -> hsm_20231113_models.GetBackupResponse:
        """
        @summary Queries the information about a specified backup.
        
        @param request: GetBackupRequest
        @return: GetBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_backup_with_options_async(request, runtime)

    def get_cluster_with_options(
        self,
        request: hsm_20231113_models.GetClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.GetClusterResponse:
        """
        @summary Queries information about a specified cluster.
        
        @param request: GetClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCluster',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.GetClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_with_options_async(
        self,
        request: hsm_20231113_models.GetClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.GetClusterResponse:
        """
        @summary Queries information about a specified cluster.
        
        @param request: GetClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCluster',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.GetClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster(
        self,
        request: hsm_20231113_models.GetClusterRequest,
    ) -> hsm_20231113_models.GetClusterResponse:
        """
        @summary Queries information about a specified cluster.
        
        @param request: GetClusterRequest
        @return: GetClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_with_options(request, runtime)

    async def get_cluster_async(
        self,
        request: hsm_20231113_models.GetClusterRequest,
    ) -> hsm_20231113_models.GetClusterResponse:
        """
        @summary Queries information about a specified cluster.
        
        @param request: GetClusterRequest
        @return: GetClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_cluster_with_options_async(request, runtime)

    def get_image_with_options(
        self,
        request: hsm_20231113_models.GetImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.GetImageResponse:
        """
        @summary Queries information about an image.
        
        @param request: GetImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImage',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.GetImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_with_options_async(
        self,
        request: hsm_20231113_models.GetImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.GetImageResponse:
        """
        @summary Queries information about an image.
        
        @param request: GetImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImage',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.GetImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image(
        self,
        request: hsm_20231113_models.GetImageRequest,
    ) -> hsm_20231113_models.GetImageResponse:
        """
        @summary Queries information about an image.
        
        @param request: GetImageRequest
        @return: GetImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_image_with_options(request, runtime)

    async def get_image_async(
        self,
        request: hsm_20231113_models.GetImageRequest,
    ) -> hsm_20231113_models.GetImageResponse:
        """
        @summary Queries information about an image.
        
        @param request: GetImageRequest
        @return: GetImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_image_with_options_async(request, runtime)

    def get_instance_with_options(
        self,
        request: hsm_20231113_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.GetInstanceResponse:
        """
        @summary Queries information about a specified hardware security module (HSM).
        
        @param request: GetInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: hsm_20231113_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.GetInstanceResponse:
        """
        @summary Queries information about a specified hardware security module (HSM).
        
        @param request: GetInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        request: hsm_20231113_models.GetInstanceRequest,
    ) -> hsm_20231113_models.GetInstanceResponse:
        """
        @summary Queries information about a specified hardware security module (HSM).
        
        @param request: GetInstanceRequest
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    async def get_instance_async(
        self,
        request: hsm_20231113_models.GetInstanceRequest,
    ) -> hsm_20231113_models.GetInstanceResponse:
        """
        @summary Queries information about a specified hardware security module (HSM).
        
        @param request: GetInstanceRequest
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_with_options_async(request, runtime)

    def get_job_with_options(
        self,
        request: hsm_20231113_models.GetJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.GetJobResponse:
        """
        @summary Queries the details of an asynchronous task.
        
        @param request: GetJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_with_options_async(
        self,
        request: hsm_20231113_models.GetJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.GetJobResponse:
        """
        @summary Queries the details of an asynchronous task.
        
        @param request: GetJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.GetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job(
        self,
        request: hsm_20231113_models.GetJobRequest,
    ) -> hsm_20231113_models.GetJobResponse:
        """
        @summary Queries the details of an asynchronous task.
        
        @param request: GetJobRequest
        @return: GetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_job_with_options(request, runtime)

    async def get_job_async(
        self,
        request: hsm_20231113_models.GetJobRequest,
    ) -> hsm_20231113_models.GetJobResponse:
        """
        @summary Queries the details of an asynchronous task.
        
        @param request: GetJobRequest
        @return: GetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_job_with_options_async(request, runtime)

    def initialize_audit_log_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.InitializeAuditLogResponse:
        """
        @summary Authorizes Cloud Hardware Security Module to deliver logs.
        
        @param request: InitializeAuditLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitializeAuditLogResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='InitializeAuditLog',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.InitializeAuditLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def initialize_audit_log_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.InitializeAuditLogResponse:
        """
        @summary Authorizes Cloud Hardware Security Module to deliver logs.
        
        @param request: InitializeAuditLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitializeAuditLogResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='InitializeAuditLog',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.InitializeAuditLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initialize_audit_log(self) -> hsm_20231113_models.InitializeAuditLogResponse:
        """
        @summary Authorizes Cloud Hardware Security Module to deliver logs.
        
        @return: InitializeAuditLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.initialize_audit_log_with_options(runtime)

    async def initialize_audit_log_async(self) -> hsm_20231113_models.InitializeAuditLogResponse:
        """
        @summary Authorizes Cloud Hardware Security Module to deliver logs.
        
        @return: InitializeAuditLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.initialize_audit_log_with_options_async(runtime)

    def initialize_cluster_with_options(
        self,
        request: hsm_20231113_models.InitializeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.InitializeClusterResponse:
        """
        @summary Initializes a cluster.
        
        @description    The cluster is not initialized, but the master hardware security module (HSM) of the cluster is initialized.
        Two or more vSwitches are configured for the cluster.
        
        @param request: InitializeClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitializeClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitializeCluster',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.InitializeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def initialize_cluster_with_options_async(
        self,
        request: hsm_20231113_models.InitializeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.InitializeClusterResponse:
        """
        @summary Initializes a cluster.
        
        @description    The cluster is not initialized, but the master hardware security module (HSM) of the cluster is initialized.
        Two or more vSwitches are configured for the cluster.
        
        @param request: InitializeClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitializeClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitializeCluster',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.InitializeClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initialize_cluster(
        self,
        request: hsm_20231113_models.InitializeClusterRequest,
    ) -> hsm_20231113_models.InitializeClusterResponse:
        """
        @summary Initializes a cluster.
        
        @description    The cluster is not initialized, but the master hardware security module (HSM) of the cluster is initialized.
        Two or more vSwitches are configured for the cluster.
        
        @param request: InitializeClusterRequest
        @return: InitializeClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.initialize_cluster_with_options(request, runtime)

    async def initialize_cluster_async(
        self,
        request: hsm_20231113_models.InitializeClusterRequest,
    ) -> hsm_20231113_models.InitializeClusterResponse:
        """
        @summary Initializes a cluster.
        
        @description    The cluster is not initialized, but the master hardware security module (HSM) of the cluster is initialized.
        Two or more vSwitches are configured for the cluster.
        
        @param request: InitializeClusterRequest
        @return: InitializeClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.initialize_cluster_with_options_async(request, runtime)

    def join_cluster_with_options(
        self,
        request: hsm_20231113_models.JoinClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.JoinClusterResponse:
        """
        @summary Adds a hardware security module (HSM) to the current cluster.
        
        @description    You can add the HSM to only the cluster that is in the INITIALIZED state.
        The HSM that you want to add to the cluster is enabled or disabled and is not initialized.
        
        @param request: JoinClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: JoinClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='JoinCluster',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.JoinClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def join_cluster_with_options_async(
        self,
        request: hsm_20231113_models.JoinClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.JoinClusterResponse:
        """
        @summary Adds a hardware security module (HSM) to the current cluster.
        
        @description    You can add the HSM to only the cluster that is in the INITIALIZED state.
        The HSM that you want to add to the cluster is enabled or disabled and is not initialized.
        
        @param request: JoinClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: JoinClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='JoinCluster',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.JoinClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def join_cluster(
        self,
        request: hsm_20231113_models.JoinClusterRequest,
    ) -> hsm_20231113_models.JoinClusterResponse:
        """
        @summary Adds a hardware security module (HSM) to the current cluster.
        
        @description    You can add the HSM to only the cluster that is in the INITIALIZED state.
        The HSM that you want to add to the cluster is enabled or disabled and is not initialized.
        
        @param request: JoinClusterRequest
        @return: JoinClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.join_cluster_with_options(request, runtime)

    async def join_cluster_async(
        self,
        request: hsm_20231113_models.JoinClusterRequest,
    ) -> hsm_20231113_models.JoinClusterResponse:
        """
        @summary Adds a hardware security module (HSM) to the current cluster.
        
        @description    You can add the HSM to only the cluster that is in the INITIALIZED state.
        The HSM that you want to add to the cluster is enabled or disabled and is not initialized.
        
        @param request: JoinClusterRequest
        @return: JoinClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.join_cluster_with_options_async(request, runtime)

    def leave_cluster_with_options(
        self,
        request: hsm_20231113_models.LeaveClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.LeaveClusterResponse:
        """
        @summary Removes a hardware security module (HSM) from the current cluster.
        
        @description    If non-master HSMs exist in a cluster, the master HSM cannot be removed from the cluster.
        After the master HSM is removed from a cluster, the cluster enters the TO_DELETE state and cannot be restored to the available state. Proceed with caution.
        
        @param request: LeaveClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LeaveClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LeaveCluster',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.LeaveClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def leave_cluster_with_options_async(
        self,
        request: hsm_20231113_models.LeaveClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.LeaveClusterResponse:
        """
        @summary Removes a hardware security module (HSM) from the current cluster.
        
        @description    If non-master HSMs exist in a cluster, the master HSM cannot be removed from the cluster.
        After the master HSM is removed from a cluster, the cluster enters the TO_DELETE state and cannot be restored to the available state. Proceed with caution.
        
        @param request: LeaveClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LeaveClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LeaveCluster',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.LeaveClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def leave_cluster(
        self,
        request: hsm_20231113_models.LeaveClusterRequest,
    ) -> hsm_20231113_models.LeaveClusterResponse:
        """
        @summary Removes a hardware security module (HSM) from the current cluster.
        
        @description    If non-master HSMs exist in a cluster, the master HSM cannot be removed from the cluster.
        After the master HSM is removed from a cluster, the cluster enters the TO_DELETE state and cannot be restored to the available state. Proceed with caution.
        
        @param request: LeaveClusterRequest
        @return: LeaveClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.leave_cluster_with_options(request, runtime)

    async def leave_cluster_async(
        self,
        request: hsm_20231113_models.LeaveClusterRequest,
    ) -> hsm_20231113_models.LeaveClusterResponse:
        """
        @summary Removes a hardware security module (HSM) from the current cluster.
        
        @description    If non-master HSMs exist in a cluster, the master HSM cannot be removed from the cluster.
        After the master HSM is removed from a cluster, the cluster enters the TO_DELETE state and cannot be restored to the available state. Proceed with caution.
        
        @param request: LeaveClusterRequest
        @return: LeaveClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.leave_cluster_with_options_async(request, runtime)

    def list_backups_with_options(
        self,
        request: hsm_20231113_models.ListBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ListBackupsResponse:
        """
        @summary Queries the backups that meet the query conditions.
        
        @param request: ListBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBackups',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ListBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_backups_with_options_async(
        self,
        request: hsm_20231113_models.ListBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ListBackupsResponse:
        """
        @summary Queries the backups that meet the query conditions.
        
        @param request: ListBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBackups',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ListBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_backups(
        self,
        request: hsm_20231113_models.ListBackupsRequest,
    ) -> hsm_20231113_models.ListBackupsResponse:
        """
        @summary Queries the backups that meet the query conditions.
        
        @param request: ListBackupsRequest
        @return: ListBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_backups_with_options(request, runtime)

    async def list_backups_async(
        self,
        request: hsm_20231113_models.ListBackupsRequest,
    ) -> hsm_20231113_models.ListBackupsResponse:
        """
        @summary Queries the backups that meet the query conditions.
        
        @param request: ListBackupsRequest
        @return: ListBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_backups_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        request: hsm_20231113_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ListClustersResponse:
        """
        @summary Queries the clusters that meet the query conditions.
        
        @param request: ListClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClustersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: hsm_20231113_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ListClustersResponse:
        """
        @summary Queries the clusters that meet the query conditions.
        
        @param request: ListClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClustersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ListClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clusters(
        self,
        request: hsm_20231113_models.ListClustersRequest,
    ) -> hsm_20231113_models.ListClustersResponse:
        """
        @summary Queries the clusters that meet the query conditions.
        
        @param request: ListClustersRequest
        @return: ListClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    async def list_clusters_async(
        self,
        request: hsm_20231113_models.ListClustersRequest,
    ) -> hsm_20231113_models.ListClustersResponse:
        """
        @summary Queries the clusters that meet the query conditions.
        
        @param request: ListClustersRequest
        @return: ListClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_clusters_with_options_async(request, runtime)

    def list_images_with_options(
        self,
        request: hsm_20231113_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ListImagesResponse:
        """
        @summary Queries the images that meet the specified conditions.
        
        @param request: ListImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_images_with_options_async(
        self,
        request: hsm_20231113_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ListImagesResponse:
        """
        @summary Queries the images that meet the specified conditions.
        
        @param request: ListImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ListImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_images(
        self,
        request: hsm_20231113_models.ListImagesRequest,
    ) -> hsm_20231113_models.ListImagesResponse:
        """
        @summary Queries the images that meet the specified conditions.
        
        @param request: ListImagesRequest
        @return: ListImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_images_with_options(request, runtime)

    async def list_images_async(
        self,
        request: hsm_20231113_models.ListImagesRequest,
    ) -> hsm_20231113_models.ListImagesResponse:
        """
        @summary Queries the images that meet the specified conditions.
        
        @param request: ListImagesRequest
        @return: ListImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_images_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: hsm_20231113_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ListInstancesResponse:
        """
        @summary Queries the hardware security modules (HSMs) that meet the query conditions.
        
        @param request: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tenant_isolation_type):
            body['TenantIsolationType'] = request.tenant_isolation_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: hsm_20231113_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ListInstancesResponse:
        """
        @summary Queries the hardware security modules (HSMs) that meet the query conditions.
        
        @param request: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tenant_isolation_type):
            body['TenantIsolationType'] = request.tenant_isolation_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: hsm_20231113_models.ListInstancesRequest,
    ) -> hsm_20231113_models.ListInstancesResponse:
        """
        @summary Queries the hardware security modules (HSMs) that meet the query conditions.
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: hsm_20231113_models.ListInstancesRequest,
    ) -> hsm_20231113_models.ListInstancesResponse:
        """
        @summary Queries the hardware security modules (HSMs) that meet the query conditions.
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: hsm_20231113_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.MoveResourceGroupResponse:
        """
        @summary Moves a resource to a new resource group.
        
        @param request: MoveResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceGroupResponse
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: hsm_20231113_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.MoveResourceGroupResponse:
        """
        @summary Moves a resource to a new resource group.
        
        @param request: MoveResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceGroupResponse
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: hsm_20231113_models.MoveResourceGroupRequest,
    ) -> hsm_20231113_models.MoveResourceGroupResponse:
        """
        @summary Moves a resource to a new resource group.
        
        @param request: MoveResourceGroupRequest
        @return: MoveResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: hsm_20231113_models.MoveResourceGroupRequest,
    ) -> hsm_20231113_models.MoveResourceGroupResponse:
        """
        @summary Moves a resource to a new resource group.
        
        @param request: MoveResourceGroupRequest
        @return: MoveResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def pause_instance_with_options(
        self,
        request: hsm_20231113_models.PauseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.PauseInstanceResponse:
        """
        @summary Disables a hardware security module (HSM).
        
        @description After you disable an HSM, the relevant service operations fail. Proceed with caution.
        
        @param request: PauseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PauseInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PauseInstance',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.PauseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_instance_with_options_async(
        self,
        request: hsm_20231113_models.PauseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.PauseInstanceResponse:
        """
        @summary Disables a hardware security module (HSM).
        
        @description After you disable an HSM, the relevant service operations fail. Proceed with caution.
        
        @param request: PauseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PauseInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PauseInstance',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.PauseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_instance(
        self,
        request: hsm_20231113_models.PauseInstanceRequest,
    ) -> hsm_20231113_models.PauseInstanceResponse:
        """
        @summary Disables a hardware security module (HSM).
        
        @description After you disable an HSM, the relevant service operations fail. Proceed with caution.
        
        @param request: PauseInstanceRequest
        @return: PauseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.pause_instance_with_options(request, runtime)

    async def pause_instance_async(
        self,
        request: hsm_20231113_models.PauseInstanceRequest,
    ) -> hsm_20231113_models.PauseInstanceResponse:
        """
        @summary Disables a hardware security module (HSM).
        
        @description After you disable an HSM, the relevant service operations fail. Proceed with caution.
        
        @param request: PauseInstanceRequest
        @return: PauseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.pause_instance_with_options_async(request, runtime)

    def quick_init_instance_with_options(
        self,
        request: hsm_20231113_models.QuickInitInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.QuickInitInstanceResponse:
        """
        @summary Initializes a hardware security module (HSM).
        
        @description This operation is supported only for general virtual security modules (GVSMs) in the Chinese mainland.
        
        @param request: QuickInitInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuickInitInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuickInitInstance',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.QuickInitInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def quick_init_instance_with_options_async(
        self,
        request: hsm_20231113_models.QuickInitInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.QuickInitInstanceResponse:
        """
        @summary Initializes a hardware security module (HSM).
        
        @description This operation is supported only for general virtual security modules (GVSMs) in the Chinese mainland.
        
        @param request: QuickInitInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuickInitInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuickInitInstance',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.QuickInitInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def quick_init_instance(
        self,
        request: hsm_20231113_models.QuickInitInstanceRequest,
    ) -> hsm_20231113_models.QuickInitInstanceResponse:
        """
        @summary Initializes a hardware security module (HSM).
        
        @description This operation is supported only for general virtual security modules (GVSMs) in the Chinese mainland.
        
        @param request: QuickInitInstanceRequest
        @return: QuickInitInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.quick_init_instance_with_options(request, runtime)

    async def quick_init_instance_async(
        self,
        request: hsm_20231113_models.QuickInitInstanceRequest,
    ) -> hsm_20231113_models.QuickInitInstanceResponse:
        """
        @summary Initializes a hardware security module (HSM).
        
        @description This operation is supported only for general virtual security modules (GVSMs) in the Chinese mainland.
        
        @param request: QuickInitInstanceRequest
        @return: QuickInitInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.quick_init_instance_with_options_async(request, runtime)

    def reset_backup_with_options(
        self,
        request: hsm_20231113_models.ResetBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ResetBackupResponse:
        """
        @summary Disassociates a backup from a hardware security module (HSM).
        
        @description This operation is available only for HSMs in the Chinese mainland.
        
        @param request: ResetBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetBackup',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ResetBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_backup_with_options_async(
        self,
        request: hsm_20231113_models.ResetBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ResetBackupResponse:
        """
        @summary Disassociates a backup from a hardware security module (HSM).
        
        @description This operation is available only for HSMs in the Chinese mainland.
        
        @param request: ResetBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetBackup',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ResetBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_backup(
        self,
        request: hsm_20231113_models.ResetBackupRequest,
    ) -> hsm_20231113_models.ResetBackupResponse:
        """
        @summary Disassociates a backup from a hardware security module (HSM).
        
        @description This operation is available only for HSMs in the Chinese mainland.
        
        @param request: ResetBackupRequest
        @return: ResetBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_backup_with_options(request, runtime)

    async def reset_backup_async(
        self,
        request: hsm_20231113_models.ResetBackupRequest,
    ) -> hsm_20231113_models.ResetBackupResponse:
        """
        @summary Disassociates a backup from a hardware security module (HSM).
        
        @description This operation is available only for HSMs in the Chinese mainland.
        
        @param request: ResetBackupRequest
        @return: ResetBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_backup_with_options_async(request, runtime)

    def reset_instance_with_options(
        self,
        request: hsm_20231113_models.ResetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ResetInstanceResponse:
        """
        @summary Resets a hardware security module (HSM).
        
        @description After an HSM is reset, all related data is deleted and cannot be recovered. Proceed with caution.
        
        @param request: ResetInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetInstance',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ResetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_instance_with_options_async(
        self,
        request: hsm_20231113_models.ResetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ResetInstanceResponse:
        """
        @summary Resets a hardware security module (HSM).
        
        @description After an HSM is reset, all related data is deleted and cannot be recovered. Proceed with caution.
        
        @param request: ResetInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetInstance',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ResetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_instance(
        self,
        request: hsm_20231113_models.ResetInstanceRequest,
    ) -> hsm_20231113_models.ResetInstanceResponse:
        """
        @summary Resets a hardware security module (HSM).
        
        @description After an HSM is reset, all related data is deleted and cannot be recovered. Proceed with caution.
        
        @param request: ResetInstanceRequest
        @return: ResetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_instance_with_options(request, runtime)

    async def reset_instance_async(
        self,
        request: hsm_20231113_models.ResetInstanceRequest,
    ) -> hsm_20231113_models.ResetInstanceResponse:
        """
        @summary Resets a hardware security module (HSM).
        
        @description After an HSM is reset, all related data is deleted and cannot be recovered. Proceed with caution.
        
        @param request: ResetInstanceRequest
        @return: ResetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_instance_with_options_async(request, runtime)

    def restore_instance_with_options(
        self,
        request: hsm_20231113_models.RestoreInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.RestoreInstanceResponse:
        """
        @summary Restores a hardware security module (HSM) by using an image.
        
        @description You can use images to restore only HSMs that are paused or disabled.
        
        @param request: RestoreInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestoreInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestoreInstance',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.RestoreInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_instance_with_options_async(
        self,
        request: hsm_20231113_models.RestoreInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.RestoreInstanceResponse:
        """
        @summary Restores a hardware security module (HSM) by using an image.
        
        @description You can use images to restore only HSMs that are paused or disabled.
        
        @param request: RestoreInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestoreInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestoreInstance',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.RestoreInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restore_instance(
        self,
        request: hsm_20231113_models.RestoreInstanceRequest,
    ) -> hsm_20231113_models.RestoreInstanceResponse:
        """
        @summary Restores a hardware security module (HSM) by using an image.
        
        @description You can use images to restore only HSMs that are paused or disabled.
        
        @param request: RestoreInstanceRequest
        @return: RestoreInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restore_instance_with_options(request, runtime)

    async def restore_instance_async(
        self,
        request: hsm_20231113_models.RestoreInstanceRequest,
    ) -> hsm_20231113_models.RestoreInstanceResponse:
        """
        @summary Restores a hardware security module (HSM) by using an image.
        
        @description You can use images to restore only HSMs that are paused or disabled.
        
        @param request: RestoreInstanceRequest
        @return: RestoreInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restore_instance_with_options_async(request, runtime)

    def resume_instance_with_options(
        self,
        request: hsm_20231113_models.ResumeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ResumeInstanceResponse:
        """
        @summary Resumes a disabled hardware security module (HSM).
        
        @param request: ResumeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeInstance',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ResumeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_instance_with_options_async(
        self,
        request: hsm_20231113_models.ResumeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ResumeInstanceResponse:
        """
        @summary Resumes a disabled hardware security module (HSM).
        
        @param request: ResumeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeInstance',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ResumeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_instance(
        self,
        request: hsm_20231113_models.ResumeInstanceRequest,
    ) -> hsm_20231113_models.ResumeInstanceResponse:
        """
        @summary Resumes a disabled hardware security module (HSM).
        
        @param request: ResumeInstanceRequest
        @return: ResumeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resume_instance_with_options(request, runtime)

    async def resume_instance_async(
        self,
        request: hsm_20231113_models.ResumeInstanceRequest,
    ) -> hsm_20231113_models.ResumeInstanceResponse:
        """
        @summary Resumes a disabled hardware security module (HSM).
        
        @param request: ResumeInstanceRequest
        @return: ResumeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resume_instance_with_options_async(request, runtime)

    def switch_cluster_master_with_options(
        self,
        request: hsm_20231113_models.SwitchClusterMasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.SwitchClusterMasterResponse:
        """
        @summary Promotes a slave hardware security module (HSM) to the master HSM within the cluster. Clusters that are manually synchronized in the Chinese Mainland do not support this operation.
        
        @param request: SwitchClusterMasterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchClusterMasterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SwitchClusterMaster',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.SwitchClusterMasterResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_cluster_master_with_options_async(
        self,
        request: hsm_20231113_models.SwitchClusterMasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.SwitchClusterMasterResponse:
        """
        @summary Promotes a slave hardware security module (HSM) to the master HSM within the cluster. Clusters that are manually synchronized in the Chinese Mainland do not support this operation.
        
        @param request: SwitchClusterMasterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchClusterMasterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SwitchClusterMaster',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.SwitchClusterMasterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_cluster_master(
        self,
        request: hsm_20231113_models.SwitchClusterMasterRequest,
    ) -> hsm_20231113_models.SwitchClusterMasterResponse:
        """
        @summary Promotes a slave hardware security module (HSM) to the master HSM within the cluster. Clusters that are manually synchronized in the Chinese Mainland do not support this operation.
        
        @param request: SwitchClusterMasterRequest
        @return: SwitchClusterMasterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_cluster_master_with_options(request, runtime)

    async def switch_cluster_master_async(
        self,
        request: hsm_20231113_models.SwitchClusterMasterRequest,
    ) -> hsm_20231113_models.SwitchClusterMasterResponse:
        """
        @summary Promotes a slave hardware security module (HSM) to the master HSM within the cluster. Clusters that are manually synchronized in the Chinese Mainland do not support this operation.
        
        @param request: SwitchClusterMasterRequest
        @return: SwitchClusterMasterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.switch_cluster_master_with_options_async(request, runtime)

    def sync_cluster_with_options(
        self,
        request: hsm_20231113_models.SyncClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.SyncClusterResponse:
        """
        @summary Synchronizes the data of hardware security modules (HSMs) in a cluster.
        
        @description    This operation is used for manually synchronizing data within clusters located in the Chinese Mainland. For clusters outside the Chinese Mainland, automatic data synchronization is supported, and this operation is unnecessary. If you attempt to use this operation, a 400 error code will be returned.
        The data synchronization takes approximately 5 minutes. To avoid service interruptions, we recommend performing this operation during off-peak hours.
        
        @param request: SyncClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncCluster',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.SyncClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_cluster_with_options_async(
        self,
        request: hsm_20231113_models.SyncClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.SyncClusterResponse:
        """
        @summary Synchronizes the data of hardware security modules (HSMs) in a cluster.
        
        @description    This operation is used for manually synchronizing data within clusters located in the Chinese Mainland. For clusters outside the Chinese Mainland, automatic data synchronization is supported, and this operation is unnecessary. If you attempt to use this operation, a 400 error code will be returned.
        The data synchronization takes approximately 5 minutes. To avoid service interruptions, we recommend performing this operation during off-peak hours.
        
        @param request: SyncClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncCluster',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.SyncClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_cluster(
        self,
        request: hsm_20231113_models.SyncClusterRequest,
    ) -> hsm_20231113_models.SyncClusterResponse:
        """
        @summary Synchronizes the data of hardware security modules (HSMs) in a cluster.
        
        @description    This operation is used for manually synchronizing data within clusters located in the Chinese Mainland. For clusters outside the Chinese Mainland, automatic data synchronization is supported, and this operation is unnecessary. If you attempt to use this operation, a 400 error code will be returned.
        The data synchronization takes approximately 5 minutes. To avoid service interruptions, we recommend performing this operation during off-peak hours.
        
        @param request: SyncClusterRequest
        @return: SyncClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sync_cluster_with_options(request, runtime)

    async def sync_cluster_async(
        self,
        request: hsm_20231113_models.SyncClusterRequest,
    ) -> hsm_20231113_models.SyncClusterResponse:
        """
        @summary Synchronizes the data of hardware security modules (HSMs) in a cluster.
        
        @description    This operation is used for manually synchronizing data within clusters located in the Chinese Mainland. For clusters outside the Chinese Mainland, automatic data synchronization is supported, and this operation is unnecessary. If you attempt to use this operation, a 400 error code will be returned.
        The data synchronization takes approximately 5 minutes. To avoid service interruptions, we recommend performing this operation during off-peak hours.
        
        @param request: SyncClusterRequest
        @return: SyncClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sync_cluster_with_options_async(request, runtime)
