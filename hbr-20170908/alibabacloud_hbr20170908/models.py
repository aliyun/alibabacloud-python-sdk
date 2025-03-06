# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class OtsDetail(TeaModel):
    def __init__(
        self,
        table_names: List[str] = None,
    ):
        self.table_names = table_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_names is not None:
            result['TableNames'] = self.table_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')
        return self


class OtsTableRestoreDetail(TeaModel):
    def __init__(
        self,
        batch_channel_count: int = None,
        index_name_suffix: str = None,
        overwrite_existing: bool = None,
        re_generate_auto_increment_pk: bool = None,
        restore_index: bool = None,
        restore_search_index: bool = None,
        search_index_name_suffix: str = None,
    ):
        self.batch_channel_count = batch_channel_count
        self.index_name_suffix = index_name_suffix
        self.overwrite_existing = overwrite_existing
        self.re_generate_auto_increment_pk = re_generate_auto_increment_pk
        self.restore_index = restore_index
        self.restore_search_index = restore_search_index
        self.search_index_name_suffix = search_index_name_suffix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_channel_count is not None:
            result['BatchChannelCount'] = self.batch_channel_count
        if self.index_name_suffix is not None:
            result['IndexNameSuffix'] = self.index_name_suffix
        if self.overwrite_existing is not None:
            result['OverwriteExisting'] = self.overwrite_existing
        if self.re_generate_auto_increment_pk is not None:
            result['ReGenerateAutoIncrementPK'] = self.re_generate_auto_increment_pk
        if self.restore_index is not None:
            result['RestoreIndex'] = self.restore_index
        if self.restore_search_index is not None:
            result['RestoreSearchIndex'] = self.restore_search_index
        if self.search_index_name_suffix is not None:
            result['SearchIndexNameSuffix'] = self.search_index_name_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchChannelCount') is not None:
            self.batch_channel_count = m.get('BatchChannelCount')
        if m.get('IndexNameSuffix') is not None:
            self.index_name_suffix = m.get('IndexNameSuffix')
        if m.get('OverwriteExisting') is not None:
            self.overwrite_existing = m.get('OverwriteExisting')
        if m.get('ReGenerateAutoIncrementPK') is not None:
            self.re_generate_auto_increment_pk = m.get('ReGenerateAutoIncrementPK')
        if m.get('RestoreIndex') is not None:
            self.restore_index = m.get('RestoreIndex')
        if m.get('RestoreSearchIndex') is not None:
            self.restore_search_index = m.get('RestoreSearchIndex')
        if m.get('SearchIndexNameSuffix') is not None:
            self.search_index_name_suffix = m.get('SearchIndexNameSuffix')
        return self


class Report(TeaModel):
    def __init__(
        self,
        failed_files: str = None,
        skipped_files: str = None,
        success_files: str = None,
        total_files: str = None,
    ):
        self.failed_files = failed_files
        self.skipped_files = skipped_files
        self.success_files = success_files
        self.total_files = total_files

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_files is not None:
            result['FailedFiles'] = self.failed_files
        if self.skipped_files is not None:
            result['SkippedFiles'] = self.skipped_files
        if self.success_files is not None:
            result['SuccessFiles'] = self.success_files
        if self.total_files is not None:
            result['TotalFiles'] = self.total_files
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedFiles') is not None:
            self.failed_files = m.get('FailedFiles')
        if m.get('SkippedFiles') is not None:
            self.skipped_files = m.get('SkippedFiles')
        if m.get('SuccessFiles') is not None:
            self.success_files = m.get('SuccessFiles')
        if m.get('TotalFiles') is not None:
            self.total_files = m.get('TotalFiles')
        return self


class Rule(TeaModel):
    def __init__(
        self,
        backup_type: str = None,
        destination_region_id: str = None,
        destination_retention: int = None,
        disabled: bool = None,
        do_copy: bool = None,
        retention: int = None,
        rule_name: str = None,
        schedule: str = None,
    ):
        self.backup_type = backup_type
        self.destination_region_id = destination_region_id
        self.destination_retention = destination_retention
        self.disabled = disabled
        self.do_copy = do_copy
        self.retention = retention
        self.rule_name = rule_name
        self.schedule = schedule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id
        if self.destination_retention is not None:
            result['DestinationRetention'] = self.destination_retention
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.do_copy is not None:
            result['DoCopy'] = self.do_copy
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')
        if m.get('DestinationRetention') is not None:
            self.destination_retention = m.get('DestinationRetention')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('DoCopy') is not None:
            self.do_copy = m.get('DoCopy')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class AddContainerClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_type: str = None,
        description: str = None,
        identifier: str = None,
        name: str = None,
        network_type: str = None,
    ):
        # The type of the cluster. Only Container Service for Kubernetes (ACK) clusters are supported.
        # 
        # This parameter is required.
        self.cluster_type = cluster_type
        # The description of the cluster.
        self.description = description
        # The ID of the cluster that you want to register.
        # 
        # This parameter is required.
        self.identifier = identifier
        # The name of the cluster.
        self.name = name
        # The network type of the cluster. Valid values:
        # 
        # *   **CLASSIC**: the classic network
        # *   **VPC**: a virtual private cloud (VPC)
        # 
        # This parameter is required.
        self.network_type = network_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.description is not None:
            result['Description'] = self.description
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.name is not None:
            result['Name'] = self.name
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        return self


class AddContainerClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        token: str = None,
    ):
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code
        # The message that is returned. If the request is successful, a value of successful is returned. If the request fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        # 
        # *   true: The request is successful.
        # *   false: The request fails.
        self.success = success
        # The token that is used to register the Hybrid Backup Recovery (HBR) client in the cluster.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class AddContainerClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddContainerClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddContainerClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelBackupJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        vault_id: str = None,
    ):
        # The ID of the backup job.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CancelBackupJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code
        # The message that is returned. If the request is successful, a value of successful is returned. If the request fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        # 
        # *   true: The request is successful.
        # *   false: The request fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelBackupJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelBackupJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelBackupJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelRestoreJobRequest(TeaModel):
    def __init__(
        self,
        restore_id: str = None,
        vault_id: str = None,
    ):
        # The ID of the restore job.
        # 
        # This parameter is required.
        self.restore_id = restore_id
        # The ID of the backup vault.
        # 
        # This parameter is required.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.restore_id is not None:
            result['RestoreId'] = self.restore_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RestoreId') is not None:
            self.restore_id = m.get('RestoreId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CancelRestoreJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelRestoreJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelRestoreJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelRestoreJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        new_resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the new resource group. You can view the available resource groups in the Resource Management console.
        # 
        # This parameter is required.
        self.new_resource_group_id = new_resource_group_id
        # The ID of the resource. The value of this parameter varies with the resource type. For example, if the ResourceType parameter is set to vault, the ResourceId parameter specifies the ID of the backup vault.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # 
        # *   **vault**: backup vault
        # *   **client**: backup client
        # *   **hanainstance**: SAP HANA instance
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckRoleRequest(TeaModel):
    def __init__(
        self,
        check_role_type: str = None,
        cross_account_role_name: str = None,
        cross_account_user_id: int = None,
    ):
        # The type of the role. Valid values:
        # 
        # *   EcsRole: a role with the permissions to access Elastic Compute Service (ECS) resources
        # *   CsgRole: a role with the permissions to perform Cloud Storage Gateway (CSG) backup
        # *   NasRole: a role with the permissions to perform NAS backup
        # *   OssRole: a role with the permissions to perform Object Storage Service (OSS) backup
        # *   UdmRole: a role with the permissions to perform ECS instance backup
        # *   VMwareLocalRole: a role with the permissions to back up on-premises VMware virtual machines (VMs)
        # *   VMwareCloudRole: a role with the permissions to back up VMs deployed on Alibaba Cloud VMware Service (ACVS)
        # *   EcsBackupRole: a role with the permissions to perform ECS backup
        # *   OtsRole: a role with the permissions to perform Tablestore backup
        # *   CrossAccountRole: a role with the permissions to perform cross-account backup
        self.check_role_type = check_role_type
        # The name of the Resource Access Management (RAM) role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_role_type is not None:
            result['CheckRoleType'] = self.check_role_type
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckRoleType') is not None:
            self.check_role_type = m.get('CheckRoleType')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        return self


class CheckRoleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckRoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBackupJobRequest(TeaModel):
    def __init__(
        self,
        backup_type: str = None,
        cluster_id: str = None,
        container_cluster_id: str = None,
        container_resources: str = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        detail: Dict[str, Any] = None,
        exclude: str = None,
        include: str = None,
        initiated_by_ack: bool = None,
        instance_id: str = None,
        job_name: str = None,
        options: str = None,
        retention: int = None,
        source_type: str = None,
        speed_limit: str = None,
        vault_id: str = None,
    ):
        # The backup type. This parameter is required only if you set the SourceType parameter to UDM_ECS.
        # 
        # *   **COMPLETE**: full backup
        self.backup_type = backup_type
        # You do not need to specify this parameter.
        self.cluster_id = cluster_id
        # You do not need to specify this parameter.
        self.container_cluster_id = container_cluster_id
        # You do not need to specify this parameter.
        self.container_resources = container_resources
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # This parameter is required only if you set the **SourceType** parameter to **UDM_ECS**. The value is a JSON string. Valid values:
        # 
        # *   doCopy: specifies whether to enable remote replication.
        # 
        # *   destinationRegionId: the destination region for remote replication.
        # 
        # *   destinationRetention: the retention period of the backup point for remote replication.
        # 
        # *   diskIdList: the IDs of the disks that are to be backed up. If this parameter is left empty, all disks are backed up.
        # 
        # *   snapshotGroup: specifies whether to use a snapshot-consistent group. This parameter is valid only if all disks of the ECS instance are Enterprise SSDs (ESSDs).
        # 
        # *   appConsistent: specifies whether to use the application-consistent backup feature. This parameter must be used with the preScriptPath and postScriptPath parameters.
        # 
        # *   preScriptPath: the path to the pre-freeze scripts.
        # 
        # *   postScriptPath: the path to the post-thaw scripts.
        # 
        # *   enableWriters: This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies whether to create application-consistent snapshots.
        # 
        #     *   true: creates application-consistent snapshots.
        #     *   false: creates file system-consistent snapshots.
        # 
        # *   enableFsFreeze: This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies whether to enable Linux fsfreeze to put file systems into the read-only state before application-consistent snapshots are created. Default value: true.
        # 
        # *   timeoutSeconds: This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies the I/O freeze timeout period. Default value: 30. Unit: seconds.
        self.detail = detail
        # This parameter does not take effect if you set the **SourceType** parameter to **UDM_ECS**. This parameter specifies the paths to the files that are excluded from the backup job. The value can be up to 255 characters in length.
        self.exclude = exclude
        # This parameter does not take effect if you set the **SourceType** parameter to **UDM_ECS**. This parameter specifies the paths to the files that are backed up. The value can be up to 255 characters in length.
        self.include = include
        # false or left empty
        self.initiated_by_ack = initiated_by_ack
        # This parameter is required only if you set the **SourceType** parameter to **UDM_ECS**. This parameter specifies the ID of the ECS instance.
        self.instance_id = instance_id
        # The name of the backup job.
        self.job_name = job_name
        # You do not need to specify this parameter.
        self.options = options
        # The retention period of the backup data. Unit: days.
        self.retention = retention
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: Elastic Compute Service (ECS) instance
        # 
        # This parameter is required.
        self.source_type = source_type
        # This parameter does not take effect if you set the **SourceType** parameter to **UDM_ECS**. This parameter specifies the throttling rules. Format: `{start}|{end}|{bandwidth}`. Separate multiple throttling rules with vertical bars (|). A specified time range cannot overlap with another time range.
        # 
        # *   **start**: the start hour.
        # *   **end**: the end hour.
        # *   **bandwidth**: the bandwidth. Unit: KB/s.
        self.speed_limit = speed_limit
        # The ID of the backup vault. This parameter is not required if you set the SourceType parameter to UDM_ECS.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.container_cluster_id is not None:
            result['ContainerClusterId'] = self.container_cluster_id
        if self.container_resources is not None:
            result['ContainerResources'] = self.container_resources
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.include is not None:
            result['Include'] = self.include
        if self.initiated_by_ack is not None:
            result['InitiatedByAck'] = self.initiated_by_ack
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.options is not None:
            result['Options'] = self.options
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ContainerClusterId') is not None:
            self.container_cluster_id = m.get('ContainerClusterId')
        if m.get('ContainerResources') is not None:
            self.container_resources = m.get('ContainerResources')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('InitiatedByAck') is not None:
            self.initiated_by_ack = m.get('InitiatedByAck')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateBackupJobShrinkRequest(TeaModel):
    def __init__(
        self,
        backup_type: str = None,
        cluster_id: str = None,
        container_cluster_id: str = None,
        container_resources: str = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        detail_shrink: str = None,
        exclude: str = None,
        include: str = None,
        initiated_by_ack: bool = None,
        instance_id: str = None,
        job_name: str = None,
        options: str = None,
        retention: int = None,
        source_type: str = None,
        speed_limit: str = None,
        vault_id: str = None,
    ):
        # The backup type. This parameter is required only if you set the SourceType parameter to UDM_ECS.
        # 
        # *   **COMPLETE**: full backup
        self.backup_type = backup_type
        # You do not need to specify this parameter.
        self.cluster_id = cluster_id
        # You do not need to specify this parameter.
        self.container_cluster_id = container_cluster_id
        # You do not need to specify this parameter.
        self.container_resources = container_resources
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # This parameter is required only if you set the **SourceType** parameter to **UDM_ECS**. The value is a JSON string. Valid values:
        # 
        # *   doCopy: specifies whether to enable remote replication.
        # 
        # *   destinationRegionId: the destination region for remote replication.
        # 
        # *   destinationRetention: the retention period of the backup point for remote replication.
        # 
        # *   diskIdList: the IDs of the disks that are to be backed up. If this parameter is left empty, all disks are backed up.
        # 
        # *   snapshotGroup: specifies whether to use a snapshot-consistent group. This parameter is valid only if all disks of the ECS instance are Enterprise SSDs (ESSDs).
        # 
        # *   appConsistent: specifies whether to use the application-consistent backup feature. This parameter must be used with the preScriptPath and postScriptPath parameters.
        # 
        # *   preScriptPath: the path to the pre-freeze scripts.
        # 
        # *   postScriptPath: the path to the post-thaw scripts.
        # 
        # *   enableWriters: This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies whether to create application-consistent snapshots.
        # 
        #     *   true: creates application-consistent snapshots.
        #     *   false: creates file system-consistent snapshots.
        # 
        # *   enableFsFreeze: This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies whether to enable Linux fsfreeze to put file systems into the read-only state before application-consistent snapshots are created. Default value: true.
        # 
        # *   timeoutSeconds: This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies the I/O freeze timeout period. Default value: 30. Unit: seconds.
        self.detail_shrink = detail_shrink
        # This parameter does not take effect if you set the **SourceType** parameter to **UDM_ECS**. This parameter specifies the paths to the files that are excluded from the backup job. The value can be up to 255 characters in length.
        self.exclude = exclude
        # This parameter does not take effect if you set the **SourceType** parameter to **UDM_ECS**. This parameter specifies the paths to the files that are backed up. The value can be up to 255 characters in length.
        self.include = include
        # false or left empty
        self.initiated_by_ack = initiated_by_ack
        # This parameter is required only if you set the **SourceType** parameter to **UDM_ECS**. This parameter specifies the ID of the ECS instance.
        self.instance_id = instance_id
        # The name of the backup job.
        self.job_name = job_name
        # You do not need to specify this parameter.
        self.options = options
        # The retention period of the backup data. Unit: days.
        self.retention = retention
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: Elastic Compute Service (ECS) instance
        # 
        # This parameter is required.
        self.source_type = source_type
        # This parameter does not take effect if you set the **SourceType** parameter to **UDM_ECS**. This parameter specifies the throttling rules. Format: `{start}|{end}|{bandwidth}`. Separate multiple throttling rules with vertical bars (|). A specified time range cannot overlap with another time range.
        # 
        # *   **start**: the start hour.
        # *   **end**: the end hour.
        # *   **bandwidth**: the bandwidth. Unit: KB/s.
        self.speed_limit = speed_limit
        # The ID of the backup vault. This parameter is not required if you set the SourceType parameter to UDM_ECS.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.container_cluster_id is not None:
            result['ContainerClusterId'] = self.container_cluster_id
        if self.container_resources is not None:
            result['ContainerResources'] = self.container_resources
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.detail_shrink is not None:
            result['Detail'] = self.detail_shrink
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.include is not None:
            result['Include'] = self.include
        if self.initiated_by_ack is not None:
            result['InitiatedByAck'] = self.initiated_by_ack
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.options is not None:
            result['Options'] = self.options
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ContainerClusterId') is not None:
            self.container_cluster_id = m.get('ContainerClusterId')
        if m.get('ContainerResources') is not None:
            self.container_resources = m.get('ContainerResources')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('Detail') is not None:
            self.detail_shrink = m.get('Detail')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('InitiatedByAck') is not None:
            self.initiated_by_ack = m.get('InitiatedByAck')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateBackupJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        job_id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The ID of the backup job.
        self.job_id = job_id
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateBackupJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBackupJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateBackupJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBackupPlanRequestRule(TeaModel):
    def __init__(
        self,
        backup_type: str = None,
        destination_region_id: str = None,
        destination_retention: int = None,
        disabled: bool = None,
        do_copy: bool = None,
        retention: int = None,
        rule_name: str = None,
        schedule: str = None,
    ):
        # Backup type.
        self.backup_type = backup_type
        # ID of the region for offsite replication.
        self.destination_region_id = destination_region_id
        # Number of days to retain offsite backups.
        self.destination_retention = destination_retention
        # Whether the rule is enabled.
        self.disabled = disabled
        # Whether to enable offsite replication.
        self.do_copy = do_copy
        # Backup retention period.
        self.retention = retention
        # Rule name.
        self.rule_name = rule_name
        # Backup strategy. Optional format: I|{startTime}|{interval}. This means that a backup task is executed every {interval} starting from {startTime}. Backup tasks for past times will not be executed. If the previous backup task has not been completed, the next backup task will not be triggered. For example, I|1631685600|P1D means a backup is performed every day starting from 2021-09-15 14:00:00.
        # 
        # - startTime: The start time of the backup, in UNIX time, in seconds.
        # - interval: ISO8601 time interval. For example, PT1H means an interval of one hour. P1D means an interval of one day.
        self.schedule = schedule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id
        if self.destination_retention is not None:
            result['DestinationRetention'] = self.destination_retention
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.do_copy is not None:
            result['DoCopy'] = self.do_copy
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')
        if m.get('DestinationRetention') is not None:
            self.destination_retention = m.get('DestinationRetention')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('DoCopy') is not None:
            self.do_copy = m.get('DoCopy')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class CreateBackupPlanRequest(TeaModel):
    def __init__(
        self,
        backup_type: str = None,
        bucket: str = None,
        change_list_path: str = None,
        cluster_id: str = None,
        create_time: int = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        data_source_id: str = None,
        dest_data_source_detail: Dict[str, Any] = None,
        dest_data_source_id: str = None,
        dest_source_type: str = None,
        detail: Dict[str, Any] = None,
        disabled: bool = None,
        exclude: str = None,
        file_system_id: str = None,
        include: str = None,
        instance_id: str = None,
        instance_name: str = None,
        keep_latest_snapshots: int = None,
        options: str = None,
        ots_detail: OtsDetail = None,
        path: List[str] = None,
        plan_name: str = None,
        prefix: str = None,
        retention: int = None,
        rule: List[CreateBackupPlanRequestRule] = None,
        schedule: str = None,
        source_type: str = None,
        speed_limit: str = None,
        udm_region_id: str = None,
        vault_id: str = None,
    ):
        # Backup type. Value: **COMPLETE**, indicating a full backup.
        # 
        # This parameter is required.
        self.backup_type = backup_type
        # This parameter is required when **SourceType** is set to **OSS**. It represents the OSS bucket name.
        self.bucket = bucket
        # Configuration for the incremental file synchronization list. (Required only for synchronization)
        self.change_list_path = change_list_path
        # The ID of the client group that executes the data synchronization plan. This parameter is required only for data synchronization.
        self.cluster_id = cluster_id
        # This parameter is required when **SourceType** is set to **NAS**. It represents the creation time of the file system, in UNIX timestamp, in seconds.
        self.create_time = create_time
        # The role name created in the RAM of the original account for cross-account backup.
        self.cross_account_role_name = cross_account_role_name
        # Cross-account backup type. Supported values:
        # - SELF_ACCOUNT: Backup within the same account
        # - CROSS_ACCOUNT: Cross-account backup
        self.cross_account_type = cross_account_type
        # The original account ID used for cross-account backup.
        self.cross_account_user_id = cross_account_user_id
        # The ID of the data source. This parameter is required only for data synchronization.
        self.data_source_id = data_source_id
        # Destination data source details. (Required only for synchronization)
        self.dest_data_source_detail = dest_data_source_detail
        # Destination data source ID. (Required only for synchronization)
        self.dest_data_source_id = dest_data_source_id
        # Destination data source type. (Required only for synchronization)
        self.dest_source_type = dest_source_type
        # Details of the whole machine backup, in JSON string format.
        # 
        # * snapshotGroup: Whether to use a consistent snapshot group (only valid if all instance disks are ESSD).
        # * appConsistent: Whether to use application consistency (requires the use of preScriptPath and postScriptPath parameters).
        # * preScriptPath: Path to the freeze script.
        # * postScriptPath: Path to the thaw script.
        self.detail = detail
        # Is the plan disabled by default
        self.disabled = disabled
        # This parameter is required only when **SourceType** is set to **ECS_FILE**. It specifies the path that should not be backed up, meaning all files under this path will not be included in the backup. The maximum length is 255 characters.
        self.exclude = exclude
        # This parameter is required when **SourceType** is set to **NAS**. It represents the file system ID.
        self.file_system_id = file_system_id
        # This parameter is required when **SourceType** is set to **ECS_FILE**. It represents the path to be backed up, and all files under this path will be backed up. Supports up to 255 characters.
        self.include = include
        # This parameter is required when **SourceType** is set to **ECS_FILE**. It represents the ECS instance ID.
        self.instance_id = instance_id
        # Table store instance name.
        self.instance_name = instance_name
        # Whether to enable retaining at least one backup version.
        # - 0 - Do not retain
        # - 1 - Retain
        self.keep_latest_snapshots = keep_latest_snapshots
        # This parameter is required when **SourceType** is set to **ECS_FILE**. It indicates whether to use the Windows system VSS to define the backup path.
        # 
        # - This feature only supports Windows type ECS instances.
        # - If there are data changes in the backup source and you need to ensure consistency between the backup data and the source data, you can configure it as `["UseVSS":true]`.
        # - After choosing to use VSS, multiple file directories cannot be backed up simultaneously.
        self.options = options
        # The details about the Tablestore instance.
        self.ots_detail = ots_detail
        # Backup paths.
        self.path = path
        # Name of the backup plan. 1 to 64 characters. The name must be unique for each data source type within a single backup vault.
        # 
        # This parameter is required.
        self.plan_name = plan_name
        # This parameter is required when **SourceType** is set to **OSS**. It represents the backup prefix. When specified, only objects matching the prefix are backed up.
        self.prefix = prefix
        # Number of days to retain the backup, with a minimum value of 1, in days.
        self.retention = retention
        # Backup plan rules.
        self.rule = rule
        # Backup policy. Optional format: `I|{startTime}|{interval}`. This indicates that a backup task will be executed every `{interval}` starting from `{startTime}`. It does not compensate for missed backup tasks due to past time. If the previous backup task has not been completed, the next backup task will not be triggered. For example, `I|1631685600|P1D` means a backup is performed every day starting from 2021-09-15 14:00:00.
        # 
        # - **startTime**: Start time of the backup, in UNIX timestamp, in seconds.
        # - **interval**: ISO8601 time interval. For example, PT1H indicates an interval of one hour, and P1D indicates an interval of one day.
        # 
        # This parameter is required.
        self.schedule = schedule
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: File Storage NAS (NAS) file systems
        # *   **OTS**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        # *   **SYNC**: data synchronization
        # 
        # This parameter is required.
        self.source_type = source_type
        # This parameter is required when **SourceType** is set to **ECS_FILE**. It represents the backup traffic control. Format: `{start}:{end}:{bandwidth}`. Multiple traffic control configurations are separated by |, and the configured times should not overlap.
        # 
        # - **start**: Start hour.
        # - **end**: End hour.
        # - **bandwidth**: Limit rate, in KB/s.
        self.speed_limit = speed_limit
        # Region where the whole machine backup instance is located.
        self.udm_region_id = udm_region_id
        # Backup vault ID.
        self.vault_id = vault_id

    def validate(self):
        if self.ots_detail:
            self.ots_detail.validate()
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.change_list_path is not None:
            result['ChangeListPath'] = self.change_list_path
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.dest_data_source_detail is not None:
            result['DestDataSourceDetail'] = self.dest_data_source_detail
        if self.dest_data_source_id is not None:
            result['DestDataSourceId'] = self.dest_data_source_id
        if self.dest_source_type is not None:
            result['DestSourceType'] = self.dest_source_type
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.include is not None:
            result['Include'] = self.include
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.keep_latest_snapshots is not None:
            result['KeepLatestSnapshots'] = self.keep_latest_snapshots
        if self.options is not None:
            result['Options'] = self.options
        if self.ots_detail is not None:
            result['OtsDetail'] = self.ots_detail.to_map()
        if self.path is not None:
            result['Path'] = self.path
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.retention is not None:
            result['Retention'] = self.retention
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        if self.udm_region_id is not None:
            result['UdmRegionId'] = self.udm_region_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('ChangeListPath') is not None:
            self.change_list_path = m.get('ChangeListPath')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('DestDataSourceDetail') is not None:
            self.dest_data_source_detail = m.get('DestDataSourceDetail')
        if m.get('DestDataSourceId') is not None:
            self.dest_data_source_id = m.get('DestDataSourceId')
        if m.get('DestSourceType') is not None:
            self.dest_source_type = m.get('DestSourceType')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('KeepLatestSnapshots') is not None:
            self.keep_latest_snapshots = m.get('KeepLatestSnapshots')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OtsDetail') is not None:
            temp_model = OtsDetail()
            self.ots_detail = temp_model.from_map(m['OtsDetail'])
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = CreateBackupPlanRequestRule()
                self.rule.append(temp_model.from_map(k))
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        if m.get('UdmRegionId') is not None:
            self.udm_region_id = m.get('UdmRegionId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateBackupPlanShrinkRequestRule(TeaModel):
    def __init__(
        self,
        backup_type: str = None,
        destination_region_id: str = None,
        destination_retention: int = None,
        disabled: bool = None,
        do_copy: bool = None,
        retention: int = None,
        rule_name: str = None,
        schedule: str = None,
    ):
        # Backup type.
        self.backup_type = backup_type
        # ID of the region for offsite replication.
        self.destination_region_id = destination_region_id
        # Number of days to retain offsite backups.
        self.destination_retention = destination_retention
        # Whether the rule is enabled.
        self.disabled = disabled
        # Whether to enable offsite replication.
        self.do_copy = do_copy
        # Backup retention period.
        self.retention = retention
        # Rule name.
        self.rule_name = rule_name
        # Backup strategy. Optional format: I|{startTime}|{interval}. This means that a backup task is executed every {interval} starting from {startTime}. Backup tasks for past times will not be executed. If the previous backup task has not been completed, the next backup task will not be triggered. For example, I|1631685600|P1D means a backup is performed every day starting from 2021-09-15 14:00:00.
        # 
        # - startTime: The start time of the backup, in UNIX time, in seconds.
        # - interval: ISO8601 time interval. For example, PT1H means an interval of one hour. P1D means an interval of one day.
        self.schedule = schedule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id
        if self.destination_retention is not None:
            result['DestinationRetention'] = self.destination_retention
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.do_copy is not None:
            result['DoCopy'] = self.do_copy
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')
        if m.get('DestinationRetention') is not None:
            self.destination_retention = m.get('DestinationRetention')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('DoCopy') is not None:
            self.do_copy = m.get('DoCopy')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class CreateBackupPlanShrinkRequest(TeaModel):
    def __init__(
        self,
        backup_type: str = None,
        bucket: str = None,
        change_list_path: str = None,
        cluster_id: str = None,
        create_time: int = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        data_source_id: str = None,
        dest_data_source_detail_shrink: str = None,
        dest_data_source_id: str = None,
        dest_source_type: str = None,
        detail_shrink: str = None,
        disabled: bool = None,
        exclude: str = None,
        file_system_id: str = None,
        include: str = None,
        instance_id: str = None,
        instance_name: str = None,
        keep_latest_snapshots: int = None,
        options: str = None,
        ots_detail_shrink: str = None,
        path: List[str] = None,
        plan_name: str = None,
        prefix: str = None,
        retention: int = None,
        rule: List[CreateBackupPlanShrinkRequestRule] = None,
        schedule: str = None,
        source_type: str = None,
        speed_limit: str = None,
        udm_region_id: str = None,
        vault_id: str = None,
    ):
        # Backup type. Value: **COMPLETE**, indicating a full backup.
        # 
        # This parameter is required.
        self.backup_type = backup_type
        # This parameter is required when **SourceType** is set to **OSS**. It represents the OSS bucket name.
        self.bucket = bucket
        # Configuration for the incremental file synchronization list. (Required only for synchronization)
        self.change_list_path = change_list_path
        # The ID of the client group that executes the data synchronization plan. This parameter is required only for data synchronization.
        self.cluster_id = cluster_id
        # This parameter is required when **SourceType** is set to **NAS**. It represents the creation time of the file system, in UNIX timestamp, in seconds.
        self.create_time = create_time
        # The role name created in the RAM of the original account for cross-account backup.
        self.cross_account_role_name = cross_account_role_name
        # Cross-account backup type. Supported values:
        # - SELF_ACCOUNT: Backup within the same account
        # - CROSS_ACCOUNT: Cross-account backup
        self.cross_account_type = cross_account_type
        # The original account ID used for cross-account backup.
        self.cross_account_user_id = cross_account_user_id
        # The ID of the data source. This parameter is required only for data synchronization.
        self.data_source_id = data_source_id
        # Destination data source details. (Required only for synchronization)
        self.dest_data_source_detail_shrink = dest_data_source_detail_shrink
        # Destination data source ID. (Required only for synchronization)
        self.dest_data_source_id = dest_data_source_id
        # Destination data source type. (Required only for synchronization)
        self.dest_source_type = dest_source_type
        # Details of the whole machine backup, in JSON string format.
        # 
        # * snapshotGroup: Whether to use a consistent snapshot group (only valid if all instance disks are ESSD).
        # * appConsistent: Whether to use application consistency (requires the use of preScriptPath and postScriptPath parameters).
        # * preScriptPath: Path to the freeze script.
        # * postScriptPath: Path to the thaw script.
        self.detail_shrink = detail_shrink
        # Is the plan disabled by default
        self.disabled = disabled
        # This parameter is required only when **SourceType** is set to **ECS_FILE**. It specifies the path that should not be backed up, meaning all files under this path will not be included in the backup. The maximum length is 255 characters.
        self.exclude = exclude
        # This parameter is required when **SourceType** is set to **NAS**. It represents the file system ID.
        self.file_system_id = file_system_id
        # This parameter is required when **SourceType** is set to **ECS_FILE**. It represents the path to be backed up, and all files under this path will be backed up. Supports up to 255 characters.
        self.include = include
        # This parameter is required when **SourceType** is set to **ECS_FILE**. It represents the ECS instance ID.
        self.instance_id = instance_id
        # Table store instance name.
        self.instance_name = instance_name
        # Whether to enable retaining at least one backup version.
        # - 0 - Do not retain
        # - 1 - Retain
        self.keep_latest_snapshots = keep_latest_snapshots
        # This parameter is required when **SourceType** is set to **ECS_FILE**. It indicates whether to use the Windows system VSS to define the backup path.
        # 
        # - This feature only supports Windows type ECS instances.
        # - If there are data changes in the backup source and you need to ensure consistency between the backup data and the source data, you can configure it as `["UseVSS":true]`.
        # - After choosing to use VSS, multiple file directories cannot be backed up simultaneously.
        self.options = options
        # The details about the Tablestore instance.
        self.ots_detail_shrink = ots_detail_shrink
        # Backup paths.
        self.path = path
        # Name of the backup plan. 1 to 64 characters. The name must be unique for each data source type within a single backup vault.
        # 
        # This parameter is required.
        self.plan_name = plan_name
        # This parameter is required when **SourceType** is set to **OSS**. It represents the backup prefix. When specified, only objects matching the prefix are backed up.
        self.prefix = prefix
        # Number of days to retain the backup, with a minimum value of 1, in days.
        self.retention = retention
        # Backup plan rules.
        self.rule = rule
        # Backup policy. Optional format: `I|{startTime}|{interval}`. This indicates that a backup task will be executed every `{interval}` starting from `{startTime}`. It does not compensate for missed backup tasks due to past time. If the previous backup task has not been completed, the next backup task will not be triggered. For example, `I|1631685600|P1D` means a backup is performed every day starting from 2021-09-15 14:00:00.
        # 
        # - **startTime**: Start time of the backup, in UNIX timestamp, in seconds.
        # - **interval**: ISO8601 time interval. For example, PT1H indicates an interval of one hour, and P1D indicates an interval of one day.
        # 
        # This parameter is required.
        self.schedule = schedule
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: File Storage NAS (NAS) file systems
        # *   **OTS**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        # *   **SYNC**: data synchronization
        # 
        # This parameter is required.
        self.source_type = source_type
        # This parameter is required when **SourceType** is set to **ECS_FILE**. It represents the backup traffic control. Format: `{start}:{end}:{bandwidth}`. Multiple traffic control configurations are separated by |, and the configured times should not overlap.
        # 
        # - **start**: Start hour.
        # - **end**: End hour.
        # - **bandwidth**: Limit rate, in KB/s.
        self.speed_limit = speed_limit
        # Region where the whole machine backup instance is located.
        self.udm_region_id = udm_region_id
        # Backup vault ID.
        self.vault_id = vault_id

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.change_list_path is not None:
            result['ChangeListPath'] = self.change_list_path
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.dest_data_source_detail_shrink is not None:
            result['DestDataSourceDetail'] = self.dest_data_source_detail_shrink
        if self.dest_data_source_id is not None:
            result['DestDataSourceId'] = self.dest_data_source_id
        if self.dest_source_type is not None:
            result['DestSourceType'] = self.dest_source_type
        if self.detail_shrink is not None:
            result['Detail'] = self.detail_shrink
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.include is not None:
            result['Include'] = self.include
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.keep_latest_snapshots is not None:
            result['KeepLatestSnapshots'] = self.keep_latest_snapshots
        if self.options is not None:
            result['Options'] = self.options
        if self.ots_detail_shrink is not None:
            result['OtsDetail'] = self.ots_detail_shrink
        if self.path is not None:
            result['Path'] = self.path
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.retention is not None:
            result['Retention'] = self.retention
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        if self.udm_region_id is not None:
            result['UdmRegionId'] = self.udm_region_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('ChangeListPath') is not None:
            self.change_list_path = m.get('ChangeListPath')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('DestDataSourceDetail') is not None:
            self.dest_data_source_detail_shrink = m.get('DestDataSourceDetail')
        if m.get('DestDataSourceId') is not None:
            self.dest_data_source_id = m.get('DestDataSourceId')
        if m.get('DestSourceType') is not None:
            self.dest_source_type = m.get('DestSourceType')
        if m.get('Detail') is not None:
            self.detail_shrink = m.get('Detail')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('KeepLatestSnapshots') is not None:
            self.keep_latest_snapshots = m.get('KeepLatestSnapshots')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OtsDetail') is not None:
            self.ots_detail_shrink = m.get('OtsDetail')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = CreateBackupPlanShrinkRequestRule()
                self.rule.append(temp_model.from_map(k))
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        if m.get('UdmRegionId') is not None:
            self.udm_region_id = m.get('UdmRegionId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        plan_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Return code, 200 indicates success.
        self.code = code
        # Description of the return message, usually returns \\"successful\\" upon success, and corresponding error messages in case of failure.
        self.message = message
        # Backup plan ID.
        self.plan_id = plan_id
        # Request ID.
        self.request_id = request_id
        # Whether the request was successful.
        # 
        # - true: Success.
        # - false: Failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClientsRequest(TeaModel):
    def __init__(
        self,
        alert_setting: str = None,
        client_info: str = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        resource_group_id: str = None,
        use_https: bool = None,
        vault_id: str = None,
    ):
        # The alert settings. Valid value: INHERITED, which indicates that the HBR client sends alert notifications by using the same method configured for the backup vault.
        self.alert_setting = alert_setting
        # The installation information of the HBR clients.
        self.client_info = client_info
        # The name of the Resource Access Management (RAM) role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # The backup type. Valid values:
        # 
        # - **SELF_ACCOUNT**: Data is backed up within the same Alibaba Cloud account.
        # - **CROSS_ACCOUNT**: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Specifies whether to transmit data over HTTPS. Valid values:
        # 
        # *   true: transmits data over HTTPS.
        # *   false: transmits data over HTTP.
        self.use_https = use_https
        # The ID of the backup vault.
        # 
        # This parameter is required.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_setting is not None:
            result['AlertSetting'] = self.alert_setting
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.use_https is not None:
            result['UseHttps'] = self.use_https
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertSetting') is not None:
            self.alert_setting = m.get('AlertSetting')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('UseHttps') is not None:
            self.use_https = m.get('UseHttps')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateClientsResponseBodyInstanceStatusesInstanceStatus(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        valid_instance: bool = None,
    ):
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # Indicates whether an HBR client can be installed on the ECS instance. Valid values:
        # 
        # *   true: An HBR client can be installed on the ECS instance.
        # *   false: An HBR client cannot be installed on the ECS instance.
        self.valid_instance = valid_instance

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.valid_instance is not None:
            result['ValidInstance'] = self.valid_instance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ValidInstance') is not None:
            self.valid_instance = m.get('ValidInstance')
        return self


class CreateClientsResponseBodyInstanceStatuses(TeaModel):
    def __init__(
        self,
        instance_status: List[CreateClientsResponseBodyInstanceStatusesInstanceStatus] = None,
    ):
        self.instance_status = instance_status

    def validate(self):
        if self.instance_status:
            for k in self.instance_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceStatus'] = []
        if self.instance_status is not None:
            for k in self.instance_status:
                result['InstanceStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_status = []
        if m.get('InstanceStatus') is not None:
            for k in m.get('InstanceStatus'):
                temp_model = CreateClientsResponseBodyInstanceStatusesInstanceStatus()
                self.instance_status.append(temp_model.from_map(k))
        return self


class CreateClientsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        instance_statuses: CreateClientsResponseBodyInstanceStatuses = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The status of the ECS instance. If you specify more than one instance IDs in the request and the status of an ECS instance does not meet the requirements to install an HBR client, an error message is returned based on the value of this parameter.
        self.instance_statuses = instance_statuses
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The ID of the asynchronous job. You can call the DescribeTask operation to query the execution result of an asynchronous job.
        self.task_id = task_id

    def validate(self):
        if self.instance_statuses:
            self.instance_statuses.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_statuses is not None:
            result['InstanceStatuses'] = self.instance_statuses.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceStatuses') is not None:
            temp_model = CreateClientsResponseBodyInstanceStatuses()
            self.instance_statuses = temp_model.from_map(m['InstanceStatuses'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateClientsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateClientsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHanaBackupPlanRequest(TeaModel):
    def __init__(
        self,
        backup_prefix: str = None,
        backup_type: str = None,
        cluster_id: str = None,
        database_name: str = None,
        plan_name: str = None,
        resource_group_id: str = None,
        schedule: str = None,
        vault_id: str = None,
    ):
        # The backup prefix.
        self.backup_prefix = backup_prefix
        # The backup type. Valid values:
        # 
        # *   COMPLETE: full backup
        # *   INCREMENTAL: incremental backup
        # *   DIFFERENTIAL: differential backup
        # 
        # This parameter is required.
        self.backup_type = backup_type
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The name of the database.
        # 
        # This parameter is required.
        self.database_name = database_name
        # The name of the backup plan.
        # 
        # This parameter is required.
        self.plan_name = plan_name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   startTime: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of one hour. P1D specifies an interval of one day.
        # 
        # This parameter is required.
        self.schedule = schedule
        # The ID of the backup vault.
        # 
        # This parameter is required.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_prefix is not None:
            result['BackupPrefix'] = self.backup_prefix
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPrefix') is not None:
            self.backup_prefix = m.get('BackupPrefix')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateHanaBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        plan_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The ID of the backup plan.
        self.plan_id = plan_id
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateHanaBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateHanaBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateHanaBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHanaInstanceRequest(TeaModel):
    def __init__(
        self,
        alert_setting: str = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        ecs_instance_id: str = None,
        hana_name: str = None,
        host: str = None,
        instance_number: int = None,
        password: str = None,
        resource_group_id: str = None,
        sid: str = None,
        use_ssl: bool = None,
        user_name: str = None,
        validate_certificate: bool = None,
        vault_id: str = None,
    ):
        # The alert settings. Valid value: INHERITED, which indicates that the Cloud Backup client sends alert notifications by using the same method configured for the backup vault.
        self.alert_setting = alert_setting
        # The name of the Resource Access Management (RAM) role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # The backup type. Valid values:
        # 
        # - **SELF_ACCOUNT**: Data is backed up within the same Alibaba Cloud account.
        # - **CROSS_ACCOUNT**: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The IDs of the ECS instances that host the SAP HANA instance to be registered. Cloud Backup installs backup clients on the specified ECS instances.
        self.ecs_instance_id = ecs_instance_id
        # The name of the SAP HANA instance.
        self.hana_name = hana_name
        # The private or internal IP address of the host where the primary node of the SAP HANA instance resides.
        self.host = host
        # The instance number of the SAP HANA system.
        self.instance_number = instance_number
        # The password that is used to connect with the SAP HANA database.
        self.password = password
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The security identifier (SID) of the SAP HANA database. For more information, see [How to find sid user and instance number of HANA db?](https://answers.sap.com/questions/555192/how-to-find-sid-user-and-instance-number-of-hana-d.html?spm=a2c4g.11186623.0.0.55c34b4ftZeXNK).
        self.sid = sid
        # Specifies whether to connect with the SAP HANA database over Secure Sockets Layer (SSL).
        self.use_ssl = use_ssl
        # The username of the SYSTEMDB database.
        self.user_name = user_name
        # Specifies whether to verify the SSL certificate of the SAP HANA database.
        self.validate_certificate = validate_certificate
        # The ID of the backup vault.
        # 
        # This parameter is required.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_setting is not None:
            result['AlertSetting'] = self.alert_setting
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.hana_name is not None:
            result['HanaName'] = self.hana_name
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number
        if self.password is not None:
            result['Password'] = self.password
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.use_ssl is not None:
            result['UseSsl'] = self.use_ssl
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.validate_certificate is not None:
            result['ValidateCertificate'] = self.validate_certificate
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertSetting') is not None:
            self.alert_setting = m.get('AlertSetting')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('HanaName') is not None:
            self.hana_name = m.get('HanaName')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('UseSsl') is not None:
            self.use_ssl = m.get('UseSsl')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('ValidateCertificate') is not None:
            self.validate_certificate = m.get('ValidateCertificate')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateHanaInstanceResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateHanaInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateHanaInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateHanaInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHanaRestoreRequest(TeaModel):
    def __init__(
        self,
        backup_id: int = None,
        backup_prefix: str = None,
        check_access: bool = None,
        clear_log: bool = None,
        cluster_id: str = None,
        database_name: str = None,
        log_position: int = None,
        master_client_id: str = None,
        mode: str = None,
        recovery_point_in_time: int = None,
        sid_admin: str = None,
        source: str = None,
        source_cluster_id: str = None,
        system_copy: bool = None,
        use_catalog: bool = None,
        use_delta: bool = None,
        vault_id: str = None,
        volume_id: int = None,
    ):
        # The ID of the backup.
        self.backup_id = backup_id
        # The backup prefix.
        # 
        # This parameter is required.
        self.backup_prefix = backup_prefix
        # Specifies whether to validate the differential backup and log backup. Valid values: true and false. If you set the value to true, HBR checks whether the required differential backup and log backup are available before the restore job starts. If the differential backup or log backup is unavailable, HBR does not start the restore job.
        self.check_access = check_access
        # Specifies whether to delete all log entries from the log area after the log entries are restored. Valid values: true and false. If you set the value to false, all log entries are deleted from the log area after the log entries are restored.
        self.clear_log = clear_log
        # The ID of the SAP HANA instance that you want to restore.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The name of the database that you want to restore.
        # 
        # This parameter is required.
        self.database_name = database_name
        # The log position to which you want to restore the database. This parameter is valid only if you set the Mode parameter to **RECOVERY_TO_LOG_POSITION**.
        self.log_position = log_position
        # The ID of the client where the primary node of the SAP HANA resides.
        self.master_client_id = master_client_id
        # The recovery mode. Valid values:
        # 
        # *   **RECOVERY_TO_MOST_RECENT**: restores the database to the recently available state to which the database has been backed up.
        # *   **RECOVERY_TO_POINT_IN_TIME**: restores the database to a specified point in time.
        # *   **RECOVERY_TO_SPECIFIC_BACKUP**: restores the database to a specified backup.
        # *   **RECOVERY_TO_LOG_POSITION**: restores the database to a specified log position.
        # 
        # This parameter is required.
        self.mode = mode
        # The point in time to which you want to restore the database. This parameter is valid only if you set the Mode parameter to **RECOVERY_TO_POINT_IN_TIME**. HBR restores the database to a state closest to the specified point in time.
        self.recovery_point_in_time = recovery_point_in_time
        # The SID admin account that is created by SAP HANA.
        self.sid_admin = sid_admin
        # The name of the source system. This parameter specifies the name of the source database that you want to restore. You must set the parameter in the `<Source database name>@SID` format.
        self.source = source
        # The ID of the source SAP HANA instance.
        self.source_cluster_id = source_cluster_id
        # Specifies whether to restore the database to a different instance.
        self.system_copy = system_copy
        # Specifies whether to use a catalog backup to restore the database. This parameter is required only if you set the Mode parameter to **RECOVERY_TO_SPECIFIC_BACKUP**. If you turn off Use Catalog, you must specify the prefix of a backup file. Then, Cloud Backup finds the backup file based on the specified prefix and restores the backup file.
        self.use_catalog = use_catalog
        # Specifies whether to use a differential backup or an incremental backup to restore the database. Valid values: true and false. If you want to use a differential backup or an incremental backup to restore the database, set the value to true. If you set the value to false, HBR uses a log backup to restore the database.
        self.use_delta = use_delta
        # The ID of the backup vault.
        self.vault_id = vault_id
        # The ID of the volume that you want to restore. This parameter is valid only if you set the Mode parameter to **RECOVERY_TO_LOG_POSITION**.
        self.volume_id = volume_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_prefix is not None:
            result['BackupPrefix'] = self.backup_prefix
        if self.check_access is not None:
            result['CheckAccess'] = self.check_access
        if self.clear_log is not None:
            result['ClearLog'] = self.clear_log
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.log_position is not None:
            result['LogPosition'] = self.log_position
        if self.master_client_id is not None:
            result['MasterClientId'] = self.master_client_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.recovery_point_in_time is not None:
            result['RecoveryPointInTime'] = self.recovery_point_in_time
        if self.sid_admin is not None:
            result['SidAdmin'] = self.sid_admin
        if self.source is not None:
            result['Source'] = self.source
        if self.source_cluster_id is not None:
            result['SourceClusterId'] = self.source_cluster_id
        if self.system_copy is not None:
            result['SystemCopy'] = self.system_copy
        if self.use_catalog is not None:
            result['UseCatalog'] = self.use_catalog
        if self.use_delta is not None:
            result['UseDelta'] = self.use_delta
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupPrefix') is not None:
            self.backup_prefix = m.get('BackupPrefix')
        if m.get('CheckAccess') is not None:
            self.check_access = m.get('CheckAccess')
        if m.get('ClearLog') is not None:
            self.clear_log = m.get('ClearLog')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('LogPosition') is not None:
            self.log_position = m.get('LogPosition')
        if m.get('MasterClientId') is not None:
            self.master_client_id = m.get('MasterClientId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RecoveryPointInTime') is not None:
            self.recovery_point_in_time = m.get('RecoveryPointInTime')
        if m.get('SidAdmin') is not None:
            self.sid_admin = m.get('SidAdmin')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceClusterId') is not None:
            self.source_cluster_id = m.get('SourceClusterId')
        if m.get('SystemCopy') is not None:
            self.system_copy = m.get('SystemCopy')
        if m.get('UseCatalog') is not None:
            self.use_catalog = m.get('UseCatalog')
        if m.get('UseDelta') is not None:
            self.use_delta = m.get('UseDelta')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        return self


class CreateHanaRestoreResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        restore_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The ID of the restore job.
        self.restore_id = restore_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.restore_id is not None:
            result['RestoreId'] = self.restore_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RestoreId') is not None:
            self.restore_id = m.get('RestoreId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateHanaRestoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateHanaRestoreResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateHanaRestoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsCommonFileSystemDetail(TeaModel):
    def __init__(
        self,
        fetch_slice_size: int = None,
        full_on_increment_fail: bool = None,
    ):
        # The size of backup shards (the number of files).
        self.fetch_slice_size = fetch_slice_size
        # Specifies whether the system performs full backup if incremental backup fails. Valid values:
        # 
        # *   **true**: The system performs full backup if incremental backup fails.
        # *   **false**: The system does not perform full backup if incremental backup fails.
        self.full_on_increment_fail = full_on_increment_fail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fetch_slice_size is not None:
            result['FetchSliceSize'] = self.fetch_slice_size
        if self.full_on_increment_fail is not None:
            result['FullOnIncrementFail'] = self.full_on_increment_fail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FetchSliceSize') is not None:
            self.fetch_slice_size = m.get('FetchSliceSize')
        if m.get('FullOnIncrementFail') is not None:
            self.full_on_increment_fail = m.get('FullOnIncrementFail')
        return self


class CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsCommonNasDetail(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        fetch_slice_size: int = None,
        full_on_increment_fail: bool = None,
    ):
        # The ID of the backup client group. When you perform on-premises NAS backup, Cloud Backup selects clients from the specified backup client group.
        self.cluster_id = cluster_id
        # The size of backup shards (the number of files).
        self.fetch_slice_size = fetch_slice_size
        # Specifies whether the system performs full backup if incremental backup fails. Valid values:
        # 
        # *   **true**: The system performs full backup if incremental backup fails.
        # *   **false**: The system does not perform full backup if incremental backup fails.
        self.full_on_increment_fail = full_on_increment_fail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.fetch_slice_size is not None:
            result['FetchSliceSize'] = self.fetch_slice_size
        if self.full_on_increment_fail is not None:
            result['FullOnIncrementFail'] = self.full_on_increment_fail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('FetchSliceSize') is not None:
            self.fetch_slice_size = m.get('FetchSliceSize')
        if m.get('FullOnIncrementFail') is not None:
            self.full_on_increment_fail = m.get('FullOnIncrementFail')
        return self


class CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsFileDetail(TeaModel):
    def __init__(
        self,
        adv_policy: bool = None,
        use_vss: bool = None,
    ):
        # Specifies whether to use an advanced policy. Valid values:
        # 
        # *   **true**: uses the advanced policy.
        # *   **false**: does not use the advanced policy.
        self.adv_policy = adv_policy
        # Specifies whether to enable the Volume Shadow Copy Service (VSS) feature. Valid values:
        # 
        # *   **true**: enables the feature.
        # *   **false**: disables the feature.
        self.use_vss = use_vss

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adv_policy is not None:
            result['AdvPolicy'] = self.adv_policy
        if self.use_vss is not None:
            result['UseVSS'] = self.use_vss
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvPolicy') is not None:
            self.adv_policy = m.get('AdvPolicy')
        if m.get('UseVSS') is not None:
            self.use_vss = m.get('UseVSS')
        return self


class CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsOssDetail(TeaModel):
    def __init__(
        self,
        ignore_archive_object: bool = None,
        inventory_cleanup_policy: str = None,
        inventory_id: str = None,
    ):
        # Do not prompt for archival type objects in task statistics and failed file lists.
        self.ignore_archive_object = ignore_archive_object
        # Specifies whether the system deletes the inventory lists when a backup is completed. This parameter is valid only when OSS inventories are used. Valid values:
        # 
        # *   **NO_CLEANUP**: does not delete inventory lists.
        # *   **DELETE_CURRENT**: deletes the current inventory list.
        # *   **DELETE_CURRENT_AND_PREVIOUS**: deletes all inventory lists.
        self.inventory_cleanup_policy = inventory_cleanup_policy
        # The name of the OSS inventory. If this parameter is not empty, the OSS inventory is used for performance optimization.
        # 
        # *   If you want to back up more than 100 million OSS objects, we recommend that you use inventory lists to accelerate incremental backup. Storage fees for inventory lists are included into your OSS bills.
        # *   A certain amount of time is required for OSS to generate inventory lists. Before inventory lists are generated, OSS objects may fail to be backed up. In this case, you can back up the OSS objects in the next backup cycle.
        self.inventory_id = inventory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ignore_archive_object is not None:
            result['IgnoreArchiveObject'] = self.ignore_archive_object
        if self.inventory_cleanup_policy is not None:
            result['InventoryCleanupPolicy'] = self.inventory_cleanup_policy
        if self.inventory_id is not None:
            result['InventoryId'] = self.inventory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoreArchiveObject') is not None:
            self.ignore_archive_object = m.get('IgnoreArchiveObject')
        if m.get('InventoryCleanupPolicy') is not None:
            self.inventory_cleanup_policy = m.get('InventoryCleanupPolicy')
        if m.get('InventoryId') is not None:
            self.inventory_id = m.get('InventoryId')
        return self


class CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsUdmDetail(TeaModel):
    def __init__(
        self,
        app_consistent: bool = None,
        disk_id_list: List[str] = None,
        enable_fs_freeze: bool = None,
        enable_writers: bool = None,
        exclude_disk_id_list: List[str] = None,
        post_script_path: str = None,
        pre_script_path: str = None,
        ram_role_name: str = None,
        snapshot_group: bool = None,
        timeout_in_seconds: int = None,
    ):
        # Specifies whether to enable application consistency. You can enable application consistency only if all disks are ESSDs.
        self.app_consistent = app_consistent
        # The IDs of the disks that need to be protected. If all disks need to be protected, this parameter is empty.
        self.disk_id_list = disk_id_list
        # This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies whether to enable Linux fsfreeze to put file systems into the read-only state before application-consistent snapshots are created. Default value: true.
        self.enable_fs_freeze = enable_fs_freeze
        # This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies whether to create application-consistent snapshots. Valid values:
        # 
        # *   true: creates application-consistent snapshots.
        # *   false: creates file system-consistent snapshots.
        # 
        # Default value: true.
        self.enable_writers = enable_writers
        # The IDs of the disks that do not need to be protected. If the DiskIdList parameter is not empty, this parameter is ignored.
        self.exclude_disk_id_list = exclude_disk_id_list
        # This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies the path of the post-thaw scripts that are executed after application-consistent snapshots are created.
        self.post_script_path = post_script_path
        # This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies the path of the pre-freeze scripts that are executed before application-consistent snapshots are created.
        self.pre_script_path = pre_script_path
        # This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies the name of the Resource Access Management (RAM) role that is required to create application-consistent snapshots.
        self.ram_role_name = ram_role_name
        # Specifies whether to create a snapshot-consistent group. You can create a snapshot-consistent group only if all disks are Enterprise SSDs (ESSDs).
        self.snapshot_group = snapshot_group
        # This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies the I/O freeze timeout period. Default value: 30. Unit: seconds.
        self.timeout_in_seconds = timeout_in_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_consistent is not None:
            result['AppConsistent'] = self.app_consistent
        if self.disk_id_list is not None:
            result['DiskIdList'] = self.disk_id_list
        if self.enable_fs_freeze is not None:
            result['EnableFsFreeze'] = self.enable_fs_freeze
        if self.enable_writers is not None:
            result['EnableWriters'] = self.enable_writers
        if self.exclude_disk_id_list is not None:
            result['ExcludeDiskIdList'] = self.exclude_disk_id_list
        if self.post_script_path is not None:
            result['PostScriptPath'] = self.post_script_path
        if self.pre_script_path is not None:
            result['PreScriptPath'] = self.pre_script_path
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.snapshot_group is not None:
            result['SnapshotGroup'] = self.snapshot_group
        if self.timeout_in_seconds is not None:
            result['TimeoutInSeconds'] = self.timeout_in_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppConsistent') is not None:
            self.app_consistent = m.get('AppConsistent')
        if m.get('DiskIdList') is not None:
            self.disk_id_list = m.get('DiskIdList')
        if m.get('EnableFsFreeze') is not None:
            self.enable_fs_freeze = m.get('EnableFsFreeze')
        if m.get('EnableWriters') is not None:
            self.enable_writers = m.get('EnableWriters')
        if m.get('ExcludeDiskIdList') is not None:
            self.exclude_disk_id_list = m.get('ExcludeDiskIdList')
        if m.get('PostScriptPath') is not None:
            self.post_script_path = m.get('PostScriptPath')
        if m.get('PreScriptPath') is not None:
            self.pre_script_path = m.get('PreScriptPath')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('SnapshotGroup') is not None:
            self.snapshot_group = m.get('SnapshotGroup')
        if m.get('TimeoutInSeconds') is not None:
            self.timeout_in_seconds = m.get('TimeoutInSeconds')
        return self


class CreatePolicyBindingsRequestPolicyBindingListAdvancedOptions(TeaModel):
    def __init__(
        self,
        common_file_system_detail: CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsCommonFileSystemDetail = None,
        common_nas_detail: CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsCommonNasDetail = None,
        file_detail: CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsFileDetail = None,
        oss_detail: CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsOssDetail = None,
        udm_detail: CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsUdmDetail = None,
    ):
        # The advanced options for CPFS backup.
        self.common_file_system_detail = common_file_system_detail
        # The advanced options for on-premises NAS backup.
        self.common_nas_detail = common_nas_detail
        # The advanced options for file backup.
        self.file_detail = file_detail
        # The advanced options for Object Storage Service (OSS) backup.
        self.oss_detail = oss_detail
        # The advanced options for ECS instance backup.
        self.udm_detail = udm_detail

    def validate(self):
        if self.common_file_system_detail:
            self.common_file_system_detail.validate()
        if self.common_nas_detail:
            self.common_nas_detail.validate()
        if self.file_detail:
            self.file_detail.validate()
        if self.oss_detail:
            self.oss_detail.validate()
        if self.udm_detail:
            self.udm_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_file_system_detail is not None:
            result['CommonFileSystemDetail'] = self.common_file_system_detail.to_map()
        if self.common_nas_detail is not None:
            result['CommonNasDetail'] = self.common_nas_detail.to_map()
        if self.file_detail is not None:
            result['FileDetail'] = self.file_detail.to_map()
        if self.oss_detail is not None:
            result['OssDetail'] = self.oss_detail.to_map()
        if self.udm_detail is not None:
            result['UdmDetail'] = self.udm_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonFileSystemDetail') is not None:
            temp_model = CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsCommonFileSystemDetail()
            self.common_file_system_detail = temp_model.from_map(m['CommonFileSystemDetail'])
        if m.get('CommonNasDetail') is not None:
            temp_model = CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsCommonNasDetail()
            self.common_nas_detail = temp_model.from_map(m['CommonNasDetail'])
        if m.get('FileDetail') is not None:
            temp_model = CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsFileDetail()
            self.file_detail = temp_model.from_map(m['FileDetail'])
        if m.get('OssDetail') is not None:
            temp_model = CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsOssDetail()
            self.oss_detail = temp_model.from_map(m['OssDetail'])
        if m.get('UdmDetail') is not None:
            temp_model = CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsUdmDetail()
            self.udm_detail = temp_model.from_map(m['UdmDetail'])
        return self


class CreatePolicyBindingsRequestPolicyBindingList(TeaModel):
    def __init__(
        self,
        advanced_options: CreatePolicyBindingsRequestPolicyBindingListAdvancedOptions = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        data_source_id: str = None,
        disabled: str = None,
        exclude: str = None,
        include: str = None,
        policy_binding_description: str = None,
        source: str = None,
        source_type: str = None,
        speed_limit: str = None,
    ):
        # The advanced options.
        self.advanced_options = advanced_options
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Specifies whether to back up and restore data within the same Alibaba Cloud account or across Alibaba Cloud accounts. Default value: SELF_ACCOUNT. Valid values:
        # 
        # *   **SELF_ACCOUNT**: backs up data within the same Alibaba Cloud account.
        # *   **CROSS_ACCOUNT**: backs up data across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The ID of the data source. The meaning of this parameter depends on the **SourceType** parameter. Valid values:
        # 
        # *   **UDM_ECS**: the ID of the Elastic Compute Service (ECS) instance
        # *   **OSS**: the name of the Object Storage Service (OSS) bucket
        # *   **NAS**: the ID of the File Storage NAS (NAS) file system
        # *   **COMMON_NAS**: the ID of the on-premises NAS file system
        # *   **ECS_FILE**: the ID of the ECS instance
        # *   **File**: the ID of the Cloud Backup client
        # *   **COMMON_FILE_SYSTEM**: the ID of the Cloud Parallel File Storage (CPFS) backup data source
        self.data_source_id = data_source_id
        # Specifies whether to disable the backup policy for the data source. Valid values:
        # 
        # *   true: disables the backup policy for the data source
        # *   false: enables the backup policy for the data source
        self.disabled = disabled
        # This parameter is required only if you set the **SourceType** parameter to **ECS_FILE**, **File**, **NAS**, **COMMON_NAS**, or **COMMON_FILE_SYSTEM**. This parameter specifies the type of files that do not need to be backed up. No files of the specified type are backed up. The value can be up to 255 characters in length.
        self.exclude = exclude
        # This parameter is required only if you set the **SourceType** parameter to **ECS_FILE**, **File**, **NAS**, **COMMON_NAS**, or **COMMON_FILE_SYSTEM**. This parameter specifies the type of files to be backed up. All files of the specified type are backed up. The value can be up to 255 characters in length.
        self.include = include
        # The description of the association.
        self.policy_binding_description = policy_binding_description
        # *   If the SourceType parameter is set to **OSS**, set the Source parameter to the prefix of the path to the folder that you want to back up. If you do not specify the Source parameter, the entire bucket (root directory) is backed up.
        # *   If the SourceType parameter is set to **ECS_FILE** or **File**, set the Source parameter to the path to the files that you want to back up. If you do not specify the Source parameter, all paths are backed up.
        # *   This parameter is required if the SourceType parameter is set to **COMMON_FILE_SYSTEM**. This parameter specifies the path to be backed up. To back up the /src path, enter ["/src"]. To back up the root path, enter ["/"].
        self.source = source
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instance
        # *   **OSS**: OSS bucket
        # *   **NAS**: NAS file system
        # *   **COMMON_NAS**: on-premises NAS file system
        # *   **ECS_FILE**: ECS file
        # *   **File**: on-premises file
        # *   **COMMON_FILE_SYSTEM**: CPFS file system
        self.source_type = source_type
        # This parameter is required only if you set the **SourceType** parameter to **ECS_FILE** or **File**. This parameter specifies the throttling rules. Format: `{start}{end}{bandwidth}`. Separate multiple throttling rules with vertical bars (|). The time ranges of the throttling rules cannot overlap.
        # 
        # *   **start**: the start hour.
        # *   **end**: the end hour.
        # *   **bandwidth**: the bandwidth. Unit: KB/s.
        self.speed_limit = speed_limit

    def validate(self):
        if self.advanced_options:
            self.advanced_options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_options is not None:
            result['AdvancedOptions'] = self.advanced_options.to_map()
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.include is not None:
            result['Include'] = self.include
        if self.policy_binding_description is not None:
            result['PolicyBindingDescription'] = self.policy_binding_description
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedOptions') is not None:
            temp_model = CreatePolicyBindingsRequestPolicyBindingListAdvancedOptions()
            self.advanced_options = temp_model.from_map(m['AdvancedOptions'])
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('PolicyBindingDescription') is not None:
            self.policy_binding_description = m.get('PolicyBindingDescription')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        return self


class CreatePolicyBindingsRequest(TeaModel):
    def __init__(
        self,
        policy_binding_list: List[CreatePolicyBindingsRequestPolicyBindingList] = None,
        policy_id: str = None,
    ):
        # The data sources that you want to bind to the backup policy.
        self.policy_binding_list = policy_binding_list
        # The ID of the backup policy.
        self.policy_id = policy_id

    def validate(self):
        if self.policy_binding_list:
            for k in self.policy_binding_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PolicyBindingList'] = []
        if self.policy_binding_list is not None:
            for k in self.policy_binding_list:
                result['PolicyBindingList'].append(k.to_map() if k else None)
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy_binding_list = []
        if m.get('PolicyBindingList') is not None:
            for k in m.get('PolicyBindingList'):
                temp_model = CreatePolicyBindingsRequestPolicyBindingList()
                self.policy_binding_list.append(temp_model.from_map(k))
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class CreatePolicyBindingsShrinkRequest(TeaModel):
    def __init__(
        self,
        policy_binding_list_shrink: str = None,
        policy_id: str = None,
    ):
        # The data sources that you want to bind to the backup policy.
        self.policy_binding_list_shrink = policy_binding_list_shrink
        # The ID of the backup policy.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_binding_list_shrink is not None:
            result['PolicyBindingList'] = self.policy_binding_list_shrink
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyBindingList') is not None:
            self.policy_binding_list_shrink = m.get('PolicyBindingList')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class CreatePolicyBindingsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePolicyBindingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePolicyBindingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePolicyBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyV2RequestRulesDataSourceFilters(TeaModel):
    def __init__(
        self,
        data_source_ids: List[str] = None,
        source_type: str = None,
    ):
        # This parameter is deprecated.
        self.data_source_ids = data_source_ids
        # The type of the data source. Valid value:
        # 
        # *   **UDM_ECS**: Elastic Compute Service (ECS) instance This type of data source is supported only if the **PolicyType** parameter is set to **UDM_ECS_ONLY**.
        # *   **OSS**: Object Storage Service (OSS) bucket This type of data source is supported only if the **PolicyType** parameter is set to **STANDARD**.
        # *   **NAS**: File Storage NAS (NAS) file system This type of data source is supported only if the **PolicyType** parameter is set to **STANDARD**.
        # *   **ECS_FILE**: ECS file This type of data source is supported only if the **PolicyType** parameter is set to **STANDARD**.
        # *   **OTS**: Tablestore instance This type of data source is supported only if the **PolicyType** parameter is set to **STANDARD**.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_ids is not None:
            result['DataSourceIds'] = self.data_source_ids
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceIds') is not None:
            self.data_source_ids = m.get('DataSourceIds')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class CreatePolicyV2RequestRulesRetentionRules(TeaModel):
    def __init__(
        self,
        advanced_retention_type: str = None,
        retention: int = None,
        which_snapshot: int = None,
    ):
        # The type of the special retention rule. Valid values:
        # 
        # *   **DAILY**: retains daily backups
        # *   **WEEKLY**: retains weekly backups
        # *   **MONTHLY**: retains monthly backups
        # *   **YEARLY**: retains yearly backups
        self.advanced_retention_type = advanced_retention_type
        # The special retention period of backups. Minimum value: 1. Unit: days.
        self.retention = retention
        # Specifies which backup is retained based on the special retention rule. Only the first backup can be retained.
        self.which_snapshot = which_snapshot

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_retention_type is not None:
            result['AdvancedRetentionType'] = self.advanced_retention_type
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.which_snapshot is not None:
            result['WhichSnapshot'] = self.which_snapshot
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedRetentionType') is not None:
            self.advanced_retention_type = m.get('AdvancedRetentionType')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('WhichSnapshot') is not None:
            self.which_snapshot = m.get('WhichSnapshot')
        return self


class CreatePolicyV2RequestRulesTagFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag-based matching rule. Valid values:
        # 
        # *   **EQUAL**: Both the tag key and tag value are matched.
        # *   **NOT**: The tag key is matched and the tag value is not matched.
        self.operator = operator
        # The tag value. If you leave this parameter empty, the value is any value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreatePolicyV2RequestRules(TeaModel):
    def __init__(
        self,
        backup_type: str = None,
        data_source_filters: List[CreatePolicyV2RequestRulesDataSourceFilters] = None,
        immutable: bool = None,
        keep_latest_snapshots: int = None,
        replication_region_id: str = None,
        retention: int = None,
        retention_rules: List[CreatePolicyV2RequestRulesRetentionRules] = None,
        rule_type: str = None,
        schedule: str = None,
        tag_filters: List[CreatePolicyV2RequestRulesTagFilters] = None,
        vault_id: str = None,
    ):
        # This parameter is required only if the **RuleType** parameter is set to **BACKUP**. This parameter specifies the backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # This parameter is required only if the **RuleType** parameter is set to **TAG**. This parameter specifies the data source filter rule.
        self.data_source_filters = data_source_filters
        # This parameter is required only if the **PolicyType** parameter is set to **UDM_ECS_ONLY**. This parameter specifies whether to enable the immutable backup feature.
        self.immutable = immutable
        # Specifies whether to enable the feature of keeping at least one backup version. Valid values:
        # 
        # *   0: The feature is disabled.
        # *   1: The feature is enabled.
        self.keep_latest_snapshots = keep_latest_snapshots
        # This parameter is required only if the **RuleType** parameter is set to **REPLICATION**. This parameter specifies the ID of the destination region.
        self.replication_region_id = replication_region_id
        # This parameter is required only if the **RuleType** parameter is set to **BACKUP**, **TRANSITION** or **REPLICATION**.
        # 
        # *   If the **RuleType** parameter is set to **BACKUP**, this parameter specifies the retention period of the backup data. The priority is lower than the Retention field of the rule with RuleType=TRANSITION. Minimum value: 1. Maximum value: 364635. Unit: days.
        # *   If the **RuleType** parameter is set to **TRANSITION**, this parameter specifies the retention period of the backup data. Minimum value: 1. Maximum value: 364635. Unit: days.
        # *   If the **RuleType** parameter is set to **REPLICATION**, this parameter specifies the retention period of remote backups. Minimum value: 1. Maximum value: 364635. Unit: days.
        self.retention = retention
        # This parameter is required only if the **RuleType** parameter is set to **TRANSITION**. This parameter specifies the special retention rules.
        self.retention_rules = retention_rules
        # The type of the rule. Each backup policy must have at least one rule of the **BACKUP** type and only one rule of the **TRANSITION** type. Valid values:
        # 
        # *   **BACKUP**: backup rule
        # *   **TRANSITION**: lifecycle rule
        # *   **REPLICATION**: replication rule
        # *   **TAG**: tag rule
        # 
        # This parameter is required.
        self.rule_type = rule_type
        # This parameter is required only if the **RuleType** parameter is set to **BACKUP**. This parameter specifies the backup schedule settings. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   startTime: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of 1 hour. P1D specifies an interval of one day.
        self.schedule = schedule
        # This parameter is required only if the **RuleType** parameter is set to **TAG**. This parameter specifies the resource tag filter rule.
        self.tag_filters = tag_filters
        # This parameter is required only if the RuleType parameter is set to BACKUP. The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        if self.data_source_filters:
            for k in self.data_source_filters:
                if k:
                    k.validate()
        if self.retention_rules:
            for k in self.retention_rules:
                if k:
                    k.validate()
        if self.tag_filters:
            for k in self.tag_filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        result['DataSourceFilters'] = []
        if self.data_source_filters is not None:
            for k in self.data_source_filters:
                result['DataSourceFilters'].append(k.to_map() if k else None)
        if self.immutable is not None:
            result['Immutable'] = self.immutable
        if self.keep_latest_snapshots is not None:
            result['KeepLatestSnapshots'] = self.keep_latest_snapshots
        if self.replication_region_id is not None:
            result['ReplicationRegionId'] = self.replication_region_id
        if self.retention is not None:
            result['Retention'] = self.retention
        result['RetentionRules'] = []
        if self.retention_rules is not None:
            for k in self.retention_rules:
                result['RetentionRules'].append(k.to_map() if k else None)
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        result['TagFilters'] = []
        if self.tag_filters is not None:
            for k in self.tag_filters:
                result['TagFilters'].append(k.to_map() if k else None)
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        self.data_source_filters = []
        if m.get('DataSourceFilters') is not None:
            for k in m.get('DataSourceFilters'):
                temp_model = CreatePolicyV2RequestRulesDataSourceFilters()
                self.data_source_filters.append(temp_model.from_map(k))
        if m.get('Immutable') is not None:
            self.immutable = m.get('Immutable')
        if m.get('KeepLatestSnapshots') is not None:
            self.keep_latest_snapshots = m.get('KeepLatestSnapshots')
        if m.get('ReplicationRegionId') is not None:
            self.replication_region_id = m.get('ReplicationRegionId')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        self.retention_rules = []
        if m.get('RetentionRules') is not None:
            for k in m.get('RetentionRules'):
                temp_model = CreatePolicyV2RequestRulesRetentionRules()
                self.retention_rules.append(temp_model.from_map(k))
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        self.tag_filters = []
        if m.get('TagFilters') is not None:
            for k in m.get('TagFilters'):
                temp_model = CreatePolicyV2RequestRulesTagFilters()
                self.tag_filters.append(temp_model.from_map(k))
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreatePolicyV2Request(TeaModel):
    def __init__(
        self,
        policy_description: str = None,
        policy_name: str = None,
        policy_type: str = None,
        rules: List[CreatePolicyV2RequestRules] = None,
    ):
        # The description of the backup policy.
        self.policy_description = policy_description
        # The name of the backup policy.
        self.policy_name = policy_name
        # The policy type. Valid values:
        # 
        # *   **STANDARD**: the general backup policy. This type of policy applies to backups other than Elastic Compute Service (ECS) instance backup.
        # *   **UDM_ECS_ONLY**: This type of policy applies only to ECS instance backup.
        # 
        # If the policy type is not specified, Cloud Backup automatically sets the policy type based on whether the backup vault is specified in the rules of the policy:
        # 
        # *   If the backup vault is specified, Cloud Backup sets the policy type to **STANDARD**.
        # *   If the backup vault is not specified, Cloud Backup sets the policy type to **UDM_ECS_ONLY**.
        self.policy_type = policy_type
        # The rules in the backup policy.
        self.rules = rules

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = CreatePolicyV2RequestRules()
                self.rules.append(temp_model.from_map(k))
        return self


class CreatePolicyV2ShrinkRequest(TeaModel):
    def __init__(
        self,
        policy_description: str = None,
        policy_name: str = None,
        policy_type: str = None,
        rules_shrink: str = None,
    ):
        # The description of the backup policy.
        self.policy_description = policy_description
        # The name of the backup policy.
        self.policy_name = policy_name
        # The policy type. Valid values:
        # 
        # *   **STANDARD**: the general backup policy. This type of policy applies to backups other than Elastic Compute Service (ECS) instance backup.
        # *   **UDM_ECS_ONLY**: This type of policy applies only to ECS instance backup.
        # 
        # If the policy type is not specified, Cloud Backup automatically sets the policy type based on whether the backup vault is specified in the rules of the policy:
        # 
        # *   If the backup vault is specified, Cloud Backup sets the policy type to **STANDARD**.
        # *   If the backup vault is not specified, Cloud Backup sets the policy type to **UDM_ECS_ONLY**.
        self.policy_type = policy_type
        # The rules in the backup policy.
        self.rules_shrink = rules_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.rules_shrink is not None:
            result['Rules'] = self.rules_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('Rules') is not None:
            self.rules_shrink = m.get('Rules')
        return self


class CreatePolicyV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        policy_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the backup policy.
        self.policy_id = policy_id
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePolicyV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePolicyV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePolicyV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateReplicationVaultRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        encrypt_type: str = None,
        kms_key_id: str = None,
        redundancy_type: str = None,
        replication_source_region_id: str = None,
        replication_source_vault_id: str = None,
        vault_name: str = None,
        vault_region_id: str = None,
        vault_storage_class: str = None,
    ):
        # The description of the backup vault. The description must be 0 to 255 characters in length.
        self.description = description
        # The method that is used to encrypt the source data. This parameter is valid only if you set the VaultType parameter to STANDARD or OTS_BACKUP. Valid values:
        # 
        # *   **HBR_PRIVATE**: The source data is encrypted by using the built-in encryption method of Hybrid Backup Recovery (HBR).
        # *   **KMS**: The source data is encrypted by using Key Management Service (KMS).
        self.encrypt_type = encrypt_type
        # The customer master key (CMK) created in KMS or the alias of the key. This parameter is required only if you set the EncryptType parameter to KMS.
        self.kms_key_id = kms_key_id
        # The data redundancy type of the backup vault. Valid values:
        # 
        # *   LRS: standard locally redundant storage (LRS). Cloud Backup stores the copies of each object on multiple devices of different facilities in the same zone. This way, Cloud Backup ensures data durability and availability even if hardware failures occur.
        # *   ZRS: standard zone-redundant storage (ZRS). Cloud Backup uses the multi-zone mechanism to distribute data across three zones within the same region. If a zone fails, the data that is stored in the other two zones is still accessible.
        self.redundancy_type = redundancy_type
        # The ID of the region where the source vault resides.
        # 
        # This parameter is required.
        self.replication_source_region_id = replication_source_region_id
        # The ID of the source vault.
        # 
        # This parameter is required.
        self.replication_source_vault_id = replication_source_vault_id
        # The name of the backup vault. The name must be 1 to 64 characters in length.
        # 
        # This parameter is required.
        self.vault_name = vault_name
        # The ID of the region where the backup vault resides.
        # 
        # This parameter is required.
        self.vault_region_id = vault_region_id
        # The storage type of the backup vault. Valid value: **STANDARD**, which indicates standard storage.
        self.vault_storage_class = vault_storage_class

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id
        if self.redundancy_type is not None:
            result['RedundancyType'] = self.redundancy_type
        if self.replication_source_region_id is not None:
            result['ReplicationSourceRegionId'] = self.replication_source_region_id
        if self.replication_source_vault_id is not None:
            result['ReplicationSourceVaultId'] = self.replication_source_vault_id
        if self.vault_name is not None:
            result['VaultName'] = self.vault_name
        if self.vault_region_id is not None:
            result['VaultRegionId'] = self.vault_region_id
        if self.vault_storage_class is not None:
            result['VaultStorageClass'] = self.vault_storage_class
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')
        if m.get('RedundancyType') is not None:
            self.redundancy_type = m.get('RedundancyType')
        if m.get('ReplicationSourceRegionId') is not None:
            self.replication_source_region_id = m.get('ReplicationSourceRegionId')
        if m.get('ReplicationSourceVaultId') is not None:
            self.replication_source_vault_id = m.get('ReplicationSourceVaultId')
        if m.get('VaultName') is not None:
            self.vault_name = m.get('VaultName')
        if m.get('VaultRegionId') is not None:
            self.vault_region_id = m.get('VaultRegionId')
        if m.get('VaultStorageClass') is not None:
            self.vault_storage_class = m.get('VaultStorageClass')
        return self


class CreateReplicationVaultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
        vault_id: str = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The ID of the job that is used to initialize the backup vault. You can call the DescribeTask operation to query the job status.
        self.task_id = task_id
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateReplicationVaultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateReplicationVaultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateReplicationVaultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRestoreJobRequest(TeaModel):
    def __init__(
        self,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        exclude: str = None,
        failback_detail: Dict[str, Any] = None,
        include: str = None,
        initiated_by_ack: bool = None,
        options: str = None,
        ots_detail: OtsTableRestoreDetail = None,
        restore_type: str = None,
        snapshot_hash: str = None,
        snapshot_id: str = None,
        source_type: str = None,
        target_bucket: str = None,
        target_container: str = None,
        target_container_cluster_id: str = None,
        target_create_time: int = None,
        target_file_system_id: str = None,
        target_instance_id: str = None,
        target_instance_name: str = None,
        target_path: str = None,
        target_prefix: str = None,
        target_table_name: str = None,
        target_time: int = None,
        udm_detail: Dict[str, Any] = None,
        udm_region_id: str = None,
        vault_id: str = None,
    ):
        # The name of the role created in the RAM of the original account for cross-account backup managed by the current account.
        self.cross_account_role_name = cross_account_role_name
        # Cross-account backup type. Supported values:
        # - SELF_ACCOUNT: Backup within the same account
        # - CROSS_ACCOUNT: Cross-account backup
        self.cross_account_type = cross_account_type
        # The original account ID managed by the current account for cross-account backup.
        self.cross_account_user_id = cross_account_user_id
        # The path not to be restored. All documents under this path will not be restored. Maximum length is 255 characters.
        self.exclude = exclude
        # Details of restoring to the local environment.
        self.failback_detail = failback_detail
        # The path to be restored. All documents under this path will be restored. Maximum length is 255 characters.
        self.include = include
        # Indicates whether it is called by the container service. Default is false.
        self.initiated_by_ack = initiated_by_ack
        # Parameters for the restore job.
        self.options = options
        # Details of the Table Store instance.
        self.ots_detail = ots_detail
        # The type of the restore destination data source. Possible values:
        #   - **ECS_FILE**: Restore to ECS file.
        #   - **OSS**: Restore to Alibaba Cloud OSS.
        #   - **NAS**: Restore to Alibaba Cloud NAS.
        #   - **OTS_TABLE**: Restore to Alibaba Cloud OTS.
        #   - **UDM_ECS_ROLLBACK**: Restore to Alibaba Cloud ECS whole machine.
        # 
        # This parameter is required.
        self.restore_type = restore_type
        # The HASH value of the backup snapshot.
        self.snapshot_hash = snapshot_hash
        # The ID of the backup snapshot.
        self.snapshot_id = snapshot_id
        # The type of the data source. Possible values:
        #   - **ECS_FILE**: Restore ECS file.
        #   - **OSS**: Restore Alibaba Cloud OSS.
        #   - **NAS**: Restore Alibaba Cloud NAS.
        #   - **OTS_TABLE**: Restore to Alibaba Cloud OTS.
        #   - **UDM_ECS**: Restore to Alibaba Cloud ECS whole machine.
        # 
        # This parameter is required.
        self.source_type = source_type
        # Valid only when **RestoreType** is **OSS**. Indicates the name of the OSS bucket at the restore destination.
        self.target_bucket = target_bucket
        # Details of the target container.
        self.target_container = target_container
        # The ID of the target container cluster.
        self.target_container_cluster_id = target_container_cluster_id
        # Valid only when **RestoreType** is **NAS**. Indicates the creation time of the file system at the restore destination.
        self.target_create_time = target_create_time
        # Valid only when **RestoreType** is **NAS**. Indicates the ID of the file system at the restore destination.
        self.target_file_system_id = target_file_system_id
        # Valid only when **RestoreType** is **ECS_FILE**. Indicates the ECS instance ID at the restore destination.
        self.target_instance_id = target_instance_id
        # The name of the target Table Store instance.
        self.target_instance_name = target_instance_name
        # Valid only when **RestoreType** is **ECS_FILE**. Indicates the file path at the restore destination.
        self.target_path = target_path
        # Valid only when **RestoreType** is **OSS**. Indicates the object prefix at the restore destination.
        self.target_prefix = target_prefix
        # The name of the data table in the target Table Store.
        self.target_table_name = target_table_name
        # The time of the Table Store to be restored. UNIX timestamp, in seconds.
        self.target_time = target_time
        # Details of the whole machine backup.
        self.udm_detail = udm_detail
        # Valid only when **SourceType** is **UDM_ECS**. Indicates the target region for the restore.
        self.udm_region_id = udm_region_id
        # The ID of the backup vault that the snapshot belongs to.
        self.vault_id = vault_id

    def validate(self):
        if self.ots_detail:
            self.ots_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.failback_detail is not None:
            result['FailbackDetail'] = self.failback_detail
        if self.include is not None:
            result['Include'] = self.include
        if self.initiated_by_ack is not None:
            result['InitiatedByAck'] = self.initiated_by_ack
        if self.options is not None:
            result['Options'] = self.options
        if self.ots_detail is not None:
            result['OtsDetail'] = self.ots_detail.to_map()
        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type
        if self.snapshot_hash is not None:
            result['SnapshotHash'] = self.snapshot_hash
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.target_bucket is not None:
            result['TargetBucket'] = self.target_bucket
        if self.target_container is not None:
            result['TargetContainer'] = self.target_container
        if self.target_container_cluster_id is not None:
            result['TargetContainerClusterId'] = self.target_container_cluster_id
        if self.target_create_time is not None:
            result['TargetCreateTime'] = self.target_create_time
        if self.target_file_system_id is not None:
            result['TargetFileSystemId'] = self.target_file_system_id
        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id
        if self.target_instance_name is not None:
            result['TargetInstanceName'] = self.target_instance_name
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.target_prefix is not None:
            result['TargetPrefix'] = self.target_prefix
        if self.target_table_name is not None:
            result['TargetTableName'] = self.target_table_name
        if self.target_time is not None:
            result['TargetTime'] = self.target_time
        if self.udm_detail is not None:
            result['UdmDetail'] = self.udm_detail
        if self.udm_region_id is not None:
            result['UdmRegionId'] = self.udm_region_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('FailbackDetail') is not None:
            self.failback_detail = m.get('FailbackDetail')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('InitiatedByAck') is not None:
            self.initiated_by_ack = m.get('InitiatedByAck')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OtsDetail') is not None:
            temp_model = OtsTableRestoreDetail()
            self.ots_detail = temp_model.from_map(m['OtsDetail'])
        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')
        if m.get('SnapshotHash') is not None:
            self.snapshot_hash = m.get('SnapshotHash')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('TargetBucket') is not None:
            self.target_bucket = m.get('TargetBucket')
        if m.get('TargetContainer') is not None:
            self.target_container = m.get('TargetContainer')
        if m.get('TargetContainerClusterId') is not None:
            self.target_container_cluster_id = m.get('TargetContainerClusterId')
        if m.get('TargetCreateTime') is not None:
            self.target_create_time = m.get('TargetCreateTime')
        if m.get('TargetFileSystemId') is not None:
            self.target_file_system_id = m.get('TargetFileSystemId')
        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')
        if m.get('TargetInstanceName') is not None:
            self.target_instance_name = m.get('TargetInstanceName')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TargetPrefix') is not None:
            self.target_prefix = m.get('TargetPrefix')
        if m.get('TargetTableName') is not None:
            self.target_table_name = m.get('TargetTableName')
        if m.get('TargetTime') is not None:
            self.target_time = m.get('TargetTime')
        if m.get('UdmDetail') is not None:
            self.udm_detail = m.get('UdmDetail')
        if m.get('UdmRegionId') is not None:
            self.udm_region_id = m.get('UdmRegionId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateRestoreJobShrinkRequest(TeaModel):
    def __init__(
        self,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        exclude: str = None,
        failback_detail_shrink: str = None,
        include: str = None,
        initiated_by_ack: bool = None,
        options: str = None,
        ots_detail_shrink: str = None,
        restore_type: str = None,
        snapshot_hash: str = None,
        snapshot_id: str = None,
        source_type: str = None,
        target_bucket: str = None,
        target_container: str = None,
        target_container_cluster_id: str = None,
        target_create_time: int = None,
        target_file_system_id: str = None,
        target_instance_id: str = None,
        target_instance_name: str = None,
        target_path: str = None,
        target_prefix: str = None,
        target_table_name: str = None,
        target_time: int = None,
        udm_detail_shrink: str = None,
        udm_region_id: str = None,
        vault_id: str = None,
    ):
        # The name of the role created in the RAM of the original account for cross-account backup managed by the current account.
        self.cross_account_role_name = cross_account_role_name
        # Cross-account backup type. Supported values:
        # - SELF_ACCOUNT: Backup within the same account
        # - CROSS_ACCOUNT: Cross-account backup
        self.cross_account_type = cross_account_type
        # The original account ID managed by the current account for cross-account backup.
        self.cross_account_user_id = cross_account_user_id
        # The path not to be restored. All documents under this path will not be restored. Maximum length is 255 characters.
        self.exclude = exclude
        # Details of restoring to the local environment.
        self.failback_detail_shrink = failback_detail_shrink
        # The path to be restored. All documents under this path will be restored. Maximum length is 255 characters.
        self.include = include
        # Indicates whether it is called by the container service. Default is false.
        self.initiated_by_ack = initiated_by_ack
        # Parameters for the restore job.
        self.options = options
        # Details of the Table Store instance.
        self.ots_detail_shrink = ots_detail_shrink
        # The type of the restore destination data source. Possible values:
        #   - **ECS_FILE**: Restore to ECS file.
        #   - **OSS**: Restore to Alibaba Cloud OSS.
        #   - **NAS**: Restore to Alibaba Cloud NAS.
        #   - **OTS_TABLE**: Restore to Alibaba Cloud OTS.
        #   - **UDM_ECS_ROLLBACK**: Restore to Alibaba Cloud ECS whole machine.
        # 
        # This parameter is required.
        self.restore_type = restore_type
        # The HASH value of the backup snapshot.
        self.snapshot_hash = snapshot_hash
        # The ID of the backup snapshot.
        self.snapshot_id = snapshot_id
        # The type of the data source. Possible values:
        #   - **ECS_FILE**: Restore ECS file.
        #   - **OSS**: Restore Alibaba Cloud OSS.
        #   - **NAS**: Restore Alibaba Cloud NAS.
        #   - **OTS_TABLE**: Restore to Alibaba Cloud OTS.
        #   - **UDM_ECS**: Restore to Alibaba Cloud ECS whole machine.
        # 
        # This parameter is required.
        self.source_type = source_type
        # Valid only when **RestoreType** is **OSS**. Indicates the name of the OSS bucket at the restore destination.
        self.target_bucket = target_bucket
        # Details of the target container.
        self.target_container = target_container
        # The ID of the target container cluster.
        self.target_container_cluster_id = target_container_cluster_id
        # Valid only when **RestoreType** is **NAS**. Indicates the creation time of the file system at the restore destination.
        self.target_create_time = target_create_time
        # Valid only when **RestoreType** is **NAS**. Indicates the ID of the file system at the restore destination.
        self.target_file_system_id = target_file_system_id
        # Valid only when **RestoreType** is **ECS_FILE**. Indicates the ECS instance ID at the restore destination.
        self.target_instance_id = target_instance_id
        # The name of the target Table Store instance.
        self.target_instance_name = target_instance_name
        # Valid only when **RestoreType** is **ECS_FILE**. Indicates the file path at the restore destination.
        self.target_path = target_path
        # Valid only when **RestoreType** is **OSS**. Indicates the object prefix at the restore destination.
        self.target_prefix = target_prefix
        # The name of the data table in the target Table Store.
        self.target_table_name = target_table_name
        # The time of the Table Store to be restored. UNIX timestamp, in seconds.
        self.target_time = target_time
        # Details of the whole machine backup.
        self.udm_detail_shrink = udm_detail_shrink
        # Valid only when **SourceType** is **UDM_ECS**. Indicates the target region for the restore.
        self.udm_region_id = udm_region_id
        # The ID of the backup vault that the snapshot belongs to.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.failback_detail_shrink is not None:
            result['FailbackDetail'] = self.failback_detail_shrink
        if self.include is not None:
            result['Include'] = self.include
        if self.initiated_by_ack is not None:
            result['InitiatedByAck'] = self.initiated_by_ack
        if self.options is not None:
            result['Options'] = self.options
        if self.ots_detail_shrink is not None:
            result['OtsDetail'] = self.ots_detail_shrink
        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type
        if self.snapshot_hash is not None:
            result['SnapshotHash'] = self.snapshot_hash
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.target_bucket is not None:
            result['TargetBucket'] = self.target_bucket
        if self.target_container is not None:
            result['TargetContainer'] = self.target_container
        if self.target_container_cluster_id is not None:
            result['TargetContainerClusterId'] = self.target_container_cluster_id
        if self.target_create_time is not None:
            result['TargetCreateTime'] = self.target_create_time
        if self.target_file_system_id is not None:
            result['TargetFileSystemId'] = self.target_file_system_id
        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id
        if self.target_instance_name is not None:
            result['TargetInstanceName'] = self.target_instance_name
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.target_prefix is not None:
            result['TargetPrefix'] = self.target_prefix
        if self.target_table_name is not None:
            result['TargetTableName'] = self.target_table_name
        if self.target_time is not None:
            result['TargetTime'] = self.target_time
        if self.udm_detail_shrink is not None:
            result['UdmDetail'] = self.udm_detail_shrink
        if self.udm_region_id is not None:
            result['UdmRegionId'] = self.udm_region_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('FailbackDetail') is not None:
            self.failback_detail_shrink = m.get('FailbackDetail')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('InitiatedByAck') is not None:
            self.initiated_by_ack = m.get('InitiatedByAck')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OtsDetail') is not None:
            self.ots_detail_shrink = m.get('OtsDetail')
        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')
        if m.get('SnapshotHash') is not None:
            self.snapshot_hash = m.get('SnapshotHash')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('TargetBucket') is not None:
            self.target_bucket = m.get('TargetBucket')
        if m.get('TargetContainer') is not None:
            self.target_container = m.get('TargetContainer')
        if m.get('TargetContainerClusterId') is not None:
            self.target_container_cluster_id = m.get('TargetContainerClusterId')
        if m.get('TargetCreateTime') is not None:
            self.target_create_time = m.get('TargetCreateTime')
        if m.get('TargetFileSystemId') is not None:
            self.target_file_system_id = m.get('TargetFileSystemId')
        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')
        if m.get('TargetInstanceName') is not None:
            self.target_instance_name = m.get('TargetInstanceName')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TargetPrefix') is not None:
            self.target_prefix = m.get('TargetPrefix')
        if m.get('TargetTableName') is not None:
            self.target_table_name = m.get('TargetTableName')
        if m.get('TargetTime') is not None:
            self.target_time = m.get('TargetTime')
        if m.get('UdmDetail') is not None:
            self.udm_detail_shrink = m.get('UdmDetail')
        if m.get('UdmRegionId') is not None:
            self.udm_region_id = m.get('UdmRegionId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateRestoreJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        restore_id: str = None,
        success: bool = None,
    ):
        # Return code, 200 indicates success.
        self.code = code
        # Description of the return message, usually \\"successful\\" when successful, and corresponding error messages when there is an error.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Restore job ID.
        self.restore_id = restore_id
        # Whether the request was successful.
        #   - true: Success
        #   - false: Failure
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.restore_id is not None:
            result['RestoreId'] = self.restore_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RestoreId') is not None:
            self.restore_id = m.get('RestoreId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRestoreJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRestoreJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRestoreJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTempFileUploadUrlRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
    ):
        # The name of the file to be uploaded.
        # 
        # This parameter is required.
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class CreateTempFileUploadUrlResponseBody(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        code: str = None,
        endpoint: str = None,
        expire_time: int = None,
        message: str = None,
        oss_access_key_id: str = None,
        policy: str = None,
        request_id: str = None,
        signature: str = None,
        success: bool = None,
        temp_file_key: str = None,
    ):
        # The name of the OSS bucket to which the file is uploaded.
        self.bucket_name = bucket_name
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The endpoint that is used to upload the file to OSS.
        self.endpoint = endpoint
        # The expiration time of the signature that is used to upload the file to OSS. This value is a UNIX timestamp. Unit: seconds.
        self.expire_time = expire_time
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The AccessKey ID that is used to upload the file to OSS.
        self.oss_access_key_id = oss_access_key_id
        # The policy that is used to upload the file to OSS.
        self.policy = policy
        # The ID of the request.
        self.request_id = request_id
        # The signature that is used to upload the file to OSS.
        self.signature = signature
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The key that is used to upload the file to OSS.
        self.temp_file_key = temp_file_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.code is not None:
            result['Code'] = self.code
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.message is not None:
            result['Message'] = self.message
        if self.oss_access_key_id is not None:
            result['OssAccessKeyId'] = self.oss_access_key_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.success is not None:
            result['Success'] = self.success
        if self.temp_file_key is not None:
            result['TempFileKey'] = self.temp_file_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OssAccessKeyId') is not None:
            self.oss_access_key_id = m.get('OssAccessKeyId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TempFileKey') is not None:
            self.temp_file_key = m.get('TempFileKey')
        return self


class CreateTempFileUploadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTempFileUploadUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTempFileUploadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVaultRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        encrypt_type: str = None,
        kms_key_id: str = None,
        vault_name: str = None,
        vault_region_id: str = None,
        vault_storage_class: str = None,
        vault_type: str = None,
        worm_enabled: bool = None,
    ):
        # The description of the backup vault. The description must be 0 to 255 characters in length.
        self.description = description
        # The method that is used to encrypt the source data. This parameter is valid only if you set the VaultType parameter to STANDARD or OTS_BACKUP. Valid values:
        # 
        # *   **HBR_PRIVATE**: The source data is encrypted by using the built-in encryption method of Hybrid Backup Recovery (HBR).
        # *   **KMS**: The source data is encrypted by using Key Management Service (KMS).
        self.encrypt_type = encrypt_type
        # The customer master key (CMK) created in KMS or the alias of the key. This parameter is required only if you set the EncryptType parameter to KMS.
        self.kms_key_id = kms_key_id
        # The name of the backup vault. The name must be 1 to 64 characters in length.
        # 
        # This parameter is required.
        self.vault_name = vault_name
        # The ID of the region where the backup vault resides.
        # 
        # This parameter is required.
        self.vault_region_id = vault_region_id
        # The storage type of the backup vault. Valid value: 
        # - **STANDARD**: standard storage.
        # - **ARCHIVE**: deprected.
        # - **COLD_ARCHIVE**: deprected.
        # - **IA**: deprected.
        self.vault_storage_class = vault_storage_class
        # The type of the backup vault. Valid values:
        # 
        # *   **STANDARD**: standard backup vault
        # *   **OTS_BACKUP**: backup vault for Tablestore
        self.vault_type = vault_type
        # Whether to enable the vault worm feature. Once the worm feature is enabled, the vault and all its backup data cannot be deleted before they automatically expire. After enabling the worm feature, it is not supported to disable it. The worm feature is only effective for standard and archive backup vault.
        self.worm_enabled = worm_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id
        if self.vault_name is not None:
            result['VaultName'] = self.vault_name
        if self.vault_region_id is not None:
            result['VaultRegionId'] = self.vault_region_id
        if self.vault_storage_class is not None:
            result['VaultStorageClass'] = self.vault_storage_class
        if self.vault_type is not None:
            result['VaultType'] = self.vault_type
        if self.worm_enabled is not None:
            result['WormEnabled'] = self.worm_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')
        if m.get('VaultName') is not None:
            self.vault_name = m.get('VaultName')
        if m.get('VaultRegionId') is not None:
            self.vault_region_id = m.get('VaultRegionId')
        if m.get('VaultStorageClass') is not None:
            self.vault_storage_class = m.get('VaultStorageClass')
        if m.get('VaultType') is not None:
            self.vault_type = m.get('VaultType')
        if m.get('WormEnabled') is not None:
            self.worm_enabled = m.get('WormEnabled')
        return self


class CreateVaultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
        vault_id: str = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The ID of the initialization task used to initialize the backup vault. You can call the DescribeTask operation to query the status of an initialization task.
        self.task_id = task_id
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateVaultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVaultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVaultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAirEcsInstanceRequest(TeaModel):
    def __init__(
        self,
        ecs_instance_id: str = None,
        uninstall_client_source_types: List[str] = None,
    ):
        # The ID of the ECS instance.
        self.ecs_instance_id = ecs_instance_id
        # The data sources for which the client needs to be uninstalled.
        self.uninstall_client_source_types = uninstall_client_source_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.uninstall_client_source_types is not None:
            result['UninstallClientSourceTypes'] = self.uninstall_client_source_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('UninstallClientSourceTypes') is not None:
            self.uninstall_client_source_types = m.get('UninstallClientSourceTypes')
        return self


class DeleteAirEcsInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        ecs_instance_id: str = None,
        uninstall_client_source_types_shrink: str = None,
    ):
        # The ID of the ECS instance.
        self.ecs_instance_id = ecs_instance_id
        # The data sources for which the client needs to be uninstalled.
        self.uninstall_client_source_types_shrink = uninstall_client_source_types_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.uninstall_client_source_types_shrink is not None:
            result['UninstallClientSourceTypes'] = self.uninstall_client_source_types_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('UninstallClientSourceTypes') is not None:
            self.uninstall_client_source_types_shrink = m.get('UninstallClientSourceTypes')
        return self


class DeleteAirEcsInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The ID of the asynchronous job. You can call the DescribeTask operation to query the execution result of an asynchronous job.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteAirEcsInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAirEcsInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAirEcsInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBackupClientRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
    ):
        # The ID of the Cloud Backup client.
        # 
        # This parameter is required.
        self.client_id = client_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        return self


class DeleteBackupClientResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteBackupClientResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBackupClientResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteBackupClientResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBackupClientResourceRequest(TeaModel):
    def __init__(
        self,
        client_ids: Dict[str, Any] = None,
    ):
        # The IDs of HBR clients. The value can be a JSON array that consists of up to 100 client IDs. Separate the IDs with commas (,).
        # 
        # This parameter is required.
        self.client_ids = client_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        return self


class DeleteBackupClientResourceShrinkRequest(TeaModel):
    def __init__(
        self,
        client_ids_shrink: str = None,
    ):
        # The IDs of HBR clients. The value can be a JSON array that consists of up to 100 client IDs. Separate the IDs with commas (,).
        # 
        # This parameter is required.
        self.client_ids_shrink = client_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids_shrink is not None:
            result['ClientIds'] = self.client_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids_shrink = m.get('ClientIds')
        return self


class DeleteBackupClientResourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteBackupClientResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBackupClientResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteBackupClientResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBackupPlanRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        require_no_running_jobs: bool = None,
        source_type: str = None,
        vault_id: str = None,
    ):
        # The ID of the backup plan.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # Specifies whether no running jobs are required.
        self.require_no_running_jobs = require_no_running_jobs
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS file systems
        # *   **UDM_ECS**: ECS instances
        # *   **OTS**: Tablestore instances
        self.source_type = source_type
        # The ID of the backup vault. This parameter is required if the SourceType parameter is not set to UDM_ECS.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.require_no_running_jobs is not None:
            result['RequireNoRunningJobs'] = self.require_no_running_jobs
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RequireNoRunningJobs') is not None:
            self.require_no_running_jobs = m.get('RequireNoRunningJobs')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DeleteBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClientRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        resource_group_id: str = None,
        vault_id: str = None,
    ):
        # The ID of the client.
        self.client_id = client_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DeleteClientResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteClientResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteClientResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteClientResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHanaBackupPlanRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        plan_id: str = None,
        resource_group_id: str = None,
        vault_id: str = None,
    ):
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the backup plan.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the backup vault.
        # 
        # This parameter is required.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DeleteHanaBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteHanaBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteHanaBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteHanaBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHanaInstanceRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        resource_group_id: str = None,
        sid: str = None,
        vault_id: str = None,
    ):
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The security identifier (SID) of the SAP HANA database. You must specify a valid SID. The SID must be three characters in length and start with a letter. For more information, see [How to find sid user and instance number of HANA db?](https://answers.sap.com/questions/555192/how-to-find-sid-user-and-instance-number-of-hana-d.html?)
        # 
        # This parameter is required.
        self.sid = sid
        # The ID of the backup vault.
        # 
        # This parameter is required.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DeleteHanaInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteHanaInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteHanaInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteHanaInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyBindingRequest(TeaModel):
    def __init__(
        self,
        data_source_ids: List[str] = None,
        policy_id: str = None,
        source_type: str = None,
    ):
        # The IDs of the data sources that you want to disassociate from the backup policy.
        self.data_source_ids = data_source_ids
        # The ID of the backup policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instance backup
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_ids is not None:
            result['DataSourceIds'] = self.data_source_ids
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceIds') is not None:
            self.data_source_ids = m.get('DataSourceIds')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class DeletePolicyBindingShrinkRequest(TeaModel):
    def __init__(
        self,
        data_source_ids_shrink: str = None,
        policy_id: str = None,
        source_type: str = None,
    ):
        # The IDs of the data sources that you want to disassociate from the backup policy.
        self.data_source_ids_shrink = data_source_ids_shrink
        # The ID of the backup policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instance backup
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_ids_shrink is not None:
            result['DataSourceIds'] = self.data_source_ids_shrink
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceIds') is not None:
            self.data_source_ids_shrink = m.get('DataSourceIds')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class DeletePolicyBindingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeletePolicyBindingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePolicyBindingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePolicyBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyV2Request(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
    ):
        # The ID of the backup policy.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class DeletePolicyV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeletePolicyV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePolicyV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePolicyV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSnapshotRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        force: bool = None,
        instance_id: str = None,
        snapshot_id: str = None,
        source_type: str = None,
        token: str = None,
        vault_id: str = None,
    ):
        # The ID of the Cloud Backup client. If you delete a backup snapshot for Elastic Compute Service (ECS) instances, you must specify one of the ClientId and **InstanceId** parameters.
        self.client_id = client_id
        # Specifies whether to forcibly delete the most recent backup snapshot. Valid values:
        # 
        # *   true: The system forcibly deletes the most recent backup snapshot.
        # *   false (default): The system does not forcibly delete the most recent backup snapshot.
        self.force = force
        # The ID of the ECS instance. If you delete a backup snapshot for ECS instances, you must specify one of the InstanceId and **ClientId** parameters.
        self.instance_id = instance_id
        # The ID of the backup snapshot.
        # 
        # This parameter is required.
        self.snapshot_id = snapshot_id
        # The type of the backup source. Valid values:
        # 
        # *   **ECS_FILE**: backup snapshots for ECS files
        # *   **OSS**: backup snapshots for Object Storage Service (OSS) buckets
        # *   **NAS**: backup snapshots for Apsara File Storage NAS (NAS) file systems
        self.source_type = source_type
        # The token that you want to delete.
        self.token = token
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.force is not None:
            result['Force'] = self.force
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.token is not None:
            result['Token'] = self.token
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DeleteSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUdmDiskRequest(TeaModel):
    def __init__(
        self,
        disk_id: str = None,
    ):
        # The disk ID.
        self.disk_id = disk_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        return self


class DeleteUdmDiskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUdmDiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUdmDiskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteUdmDiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUdmEcsInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The ID of the ECS instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteUdmEcsInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUdmEcsInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUdmEcsInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteUdmEcsInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVaultRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        token: str = None,
        vault_id: str = None,
    ):
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The token.
        self.token = token
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.token is not None:
            result['Token'] = self.token
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DeleteVaultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteVaultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVaultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteVaultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupClientsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the backup vault. Valid values of N: 1 to 20.
        # 
        # *   The tag key cannot start with `aliyun` or `acs:`.
        # *   The tag key cannot contain `http://` or `https://`.
        # *   The tag key cannot be an empty string.
        self.key = key
        # The tag value of the backup vault. Valid values of N: 1 to 20.
        # 
        # *   The tag value cannot start with `aliyun` or `acs:`.
        # *   The tag value cannot contain `http://` or `https://`.
        # *   The tag value cannot be an empty string.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeBackupClientsRequest(TeaModel):
    def __init__(
        self,
        client_ids: List[str] = None,
        client_type: str = None,
        cluster_id: str = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        instance_ids: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        tag: List[DescribeBackupClientsRequestTag] = None,
    ):
        # The IDs of HBR clients.
        self.client_ids = client_ids
        # The type of the HBR client. Valid values:
        # 
        # *   **ECS_CLIENT**: HBR client for Elastic Compute Service (ECS) file backup
        # *   **CONTAINER_CLIENT**: HBR client for container backup
        # 
        # This parameter is required.
        self.client_type = client_type
        # The ID of the cluster for the backup.
        self.cluster_id = cluster_id
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The IDs of ECS instances.
        self.instance_ids = instance_ids
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeBackupClientsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeBackupClientsShrinkRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the backup vault. Valid values of N: 1 to 20.
        # 
        # *   The tag key cannot start with `aliyun` or `acs:`.
        # *   The tag key cannot contain `http://` or `https://`.
        # *   The tag key cannot be an empty string.
        self.key = key
        # The tag value of the backup vault. Valid values of N: 1 to 20.
        # 
        # *   The tag value cannot start with `aliyun` or `acs:`.
        # *   The tag value cannot contain `http://` or `https://`.
        # *   The tag value cannot be an empty string.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeBackupClientsShrinkRequest(TeaModel):
    def __init__(
        self,
        client_ids_shrink: str = None,
        client_type: str = None,
        cluster_id: str = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        instance_ids_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        tag: List[DescribeBackupClientsShrinkRequestTag] = None,
    ):
        # The IDs of HBR clients.
        self.client_ids_shrink = client_ids_shrink
        # The type of the HBR client. Valid values:
        # 
        # *   **ECS_CLIENT**: HBR client for Elastic Compute Service (ECS) file backup
        # *   **CONTAINER_CLIENT**: HBR client for container backup
        # 
        # This parameter is required.
        self.client_type = client_type
        # The ID of the cluster for the backup.
        self.cluster_id = cluster_id
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The IDs of ECS instances.
        self.instance_ids_shrink = instance_ids_shrink
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids_shrink is not None:
            result['ClientIds'] = self.client_ids_shrink
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids_shrink = m.get('ClientIds')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeBackupClientsShrinkRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeBackupClientsResponseBodyClientsSettings(TeaModel):
    def __init__(
        self,
        alert_on_partial_complete: bool = None,
        data_network_type: str = None,
        data_proxy_setting: str = None,
        max_cpu_core: str = None,
        max_memory: int = None,
        max_worker: str = None,
        proxy_host: str = None,
        proxy_password: str = None,
        proxy_port: int = None,
        proxy_user: str = None,
        use_https: str = None,
    ):
        # Indicates whether alerts are generated for partially completed jobs. This parameter is valid only for on-premises file backup and ECS file backup.
        self.alert_on_partial_complete = alert_on_partial_complete
        # The type of the endpoint on the data plane. Valid values:
        # 
        # *   **PUBLIC**: Internet
        # *   **VPC**: virtual private cloud (VPC)
        # *   **CLASSIC**: classic network
        self.data_network_type = data_network_type
        # The proxy configuration on the data plane. Valid values:
        # 
        # *   **DISABLE**: The proxy is not used.
        # *   **USE_CONTROL_PROXY** (default): The configuration is the same as that on the control plane.
        # *   **CUSTOM**: The configuration is customized (HTTP).
        self.data_proxy_setting = data_proxy_setting
        # The number of CPU cores used by a single backup job. The value 0 indicates that the number is unlimited.
        self.max_cpu_core = max_cpu_core
        # The maximum memory that can be used by the client. Unit: bytes. Only V2.13.0 and later are supported.
        self.max_memory = max_memory
        # The number of concurrent backup jobs. The value 0 indicates that the number is unlimited.
        self.max_worker = max_worker
        # The custom host IP address of the proxy server on the data plane.
        self.proxy_host = proxy_host
        # The custom password of the proxy server on the data plane.
        self.proxy_password = proxy_password
        # The custom host port of the proxy server on the data plane.
        self.proxy_port = proxy_port
        # The custom username of the proxy server on the data plane.
        self.proxy_user = proxy_user
        # Indicates whether data on the data plane is transmitted over HTTPS. Valid values:
        # 
        # *   true: Data is transmitted over HTTPS.
        # *   false: Data is transmitted over HTTP.
        self.use_https = use_https

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_on_partial_complete is not None:
            result['AlertOnPartialComplete'] = self.alert_on_partial_complete
        if self.data_network_type is not None:
            result['DataNetworkType'] = self.data_network_type
        if self.data_proxy_setting is not None:
            result['DataProxySetting'] = self.data_proxy_setting
        if self.max_cpu_core is not None:
            result['MaxCpuCore'] = self.max_cpu_core
        if self.max_memory is not None:
            result['MaxMemory'] = self.max_memory
        if self.max_worker is not None:
            result['MaxWorker'] = self.max_worker
        if self.proxy_host is not None:
            result['ProxyHost'] = self.proxy_host
        if self.proxy_password is not None:
            result['ProxyPassword'] = self.proxy_password
        if self.proxy_port is not None:
            result['ProxyPort'] = self.proxy_port
        if self.proxy_user is not None:
            result['ProxyUser'] = self.proxy_user
        if self.use_https is not None:
            result['UseHttps'] = self.use_https
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertOnPartialComplete') is not None:
            self.alert_on_partial_complete = m.get('AlertOnPartialComplete')
        if m.get('DataNetworkType') is not None:
            self.data_network_type = m.get('DataNetworkType')
        if m.get('DataProxySetting') is not None:
            self.data_proxy_setting = m.get('DataProxySetting')
        if m.get('MaxCpuCore') is not None:
            self.max_cpu_core = m.get('MaxCpuCore')
        if m.get('MaxMemory') is not None:
            self.max_memory = m.get('MaxMemory')
        if m.get('MaxWorker') is not None:
            self.max_worker = m.get('MaxWorker')
        if m.get('ProxyHost') is not None:
            self.proxy_host = m.get('ProxyHost')
        if m.get('ProxyPassword') is not None:
            self.proxy_password = m.get('ProxyPassword')
        if m.get('ProxyPort') is not None:
            self.proxy_port = m.get('ProxyPort')
        if m.get('ProxyUser') is not None:
            self.proxy_user = m.get('ProxyUser')
        if m.get('UseHttps') is not None:
            self.use_https = m.get('UseHttps')
        return self


class DescribeBackupClientsResponseBodyClientsTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the backup vault. Valid values of N: 1 to 20
        # 
        # *   The tag key cannot start with `aliyun` or `acs:`.
        # *   The tag key cannot contain `http://` or `https://`.
        # *   The tag key cannot be an empty string.
        self.key = key
        # The tag value of the backup vault. Valid values of N: 1 to 20
        # 
        # *   The tag value cannot start with `aliyun` or `acs:`.
        # *   The tag value cannot contain `http://` or `https://`.
        # *   The tag value cannot be an empty string.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeBackupClientsResponseBodyClients(TeaModel):
    def __init__(
        self,
        appliance: bool = None,
        arch_type: str = None,
        backup_status: str = None,
        client_id: str = None,
        client_type: str = None,
        client_version: str = None,
        created_time: int = None,
        hostname: str = None,
        instance_id: str = None,
        instance_name: str = None,
        last_heart_beat_time: int = None,
        max_client_version: str = None,
        os_type: str = None,
        private_ip_v4: str = None,
        settings: DescribeBackupClientsResponseBodyClientsSettings = None,
        status: str = None,
        tags: List[DescribeBackupClientsResponseBodyClientsTags] = None,
        updated_time: int = None,
        zone_id: str = None,
    ):
        # Indicates whether the client is installed on an all-in-one PC that integrates hardware and monitoring program. Valid values:
        # 
        # *   true: The client is installed on an all-in-one PC that integrates hardware and monitoring program.
        # *   false: The client is not installed on an all-in-one PC that integrates hardware and monitoring program.
        self.appliance = appliance
        # This parameter is valid only if the **ClientType** parameter is set to **ECS_CLIENT**. This parameter indicates the system architecture where the backup client resides. Valid values:
        # 
        # *   **amd64**\
        # *   **386**\
        self.arch_type = arch_type
        # The protection status of the backup client. Valid values:
        # 
        # *   **UNPROTECTED**: The backup client is not protected.
        # *   **PROTECTED**: The backup client is protected.
        self.backup_status = backup_status
        # The ID of the backup client.
        self.client_id = client_id
        # The type of the backup client. Valid value: **ECS_CLIENT**, which indicates a client for ECS file backup.
        self.client_type = client_type
        # The version number of the backup client.
        self.client_version = client_version
        # The time when the backup client was created. The value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The hostname of the backup client.
        self.hostname = hostname
        # The instance ID.
        # 
        # *   If the client is used to back up ECS files, this parameter indicates the ID of an ECS instance.
        # *   If the client is used to back up on-premises files, this parameter indicates the hardware fingerprint that is generated based on the system information.
        self.instance_id = instance_id
        # This parameter is valid only if the **ClientType** parameter is set to **ECS_CLIENT**. This parameter indicates the name of the ECS instance.
        self.instance_name = instance_name
        # The last heartbeat time of the backup client. The value is a UNIX timestamp. Unit: seconds.
        self.last_heart_beat_time = last_heart_beat_time
        # The latest version number of the backup client.
        self.max_client_version = max_client_version
        # This parameter is valid only if the **ClientType** parameter is set to **ECS_CLIENT**. This parameter indicates the operating system type of the backup client. Valid values:
        # 
        # *   **windows**\
        # *   **linux**\
        self.os_type = os_type
        # This parameter is valid only if the **ClientType** parameter is set to **ECS_CLIENT**. This parameter indicates the internal IP address of the ECS instance.
        self.private_ip_v4 = private_ip_v4
        # The configuration information of the backup client.
        self.settings = settings
        # The status of the backup client. Valid values:
        # 
        # *   **REGISTERED**: The backup client is registered.
        # *   **ACTIVATED**: The backup client is activated.
        # *   **DEACTIVATED**: The backup client fails to be activated.
        # *   **INSTALLING**: The backup client is being installed.
        # *   **INSTALL_FAILED**: The backup client fails to be installed.
        # *   **NOT_INSTALLED**: The backup client is not installed.
        # *   **UPGRADING**: The backup client is being upgraded.
        # *   **UPGRADE_FAILED**: The backup client fails to be upgraded.
        # *   **UNINSTALLING**: The backup client is being uninstalled.
        # *   **UNINSTALL_FAILED**: The backup client fails to be uninstalled.
        # *   **STOPPED**: The backup client is out of service.
        # *   **UNKNOWN**: The backup client is disconnected.
        self.status = status
        # The tag information.
        self.tags = tags
        # The time when the backup client was updated. The value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time
        # This parameter is valid only if the **ClientType** parameter is set to **ECS_CLIENT**. This parameter indicates the zone of the backup client.
        self.zone_id = zone_id

    def validate(self):
        if self.settings:
            self.settings.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appliance is not None:
            result['Appliance'] = self.appliance
        if self.arch_type is not None:
            result['ArchType'] = self.arch_type
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.last_heart_beat_time is not None:
            result['LastHeartBeatTime'] = self.last_heart_beat_time
        if self.max_client_version is not None:
            result['MaxClientVersion'] = self.max_client_version
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.private_ip_v4 is not None:
            result['PrivateIpV4'] = self.private_ip_v4
        if self.settings is not None:
            result['Settings'] = self.settings.to_map()
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Appliance') is not None:
            self.appliance = m.get('Appliance')
        if m.get('ArchType') is not None:
            self.arch_type = m.get('ArchType')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('LastHeartBeatTime') is not None:
            self.last_heart_beat_time = m.get('LastHeartBeatTime')
        if m.get('MaxClientVersion') is not None:
            self.max_client_version = m.get('MaxClientVersion')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PrivateIpV4') is not None:
            self.private_ip_v4 = m.get('PrivateIpV4')
        if m.get('Settings') is not None:
            temp_model = DescribeBackupClientsResponseBodyClientsSettings()
            self.settings = temp_model.from_map(m['Settings'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeBackupClientsResponseBodyClientsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeBackupClientsResponseBody(TeaModel):
    def __init__(
        self,
        clients: List[DescribeBackupClientsResponseBodyClients] = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The queried backup clients.
        self.clients = clients
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The page number of the returned page. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries returned on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The total number of returned HBR clients that meet the specified conditions.
        self.total_count = total_count

    def validate(self):
        if self.clients:
            for k in self.clients:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clients'] = []
        if self.clients is not None:
            for k in self.clients:
                result['Clients'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clients = []
        if m.get('Clients') is not None:
            for k in m.get('Clients'):
                temp_model = DescribeBackupClientsResponseBodyClients()
                self.clients.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBackupClientsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupClientsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBackupClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupJobs2RequestFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # The keys in the filter. Valid values:
        # 
        # *   **RegionId**: the ID of a region
        # *   **PlanId**: the ID of a backup plan
        # *   **JobId**: the ID of a backup job
        # *   **VaultId**: the ID of a backup vault
        # *   **InstanceId**: the ID of an ECS instance
        # *   **Bucket**: the name of an OSS bucket
        # *   **FileSystemId**: the ID of a file system
        # *   **Status**: the status of a backup job
        # *   **CreatedTime**: the start time of a backup job
        # *   **CompleteTime**: the end time of a backup job
        # *   **instanceName**: the name of a Tablestore instance
        self.key = key
        # The matching method. Default value: IN. This parameter specifies the operator that you want to use to match a key and a value in the filter. Valid values:
        # 
        # *   **EQUAL**: equal to
        # *   **NOT_EQUAL**: not equal to
        # *   **GREATER_THAN**: greater than
        # *   **GREATER_THAN_OR_EQUAL**: greater than or equal to
        # *   **LESS_THAN**: less than
        # *   **LESS_THAN_OR_EQUAL**: less than or equal to
        # *   **BETWEEN**: specifies a JSON array as a range. The results must fall within the range in the `[Minimum value,maximum value]` format.
        # *   **IN**: specifies an array as a collection. The results must fall within the collection.
        # 
        # >  If you specify **CompleteTime** as a key to query backup jobs, you cannot use the IN operator to perform a match.
        self.operator = operator
        # The values that you want to match in the filter.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeBackupJobs2Request(TeaModel):
    def __init__(
        self,
        filters: List[DescribeBackupJobs2RequestFilters] = None,
        page_number: int = None,
        page_size: int = None,
        sort_direction: str = None,
        source_type: str = None,
    ):
        # The keys that you want to match in the filter.
        self.filters = filters
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The order in which you want to sort the results. Valid values:
        # 
        # *   **ASCEND**: sorts the results in ascending order
        # *   **DESCEND** (default value): sorts the results in descending order
        self.sort_direction = sort_direction
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS file systems
        # *   **OTS**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        # *   **UDM_ECS_DISK**: ECS disks
        self.source_type = source_type

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = DescribeBackupJobs2RequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class DescribeBackupJobs2ResponseBodyBackupJobsBackupJobDetailDiskNativeSnapshotIdList(TeaModel):
    def __init__(
        self,
        disk_native_snapshot_id: List[str] = None,
    ):
        self.disk_native_snapshot_id = disk_native_snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_native_snapshot_id is not None:
            result['DiskNativeSnapshotId'] = self.disk_native_snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskNativeSnapshotId') is not None:
            self.disk_native_snapshot_id = m.get('DiskNativeSnapshotId')
        return self


class DescribeBackupJobs2ResponseBodyBackupJobsBackupJobDetail(TeaModel):
    def __init__(
        self,
        destination_native_snapshot_error_message: str = None,
        destination_native_snapshot_id: str = None,
        destination_native_snapshot_progress: int = None,
        destination_native_snapshot_status: str = None,
        destination_retention: int = None,
        destination_snapshot_id: str = None,
        disk_native_snapshot_id_list: DescribeBackupJobs2ResponseBodyBackupJobsBackupJobDetailDiskNativeSnapshotIdList = None,
        do_copy: bool = None,
        instance_infos: Dict[str, Any] = None,
        native_snapshot_id: str = None,
    ):
        # The information about the remote replication failure.
        self.destination_native_snapshot_error_message = destination_native_snapshot_error_message
        # The ID of the remote replication snapshot.
        self.destination_native_snapshot_id = destination_native_snapshot_id
        # The progress of the remote replication.
        self.destination_native_snapshot_progress = destination_native_snapshot_progress
        # The state of the remote replication.
        self.destination_native_snapshot_status = destination_native_snapshot_status
        # The retention period of the remote replication backup.
        self.destination_retention = destination_retention
        # The ID of the remote replication backup.
        self.destination_snapshot_id = destination_snapshot_id
        # The mapping between snapshots and disks.
        self.disk_native_snapshot_id_list = disk_native_snapshot_id_list
        # Indicates whether remote replication is enabled.
        self.do_copy = do_copy
        # The ecs instance infos.
        self.instance_infos = instance_infos
        # The ID of the backup snapshot.
        self.native_snapshot_id = native_snapshot_id

    def validate(self):
        if self.disk_native_snapshot_id_list:
            self.disk_native_snapshot_id_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_native_snapshot_error_message is not None:
            result['DestinationNativeSnapshotErrorMessage'] = self.destination_native_snapshot_error_message
        if self.destination_native_snapshot_id is not None:
            result['DestinationNativeSnapshotId'] = self.destination_native_snapshot_id
        if self.destination_native_snapshot_progress is not None:
            result['DestinationNativeSnapshotProgress'] = self.destination_native_snapshot_progress
        if self.destination_native_snapshot_status is not None:
            result['DestinationNativeSnapshotStatus'] = self.destination_native_snapshot_status
        if self.destination_retention is not None:
            result['DestinationRetention'] = self.destination_retention
        if self.destination_snapshot_id is not None:
            result['DestinationSnapshotId'] = self.destination_snapshot_id
        if self.disk_native_snapshot_id_list is not None:
            result['DiskNativeSnapshotIdList'] = self.disk_native_snapshot_id_list.to_map()
        if self.do_copy is not None:
            result['DoCopy'] = self.do_copy
        if self.instance_infos is not None:
            result['InstanceInfos'] = self.instance_infos
        if self.native_snapshot_id is not None:
            result['NativeSnapshotId'] = self.native_snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationNativeSnapshotErrorMessage') is not None:
            self.destination_native_snapshot_error_message = m.get('DestinationNativeSnapshotErrorMessage')
        if m.get('DestinationNativeSnapshotId') is not None:
            self.destination_native_snapshot_id = m.get('DestinationNativeSnapshotId')
        if m.get('DestinationNativeSnapshotProgress') is not None:
            self.destination_native_snapshot_progress = m.get('DestinationNativeSnapshotProgress')
        if m.get('DestinationNativeSnapshotStatus') is not None:
            self.destination_native_snapshot_status = m.get('DestinationNativeSnapshotStatus')
        if m.get('DestinationRetention') is not None:
            self.destination_retention = m.get('DestinationRetention')
        if m.get('DestinationSnapshotId') is not None:
            self.destination_snapshot_id = m.get('DestinationSnapshotId')
        if m.get('DiskNativeSnapshotIdList') is not None:
            temp_model = DescribeBackupJobs2ResponseBodyBackupJobsBackupJobDetailDiskNativeSnapshotIdList()
            self.disk_native_snapshot_id_list = temp_model.from_map(m['DiskNativeSnapshotIdList'])
        if m.get('DoCopy') is not None:
            self.do_copy = m.get('DoCopy')
        if m.get('InstanceInfos') is not None:
            self.instance_infos = m.get('InstanceInfos')
        if m.get('NativeSnapshotId') is not None:
            self.native_snapshot_id = m.get('NativeSnapshotId')
        return self


class DescribeBackupJobs2ResponseBodyBackupJobsBackupJobOtsDetailTableNames(TeaModel):
    def __init__(
        self,
        table_name: List[str] = None,
    ):
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeBackupJobs2ResponseBodyBackupJobsBackupJobOtsDetail(TeaModel):
    def __init__(
        self,
        table_names: DescribeBackupJobs2ResponseBodyBackupJobsBackupJobOtsDetailTableNames = None,
    ):
        # The names of the destination tables in the Tablestore instance.
        self.table_names = table_names

    def validate(self):
        if self.table_names:
            self.table_names.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_names is not None:
            result['TableNames'] = self.table_names.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableNames') is not None:
            temp_model = DescribeBackupJobs2ResponseBodyBackupJobsBackupJobOtsDetailTableNames()
            self.table_names = temp_model.from_map(m['TableNames'])
        return self


class DescribeBackupJobs2ResponseBodyBackupJobsBackupJobPaths(TeaModel):
    def __init__(
        self,
        path: List[str] = None,
    ):
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeBackupJobs2ResponseBodyBackupJobsBackupJobReport(TeaModel):
    def __init__(
        self,
        failed_files: str = None,
        report_task_status: str = None,
        skipped_files: str = None,
        success_files: str = None,
        total_files: str = None,
    ):
        # List of failed files
        self.failed_files = failed_files
        # Report generation status.
        self.report_task_status = report_task_status
        # List of skipped files
        self.skipped_files = skipped_files
        # List of successful files.
        self.success_files = success_files
        # List of all files. (This field is not returned for data synchronization)
        self.total_files = total_files

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_files is not None:
            result['FailedFiles'] = self.failed_files
        if self.report_task_status is not None:
            result['ReportTaskStatus'] = self.report_task_status
        if self.skipped_files is not None:
            result['SkippedFiles'] = self.skipped_files
        if self.success_files is not None:
            result['SuccessFiles'] = self.success_files
        if self.total_files is not None:
            result['TotalFiles'] = self.total_files
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedFiles') is not None:
            self.failed_files = m.get('FailedFiles')
        if m.get('ReportTaskStatus') is not None:
            self.report_task_status = m.get('ReportTaskStatus')
        if m.get('SkippedFiles') is not None:
            self.skipped_files = m.get('SkippedFiles')
        if m.get('SuccessFiles') is not None:
            self.success_files = m.get('SuccessFiles')
        if m.get('TotalFiles') is not None:
            self.total_files = m.get('TotalFiles')
        return self


class DescribeBackupJobs2ResponseBodyBackupJobsBackupJob(TeaModel):
    def __init__(
        self,
        actual_bytes: int = None,
        actual_files: int = None,
        actual_items: int = None,
        backup_type: str = None,
        bucket: str = None,
        bytes_done: int = None,
        bytes_total: int = None,
        change_list_path: str = None,
        client_id: str = None,
        complete_time: int = None,
        create_time: int = None,
        created_time: int = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        dest_data_source_detail: str = None,
        dest_data_source_id: str = None,
        dest_source_type: str = None,
        detail: DescribeBackupJobs2ResponseBodyBackupJobsBackupJobDetail = None,
        error_message: str = None,
        exclude: str = None,
        file_system_id: str = None,
        files_done: int = None,
        files_total: int = None,
        identifier: str = None,
        include: str = None,
        instance_id: str = None,
        instance_name: str = None,
        items_done: int = None,
        items_total: int = None,
        job_id: str = None,
        job_name: str = None,
        options: str = None,
        ots_detail: DescribeBackupJobs2ResponseBodyBackupJobsBackupJobOtsDetail = None,
        paths: DescribeBackupJobs2ResponseBodyBackupJobsBackupJobPaths = None,
        plan_id: str = None,
        prefix: str = None,
        progress: int = None,
        report: DescribeBackupJobs2ResponseBodyBackupJobsBackupJobReport = None,
        source_type: str = None,
        speed: int = None,
        speed_limit: str = None,
        start_time: int = None,
        status: str = None,
        table_name: str = None,
        updated_time: int = None,
        vault_id: str = None,
    ):
        # The actual amount of data that is backed up after duplicates are removed. Unit: bytes.
        self.actual_bytes = actual_bytes
        # The number of files that are actually processed.
        self.actual_files = actual_files
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the actual number of objects that are backed up by the backup job.
        self.actual_items = actual_items
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # This parameter is returned only if the **SourceType** parameter is set to **OSS**. This parameter indicates the name of the OSS bucket that is backed up.
        self.bucket = bucket
        # The actual amount of data that is generated by incremental backups. Unit: bytes.
        self.bytes_done = bytes_done
        # The total amount of data that is backed up from the data source. Unit: bytes.
        self.bytes_total = bytes_total
        # The data source details at the destination. Thisparameter is returned only for data synchronization.
        self.change_list_path = change_list_path
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the ID of the backup client.
        self.client_id = client_id
        # The time when the backup job was completed. This value is a UNIX timestamp. Unit: seconds.
        self.complete_time = complete_time
        # This parameter is returned only if the **SourceType** parameter is set to **NAS**. This parameter indicates the time when the file system was created. This value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time
        # The time when the backup job was created. This value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # Destination data source details. (Required only for synchronization)
        self.dest_data_source_detail = dest_data_source_detail
        # Destination data source ID. (Required only for synchronization)
        self.dest_data_source_id = dest_data_source_id
        # Destination data source type. (Required only for synchronization)
        self.dest_source_type = dest_source_type
        # The udm backup job detail.
        self.detail = detail
        # The error message that is returned for the backup job.
        self.error_message = error_message
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the paths to the files that are excluded from the backup job. The value must be 1 to 255 characters in length.
        self.exclude = exclude
        # This parameter is returned only if the **SourceType** parameter is set to **NAS**. This parameter indicates the ID of the NAS file system.
        self.file_system_id = file_system_id
        # The number of files that have been processed.
        self.files_done = files_done
        # The total number of files to be processed.
        self.files_total = files_total
        # The identifier of the container cluster. For a Container Service for Kubernetes (ACK) cluster, specify the cluster ID.
        self.identifier = identifier
        # The paths to the files that are included in the backup job.
        self.include = include
        # This parameter is returned only if the **SourceType** parameter is set to **NAS**. This parameter indicates the ID of the ECS instance.
        self.instance_id = instance_id
        # The name of the Tablestore instance.
        self.instance_name = instance_name
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the number of objects that are backed up.
        self.items_done = items_done
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the total number of objects in the data source.
        self.items_total = items_total
        # The ID of the backup job.
        self.job_id = job_id
        # The name of the backup job.
        self.job_name = job_name
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates whether Windows VSS is used to define a backup path.
        # 
        # *   This parameter is available only for Windows ECS instances.
        # *   If data changes occur in the backup source, the source data must be the same as the data to be backed up before the system sets this parameter to `["UseVSS":true]`.
        # *   If you use VSS, you cannot back up data from multiple directories.
        self.options = options
        # The details about the Tablestore instance.
        self.ots_detail = ots_detail
        # The backup paths.
        self.paths = paths
        # The ID of the backup plan.
        self.plan_id = plan_id
        # This parameter is returned only if the **SourceType** parameter is set to **OSS**. This parameter indicates the prefix of objects that are backed up.
        self.prefix = prefix
        # The backup progress. For example, 10000 indicates that the progress is 100%.
        self.progress = progress
        # Task Report
        self.report = report
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: ECS files
        # *   **OSS**: OSS buckets
        # *   **NAS**: NAS file systems
        self.source_type = source_type
        # The average speed at which data is backed up. Unit: KB/s.
        self.speed = speed
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the throttling rules. Format: `{start}{end}{bandwidth}`. Multiple throttling rules are separated with vertical bars (`{start}|{end}|{bandwidth}`). A specified time range cannot overlap with another one.
        # 
        # *   **start**: the start hour
        # *   **end**: the end hour
        # *   **bandwidth**: the bandwidth. Unit: KB/s.
        self.speed_limit = speed_limit
        # The time when the backup job started. This value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time
        # The status of the backup job. Valid values:
        # 
        # *   **COMPLETE**: The backup job is completed.
        # *   **PARTIAL_COMPLETE**: The backup job is partially completed.
        # *   **FAILED**: The restore job has failed.
        self.status = status
        # The name of a destination table in the Tablestore instance.
        self.table_name = table_name
        # The time when the backup job was updated. This value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        if self.detail:
            self.detail.validate()
        if self.ots_detail:
            self.ots_detail.validate()
        if self.paths:
            self.paths.validate()
        if self.report:
            self.report.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_bytes is not None:
            result['ActualBytes'] = self.actual_bytes
        if self.actual_files is not None:
            result['ActualFiles'] = self.actual_files
        if self.actual_items is not None:
            result['ActualItems'] = self.actual_items
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.bytes_done is not None:
            result['BytesDone'] = self.bytes_done
        if self.bytes_total is not None:
            result['BytesTotal'] = self.bytes_total
        if self.change_list_path is not None:
            result['ChangeListPath'] = self.change_list_path
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.dest_data_source_detail is not None:
            result['DestDataSourceDetail'] = self.dest_data_source_detail
        if self.dest_data_source_id is not None:
            result['DestDataSourceId'] = self.dest_data_source_id
        if self.dest_source_type is not None:
            result['DestSourceType'] = self.dest_source_type
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.files_done is not None:
            result['FilesDone'] = self.files_done
        if self.files_total is not None:
            result['FilesTotal'] = self.files_total
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.include is not None:
            result['Include'] = self.include
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.items_done is not None:
            result['ItemsDone'] = self.items_done
        if self.items_total is not None:
            result['ItemsTotal'] = self.items_total
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.options is not None:
            result['Options'] = self.options
        if self.ots_detail is not None:
            result['OtsDetail'] = self.ots_detail.to_map()
        if self.paths is not None:
            result['Paths'] = self.paths.to_map()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.report is not None:
            result['Report'] = self.report.to_map()
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualBytes') is not None:
            self.actual_bytes = m.get('ActualBytes')
        if m.get('ActualFiles') is not None:
            self.actual_files = m.get('ActualFiles')
        if m.get('ActualItems') is not None:
            self.actual_items = m.get('ActualItems')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('BytesDone') is not None:
            self.bytes_done = m.get('BytesDone')
        if m.get('BytesTotal') is not None:
            self.bytes_total = m.get('BytesTotal')
        if m.get('ChangeListPath') is not None:
            self.change_list_path = m.get('ChangeListPath')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('DestDataSourceDetail') is not None:
            self.dest_data_source_detail = m.get('DestDataSourceDetail')
        if m.get('DestDataSourceId') is not None:
            self.dest_data_source_id = m.get('DestDataSourceId')
        if m.get('DestSourceType') is not None:
            self.dest_source_type = m.get('DestSourceType')
        if m.get('Detail') is not None:
            temp_model = DescribeBackupJobs2ResponseBodyBackupJobsBackupJobDetail()
            self.detail = temp_model.from_map(m['Detail'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FilesDone') is not None:
            self.files_done = m.get('FilesDone')
        if m.get('FilesTotal') is not None:
            self.files_total = m.get('FilesTotal')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ItemsDone') is not None:
            self.items_done = m.get('ItemsDone')
        if m.get('ItemsTotal') is not None:
            self.items_total = m.get('ItemsTotal')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OtsDetail') is not None:
            temp_model = DescribeBackupJobs2ResponseBodyBackupJobsBackupJobOtsDetail()
            self.ots_detail = temp_model.from_map(m['OtsDetail'])
        if m.get('Paths') is not None:
            temp_model = DescribeBackupJobs2ResponseBodyBackupJobsBackupJobPaths()
            self.paths = temp_model.from_map(m['Paths'])
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Report') is not None:
            temp_model = DescribeBackupJobs2ResponseBodyBackupJobsBackupJobReport()
            self.report = temp_model.from_map(m['Report'])
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeBackupJobs2ResponseBodyBackupJobs(TeaModel):
    def __init__(
        self,
        backup_job: List[DescribeBackupJobs2ResponseBodyBackupJobsBackupJob] = None,
    ):
        self.backup_job = backup_job

    def validate(self):
        if self.backup_job:
            for k in self.backup_job:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackupJob'] = []
        if self.backup_job is not None:
            for k in self.backup_job:
                result['BackupJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_job = []
        if m.get('BackupJob') is not None:
            for k in m.get('BackupJob'):
                temp_model = DescribeBackupJobs2ResponseBodyBackupJobsBackupJob()
                self.backup_job.append(temp_model.from_map(k))
        return self


class DescribeBackupJobs2ResponseBody(TeaModel):
    def __init__(
        self,
        backup_jobs: DescribeBackupJobs2ResponseBodyBackupJobs = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The returned backup jobs that meet the specified conditions.
        self.backup_jobs = backup_jobs
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The page number of the returned page. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries returned per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful.
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The total number of returned backup jobs that meet the specified conditions.
        self.total_count = total_count

    def validate(self):
        if self.backup_jobs:
            self.backup_jobs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_jobs is not None:
            result['BackupJobs'] = self.backup_jobs.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupJobs') is not None:
            temp_model = DescribeBackupJobs2ResponseBodyBackupJobs()
            self.backup_jobs = temp_model.from_map(m['BackupJobs'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBackupJobs2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupJobs2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBackupJobs2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPlansRequestFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # The keys in the filter. Valid values:
        # 
        # *   **regionId**: the ID of a region
        # *   **planId**: the ID of a backup plan
        # *   **sourceType**: the type of a data source
        # *   **vaultId**: the ID of a backup vault
        # *   **instanceName**: the name of an instance
        # *   **instanceId**: the ID of an instance
        # *   **planName**: the name of a backup plan
        self.key = key
        # The values that you want to match in the filter.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeBackupPlansRequest(TeaModel):
    def __init__(
        self,
        filters: List[DescribeBackupPlansRequestFilters] = None,
        page_number: int = None,
        page_size: int = None,
        source_type: str = None,
    ):
        # The filters.
        self.filters = filters
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS file systems
        # *   **OTS**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        self.source_type = source_type

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = DescribeBackupPlansRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlanHitTagsHitTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag-based matching rule. Valid values:
        # 
        # *   **EQUAL**: Both the tag key and tag value are matched.
        # *   **NOT**: The tag key is matched and the tag value is not matched.
        self.operator = operator
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlanHitTags(TeaModel):
    def __init__(
        self,
        hit_tag: List[DescribeBackupPlansResponseBodyBackupPlansBackupPlanHitTagsHitTag] = None,
    ):
        self.hit_tag = hit_tag

    def validate(self):
        if self.hit_tag:
            for k in self.hit_tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HitTag'] = []
        if self.hit_tag is not None:
            for k in self.hit_tag:
                result['HitTag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit_tag = []
        if m.get('HitTag') is not None:
            for k in m.get('HitTag'):
                temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlanHitTagsHitTag()
                self.hit_tag.append(temp_model.from_map(k))
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlanOtsDetailTableNames(TeaModel):
    def __init__(
        self,
        table_name: List[str] = None,
    ):
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlanOtsDetail(TeaModel):
    def __init__(
        self,
        table_names: DescribeBackupPlansResponseBodyBackupPlansBackupPlanOtsDetailTableNames = None,
    ):
        # The names of the tables in the Tablestore instance.
        self.table_names = table_names

    def validate(self):
        if self.table_names:
            self.table_names.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_names is not None:
            result['TableNames'] = self.table_names.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableNames') is not None:
            temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlanOtsDetailTableNames()
            self.table_names = temp_model.from_map(m['TableNames'])
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlanPaths(TeaModel):
    def __init__(
        self,
        path: List[str] = None,
    ):
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlanResourcesResource(TeaModel):
    def __init__(
        self,
        extra: str = None,
        resource_id: str = None,
        source_type: str = None,
    ):
        # Additional information about the data source.
        self.extra = extra
        # The ID of the data source.
        self.resource_id = resource_id
        # The type of the data source. Valid value: **UDM_DISK**.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlanResources(TeaModel):
    def __init__(
        self,
        resource: List[DescribeBackupPlansResponseBodyBackupPlansBackupPlanResourcesResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlanResourcesResource()
                self.resource.append(temp_model.from_map(k))
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlanRulesRule(TeaModel):
    def __init__(
        self,
        backup_type: str = None,
        destination_region_id: str = None,
        destination_retention: int = None,
        disabled: bool = None,
        do_copy: bool = None,
        retention: int = None,
        rule_id: str = None,
        rule_name: str = None,
        schedule: str = None,
    ):
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # The ID of the region in which the remote backup vault resides.
        self.destination_region_id = destination_region_id
        # The retention period of the backup data in remote backup mode. Unit: days.
        self.destination_retention = destination_retention
        # Indicates whether the policy is disabled.
        self.disabled = disabled
        # Indicates whether the snapshot data is backed up to the backup vault.
        self.do_copy = do_copy
        # The retention period of the backup data. Unit: days.
        self.retention = retention
        # The policy ID.
        self.rule_id = rule_id
        # The policy name.
        self.rule_name = rule_name
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified by `{startTime}` and the subsequent backup jobs at an interval that is specified by `{interval}`. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` indicates that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   `startTime`: the time at which the system starts to run a backup job. The time follows the UNIX time format. Unit: seconds.
        # *   `interval`: the interval at which the system runs a backup job. The interval follows the ISO 8601 standard. For example, PT1H indicates an interval of 1 hour. P1D indicates an interval of one day.
        self.schedule = schedule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id
        if self.destination_retention is not None:
            result['DestinationRetention'] = self.destination_retention
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.do_copy is not None:
            result['DoCopy'] = self.do_copy
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')
        if m.get('DestinationRetention') is not None:
            self.destination_retention = m.get('DestinationRetention')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('DoCopy') is not None:
            self.do_copy = m.get('DoCopy')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlanRules(TeaModel):
    def __init__(
        self,
        rule: List[DescribeBackupPlansResponseBodyBackupPlansBackupPlanRulesRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlanRulesRule()
                self.rule.append(temp_model.from_map(k))
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlanTrialInfo(TeaModel):
    def __init__(
        self,
        keep_after_trial_expiration: bool = None,
        trial_expire_time: int = None,
        trial_start_time: int = None,
        trial_vault_release_time: int = None,
    ):
        # Indicates whether you are billed based on the pay-as-you-go method after the free trial ends.
        self.keep_after_trial_expiration = keep_after_trial_expiration
        # The expiration time of the free trial.
        self.trial_expire_time = trial_expire_time
        # The start time of the free trial.
        self.trial_start_time = trial_start_time
        # The time when the free-trial backup vault is released.
        self.trial_vault_release_time = trial_vault_release_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keep_after_trial_expiration is not None:
            result['KeepAfterTrialExpiration'] = self.keep_after_trial_expiration
        if self.trial_expire_time is not None:
            result['TrialExpireTime'] = self.trial_expire_time
        if self.trial_start_time is not None:
            result['TrialStartTime'] = self.trial_start_time
        if self.trial_vault_release_time is not None:
            result['TrialVaultReleaseTime'] = self.trial_vault_release_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeepAfterTrialExpiration') is not None:
            self.keep_after_trial_expiration = m.get('KeepAfterTrialExpiration')
        if m.get('TrialExpireTime') is not None:
            self.trial_expire_time = m.get('TrialExpireTime')
        if m.get('TrialStartTime') is not None:
            self.trial_start_time = m.get('TrialStartTime')
        if m.get('TrialVaultReleaseTime') is not None:
            self.trial_vault_release_time = m.get('TrialVaultReleaseTime')
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlan(TeaModel):
    def __init__(
        self,
        backup_source_group_id: str = None,
        backup_type: str = None,
        bucket: str = None,
        change_list_path: str = None,
        client_id: str = None,
        cluster_id: str = None,
        create_time: int = None,
        created_by_tag: bool = None,
        created_time: int = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        data_source_id: str = None,
        dest_data_source_detail: str = None,
        dest_data_source_id: str = None,
        dest_source_type: str = None,
        detail: str = None,
        disabled: bool = None,
        exclude: str = None,
        file_system_id: str = None,
        hit_tags: DescribeBackupPlansResponseBodyBackupPlansBackupPlanHitTags = None,
        include: str = None,
        instance_group_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        keep_latest_snapshots: int = None,
        latest_execute_job_id: str = None,
        options: str = None,
        ots_detail: DescribeBackupPlansResponseBodyBackupPlansBackupPlanOtsDetail = None,
        paths: DescribeBackupPlansResponseBodyBackupPlansBackupPlanPaths = None,
        plan_id: str = None,
        plan_name: str = None,
        prefix: str = None,
        resources: DescribeBackupPlansResponseBodyBackupPlansBackupPlanResources = None,
        retention: int = None,
        rules: DescribeBackupPlansResponseBodyBackupPlansBackupPlanRules = None,
        schedule: str = None,
        source_type: str = None,
        speed_limit: str = None,
        trial_info: DescribeBackupPlansResponseBodyBackupPlansBackupPlanTrialInfo = None,
        updated_time: int = None,
        vault_id: str = None,
    ):
        # The ID of the data source group.
        self.backup_source_group_id = backup_source_group_id
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # This parameter is valid only when **SourceType** is set to **OSS**. This parameter indicates the name of the OSS bucket.
        self.bucket = bucket
        # The configurations of the incremental file synchronization. This parameter is returned only for data synchronization.
        self.change_list_path = change_list_path
        # The ID of the backup client.
        self.client_id = client_id
        # The ID of the client group.
        self.cluster_id = cluster_id
        # This parameter is valid only when **SourceType** is set to **NAS**. This parameter indicates the time when the file system was created. This value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time
        # Indicates whether a backup plan is automatically created based on tags.
        self.created_by_tag = created_by_tag
        # The time when the backup plan was created. This value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The name of the Resource Access Management (RAM) role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Indicates whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT
        # *   CROSS_ACCOUNT
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The ID of the data source.
        self.data_source_id = data_source_id
        # The data source details at the destination. This parameter is returned only for data synchronization.
        self.dest_data_source_detail = dest_data_source_detail
        # The data source ID at the destination. This parameter is returned only for data synchronization.
        self.dest_data_source_id = dest_data_source_id
        # The data source type at the destination. This parameter is returned only for data synchronization.
        self.dest_source_type = dest_source_type
        # The details about ECS instance backup.
        self.detail = detail
        # Indicates whether the backup plan is disabled. Valid values:
        # 
        # *   true: The backup plan is disabled.
        # *   false: The backup plan is enabled.
        self.disabled = disabled
        # This parameter is valid only when **SourceType** is set to **ECS_FILE**. This parameter indicates the paths to the files that are excluded from the backup job.
        self.exclude = exclude
        # This parameter is valid only when **SourceType** is set to **NAS**. This parameter indicates the ID of the NAS file system.
        self.file_system_id = file_system_id
        # The matched tag rules.
        self.hit_tags = hit_tags
        # This parameter is valid only when **SourceType** is set to **ECS_FILE**. This parameter indicates the paths to the files that are backed up.
        self.include = include
        # The ID of the instance group.
        self.instance_group_id = instance_group_id
        # This parameter is valid only when **SourceType** is set to **ECS_FILE**. This parameter indicates the ID of the ECS instance.
        self.instance_id = instance_id
        # The name of the Tablestore instance.
        self.instance_name = instance_name
        # Indicates whether the feature of keeping at least one backup version is enabled. Valid values:
        # 
        # *   0: The feature is disabled.
        # *   1: The feature is enabled.
        self.keep_latest_snapshots = keep_latest_snapshots
        # The latest execution job id of plan.
        self.latest_execute_job_id = latest_execute_job_id
        # This parameter is valid only when **SourceType** is set to **ECS_FILE**. This parameter indicates whether Windows Volume Shadow Copy Service (VSS) is used to define a source path.
        self.options = options
        # The details about the Tablestore instance.
        self.ots_detail = ots_detail
        # The source paths. This parameter is valid only when **SourceType** is set to **ECS_FILE**.
        self.paths = paths
        # The ID of the backup plan.
        self.plan_id = plan_id
        # The name of the backup plan.
        self.plan_name = plan_name
        # This parameter is valid only when **SourceType** is set to **OSS**. This parameter indicates the prefix of the objects that are backed up.
        self.prefix = prefix
        # The backup resources. This parameter is valid only for disk backup.
        self.resources = resources
        # The retention period of the backup data. Unit: days.
        self.retention = retention
        # The backup policies. This parameter is valid only for disk backup.
        self.rules = rules
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified by `{startTime}` and the subsequent backup jobs at an interval that is specified by `{interval}`. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` indicates that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   **startTime**: the time at which the system starts to run a backup job. The time follows the UNIX time format. Unit: seconds.
        # *   **interval**: the interval at which the system runs a backup job. The interval follows the ISO 8601 standard. For example, PT1H indicates an interval of 1 hour. P1D indicates an interval of one day.
        self.schedule = schedule
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: ECS files
        # *   **OSS**: OSS buckets
        # *   **NAS**: NAS file systems
        # *   **OTS**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        self.source_type = source_type
        # This parameter is valid only when **SourceType** is set to **ECS_FILE**. This parameter indicates the throttling rules. Format: `{start}|{end}|{bandwidth}`. Multiple throttling rules are separated with vertical bars (`|`). A time range cannot overlap with another one.
        # 
        # *   start: the start hour.
        # *   end: the end hour.
        # *   bandwidth: the bandwidth. Unit: KB.
        self.speed_limit = speed_limit
        # The free trial information.
        self.trial_info = trial_info
        # The time when the backup plan was updated. This value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        if self.hit_tags:
            self.hit_tags.validate()
        if self.ots_detail:
            self.ots_detail.validate()
        if self.paths:
            self.paths.validate()
        if self.resources:
            self.resources.validate()
        if self.rules:
            self.rules.validate()
        if self.trial_info:
            self.trial_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_source_group_id is not None:
            result['BackupSourceGroupId'] = self.backup_source_group_id
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.change_list_path is not None:
            result['ChangeListPath'] = self.change_list_path
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.created_by_tag is not None:
            result['CreatedByTag'] = self.created_by_tag
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.dest_data_source_detail is not None:
            result['DestDataSourceDetail'] = self.dest_data_source_detail
        if self.dest_data_source_id is not None:
            result['DestDataSourceId'] = self.dest_data_source_id
        if self.dest_source_type is not None:
            result['DestSourceType'] = self.dest_source_type
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.hit_tags is not None:
            result['HitTags'] = self.hit_tags.to_map()
        if self.include is not None:
            result['Include'] = self.include
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.keep_latest_snapshots is not None:
            result['KeepLatestSnapshots'] = self.keep_latest_snapshots
        if self.latest_execute_job_id is not None:
            result['LatestExecuteJobId'] = self.latest_execute_job_id
        if self.options is not None:
            result['Options'] = self.options
        if self.ots_detail is not None:
            result['OtsDetail'] = self.ots_detail.to_map()
        if self.paths is not None:
            result['Paths'] = self.paths.to_map()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        if self.trial_info is not None:
            result['TrialInfo'] = self.trial_info.to_map()
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSourceGroupId') is not None:
            self.backup_source_group_id = m.get('BackupSourceGroupId')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('ChangeListPath') is not None:
            self.change_list_path = m.get('ChangeListPath')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatedByTag') is not None:
            self.created_by_tag = m.get('CreatedByTag')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('DestDataSourceDetail') is not None:
            self.dest_data_source_detail = m.get('DestDataSourceDetail')
        if m.get('DestDataSourceId') is not None:
            self.dest_data_source_id = m.get('DestDataSourceId')
        if m.get('DestSourceType') is not None:
            self.dest_source_type = m.get('DestSourceType')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('HitTags') is not None:
            temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlanHitTags()
            self.hit_tags = temp_model.from_map(m['HitTags'])
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('KeepLatestSnapshots') is not None:
            self.keep_latest_snapshots = m.get('KeepLatestSnapshots')
        if m.get('LatestExecuteJobId') is not None:
            self.latest_execute_job_id = m.get('LatestExecuteJobId')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OtsDetail') is not None:
            temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlanOtsDetail()
            self.ots_detail = temp_model.from_map(m['OtsDetail'])
        if m.get('Paths') is not None:
            temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlanPaths()
            self.paths = temp_model.from_map(m['Paths'])
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Resources') is not None:
            temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlanResources()
            self.resources = temp_model.from_map(m['Resources'])
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('Rules') is not None:
            temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlanRules()
            self.rules = temp_model.from_map(m['Rules'])
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        if m.get('TrialInfo') is not None:
            temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlanTrialInfo()
            self.trial_info = temp_model.from_map(m['TrialInfo'])
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeBackupPlansResponseBodyBackupPlans(TeaModel):
    def __init__(
        self,
        backup_plan: List[DescribeBackupPlansResponseBodyBackupPlansBackupPlan] = None,
    ):
        self.backup_plan = backup_plan

    def validate(self):
        if self.backup_plan:
            for k in self.backup_plan:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackupPlan'] = []
        if self.backup_plan is not None:
            for k in self.backup_plan:
                result['BackupPlan'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_plan = []
        if m.get('BackupPlan') is not None:
            for k in m.get('BackupPlan'):
                temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlan()
                self.backup_plan.append(temp_model.from_map(k))
        return self


class DescribeBackupPlansResponseBody(TeaModel):
    def __init__(
        self,
        backup_plans: DescribeBackupPlansResponseBodyBackupPlans = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The queried backup plans.
        self.backup_plans = backup_plans
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The page number of the returned page. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries returned on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The total number of returned backup plans that meet the specified conditions.
        self.total_count = total_count

    def validate(self):
        if self.backup_plans:
            self.backup_plans.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plans is not None:
            result['BackupPlans'] = self.backup_plans.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlans') is not None:
            temp_model = DescribeBackupPlansResponseBodyBackupPlans()
            self.backup_plans = temp_model.from_map(m['BackupPlans'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBackupPlansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupPlansResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBackupPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClientsRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_type: str = None,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        source_type: str = None,
        vault_id: str = None,
    ):
        # The ID of the Cloud Backup client.
        self.client_id = client_id
        # The type of the Cloud Backup client. Valid value: **ECS_AGENT**, which indicates an SAP HANA backup client.
        self.client_type = client_type
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The type of the data source. Valid value:**HANA**, which indicates SAP HANA backup.
        self.source_type = source_type
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeClientsResponseBodyClientsClient(TeaModel):
    def __init__(
        self,
        alert_setting: str = None,
        client_id: str = None,
        client_name: str = None,
        client_type: str = None,
        client_version: str = None,
        cluster_id: str = None,
        created_time: int = None,
        heart_beat_time: int = None,
        instance_id: str = None,
        instance_name: str = None,
        max_version: str = None,
        network_type: str = None,
        status: str = None,
        status_message: str = None,
        updated_time: int = None,
        use_https: bool = None,
        vault_id: str = None,
    ):
        # The alert settings. Valid value: INHERITED, which indicates that the Cloud Backup client sends alert notifications by using the same method configured for the backup vault.
        self.alert_setting = alert_setting
        # The ID of the Cloud Backup client.
        self.client_id = client_id
        # The client name.
        self.client_name = client_name
        # The type of the Cloud Backup client. Valid value: **ECS_AGENT**, which indicates an SAP HANA backup client.
        self.client_type = client_type
        # The version number of the Cloud Backup client.
        self.client_version = client_version
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id
        # The time when the Cloud Backup client was created.
        self.created_time = created_time
        self.heart_beat_time = heart_beat_time
        # The instance ID.
        self.instance_id = instance_id
        # The name of the ECS instance.
        self.instance_name = instance_name
        # The maximum version number of the Cloud Backup client.
        self.max_version = max_version
        # The network type. Valid values:
        # 
        # *   **CLASSIC**: the classic network
        # *   **VPC**: the virtual private cloud (VPC)
        self.network_type = network_type
        # The status of the Cloud Backup client. Valid values:
        # 
        # *   **REGISTERED**: The backup client is registered.
        # *   **ACTIVATED**: The backup client is activated.
        # *   **DEACTIVATED**: The backup client fails to be activated.
        # *   **INSTALLING**: The backup client is being installed.
        # *   **INSTALL_FAILED**: The backup client fails to be installed.
        # *   **NOT_INSTALLED**: The backup client is not installed.
        # *   **UPGRADING**: The backup client is being upgraded.
        # *   **UPGRADE_FAILED**: The backup client fails to be upgraded.
        # *   **UNINSTALLING**: The backup client is being uninstalled.
        # *   **UNINSTALL_FAILED**: The backup client fails to be uninstalled.
        # *   **STOPPED**: The backup client is out of service.
        # *   **UNKNOWN**: The backup client is disconnected.
        self.status = status
        # The status information.
        self.status_message = status_message
        # The time when the Cloud Backup client was updated. This value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time
        # Indicates whether data is transmitted over HTTPS. Valid values:
        # 
        # *   true: Data is transmitted over HTTPS.
        # *   false: Data is transmitted over HTTP.
        self.use_https = use_https
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_setting is not None:
            result['AlertSetting'] = self.alert_setting
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_name is not None:
            result['ClientName'] = self.client_name
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.heart_beat_time is not None:
            result['HeartBeatTime'] = self.heart_beat_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.max_version is not None:
            result['MaxVersion'] = self.max_version
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.use_https is not None:
            result['UseHttps'] = self.use_https
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertSetting') is not None:
            self.alert_setting = m.get('AlertSetting')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientName') is not None:
            self.client_name = m.get('ClientName')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('HeartBeatTime') is not None:
            self.heart_beat_time = m.get('HeartBeatTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('MaxVersion') is not None:
            self.max_version = m.get('MaxVersion')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('UseHttps') is not None:
            self.use_https = m.get('UseHttps')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeClientsResponseBodyClients(TeaModel):
    def __init__(
        self,
        client: List[DescribeClientsResponseBodyClientsClient] = None,
    ):
        self.client = client

    def validate(self):
        if self.client:
            for k in self.client:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Client'] = []
        if self.client is not None:
            for k in self.client:
                result['Client'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client = []
        if m.get('Client') is not None:
            for k in m.get('Client'):
                temp_model = DescribeClientsResponseBodyClientsClient()
                self.client.append(temp_model.from_map(k))
        return self


class DescribeClientsResponseBody(TeaModel):
    def __init__(
        self,
        clients: DescribeClientsResponseBodyClients = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The Cloud Backup clients.
        self.clients = clients
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.clients:
            self.clients.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clients is not None:
            result['Clients'] = self.clients.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clients') is not None:
            temp_model = DescribeClientsResponseBodyClients()
            self.clients = temp_model.from_map(m['Clients'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeClientsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClientsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        identifier: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The identifier of the container cluster. For a Container Service for Kubernetes (ACK) cluster, specify the cluster ID.
        self.identifier = identifier
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeContainerClusterResponseBodyClusters(TeaModel):
    def __init__(
        self,
        agent_status: str = None,
        cluster_id: str = None,
        cluster_type: str = None,
        description: str = None,
        identifier: str = None,
        name: str = None,
        network_type: str = None,
        token: str = None,
    ):
        # The status of the client. Valid values:
        # 
        # *   **MISS**: The client is disconnected.
        # *   **UNKNOWN**: The client is in an unknown state.
        # *   **READY**: The client is ready.
        self.agent_status = agent_status
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The type of the cluster. Valid value: ACK, which indicates ACK clusters.
        self.cluster_type = cluster_type
        # The description.
        self.description = description
        # The identifier of the cluster.
        self.identifier = identifier
        # The name of the instance.
        self.name = name
        # The network type of the cluster. Valid values:
        # 
        # *   **CLASSIC**: the classic network
        # *   **VPC**: virtual private cloud (VPC)
        self.network_type = network_type
        # The token that is used to register the Hybrid Backup Recovery (HBR) client in the cluster.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.description is not None:
            result['Description'] = self.description
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.name is not None:
            result['Name'] = self.name
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class DescribeContainerClusterResponseBody(TeaModel):
    def __init__(
        self,
        clusters: List[DescribeContainerClusterResponseBodyClusters] = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The information of clusters.
        self.clusters = clusters
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The page number of the returned page. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries returned on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = DescribeContainerClusterResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeContainerClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeContainerClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeContainerClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCrossAccountsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeCrossAccountsResponseBodyCrossAccountsCrossAccount(TeaModel):
    def __init__(
        self,
        alias: str = None,
        created_time: int = None,
        cross_account_role_name: str = None,
        cross_account_user_id: int = None,
        id: int = None,
        owner_id: int = None,
        updated_time: int = None,
    ):
        # The account alias. The value can be up to 32 bits in length.
        self.alias = alias
        # The time when the account was created. This value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The ID of the backup type.
        self.id = id
        # The ID of the current account.
        self.owner_id = owner_id
        # The time when the account information was updated. The value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class DescribeCrossAccountsResponseBodyCrossAccounts(TeaModel):
    def __init__(
        self,
        cross_account: List[DescribeCrossAccountsResponseBodyCrossAccountsCrossAccount] = None,
    ):
        self.cross_account = cross_account

    def validate(self):
        if self.cross_account:
            for k in self.cross_account:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CrossAccount'] = []
        if self.cross_account is not None:
            for k in self.cross_account:
                result['CrossAccount'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cross_account = []
        if m.get('CrossAccount') is not None:
            for k in m.get('CrossAccount'):
                temp_model = DescribeCrossAccountsResponseBodyCrossAccountsCrossAccount()
                self.cross_account.append(temp_model.from_map(k))
        return self


class DescribeCrossAccountsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        cross_accounts: DescribeCrossAccountsResponseBodyCrossAccounts = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The information about the accounts used in cross-account backup.
        self.cross_accounts = cross_accounts
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.cross_accounts:
            self.cross_accounts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.cross_accounts is not None:
            result['CrossAccounts'] = self.cross_accounts.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CrossAccounts') is not None:
            temp_model = DescribeCrossAccountsResponseBodyCrossAccounts()
            self.cross_accounts = temp_model.from_map(m['CrossAccounts'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCrossAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCrossAccountsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCrossAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHanaBackupPlansRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        database_name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        vault_id: str = None,
    ):
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The database name.
        self.database_name = database_name
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeHanaBackupPlansResponseBodyHanaBackupPlansHanaBackupPlan(TeaModel):
    def __init__(
        self,
        backup_prefix: str = None,
        backup_type: str = None,
        cluster_id: str = None,
        database_name: str = None,
        disabled: bool = None,
        plan_id: str = None,
        plan_name: str = None,
        schedule: str = None,
        vault_id: str = None,
    ):
        # The backup prefix.
        self.backup_prefix = backup_prefix
        # The backup type. Valid values:
        # 
        # *   COMPLETE: full backup
        # *   INCREMENTAL: incremental backup
        # *   DIFFERENTIAL: differential backup
        self.backup_type = backup_type
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id
        # The database name.
        self.database_name = database_name
        # Indicates whether the backup plan is disabled. Valid values:
        # 
        # *   true: The backup plan is disabled.
        # *   false: The backup plan is enabled.
        self.disabled = disabled
        # The ID of the backup plan.
        self.plan_id = plan_id
        # The name of the backup plan.
        self.plan_name = plan_name
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` indicates that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   startTime: the time at which the system starts to run a backup job. The time follows the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system runs a backup job. The interval follows the ISO 8601 standard. For example, PT1H indicates an interval of 1 hour. P1D indicates an interval of one day.
        self.schedule = schedule
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_prefix is not None:
            result['BackupPrefix'] = self.backup_prefix
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPrefix') is not None:
            self.backup_prefix = m.get('BackupPrefix')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeHanaBackupPlansResponseBodyHanaBackupPlans(TeaModel):
    def __init__(
        self,
        hana_backup_plan: List[DescribeHanaBackupPlansResponseBodyHanaBackupPlansHanaBackupPlan] = None,
    ):
        self.hana_backup_plan = hana_backup_plan

    def validate(self):
        if self.hana_backup_plan:
            for k in self.hana_backup_plan:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HanaBackupPlan'] = []
        if self.hana_backup_plan is not None:
            for k in self.hana_backup_plan:
                result['HanaBackupPlan'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hana_backup_plan = []
        if m.get('HanaBackupPlan') is not None:
            for k in m.get('HanaBackupPlan'):
                temp_model = DescribeHanaBackupPlansResponseBodyHanaBackupPlansHanaBackupPlan()
                self.hana_backup_plan.append(temp_model.from_map(k))
        return self


class DescribeHanaBackupPlansResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        hana_backup_plans: DescribeHanaBackupPlansResponseBodyHanaBackupPlans = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The details of the backup plan.
        self.hana_backup_plans = hana_backup_plans
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.hana_backup_plans:
            self.hana_backup_plans.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.hana_backup_plans is not None:
            result['HanaBackupPlans'] = self.hana_backup_plans.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HanaBackupPlans') is not None:
            temp_model = DescribeHanaBackupPlansResponseBodyHanaBackupPlans()
            self.hana_backup_plans = temp_model.from_map(m['HanaBackupPlans'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeHanaBackupPlansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHanaBackupPlansResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHanaBackupPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHanaBackupSettingRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        database_name: str = None,
        vault_id: str = None,
    ):
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The name of the database.
        self.database_name = database_name
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeHanaBackupSettingResponseBodyHanaBackupSetting(TeaModel):
    def __init__(
        self,
        catalog_backup_parameter_file: str = None,
        catalog_backup_using_backint: bool = None,
        data_backup_parameter_file: str = None,
        database_name: str = None,
        enable_auto_log_backup: bool = None,
        log_backup_parameter_file: str = None,
        log_backup_timeout: int = None,
        log_backup_using_backint: bool = None,
    ):
        # The configuration file for catalog backup.
        self.catalog_backup_parameter_file = catalog_backup_parameter_file
        # Indicates whether Backint is used to back up catalogs. Valid values:
        # 
        # *   true: Backint is used to back up catalogs.
        # *   false: Backint is not used to back up catalogs.
        self.catalog_backup_using_backint = catalog_backup_using_backint
        # The configuration file for data backup.
        self.data_backup_parameter_file = data_backup_parameter_file
        # The name of the database.
        self.database_name = database_name
        # Indicates whether automatic log backup is enabled. Valid values:
        # 
        # *   **true**: Automatic log backup is enabled.
        # *   **false**: Automatic log backup is disabled.
        self.enable_auto_log_backup = enable_auto_log_backup
        # The configuration file for log backup.
        self.log_backup_parameter_file = log_backup_parameter_file
        # The interval at which logs are backed up. Unit: seconds.
        self.log_backup_timeout = log_backup_timeout
        # Indicates whether Backint is used to back up logs. Valid values:
        # 
        # *   true: Backint is used to back up logs.
        # *   false: Backint is not used to back up logs.
        self.log_backup_using_backint = log_backup_using_backint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_backup_parameter_file is not None:
            result['CatalogBackupParameterFile'] = self.catalog_backup_parameter_file
        if self.catalog_backup_using_backint is not None:
            result['CatalogBackupUsingBackint'] = self.catalog_backup_using_backint
        if self.data_backup_parameter_file is not None:
            result['DataBackupParameterFile'] = self.data_backup_parameter_file
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.enable_auto_log_backup is not None:
            result['EnableAutoLogBackup'] = self.enable_auto_log_backup
        if self.log_backup_parameter_file is not None:
            result['LogBackupParameterFile'] = self.log_backup_parameter_file
        if self.log_backup_timeout is not None:
            result['LogBackupTimeout'] = self.log_backup_timeout
        if self.log_backup_using_backint is not None:
            result['LogBackupUsingBackint'] = self.log_backup_using_backint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogBackupParameterFile') is not None:
            self.catalog_backup_parameter_file = m.get('CatalogBackupParameterFile')
        if m.get('CatalogBackupUsingBackint') is not None:
            self.catalog_backup_using_backint = m.get('CatalogBackupUsingBackint')
        if m.get('DataBackupParameterFile') is not None:
            self.data_backup_parameter_file = m.get('DataBackupParameterFile')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EnableAutoLogBackup') is not None:
            self.enable_auto_log_backup = m.get('EnableAutoLogBackup')
        if m.get('LogBackupParameterFile') is not None:
            self.log_backup_parameter_file = m.get('LogBackupParameterFile')
        if m.get('LogBackupTimeout') is not None:
            self.log_backup_timeout = m.get('LogBackupTimeout')
        if m.get('LogBackupUsingBackint') is not None:
            self.log_backup_using_backint = m.get('LogBackupUsingBackint')
        return self


class DescribeHanaBackupSettingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        hana_backup_setting: DescribeHanaBackupSettingResponseBodyHanaBackupSetting = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The backup settings.
        self.hana_backup_setting = hana_backup_setting
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success

    def validate(self):
        if self.hana_backup_setting:
            self.hana_backup_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.hana_backup_setting is not None:
            result['HanaBackupSetting'] = self.hana_backup_setting.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HanaBackupSetting') is not None:
            temp_model = DescribeHanaBackupSettingResponseBodyHanaBackupSetting()
            self.hana_backup_setting = temp_model.from_map(m['HanaBackupSetting'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeHanaBackupSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHanaBackupSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHanaBackupSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHanaBackupsAsyncRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        database_name: str = None,
        include_differential: bool = None,
        include_incremental: bool = None,
        include_log: bool = None,
        log_position: int = None,
        mode: str = None,
        page_number: int = None,
        page_size: int = None,
        recovery_point_in_time: int = None,
        resource_group_id: str = None,
        source: str = None,
        source_cluster_id: str = None,
        system_copy: bool = None,
        use_backint: bool = None,
        vault_id: str = None,
        volume_id: int = None,
    ):
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The database name.
        self.database_name = database_name
        # Specifies whether to include differential backups in the query results. Valid values:
        # 
        # *   true: includes differential backups.
        # *   false: excludes differential backups.
        self.include_differential = include_differential
        # Specifies whether to include incremental backups in the query results. Valid values:
        # 
        # *   true: includes incremental backups.
        # *   false: excludes incremental backups.
        self.include_incremental = include_incremental
        # Specifies whether to include log backups in the query results. Valid values:
        # 
        # *   true: includes log backups.
        # *   false: excludes log backups.
        self.include_log = include_log
        # The log position to which you want to restore the database. This parameter is valid only if you set the Mode parameter to **RECOVERY_TO_LOG_POSITION**.
        self.log_position = log_position
        # The recovery mode. Valid values:
        # 
        # *   **RECOVERY_TO_MOST_RECENT**: restores the database to the recently available state to which the database has been backed up.
        # *   **RECOVERY_TO_POINT_IN_TIME**: restores the database to a specified point in time.
        # *   **RECOVERY_TO_SPECIFIC_BACKUP**: restores the database to a specified backup.
        # *   **RECOVERY_TO_LOG_POSITION**: restores the database to a specified log position.
        self.mode = mode
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The point in time to which you want to restore the database. This parameter is valid only if you set the Mode parameter to **RECOVERY_TO_POINT_IN_TIME**. Cloud Backup restores the database to a state closest to the specified point in time.
        self.recovery_point_in_time = recovery_point_in_time
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The name of the source system. This parameter specifies the name of the source database that you want to restore. You must set the parameter in the `<Source database name>@SID` format.
        self.source = source
        # The ID of the source SAP HANA instance.
        self.source_cluster_id = source_cluster_id
        # Specifies whether to restore the database to a different instance.
        # 
        # *   true: restores the database to a different instance.
        # *   false: restores the database within the same instance.
        self.system_copy = system_copy
        # Specifies whether Backint is used. Valid values:
        # 
        # *   true: Backint is used.
        # *   false: Backint is not used.
        self.use_backint = use_backint
        # The ID of the backup vault.
        self.vault_id = vault_id
        # The ID of the volume that you want to restore. This parameter is valid only if you set the Mode parameter to **RECOVERY_TO_LOG_POSITION**.
        self.volume_id = volume_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.include_differential is not None:
            result['IncludeDifferential'] = self.include_differential
        if self.include_incremental is not None:
            result['IncludeIncremental'] = self.include_incremental
        if self.include_log is not None:
            result['IncludeLog'] = self.include_log
        if self.log_position is not None:
            result['LogPosition'] = self.log_position
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.recovery_point_in_time is not None:
            result['RecoveryPointInTime'] = self.recovery_point_in_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_cluster_id is not None:
            result['SourceClusterId'] = self.source_cluster_id
        if self.system_copy is not None:
            result['SystemCopy'] = self.system_copy
        if self.use_backint is not None:
            result['UseBackint'] = self.use_backint
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IncludeDifferential') is not None:
            self.include_differential = m.get('IncludeDifferential')
        if m.get('IncludeIncremental') is not None:
            self.include_incremental = m.get('IncludeIncremental')
        if m.get('IncludeLog') is not None:
            self.include_log = m.get('IncludeLog')
        if m.get('LogPosition') is not None:
            self.log_position = m.get('LogPosition')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RecoveryPointInTime') is not None:
            self.recovery_point_in_time = m.get('RecoveryPointInTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceClusterId') is not None:
            self.source_cluster_id = m.get('SourceClusterId')
        if m.get('SystemCopy') is not None:
            self.system_copy = m.get('SystemCopy')
        if m.get('UseBackint') is not None:
            self.use_backint = m.get('UseBackint')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        return self


class DescribeHanaBackupsAsyncResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The ID of the asynchronous job. You can call the DescribeTask operation to query the execution result of an asynchronous job.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeHanaBackupsAsyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHanaBackupsAsyncResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHanaBackupsAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHanaDatabasesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        vault_id: str = None,
    ):
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeHanaDatabasesResponseBodyHanaDatabasesHanaDatabase(TeaModel):
    def __init__(
        self,
        active_status: str = None,
        database_name: str = None,
        detail: str = None,
        host: str = None,
        service_name: str = None,
        sql_port: int = None,
    ):
        # Indicates whether the database is started. Valid values:
        # 
        # *   **YES**: The database is started.
        # *   **NO**: The database is not started.
        self.active_status = active_status
        # The database name.
        self.database_name = database_name
        # The detailed information.
        self.detail = detail
        # The hostname.
        self.host = host
        # The service name.
        self.service_name = service_name
        # The port number.
        self.sql_port = sql_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_status is not None:
            result['ActiveStatus'] = self.active_status
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.host is not None:
            result['Host'] = self.host
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.sql_port is not None:
            result['SqlPort'] = self.sql_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveStatus') is not None:
            self.active_status = m.get('ActiveStatus')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SqlPort') is not None:
            self.sql_port = m.get('SqlPort')
        return self


class DescribeHanaDatabasesResponseBodyHanaDatabases(TeaModel):
    def __init__(
        self,
        hana_database: List[DescribeHanaDatabasesResponseBodyHanaDatabasesHanaDatabase] = None,
    ):
        self.hana_database = hana_database

    def validate(self):
        if self.hana_database:
            for k in self.hana_database:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HanaDatabase'] = []
        if self.hana_database is not None:
            for k in self.hana_database:
                result['HanaDatabase'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hana_database = []
        if m.get('HanaDatabase') is not None:
            for k in m.get('HanaDatabase'):
                temp_model = DescribeHanaDatabasesResponseBodyHanaDatabasesHanaDatabase()
                self.hana_database.append(temp_model.from_map(k))
        return self


class DescribeHanaDatabasesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        hana_databases: DescribeHanaDatabasesResponseBodyHanaDatabases = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The information about SAP HANA databases.
        self.hana_databases = hana_databases
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.hana_databases:
            self.hana_databases.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.hana_databases is not None:
            result['HanaDatabases'] = self.hana_databases.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HanaDatabases') is not None:
            temp_model = DescribeHanaDatabasesResponseBodyHanaDatabases()
            self.hana_databases = temp_model.from_map(m['HanaDatabases'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeHanaDatabasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHanaDatabasesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHanaDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHanaInstancesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHanaInstancesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        tag: List[DescribeHanaInstancesRequestTag] = None,
        vault_id: str = None,
    ):
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags of the SAP HANA instance.
        self.tag = tag
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeHanaInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeHanaInstancesResponseBodyHanasHanaTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHanaInstancesResponseBodyHanasHanaTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeHanaInstancesResponseBodyHanasHanaTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeHanaInstancesResponseBodyHanasHanaTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeHanaInstancesResponseBodyHanasHana(TeaModel):
    def __init__(
        self,
        alert_setting: str = None,
        cluster_id: str = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        hana_name: str = None,
        host: str = None,
        instance_number: int = None,
        resource_group_id: str = None,
        status: int = None,
        status_message: str = None,
        tags: DescribeHanaInstancesResponseBodyHanasHanaTags = None,
        use_ssl: bool = None,
        user_name: str = None,
        validate_certificate: bool = None,
        vault_id: str = None,
    ):
        # The alert settings. Valid value: INHERITED, which indicates that the Cloud Backup client sends alert notifications by using the same method configured for the backup vault.
        self.alert_setting = alert_setting
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id
        # The name of the Resource Access Management (RAM) role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   **SELF_ACCOUNT**: Data is backed up within the same Alibaba Cloud account.
        # *   **CROSS_ACCOUNT**: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The name of the SAP HANA instance.
        self.hana_name = hana_name
        # The private or internal IP address of the host where the primary node of the SAP HANA instance resides.
        self.host = host
        # The instance number of the SAP HANA system.
        self.instance_number = instance_number
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The status of the SAP HANA instance. Valid values:
        # 
        # *   INITIALIZING: The instance is being initialized.
        # *   INITIALIZED: The instance is registered.
        # *   INVALID_HANA_NODE: The instance is invalid.
        # *   INITIALIZE_FAILED: The client fails to be installed on the instance.
        self.status = status
        # The status information.
        self.status_message = status_message
        # The tags of the SAP HANA instance.
        self.tags = tags
        # Indicates whether the SAP HANA instance is connected over Secure Sockets Layer (SSL). Valid values:
        # 
        # *   true: The SAP HANA instance is connected over SSL.
        # *   false: The SAP HANA instance is not connected over SSL.
        self.use_ssl = use_ssl
        # The username of the SYSTEMDB database.
        self.user_name = user_name
        # Indicates whether the SSL certificate of the SAP HANA instance is verified.
        self.validate_certificate = validate_certificate
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_setting is not None:
            result['AlertSetting'] = self.alert_setting
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.hana_name is not None:
            result['HanaName'] = self.hana_name
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.use_ssl is not None:
            result['UseSsl'] = self.use_ssl
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.validate_certificate is not None:
            result['ValidateCertificate'] = self.validate_certificate
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertSetting') is not None:
            self.alert_setting = m.get('AlertSetting')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('HanaName') is not None:
            self.hana_name = m.get('HanaName')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('Tags') is not None:
            temp_model = DescribeHanaInstancesResponseBodyHanasHanaTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('UseSsl') is not None:
            self.use_ssl = m.get('UseSsl')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('ValidateCertificate') is not None:
            self.validate_certificate = m.get('ValidateCertificate')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeHanaInstancesResponseBodyHanas(TeaModel):
    def __init__(
        self,
        hana: List[DescribeHanaInstancesResponseBodyHanasHana] = None,
    ):
        self.hana = hana

    def validate(self):
        if self.hana:
            for k in self.hana:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Hana'] = []
        if self.hana is not None:
            for k in self.hana:
                result['Hana'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hana = []
        if m.get('Hana') is not None:
            for k in m.get('Hana'):
                temp_model = DescribeHanaInstancesResponseBodyHanasHana()
                self.hana.append(temp_model.from_map(k))
        return self


class DescribeHanaInstancesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        hanas: DescribeHanaInstancesResponseBodyHanas = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The information about the SAP HANA instances.
        self.hanas = hanas
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.hanas:
            self.hanas.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.hanas is not None:
            result['Hanas'] = self.hanas.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Hanas') is not None:
            temp_model = DescribeHanaInstancesResponseBodyHanas()
            self.hanas = temp_model.from_map(m['Hanas'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeHanaInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHanaInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHanaInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHanaRestoresRequest(TeaModel):
    def __init__(
        self,
        backup_id: int = None,
        cluster_id: str = None,
        database_name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        restore_id: str = None,
        restore_status: str = None,
        vault_id: str = None,
    ):
        # The backup ID.
        self.backup_id = backup_id
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The database name.
        self.database_name = database_name
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.\\`
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the restore job.
        self.restore_id = restore_id
        # The status of the restore job. Valid values:
        # 
        # *   **RUNNING**: The job is running.
        # *   **COMPLETE**: The job is completed.
        # *   **PARTIAL_COMPLETE**: The job is partially completed.
        # *   **FAILED**: The job failed.
        # *   **CANCELED**: The job is canceled.
        # *   **EXPIRED**: The job timed out.
        self.restore_status = restore_status
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.restore_id is not None:
            result['RestoreId'] = self.restore_id
        if self.restore_status is not None:
            result['RestoreStatus'] = self.restore_status
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RestoreId') is not None:
            self.restore_id = m.get('RestoreId')
        if m.get('RestoreStatus') is not None:
            self.restore_status = m.get('RestoreStatus')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeHanaRestoresResponseBodyHanaRestoreHanaRestores(TeaModel):
    def __init__(
        self,
        backup_id: int = None,
        backup_prefix: str = None,
        check_access: bool = None,
        clear_log: bool = None,
        cluster_id: str = None,
        current_phase: int = None,
        current_progress: int = None,
        database_name: str = None,
        database_restore_id: int = None,
        end_time: int = None,
        log_position: int = None,
        max_phase: int = None,
        max_progress: int = None,
        message: str = None,
        mode: str = None,
        phase: str = None,
        reached_time: int = None,
        recovery_point_in_time: int = None,
        restore_id: str = None,
        source: str = None,
        source_cluster_id: str = None,
        start_time: int = None,
        state: str = None,
        status: str = None,
        system_copy: bool = None,
        use_catalog: bool = None,
        use_delta: bool = None,
        vault_id: str = None,
        volume_id: int = None,
    ):
        # The backup ID.
        self.backup_id = backup_id
        # The backup prefix.
        self.backup_prefix = backup_prefix
        # Indicates whether the differential backup and log backup are validated. Valid values:
        # 
        # *   true: Cloud Backup checks whether the required differential backup and log backup are available before the restore job starts. If the differential backup or log backup is unavailable, Cloud Backup does not start the restore job.
        # *   false: Cloud Backup does not check whether the required differential backup and log backup are available before the restore job starts.
        self.check_access = check_access
        # Indicates whether all log entries are deleted from the log area after the log entries are restored. Valid values: true and false. If the return value is false, all log entries are deleted from the log area after the log entries are restored.
        self.clear_log = clear_log
        # The ID of the SAP HANA instance that is restored.
        self.cluster_id = cluster_id
        # The current recovery phase. This value is obtained from SAP HANA.
        self.current_phase = current_phase
        # The current progress. This value is obtained from SAP HANA.
        self.current_progress = current_progress
        # The database name.
        self.database_name = database_name
        # The ID of the database recovery.
        self.database_restore_id = database_restore_id
        # The time when the restore job ends. This value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time
        # The log position to which the database is restored. This parameter is returned only if the value of the Mode parameter is **RECOVERY_TO_LOG_POSITION**.
        self.log_position = log_position
        # The maximum recovery phase. This value is obtained from SAP HANA.
        self.max_phase = max_phase
        # The maximum progress. This value is obtained from SAP HANA.
        self.max_progress = max_progress
        # The details of the recovery phase.
        self.message = message
        # The recovery mode. Valid values:
        # 
        # *   **RECOVERY_TO_MOST_RECENT**: The database is restored to the recently available state to which the database has been backed up.
        # *   **RECOVERY_TO_POINT_IN_TIME**: The database is restored to a specified point in time.
        # *   **RECOVERY_TO_SPECIFIC_BACKUP**: The database is restored to a specified backup.
        # *   **RECOVERY_TO_LOG_POSITION**: The database is restored to a specified log position.
        self.mode = mode
        # The recovery phase.
        self.phase = phase
        # The point in time at which the database is restored.
        self.reached_time = reached_time
        # The point in time to which the database is restored. This parameter is returned only if the value of the Mode parameter is **RECOVERY_TO_POINT_IN_TIME**. Cloud Backup restores the database to a state closest to the specified point in time.
        self.recovery_point_in_time = recovery_point_in_time
        # The ID of the restore job.
        self.restore_id = restore_id
        # The name of the source system. This parameter indicates the name of the source database that is restored. Format: `<Source database name>@SID`.
        self.source = source
        # The ID of the source SAP HANA instance.
        self.source_cluster_id = source_cluster_id
        # The time when the restore job starts. This value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time
        # The recovery status. This value is obtained from SAP HANA.
        self.state = state
        # The status of the restore job. Valid values:
        # 
        # *   **RUNNING**: The job is running.
        # *   **COMPLETE**: The job is completed.
        # *   **PARTIAL_COMPLETE**: The job is partially completed.
        # *   **FAILED**: The job failed.
        # *   **CANCELED**: The job is canceled.
        # *   **EXPIRED**: The job timed out.
        self.status = status
        # Indicates whether the database is restored to a different instance. Valid values:
        # 
        # *   true: The database is restored to a different instance.
        # *   false: The database is restored within the same instance.
        self.system_copy = system_copy
        # Indicates whether a catalog backup is used to restore the database. This parameter is returned only if the value of the Mode parameter is **RECOVERY_TO_SPECIFIC_BACKUP**. If the return value is false, Cloud Backup finds the backup file based on the specified prefix and then restores the backup file.
        self.use_catalog = use_catalog
        # Indicates whether a differential backup or an incremental backup is used to restore the database. Valid values: true and false. If the return value is true, Cloud Backup uses a differential backup or an incremental backup to restore the database. If the return value is false, Cloud Backup uses a log backup to restore the database.
        self.use_delta = use_delta
        # The ID of the backup vault.
        self.vault_id = vault_id
        # The ID of the volume that is restored. This parameter is returned only if the value of the Mode parameter is **RECOVERY_TO_LOG_POSITION**.
        self.volume_id = volume_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupID'] = self.backup_id
        if self.backup_prefix is not None:
            result['BackupPrefix'] = self.backup_prefix
        if self.check_access is not None:
            result['CheckAccess'] = self.check_access
        if self.clear_log is not None:
            result['ClearLog'] = self.clear_log
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.current_phase is not None:
            result['CurrentPhase'] = self.current_phase
        if self.current_progress is not None:
            result['CurrentProgress'] = self.current_progress
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.database_restore_id is not None:
            result['DatabaseRestoreId'] = self.database_restore_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.log_position is not None:
            result['LogPosition'] = self.log_position
        if self.max_phase is not None:
            result['MaxPhase'] = self.max_phase
        if self.max_progress is not None:
            result['MaxProgress'] = self.max_progress
        if self.message is not None:
            result['Message'] = self.message
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.reached_time is not None:
            result['ReachedTime'] = self.reached_time
        if self.recovery_point_in_time is not None:
            result['RecoveryPointInTime'] = self.recovery_point_in_time
        if self.restore_id is not None:
            result['RestoreId'] = self.restore_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_cluster_id is not None:
            result['SourceClusterId'] = self.source_cluster_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.system_copy is not None:
            result['SystemCopy'] = self.system_copy
        if self.use_catalog is not None:
            result['UseCatalog'] = self.use_catalog
        if self.use_delta is not None:
            result['UseDelta'] = self.use_delta
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupID') is not None:
            self.backup_id = m.get('BackupID')
        if m.get('BackupPrefix') is not None:
            self.backup_prefix = m.get('BackupPrefix')
        if m.get('CheckAccess') is not None:
            self.check_access = m.get('CheckAccess')
        if m.get('ClearLog') is not None:
            self.clear_log = m.get('ClearLog')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CurrentPhase') is not None:
            self.current_phase = m.get('CurrentPhase')
        if m.get('CurrentProgress') is not None:
            self.current_progress = m.get('CurrentProgress')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DatabaseRestoreId') is not None:
            self.database_restore_id = m.get('DatabaseRestoreId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LogPosition') is not None:
            self.log_position = m.get('LogPosition')
        if m.get('MaxPhase') is not None:
            self.max_phase = m.get('MaxPhase')
        if m.get('MaxProgress') is not None:
            self.max_progress = m.get('MaxProgress')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('ReachedTime') is not None:
            self.reached_time = m.get('ReachedTime')
        if m.get('RecoveryPointInTime') is not None:
            self.recovery_point_in_time = m.get('RecoveryPointInTime')
        if m.get('RestoreId') is not None:
            self.restore_id = m.get('RestoreId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceClusterId') is not None:
            self.source_cluster_id = m.get('SourceClusterId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SystemCopy') is not None:
            self.system_copy = m.get('SystemCopy')
        if m.get('UseCatalog') is not None:
            self.use_catalog = m.get('UseCatalog')
        if m.get('UseDelta') is not None:
            self.use_delta = m.get('UseDelta')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        return self


class DescribeHanaRestoresResponseBodyHanaRestore(TeaModel):
    def __init__(
        self,
        hana_restores: List[DescribeHanaRestoresResponseBodyHanaRestoreHanaRestores] = None,
    ):
        self.hana_restores = hana_restores

    def validate(self):
        if self.hana_restores:
            for k in self.hana_restores:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HanaRestores'] = []
        if self.hana_restores is not None:
            for k in self.hana_restores:
                result['HanaRestores'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hana_restores = []
        if m.get('HanaRestores') is not None:
            for k in m.get('HanaRestores'):
                temp_model = DescribeHanaRestoresResponseBodyHanaRestoreHanaRestores()
                self.hana_restores.append(temp_model.from_map(k))
        return self


class DescribeHanaRestoresResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        hana_restore: DescribeHanaRestoresResponseBodyHanaRestore = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The information about restore jobs.
        self.hana_restore = hana_restore
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.hana_restore:
            self.hana_restore.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.hana_restore is not None:
            result['HanaRestore'] = self.hana_restore.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HanaRestore') is not None:
            temp_model = DescribeHanaRestoresResponseBodyHanaRestore()
            self.hana_restore = temp_model.from_map(m['HanaRestore'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeHanaRestoresResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHanaRestoresResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHanaRestoresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHanaRetentionSettingRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        database_name: str = None,
        vault_id: str = None,
    ):
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The database name.
        self.database_name = database_name
        # The ID of the backup vault.
        # 
        # This parameter is required.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeHanaRetentionSettingResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        code: str = None,
        database_name: str = None,
        disabled: bool = None,
        message: str = None,
        request_id: str = None,
        retention_days: int = None,
        schedule: str = None,
        success: bool = None,
        vault_id: str = None,
    ):
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The database name.
        self.database_name = database_name
        # Indicates whether the backup is permanently retained. Valid values:
        # 
        # *   true: The backup is permanently retained.
        # *   false: The backup is retained for the specified number of days.
        self.disabled = disabled
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The number of days for which the backup is retained. If the value of the Disabled parameter is false, the backup is retained for the number of days specified by this parameter.
        self.retention_days = retention_days
        # The policy to update the retention period. Format: `I|{startTime}|{interval}`, which indicates that the retention period is updated at an interval of {interval} starting from {startTime}.
        # 
        # *   startTime: the time at which the system starts to run a backup job. The time follows the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system runs a backup job. The interval follows the ISO 8601 standard. For example, PT1H indicates an interval of 1 hour. P1D indicates an interval of one day.
        self.schedule = schedule
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.code is not None:
            result['Code'] = self.code
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.success is not None:
            result['Success'] = self.success
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeHanaRetentionSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHanaRetentionSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHanaRetentionSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOtsTableSnapshotsRequestOtsInstances(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        table_names: List[str] = None,
    ):
        # The name of the Tablestore instance.
        self.instance_name = instance_name
        # The names of the tables in the Tablestore instance.
        self.table_names = table_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.table_names is not None:
            result['TableNames'] = self.table_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')
        return self


class DescribeOtsTableSnapshotsRequest(TeaModel):
    def __init__(
        self,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        end_time: int = None,
        limit: int = None,
        next_token: str = None,
        ots_instances: List[DescribeOtsTableSnapshotsRequestOtsInstances] = None,
        snapshot_ids: List[str] = None,
        start_time: int = None,
    ):
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The UID of the source account used for cross-account backup.
        self.cross_account_user_id = cross_account_user_id
        # The end time of the backup. The value must be a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time
        # The maximum number of rows that you want the current query to return.
        self.limit = limit
        # The token that is required to obtain the next page of backup snapshots.
        self.next_token = next_token
        # The Tablestore instances that are backed up.
        self.ots_instances = ots_instances
        # The snapshot IDs.
        self.snapshot_ids = snapshot_ids
        # The start time of the backup. The value must be a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time

    def validate(self):
        if self.ots_instances:
            for k in self.ots_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['OtsInstances'] = []
        if self.ots_instances is not None:
            for k in self.ots_instances:
                result['OtsInstances'].append(k.to_map() if k else None)
        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.ots_instances = []
        if m.get('OtsInstances') is not None:
            for k in m.get('OtsInstances'):
                temp_model = DescribeOtsTableSnapshotsRequestOtsInstances()
                self.ots_instances.append(temp_model.from_map(k))
        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeOtsTableSnapshotsResponseBodySnapshots(TeaModel):
    def __init__(
        self,
        actual_bytes: str = None,
        backup_type: str = None,
        bytes_total: int = None,
        complete_time: int = None,
        create_time: int = None,
        created_time: int = None,
        instance_name: str = None,
        job_id: str = None,
        parent_snapshot_hash: str = None,
        range_end: int = None,
        range_start: int = None,
        retention: int = None,
        snapshot_hash: str = None,
        snapshot_id: str = None,
        source_type: str = None,
        start_time: int = None,
        status: str = None,
        table_name: str = None,
        updated_time: int = None,
        vault_id: str = None,
    ):
        # The actual data amount of backup snapshots after duplicates are removed. Unit: bytes.
        self.actual_bytes = actual_bytes
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # The total amount of data. Unit: bytes.
        self.bytes_total = bytes_total
        # The time when the backup snapshot was completed. The value is a UNIX timestamp. Unit: seconds.
        self.complete_time = complete_time
        # The time when the Tablestore instance was created. The value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time
        # The time when the backup snapshot was created. The value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The name of the Tablestore instance.
        self.instance_name = instance_name
        # The ID of the backup job.
        self.job_id = job_id
        # The hash value of the parent backup snapshot.
        self.parent_snapshot_hash = parent_snapshot_hash
        # The time when the backup job ended. The value is a UNIX timestamp. Unit: milliseconds.
        self.range_end = range_end
        # The time when the backup job started. The value is a UNIX timestamp. Unit: milliseconds.
        self.range_start = range_start
        # The retention period of the backup snapshot. Unit: days.
        self.retention = retention
        # The hash value of the backup snapshot.
        self.snapshot_hash = snapshot_hash
        # The ID of the backup snapshot.
        self.snapshot_id = snapshot_id
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: backup snapshots for Elastic Compute Service (ECS) files
        # *   **OSS**: backup snapshots for Object Storage Service (OSS) buckets
        # *   **NAS**: backup snapshots for Apsara File Storage NAS file systems
        # *   **OTS_TABLE**: backup snapshots for Tablestore instances
        self.source_type = source_type
        # The time when the backup snapshot started. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time
        # The status of the backup job. Valid values:
        # 
        # *   **COMPLETE**: The backup job is completed.
        # *   **PARTIAL_COMPLETE**: The backup job is partially completed.
        # *   **FAILED**: The backup job has failed.
        self.status = status
        # The name of the table in the Tablestore instance.
        self.table_name = table_name
        # The time when the backup snapshot was updated. The value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time
        # The ID of the backup vault that stores the backup snapshot.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_bytes is not None:
            result['ActualBytes'] = self.actual_bytes
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.bytes_total is not None:
            result['BytesTotal'] = self.bytes_total
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.parent_snapshot_hash is not None:
            result['ParentSnapshotHash'] = self.parent_snapshot_hash
        if self.range_end is not None:
            result['RangeEnd'] = self.range_end
        if self.range_start is not None:
            result['RangeStart'] = self.range_start
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.snapshot_hash is not None:
            result['SnapshotHash'] = self.snapshot_hash
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualBytes') is not None:
            self.actual_bytes = m.get('ActualBytes')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BytesTotal') is not None:
            self.bytes_total = m.get('BytesTotal')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ParentSnapshotHash') is not None:
            self.parent_snapshot_hash = m.get('ParentSnapshotHash')
        if m.get('RangeEnd') is not None:
            self.range_end = m.get('RangeEnd')
        if m.get('RangeStart') is not None:
            self.range_start = m.get('RangeStart')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('SnapshotHash') is not None:
            self.snapshot_hash = m.get('SnapshotHash')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeOtsTableSnapshotsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        limit: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        snapshots: List[DescribeOtsTableSnapshotsResponseBodySnapshots] = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The number of backup snapshots that are displayed on the current page.
        self.limit = limit
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The token that is required to obtain the next page of backup snapshots.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The backup snapshots.
        self.snapshots = snapshots
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.snapshots:
            for k in self.snapshots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = DescribeOtsTableSnapshotsResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeOtsTableSnapshotsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOtsTableSnapshotsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeOtsTableSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePoliciesV2Request(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        policy_id: str = None,
    ):
        # The number of results for each query.
        # 
        # Valid values: 10 to 100. Default value: 10.
        self.max_results = max_results
        # The token that is used to obtain the next page of backup policies.
        self.next_token = next_token
        # The ID of the backup policy.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class DescribePoliciesV2ResponseBodyPoliciesRulesDataSourceFilters(TeaModel):
    def __init__(
        self,
        data_source_ids: List[str] = None,
        source_type: str = None,
    ):
        # Deprecated.
        self.data_source_ids = data_source_ids
        # Data source type. The value range is as follows: 
        # - **UDM_ECS**: Indicates ECS server backup. 
        # - **OSS**: Indicates OSS backup. 
        # - **NAS**: Indicates Alibaba Cloud NAS backup. 
        # - **ECS_FILE**: Indicates ECS file backup. 
        # - **OTS**: Indicates Tablestore backup.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_ids is not None:
            result['DataSourceIds'] = self.data_source_ids
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceIds') is not None:
            self.data_source_ids = m.get('DataSourceIds')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class DescribePoliciesV2ResponseBodyPoliciesRulesRetentionRules(TeaModel):
    def __init__(
        self,
        advanced_retention_type: str = None,
        retention: int = None,
        which_snapshot: int = None,
    ):
        # The type of the special retention rule. Valid values:
        # 
        # *   **WEEKLY**: weekly backups
        # *   **MONTHLY**: monthly backups
        # *   **YEARLY**: yearly backups
        self.advanced_retention_type = advanced_retention_type
        # The special retention period of backups. Minimum value: 1. Unit: days.
        self.retention = retention
        # Indicates which backup is retained based on the special retention rule. Only the first backup can be retained.
        self.which_snapshot = which_snapshot

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_retention_type is not None:
            result['AdvancedRetentionType'] = self.advanced_retention_type
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.which_snapshot is not None:
            result['WhichSnapshot'] = self.which_snapshot
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedRetentionType') is not None:
            self.advanced_retention_type = m.get('AdvancedRetentionType')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('WhichSnapshot') is not None:
            self.which_snapshot = m.get('WhichSnapshot')
        return self


class DescribePoliciesV2ResponseBodyPoliciesRulesTagFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # Tag key
        self.key = key
        # Tag matching rules, supporting: - **EQUAL**: Matches both the tag key and tag value. - **NOT**: Matches the tag key but not the tag value.
        self.operator = operator
        # Tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribePoliciesV2ResponseBodyPoliciesRules(TeaModel):
    def __init__(
        self,
        archive_days: int = None,
        backup_type: str = None,
        data_source_filters: List[DescribePoliciesV2ResponseBodyPoliciesRulesDataSourceFilters] = None,
        immutable: bool = None,
        keep_latest_snapshots: int = None,
        replication_region_id: str = None,
        retention: int = None,
        retention_rules: List[DescribePoliciesV2ResponseBodyPoliciesRulesRetentionRules] = None,
        rule_id: str = None,
        rule_type: str = None,
        schedule: str = None,
        tag_filters: List[DescribePoliciesV2ResponseBodyPoliciesRulesTagFilters] = None,
        vault_id: str = None,
    ):
        # This parameter is returned only if the value of the **RuleType** parameter is **TRANSITION**. This parameter indicates the time when data is dumped from a backup vault to an archive vault. Unit: days.
        self.archive_days = archive_days
        # This parameter is returned only if the value of the **RuleType** parameter is **BACKUP**. This parameter indicates the backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # This parameter is required only when **RuleType** is set to **TAG**. It defines the data source filtering rule.
        self.data_source_filters = data_source_filters
        # This parameter is returned only if the **PolicyType** is **UDM_ECS_ONLY**. This parameter indicates whether the immutable backup feature is enabled.
        self.immutable = immutable
        # Indicates whether the feature of keeping at least one backup version is enabled. Valid values:
        # 
        # *   **0**: The feature is disabled.
        # *   **1**: The feature is enabled.
        self.keep_latest_snapshots = keep_latest_snapshots
        # This parameter is returned only if the value of the **RuleType** parameter is **REPLICATION**. This parameter indicates the ID of the destination region.
        self.replication_region_id = replication_region_id
        # This parameter is returned only if the value of the **RuleType** parameter is **TRANSITION** or **REPLICATION**.
        # 
        # *   If the value of the **RuleType** parameter is **TRANSITION**, this parameter indicates the retention period of the backup data. Minimum value: 1. Unit: days.
        # *   If the value of the **RuleType** parameter is **REPLICATION**, this parameter indicates the retention period of remote backups. Minimum value: 1. Unit: days.
        self.retention = retention
        # This parameter is returned only if the value of the **RuleType** parameter is **TRANSITION**. This parameter indicates the special retention rules.
        self.retention_rules = retention_rules
        # The rule ID.
        self.rule_id = rule_id
        # The type of the rule. Each backup policy must have at least one rule of the **BACKUP** type and only one rule of the **TRANSITION** type. Valid values:
        # 
        # *   **BACKUP**: backup rule
        # *   **TRANSITION**: lifecycle rule
        # *   **REPLICATION**: replication rule
        self.rule_type = rule_type
        # This parameter is returned only if the value of the **RuleType** parameter is **BACKUP**. This parameter indicates the backup schedule settings. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` indicates that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   startTime: the time at which the system starts to run a backup job. The time follows the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system runs a backup job. The interval follows the ISO 8601 standard. For example, PT1H indicates an interval of 1 hour. P1D indicates an interval of one day.
        self.schedule = schedule
        # This parameter is required only when **RuleType** is set to **TAG**. It defines the resource tag filtering rule.
        self.tag_filters = tag_filters
        # This parameter is returned only if the value of the RuleType parameter is BACKUP. The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        if self.data_source_filters:
            for k in self.data_source_filters:
                if k:
                    k.validate()
        if self.retention_rules:
            for k in self.retention_rules:
                if k:
                    k.validate()
        if self.tag_filters:
            for k in self.tag_filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_days is not None:
            result['ArchiveDays'] = self.archive_days
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        result['DataSourceFilters'] = []
        if self.data_source_filters is not None:
            for k in self.data_source_filters:
                result['DataSourceFilters'].append(k.to_map() if k else None)
        if self.immutable is not None:
            result['Immutable'] = self.immutable
        if self.keep_latest_snapshots is not None:
            result['KeepLatestSnapshots'] = self.keep_latest_snapshots
        if self.replication_region_id is not None:
            result['ReplicationRegionId'] = self.replication_region_id
        if self.retention is not None:
            result['Retention'] = self.retention
        result['RetentionRules'] = []
        if self.retention_rules is not None:
            for k in self.retention_rules:
                result['RetentionRules'].append(k.to_map() if k else None)
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        result['TagFilters'] = []
        if self.tag_filters is not None:
            for k in self.tag_filters:
                result['TagFilters'].append(k.to_map() if k else None)
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveDays') is not None:
            self.archive_days = m.get('ArchiveDays')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        self.data_source_filters = []
        if m.get('DataSourceFilters') is not None:
            for k in m.get('DataSourceFilters'):
                temp_model = DescribePoliciesV2ResponseBodyPoliciesRulesDataSourceFilters()
                self.data_source_filters.append(temp_model.from_map(k))
        if m.get('Immutable') is not None:
            self.immutable = m.get('Immutable')
        if m.get('KeepLatestSnapshots') is not None:
            self.keep_latest_snapshots = m.get('KeepLatestSnapshots')
        if m.get('ReplicationRegionId') is not None:
            self.replication_region_id = m.get('ReplicationRegionId')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        self.retention_rules = []
        if m.get('RetentionRules') is not None:
            for k in m.get('RetentionRules'):
                temp_model = DescribePoliciesV2ResponseBodyPoliciesRulesRetentionRules()
                self.retention_rules.append(temp_model.from_map(k))
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        self.tag_filters = []
        if m.get('TagFilters') is not None:
            for k in m.get('TagFilters'):
                temp_model = DescribePoliciesV2ResponseBodyPoliciesRulesTagFilters()
                self.tag_filters.append(temp_model.from_map(k))
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribePoliciesV2ResponseBodyPolicies(TeaModel):
    def __init__(
        self,
        created_time: int = None,
        policy_binding_count: int = None,
        policy_description: str = None,
        policy_id: str = None,
        policy_name: str = None,
        policy_type: str = None,
        rules: List[DescribePoliciesV2ResponseBodyPoliciesRules] = None,
        updated_time: int = None,
    ):
        # The time when the backup policy was created. The value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The number of data sources that are bound to the backup policy.
        self.policy_binding_count = policy_binding_count
        # The description of the backup policy.
        self.policy_description = policy_description
        # The ID of the backup policy.
        self.policy_id = policy_id
        # The name of the backup policy.
        self.policy_name = policy_name
        # The policy type. Valid values:
        # 
        # *   **STANDARD**: the general backup policy. This type of policy applies to backups other than Elastic Compute Service (ECS) instance backup.
        # *   **UDM_ECS_ONLY**: the ECS instance backup policy. This type of policy applies only to ECS instance backup.
        self.policy_type = policy_type
        # The rules in the backup policy.
        self.rules = rules
        # The time when the backup policy was updated. The value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.policy_binding_count is not None:
            result['PolicyBindingCount'] = self.policy_binding_count
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('PolicyBindingCount') is not None:
            self.policy_binding_count = m.get('PolicyBindingCount')
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribePoliciesV2ResponseBodyPoliciesRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class DescribePoliciesV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        policies: List[DescribePoliciesV2ResponseBodyPolicies] = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The number of results for each query.
        # 
        # Valid values: 10 to 100. Default value: 10.
        self.max_results = max_results
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The token that is used to obtain the next page of backup policies.
        self.next_token = next_token
        # The backup policies.
        self.policies = policies
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = DescribePoliciesV2ResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePoliciesV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePoliciesV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePoliciesV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyBindingsRequestFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # Key in the query filter. Possible values include:
        # 
        # - **PolicyId**: Backup policy ID
        # - **DataSourceId**: ECS instance ID
        # - **DataSourceType**: Data source type
        self.key = key
        # Matching method. Default is IN. This refers to the matching operation (Operator) supported by the Key and Value in the filter. Possible values include:
        # 
        # - **EQUAL**: Equal to
        # - **NOT_EQUAL**: Not equal to
        # - **GREATER_THAN**: Greater than
        # - **GREATER_THAN_OR_EQUAL**: Greater than or equal to
        # - **LESS_THAN**: Less than
        # - **LESS_THAN_OR_EQUAL**: Less than or equal to
        # - **BETWEEN**: Range, where value is a JSON array `[lower_bound, upper_bound]`.
        # - **IN**: In the set, where value is an array.
        self.operator = operator
        # Values to be matched in the query filter.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribePolicyBindingsRequest(TeaModel):
    def __init__(
        self,
        data_source_ids: List[str] = None,
        filters: List[DescribePolicyBindingsRequestFilters] = None,
        max_results: int = None,
        next_token: str = None,
        policy_id: str = None,
        source_type: str = None,
    ):
        # List of data source IDs.
        self.data_source_ids = data_source_ids
        # Query filters.
        self.filters = filters
        # Number of results per query.
        # 
        # Range: 10~100. Default: 10.
        self.max_results = max_results
        # Token required to fetch the next page of policy and data source associations.
        self.next_token = next_token
        # Policy ID.
        self.policy_id = policy_id
        # Data source type. Possible values:
        # * **UDM_ECS**: Indicates ECS full machine backup.
        self.source_type = source_type

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_ids is not None:
            result['DataSourceIds'] = self.data_source_ids
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceIds') is not None:
            self.data_source_ids = m.get('DataSourceIds')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = DescribePolicyBindingsRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class DescribePolicyBindingsShrinkRequestFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # Key in the query filter. Possible values include:
        # 
        # - **PolicyId**: Backup policy ID
        # - **DataSourceId**: ECS instance ID
        # - **DataSourceType**: Data source type
        self.key = key
        # Matching method. Default is IN. This refers to the matching operation (Operator) supported by the Key and Value in the filter. Possible values include:
        # 
        # - **EQUAL**: Equal to
        # - **NOT_EQUAL**: Not equal to
        # - **GREATER_THAN**: Greater than
        # - **GREATER_THAN_OR_EQUAL**: Greater than or equal to
        # - **LESS_THAN**: Less than
        # - **LESS_THAN_OR_EQUAL**: Less than or equal to
        # - **BETWEEN**: Range, where value is a JSON array `[lower_bound, upper_bound]`.
        # - **IN**: In the set, where value is an array.
        self.operator = operator
        # Values to be matched in the query filter.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribePolicyBindingsShrinkRequest(TeaModel):
    def __init__(
        self,
        data_source_ids_shrink: str = None,
        filters: List[DescribePolicyBindingsShrinkRequestFilters] = None,
        max_results: int = None,
        next_token: str = None,
        policy_id: str = None,
        source_type: str = None,
    ):
        # List of data source IDs.
        self.data_source_ids_shrink = data_source_ids_shrink
        # Query filters.
        self.filters = filters
        # Number of results per query.
        # 
        # Range: 10~100. Default: 10.
        self.max_results = max_results
        # Token required to fetch the next page of policy and data source associations.
        self.next_token = next_token
        # Policy ID.
        self.policy_id = policy_id
        # Data source type. Possible values:
        # * **UDM_ECS**: Indicates ECS full machine backup.
        self.source_type = source_type

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_ids_shrink is not None:
            result['DataSourceIds'] = self.data_source_ids_shrink
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceIds') is not None:
            self.data_source_ids_shrink = m.get('DataSourceIds')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = DescribePolicyBindingsShrinkRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsCommonFileSystemDetail(TeaModel):
    def __init__(
        self,
        fetch_slice_size: int = None,
        full_on_increment_fail: bool = None,
    ):
        # Backup shard size (number of files).
        self.fetch_slice_size = fetch_slice_size
        # Whether to switch to a full backup when an incremental backup fails. Values:
        # - **true**: Switch to full backup on failure.
        # - **false**: Do not switch to full backup on failure.
        self.full_on_increment_fail = full_on_increment_fail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fetch_slice_size is not None:
            result['FetchSliceSize'] = self.fetch_slice_size
        if self.full_on_increment_fail is not None:
            result['FullOnIncrementFail'] = self.full_on_increment_fail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FetchSliceSize') is not None:
            self.fetch_slice_size = m.get('FetchSliceSize')
        if m.get('FullOnIncrementFail') is not None:
            self.full_on_increment_fail = m.get('FullOnIncrementFail')
        return self


class DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsCommonNasDetail(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        cluster_id: str = None,
        fetch_slice_size: int = None,
        full_on_increment_fail: bool = None,
    ):
        # Backup client ID.
        self.client_id = client_id
        # Client group ID.
        self.cluster_id = cluster_id
        # Backup slice size (number of files).
        self.fetch_slice_size = fetch_slice_size
        # Whether to switch to a full backup when an incremental backup fails. Values:
        # - **true**: Switch to full backup on failure.
        # - **false**: Do not switch to full backup on failure.
        self.full_on_increment_fail = full_on_increment_fail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.fetch_slice_size is not None:
            result['FetchSliceSize'] = self.fetch_slice_size
        if self.full_on_increment_fail is not None:
            result['FullOnIncrementFail'] = self.full_on_increment_fail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('FetchSliceSize') is not None:
            self.fetch_slice_size = m.get('FetchSliceSize')
        if m.get('FullOnIncrementFail') is not None:
            self.full_on_increment_fail = m.get('FullOnIncrementFail')
        return self


class DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsFileDetail(TeaModel):
    def __init__(
        self,
        adv_policy: bool = None,
        use_vss: bool = None,
    ):
        # Whether to use advanced policies. Values:
        # - **true**: Use.
        # - **false**: Do not use.
        self.adv_policy = adv_policy
        # Whether to enable VSS (Windows) functionality. Values:
        # - **true**: Enable.
        # - **false**: Disable.
        self.use_vss = use_vss

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adv_policy is not None:
            result['AdvPolicy'] = self.adv_policy
        if self.use_vss is not None:
            result['UseVSS'] = self.use_vss
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvPolicy') is not None:
            self.adv_policy = m.get('AdvPolicy')
        if m.get('UseVSS') is not None:
            self.use_vss = m.get('UseVSS')
        return self


class DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsOssDetail(TeaModel):
    def __init__(
        self,
        ignore_archive_object: bool = None,
        inventory_cleanup_policy: str = None,
        inventory_id: str = None,
    ):
        # Do not prompt for archive-type objects in the task statistics and failed file list.
        self.ignore_archive_object = ignore_archive_object
        # Whether to delete the inventory file after the backup. This is only effective when using an OSS inventory. Supported values:
        # - **NO_CLEANUP**: Do not delete.
        # - **DELETE_CURRENT**: Delete the current file.
        # - **DELETE_CURRENT_AND_PREVIOUS**: Delete all files.
        self.inventory_cleanup_policy = inventory_cleanup_policy
        # The name of the OSS inventory. If this value is not empty, the OSS inventory will be used for performance optimization.
        # - It is recommended to use an inventory for backing up more than 100 million OSS objects to improve incremental performance. Storage costs for the inventory files are charged separately by the OSS service.
        # - The generation of the OSS inventory file takes time, and the backup may fail before the inventory file is generated. You can wait for the next cycle to execute.
        self.inventory_id = inventory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ignore_archive_object is not None:
            result['IgnoreArchiveObject'] = self.ignore_archive_object
        if self.inventory_cleanup_policy is not None:
            result['InventoryCleanupPolicy'] = self.inventory_cleanup_policy
        if self.inventory_id is not None:
            result['InventoryId'] = self.inventory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoreArchiveObject') is not None:
            self.ignore_archive_object = m.get('IgnoreArchiveObject')
        if m.get('InventoryCleanupPolicy') is not None:
            self.inventory_cleanup_policy = m.get('InventoryCleanupPolicy')
        if m.get('InventoryId') is not None:
            self.inventory_id = m.get('InventoryId')
        return self


class DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsUdmDetail(TeaModel):
    def __init__(
        self,
        app_consistent: bool = None,
        destination_kms_key_id: str = None,
        disk_id_list: List[str] = None,
        enable_fs_freeze: bool = None,
        enable_writers: bool = None,
        exclude_disk_id_list: List[str] = None,
        post_script_path: str = None,
        pre_script_path: str = None,
        ram_role_name: str = None,
        snapshot_group: bool = None,
        timeout_in_seconds: int = None,
    ):
        # 是否创建应用一致性。仅云盘类型全部为ESSD时，支持创建快照应用一致性。
        self.app_consistent = app_consistent
        # The custom KMS key ID in the destination region. When this field is not empty and cross-region replication is enabled, the specified key will be used for encrypting the cross-region replication.
        self.destination_kms_key_id = destination_kms_key_id
        # List of disk IDs that need protection. This value is empty when protecting all disks.
        self.disk_id_list = disk_id_list
        # This parameter is required when **AppConsistent** is **true**. It indicates whether to use the Linux FsFreeze mechanism to ensure the file system is in a read-only consistent state before creating an application-consistent snapshot. The default value is true.
        self.enable_fs_freeze = enable_fs_freeze
        # This parameter is required when **AppConsistent** is **true**. It determines whether to set an application-consistent snapshot:
        # - **true**: Create an application-consistent snapshot
        # - **false**: Create a file system-consistent snapshot
        # 
        # The default value is true.
        self.enable_writers = enable_writers
        # List of disk IDs that do not need protection. This parameter is ignored if DiskIdList is not empty.
        self.exclude_disk_id_list = exclude_disk_id_list
        # This parameter is required when **AppConsistent** is **true**. It specifies the path of the unfreeze script to be executed after creating an application-consistent snapshot.
        self.post_script_path = post_script_path
        # This parameter is required when **AppConsistent** is **true**. It specifies the path of the freeze script to be executed before creating an application-consistent snapshot.
        self.pre_script_path = pre_script_path
        # This parameter is required when **AppConsistent** is **true**. It specifies the RAM role name needed for creating an application-consistent snapshot.
        self.ram_role_name = ram_role_name
        # Indicates whether to create a snapshot consistency group. Only supported when all disk types are ESSD.
        self.snapshot_group = snapshot_group
        # This parameter is required when **AppConsistent** is **true**. It specifies the IO freeze timeout duration. The default value is 30 seconds.
        self.timeout_in_seconds = timeout_in_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_consistent is not None:
            result['AppConsistent'] = self.app_consistent
        if self.destination_kms_key_id is not None:
            result['DestinationKmsKeyId'] = self.destination_kms_key_id
        if self.disk_id_list is not None:
            result['DiskIdList'] = self.disk_id_list
        if self.enable_fs_freeze is not None:
            result['EnableFsFreeze'] = self.enable_fs_freeze
        if self.enable_writers is not None:
            result['EnableWriters'] = self.enable_writers
        if self.exclude_disk_id_list is not None:
            result['ExcludeDiskIdList'] = self.exclude_disk_id_list
        if self.post_script_path is not None:
            result['PostScriptPath'] = self.post_script_path
        if self.pre_script_path is not None:
            result['PreScriptPath'] = self.pre_script_path
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.snapshot_group is not None:
            result['SnapshotGroup'] = self.snapshot_group
        if self.timeout_in_seconds is not None:
            result['TimeoutInSeconds'] = self.timeout_in_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppConsistent') is not None:
            self.app_consistent = m.get('AppConsistent')
        if m.get('DestinationKmsKeyId') is not None:
            self.destination_kms_key_id = m.get('DestinationKmsKeyId')
        if m.get('DiskIdList') is not None:
            self.disk_id_list = m.get('DiskIdList')
        if m.get('EnableFsFreeze') is not None:
            self.enable_fs_freeze = m.get('EnableFsFreeze')
        if m.get('EnableWriters') is not None:
            self.enable_writers = m.get('EnableWriters')
        if m.get('ExcludeDiskIdList') is not None:
            self.exclude_disk_id_list = m.get('ExcludeDiskIdList')
        if m.get('PostScriptPath') is not None:
            self.post_script_path = m.get('PostScriptPath')
        if m.get('PreScriptPath') is not None:
            self.pre_script_path = m.get('PreScriptPath')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('SnapshotGroup') is not None:
            self.snapshot_group = m.get('SnapshotGroup')
        if m.get('TimeoutInSeconds') is not None:
            self.timeout_in_seconds = m.get('TimeoutInSeconds')
        return self


class DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptions(TeaModel):
    def __init__(
        self,
        common_file_system_detail: DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsCommonFileSystemDetail = None,
        common_nas_detail: DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsCommonNasDetail = None,
        file_detail: DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsFileDetail = None,
        oss_detail: DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsOssDetail = None,
        udm_detail: DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsUdmDetail = None,
    ):
        # Advanced options for large-scale file system backup.
        self.common_file_system_detail = common_file_system_detail
        # Advanced options for local NAS.
        self.common_nas_detail = common_nas_detail
        # Advanced options for file backup.
        self.file_detail = file_detail
        # Advanced options for OSS backup.
        self.oss_detail = oss_detail
        # Advanced options for full machine backup.
        self.udm_detail = udm_detail

    def validate(self):
        if self.common_file_system_detail:
            self.common_file_system_detail.validate()
        if self.common_nas_detail:
            self.common_nas_detail.validate()
        if self.file_detail:
            self.file_detail.validate()
        if self.oss_detail:
            self.oss_detail.validate()
        if self.udm_detail:
            self.udm_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_file_system_detail is not None:
            result['CommonFileSystemDetail'] = self.common_file_system_detail.to_map()
        if self.common_nas_detail is not None:
            result['CommonNasDetail'] = self.common_nas_detail.to_map()
        if self.file_detail is not None:
            result['FileDetail'] = self.file_detail.to_map()
        if self.oss_detail is not None:
            result['OssDetail'] = self.oss_detail.to_map()
        if self.udm_detail is not None:
            result['UdmDetail'] = self.udm_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonFileSystemDetail') is not None:
            temp_model = DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsCommonFileSystemDetail()
            self.common_file_system_detail = temp_model.from_map(m['CommonFileSystemDetail'])
        if m.get('CommonNasDetail') is not None:
            temp_model = DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsCommonNasDetail()
            self.common_nas_detail = temp_model.from_map(m['CommonNasDetail'])
        if m.get('FileDetail') is not None:
            temp_model = DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsFileDetail()
            self.file_detail = temp_model.from_map(m['FileDetail'])
        if m.get('OssDetail') is not None:
            temp_model = DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsOssDetail()
            self.oss_detail = temp_model.from_map(m['OssDetail'])
        if m.get('UdmDetail') is not None:
            temp_model = DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsUdmDetail()
            self.udm_detail = temp_model.from_map(m['UdmDetail'])
        return self


class DescribePolicyBindingsResponseBodyPolicyBindingsHitTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # Tag key.
        self.key = key
        # Tag matching rule.
        # - **EQUAL**: Matches both the tag key and tag value.
        # - **NOT**: Matches the tag key but not the tag value.
        self.operator = operator
        # Tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribePolicyBindingsResponseBodyPolicyBindings(TeaModel):
    def __init__(
        self,
        advanced_options: DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptions = None,
        created_by_tag: bool = None,
        created_time: int = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        data_source_id: str = None,
        disabled: bool = None,
        exclude: str = None,
        hit_tags: List[DescribePolicyBindingsResponseBodyPolicyBindingsHitTags] = None,
        include: str = None,
        policy_binding_description: str = None,
        policy_binding_id: str = None,
        policy_id: str = None,
        source: str = None,
        source_type: str = None,
        speed_limit: str = None,
        updated_time: int = None,
    ):
        # Advanced options.
        self.advanced_options = advanced_options
        # Whether the resource is automatically associated through the backup policy resource tag.
        self.created_by_tag = created_by_tag
        # Creation time. UNIX timestamp, in seconds.
        self.created_time = created_time
        # The name of the role created in the RAM of the original account for cross-account backup.
        self.cross_account_role_name = cross_account_role_name
        # Cross-account backup type. Supported values: 
        # - SELF_ACCOUNT: Backup within the same account
        # - CROSS_ACCOUNT: Cross-account backup
        self.cross_account_type = cross_account_type
        # The ID of the original account for cross-account backup.
        self.cross_account_user_id = cross_account_user_id
        # Data source ID.
        self.data_source_id = data_source_id
        # 策略是否对该数据源生效。
        # - true：暂停
        # - false：未暂停
        self.disabled = disabled
        # This parameter is required only when **SourceType** is **ECS_FILE** or **File**. It specifies the file types that should not be backed up, and all files of these types will be excluded. Supports up to 255 characters.
        self.exclude = exclude
        # Hit tag rules.
        self.hit_tags = hit_tags
        # This parameter is required only when **SourceType** is **ECS_FILE** or **File**. It specifies the file types to be backed up, and all files of these types will be backed up. Supports up to 255 characters.
        self.include = include
        # Bound policy description.
        self.policy_binding_description = policy_binding_description
        # Bound policy ID.
        self.policy_binding_id = policy_binding_id
        # Policy ID.
        self.policy_id = policy_id
        # - When **SourceType** is **OSS**, it indicates the prefix to be backed up. If not specified, it means backing up the entire root directory of the Bucket.
        # - When **SourceType** is **ECS_FILE** or **File**, it indicates the file directory to be backed up. If not specified, it means backing up all directories.
        self.source = source
        # Data source type, with the value range:
        # - **UDM_ECS**: indicates ECS full machine backup
        self.source_type = source_type
        # This parameter is required only when **SourceType** is **ECS_FILE** or **File**. It specifies the backup traffic control. The format is `{start}{end}{bandwidth}`. Multiple traffic control configurations are separated by commas, and the configured times must not overlap.
        # 
        # - **start**: Start hour.
        # - **end**: End hour.
        # - **bandwidth**: Limit rate, in KB/s.
        self.speed_limit = speed_limit
        # Update time. UNIX timestamp, in seconds.
        self.updated_time = updated_time

    def validate(self):
        if self.advanced_options:
            self.advanced_options.validate()
        if self.hit_tags:
            for k in self.hit_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_options is not None:
            result['AdvancedOptions'] = self.advanced_options.to_map()
        if self.created_by_tag is not None:
            result['CreatedByTag'] = self.created_by_tag
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        result['HitTags'] = []
        if self.hit_tags is not None:
            for k in self.hit_tags:
                result['HitTags'].append(k.to_map() if k else None)
        if self.include is not None:
            result['Include'] = self.include
        if self.policy_binding_description is not None:
            result['PolicyBindingDescription'] = self.policy_binding_description
        if self.policy_binding_id is not None:
            result['PolicyBindingId'] = self.policy_binding_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedOptions') is not None:
            temp_model = DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptions()
            self.advanced_options = temp_model.from_map(m['AdvancedOptions'])
        if m.get('CreatedByTag') is not None:
            self.created_by_tag = m.get('CreatedByTag')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        self.hit_tags = []
        if m.get('HitTags') is not None:
            for k in m.get('HitTags'):
                temp_model = DescribePolicyBindingsResponseBodyPolicyBindingsHitTags()
                self.hit_tags.append(temp_model.from_map(k))
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('PolicyBindingDescription') is not None:
            self.policy_binding_description = m.get('PolicyBindingDescription')
        if m.get('PolicyBindingId') is not None:
            self.policy_binding_id = m.get('PolicyBindingId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class DescribePolicyBindingsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        policy_bindings: List[DescribePolicyBindingsResponseBodyPolicyBindings] = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # Return code, 200 indicates success.
        self.code = code
        # The number of results per query.
        # 
        # Range: 10~100. Default: 10.
        self.max_results = max_results
        # Description of the return message. A successful response usually returns \\"successful\\", while an error will return a corresponding error message.
        self.message = message
        # The token required to fetch the next page of policy and data source bindings.
        self.next_token = next_token
        # List of bound policies.
        self.policy_bindings = policy_bindings
        # Request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # - true: Success
        # - false: Failure
        self.success = success
        # Total number of records.
        self.total_count = total_count

    def validate(self):
        if self.policy_bindings:
            for k in self.policy_bindings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['PolicyBindings'] = []
        if self.policy_bindings is not None:
            for k in self.policy_bindings:
                result['PolicyBindings'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.policy_bindings = []
        if m.get('PolicyBindings') is not None:
            for k in m.get('PolicyBindings'):
                temp_model = DescribePolicyBindingsResponseBodyPolicyBindings()
                self.policy_bindings.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePolicyBindingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePolicyBindingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePolicyBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecoverableOtsInstancesRequest(TeaModel):
    def __init__(
        self,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
    ):
        # The name of the Resource Access Management (RAM) role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        return self


class DescribeRecoverableOtsInstancesResponseBodyOtsInstances(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        table_names: List[str] = None,
    ):
        # The name of the Tablestore instance that can be restored.
        self.instance_name = instance_name
        # The names of the tables in the Tablestore instance.
        self.table_names = table_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.table_names is not None:
            result['TableNames'] = self.table_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')
        return self


class DescribeRecoverableOtsInstancesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        ots_instances: List[DescribeRecoverableOtsInstancesResponseBodyOtsInstances] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The list of Tablestore instances that can be restored and the tables in the instances.
        self.ots_instances = ots_instances
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.ots_instances:
            for k in self.ots_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['OtsInstances'] = []
        if self.ots_instances is not None:
            for k in self.ots_instances:
                result['OtsInstances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.ots_instances = []
        if m.get('OtsInstances') is not None:
            for k in m.get('OtsInstances'):
                temp_model = DescribeRecoverableOtsInstancesResponseBodyOtsInstances()
                self.ots_instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRecoverableOtsInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRecoverableOtsInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRecoverableOtsInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
    ):
        # The region name.
        self.local_name = local_name
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The regions returned.
        self.regions = regions
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRestoreJobs2RequestFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # The key in the filter. Valid values:
        # 
        # *   **RegionId**: the region ID
        # *   **PlanId**: the ID of a backup plan
        # *   **JobId**: the ID of a backup job
        # *   **VaultId**: the ID of a backup vault
        # *   **InstanceId**: the ID of an ECS instance
        # *   **Bucket**: the name of an OSS bucket
        # *   **FileSystemId**: the ID of a file system
        # *   **Status**: the status of a backup job
        # *   **CompleteTime**: the end time of a backup job
        self.key = key
        # The matching method. Default value: IN. This parameter specifies the operator that you want to use to match a key and a value in the filter. Valid values:
        # 
        # *   **EQUAL**: equal to
        # *   **NOT_EQUAL**: not equal to
        # *   **GREATER_THAN**: greater than
        # *   **GREATER_THAN_OR_EQUAL**: greater than or equal to
        # *   **LESS_THAN**: less than
        # *   **LESS_THAN_OR_EQUAL**: less than or equal to
        # *   **BETWEEN**: specifies a JSON array as a range. The results must fall within the range in the `[Minimum value,Maximum value]` format.
        # *   **IN**: specifies an array as a collection. The results must fall within the collection.
        # 
        # > If you specify the **CompleteTime** parameter as a key to query backup jobs, you cannot use the IN operator to perform a match.
        self.operator = operator
        # The values that you want to match in the filter.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeRestoreJobs2Request(TeaModel):
    def __init__(
        self,
        filters: List[DescribeRestoreJobs2RequestFilters] = None,
        page_number: int = None,
        page_size: int = None,
        restore_type: str = None,
    ):
        # The keys in the filter.
        self.filters = filters
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS file systems
        # *   **OTS_TABLE**: Tablestore instances
        # *   **UDM_ECS_ROLLBACK**: ECS instances
        self.restore_type = restore_type

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = DescribeRestoreJobs2RequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')
        return self


class DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJobOtsDetail(TeaModel):
    def __init__(
        self,
        batch_channel_count: int = None,
        overwrite_existing: bool = None,
    ):
        # The number of channels processed by each Tablestore restore job.
        self.batch_channel_count = batch_channel_count
        # Indicates whether the existing Tablestore restore job was overwritten.
        self.overwrite_existing = overwrite_existing

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_channel_count is not None:
            result['BatchChannelCount'] = self.batch_channel_count
        if self.overwrite_existing is not None:
            result['OverwriteExisting'] = self.overwrite_existing
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchChannelCount') is not None:
            self.batch_channel_count = m.get('BatchChannelCount')
        if m.get('OverwriteExisting') is not None:
            self.overwrite_existing = m.get('OverwriteExisting')
        return self


class DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJobReport(TeaModel):
    def __init__(
        self,
        failed_files: str = None,
        report_task_status: str = None,
        skipped_files: str = None,
        success_files: str = None,
        total_files: str = None,
    ):
        # The files that failed to be executed.
        self.failed_files = failed_files
        # The status of the report generation.
        self.report_task_status = report_task_status
        # The skipped files.
        self.skipped_files = skipped_files
        # The files that are successfully executed.
        self.success_files = success_files
        # The full files that are restored based on the file list.
        self.total_files = total_files

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_files is not None:
            result['FailedFiles'] = self.failed_files
        if self.report_task_status is not None:
            result['ReportTaskStatus'] = self.report_task_status
        if self.skipped_files is not None:
            result['SkippedFiles'] = self.skipped_files
        if self.success_files is not None:
            result['SuccessFiles'] = self.success_files
        if self.total_files is not None:
            result['TotalFiles'] = self.total_files
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedFiles') is not None:
            self.failed_files = m.get('FailedFiles')
        if m.get('ReportTaskStatus') is not None:
            self.report_task_status = m.get('ReportTaskStatus')
        if m.get('SkippedFiles') is not None:
            self.skipped_files = m.get('SkippedFiles')
        if m.get('SuccessFiles') is not None:
            self.success_files = m.get('SuccessFiles')
        if m.get('TotalFiles') is not None:
            self.total_files = m.get('TotalFiles')
        return self


class DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJob(TeaModel):
    def __init__(
        self,
        actual_bytes: int = None,
        actual_items: int = None,
        bytes_done: int = None,
        bytes_total: int = None,
        cluster_id: str = None,
        complete_time: int = None,
        created_time: int = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        error_file: str = None,
        error_message: str = None,
        exclude: str = None,
        expire_time: int = None,
        failback_detail: str = None,
        include: str = None,
        items_done: int = None,
        items_total: int = None,
        metering_bytes_done: int = None,
        metering_bytes_total: int = None,
        options: str = None,
        ots_detail: DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJobOtsDetail = None,
        parent_id: str = None,
        progress: int = None,
        report: DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJobReport = None,
        restore_id: str = None,
        restore_type: str = None,
        snapshot_hash: str = None,
        snapshot_id: str = None,
        source_type: str = None,
        speed: int = None,
        start_time: int = None,
        status: str = None,
        storage_class: str = None,
        target_bucket: str = None,
        target_client_id: str = None,
        target_create_time: int = None,
        target_data_source_id: str = None,
        target_file_system_id: str = None,
        target_instance_id: str = None,
        target_instance_name: str = None,
        target_path: str = None,
        target_prefix: str = None,
        target_table_name: str = None,
        target_time: int = None,
        udm_detail: str = None,
        updated_time: int = None,
        vault_id: str = None,
    ):
        # The actual amount of data that is restored after duplicates are removed. Unit: bytes.
        self.actual_bytes = actual_bytes
        # This parameter is valid only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the actual number of objects that are restored by the restore job.
        self.actual_items = actual_items
        # The amount of data that was restored. Unit: bytes.
        self.bytes_done = bytes_done
        # The total amount of data that was backed up from the data source. Unit: bytes.
        self.bytes_total = bytes_total
        # The ID of the client group used for restoration.
        self.cluster_id = cluster_id
        # The time when the restore job was completed. This value is a UNIX timestamp. Unit: seconds.
        self.complete_time = complete_time
        # The time when the restore job was created. This value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The name of the Resource Access Management (RAM) role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Indicates whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The files that failed to be restored.
        self.error_file = error_file
        # The error message that is returned for the restore job.
        self.error_message = error_message
        # This parameter is valid only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the paths to the files that are excluded from the restore job. The value can be up to 255 characters in length.
        self.exclude = exclude
        # The time when the restore job expires.
        self.expire_time = expire_time
        # The details about the VMware failback task.
        self.failback_detail = failback_detail
        # The paths to the files that are included in the restore job.
        self.include = include
        # This parameter is valid only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the number of restored objects.
        self.items_done = items_done
        # This parameter is valid only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the total number of objects in the data source.
        self.items_total = items_total
        # The amount of data that was restored. Unit: bytes. This parameter is valid only if the StorageClass parameter is set to ARCHIVE. The minimum billable size of the data stored at the Archive tier is 1 MB.
        self.metering_bytes_done = metering_bytes_done
        # The total amount of data that was backed up from the data source. Unit: bytes. This parameter is valid only if the StorageClass parameter is set to ARCHIVE. The minimum billable size of the data stored at the Archive tier is 1 MB.
        self.metering_bytes_total = metering_bytes_total
        # This parameter is valid only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates whether Windows Volume Shadow Copy Service (VSS) is used to define a restoration path.
        # 
        # *   This parameter is available only for Windows ECS instances.
        # *   If data changes occur in the backup source, the source data must be the same as the data to be backed up before you can set this parameter to `["UseVSS":true]`.
        # *   If you use VSS, you cannot restore data from multiple directories.
        self.options = options
        # The details about the Tablestore instance.
        self.ots_detail = ots_detail
        # The ID of the parent job.
        self.parent_id = parent_id
        # The progress of the restore job. Valid values: [0,10000]. For example, 10000 indicates that the progress is 100%.
        self.progress = progress
        # The report of the restore job.
        self.report = report
        # The ID of the restore job.
        self.restore_id = restore_id
        # The type of the restore job.
        self.restore_type = restore_type
        # The hash value of the backup snapshot.
        self.snapshot_hash = snapshot_hash
        # The ID of the snapshot used for restoration.
        self.snapshot_id = snapshot_id
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: ECS files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS (NAS) file systems
        # *   **OTS_TABLE**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        self.source_type = source_type
        # The average speed at which data is backed up. Unit: KB/s.
        self.speed = speed
        # The time when the restore job started. This value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time
        # The status of the restore job. Valid values:
        # 
        # *   **COMPLETE**: The job is completed.
        # *   **PARTIAL_COMPLETE**: The job is partially completed.
        # *   **FAILED**: The job failed.
        self.status = status
        # The storage class of the backup data. Valid values:
        # 
        # *   **STANDARD**\
        # *   **ARCHIVE**\
        self.storage_class = storage_class
        # The name of the destination OSS bucket. This parameter is returned only for OSS buckets.
        self.target_bucket = target_bucket
        # The ID of the destination client.
        self.target_client_id = target_client_id
        # The time when the file system was created. This parameter is returned only for NAS file systems.
        self.target_create_time = target_create_time
        # The ID of the destination data source.
        self.target_data_source_id = target_data_source_id
        # The ID of the destination NAS file system. This parameter is returned only for NAS file systems.
        self.target_file_system_id = target_file_system_id
        # The ID of the destination instance for the restore job.
        self.target_instance_id = target_instance_id
        # The name of the destination Tablestore instance.
        self.target_instance_name = target_instance_name
        # The destination file path of the restore job.
        self.target_path = target_path
        # The prefix of the objects that are restored. This parameter is returned only for OSS buckets.
        self.target_prefix = target_prefix
        # The name of the destination table in the Tablestore instance.
        self.target_table_name = target_table_name
        # The time when the Tablestore instance was backed up. This value is a UNIX timestamp. Unit: seconds.
        self.target_time = target_time
        # The details about Elastic Compute Service (ECS) instance backup.
        self.udm_detail = udm_detail
        # The time when the restore job was updated. This value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        if self.ots_detail:
            self.ots_detail.validate()
        if self.report:
            self.report.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_bytes is not None:
            result['ActualBytes'] = self.actual_bytes
        if self.actual_items is not None:
            result['ActualItems'] = self.actual_items
        if self.bytes_done is not None:
            result['BytesDone'] = self.bytes_done
        if self.bytes_total is not None:
            result['BytesTotal'] = self.bytes_total
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.error_file is not None:
            result['ErrorFile'] = self.error_file
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.failback_detail is not None:
            result['FailbackDetail'] = self.failback_detail
        if self.include is not None:
            result['Include'] = self.include
        if self.items_done is not None:
            result['ItemsDone'] = self.items_done
        if self.items_total is not None:
            result['ItemsTotal'] = self.items_total
        if self.metering_bytes_done is not None:
            result['MeteringBytesDone'] = self.metering_bytes_done
        if self.metering_bytes_total is not None:
            result['MeteringBytesTotal'] = self.metering_bytes_total
        if self.options is not None:
            result['Options'] = self.options
        if self.ots_detail is not None:
            result['OtsDetail'] = self.ots_detail.to_map()
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.report is not None:
            result['Report'] = self.report.to_map()
        if self.restore_id is not None:
            result['RestoreId'] = self.restore_id
        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type
        if self.snapshot_hash is not None:
            result['SnapshotHash'] = self.snapshot_hash
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        if self.target_bucket is not None:
            result['TargetBucket'] = self.target_bucket
        if self.target_client_id is not None:
            result['TargetClientId'] = self.target_client_id
        if self.target_create_time is not None:
            result['TargetCreateTime'] = self.target_create_time
        if self.target_data_source_id is not None:
            result['TargetDataSourceId'] = self.target_data_source_id
        if self.target_file_system_id is not None:
            result['TargetFileSystemId'] = self.target_file_system_id
        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id
        if self.target_instance_name is not None:
            result['TargetInstanceName'] = self.target_instance_name
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.target_prefix is not None:
            result['TargetPrefix'] = self.target_prefix
        if self.target_table_name is not None:
            result['TargetTableName'] = self.target_table_name
        if self.target_time is not None:
            result['TargetTime'] = self.target_time
        if self.udm_detail is not None:
            result['UdmDetail'] = self.udm_detail
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualBytes') is not None:
            self.actual_bytes = m.get('ActualBytes')
        if m.get('ActualItems') is not None:
            self.actual_items = m.get('ActualItems')
        if m.get('BytesDone') is not None:
            self.bytes_done = m.get('BytesDone')
        if m.get('BytesTotal') is not None:
            self.bytes_total = m.get('BytesTotal')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('ErrorFile') is not None:
            self.error_file = m.get('ErrorFile')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FailbackDetail') is not None:
            self.failback_detail = m.get('FailbackDetail')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('ItemsDone') is not None:
            self.items_done = m.get('ItemsDone')
        if m.get('ItemsTotal') is not None:
            self.items_total = m.get('ItemsTotal')
        if m.get('MeteringBytesDone') is not None:
            self.metering_bytes_done = m.get('MeteringBytesDone')
        if m.get('MeteringBytesTotal') is not None:
            self.metering_bytes_total = m.get('MeteringBytesTotal')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OtsDetail') is not None:
            temp_model = DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJobOtsDetail()
            self.ots_detail = temp_model.from_map(m['OtsDetail'])
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Report') is not None:
            temp_model = DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJobReport()
            self.report = temp_model.from_map(m['Report'])
        if m.get('RestoreId') is not None:
            self.restore_id = m.get('RestoreId')
        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')
        if m.get('SnapshotHash') is not None:
            self.snapshot_hash = m.get('SnapshotHash')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        if m.get('TargetBucket') is not None:
            self.target_bucket = m.get('TargetBucket')
        if m.get('TargetClientId') is not None:
            self.target_client_id = m.get('TargetClientId')
        if m.get('TargetCreateTime') is not None:
            self.target_create_time = m.get('TargetCreateTime')
        if m.get('TargetDataSourceId') is not None:
            self.target_data_source_id = m.get('TargetDataSourceId')
        if m.get('TargetFileSystemId') is not None:
            self.target_file_system_id = m.get('TargetFileSystemId')
        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')
        if m.get('TargetInstanceName') is not None:
            self.target_instance_name = m.get('TargetInstanceName')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TargetPrefix') is not None:
            self.target_prefix = m.get('TargetPrefix')
        if m.get('TargetTableName') is not None:
            self.target_table_name = m.get('TargetTableName')
        if m.get('TargetTime') is not None:
            self.target_time = m.get('TargetTime')
        if m.get('UdmDetail') is not None:
            self.udm_detail = m.get('UdmDetail')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeRestoreJobs2ResponseBodyRestoreJobs(TeaModel):
    def __init__(
        self,
        restore_job: List[DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJob] = None,
    ):
        self.restore_job = restore_job

    def validate(self):
        if self.restore_job:
            for k in self.restore_job:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RestoreJob'] = []
        if self.restore_job is not None:
            for k in self.restore_job:
                result['RestoreJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.restore_job = []
        if m.get('RestoreJob') is not None:
            for k in m.get('RestoreJob'):
                temp_model = DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJob()
                self.restore_job.append(temp_model.from_map(k))
        return self


class DescribeRestoreJobs2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        restore_jobs: DescribeRestoreJobs2ResponseBodyRestoreJobs = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The response status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The response message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The queried restore jobs.
        self.restore_jobs = restore_jobs
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.restore_jobs:
            self.restore_jobs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.restore_jobs is not None:
            result['RestoreJobs'] = self.restore_jobs.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RestoreJobs') is not None:
            temp_model = DescribeRestoreJobs2ResponseBodyRestoreJobs()
            self.restore_jobs = temp_model.from_map(m['RestoreJobs'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRestoreJobs2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRestoreJobs2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRestoreJobs2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTaskRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        task_id: str = None,
        token: str = None,
    ):
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the job.
        self.task_id = task_id
        # The access token.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class DescribeTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        completed_time: int = None,
        created_time: int = None,
        description: str = None,
        message: str = None,
        name: str = None,
        progress: int = None,
        request_id: str = None,
        result: str = None,
        success: bool = None,
        updated_time: int = None,
    ):
        # HttpCode
        self.code = code
        # The time when the task was complete. The time is a UNIX timestamp. Unit: seconds.
        self.completed_time = completed_time
        # The time when the job was created. This value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The status of the job. Valid values:
        # 
        # *   **created**: The job is created.
        # *   **expired**: The job expires.
        # *   **completed**: The job is completed.
        # *   **cancelled**: The job is canceled.
        self.description = description
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The name of the job.
        self.name = name
        # The progress of the job. Valid values: 0 to 100. Unit: percentage (%). If the job fails, the value -1 is returned.
        self.progress = progress
        # The ID of the request.
        self.request_id = request_id
        # The result of the job.
        self.result = result
        # Indicates whether the call is successful.
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The time when the job was updated. This value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class DescribeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUdmSnapshotsRequest(TeaModel):
    def __init__(
        self,
        disk_id: str = None,
        end_time: int = None,
        instance_id: str = None,
        job_id: str = None,
        snapshot_ids: Dict[str, Any] = None,
        source_type: str = None,
        start_time: int = None,
        udm_region_id: str = None,
    ):
        # The ID of the disk.
        self.disk_id = disk_id
        # The end of the time range to query. The value must be a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # The ID of the backup job.
        self.job_id = job_id
        # The list of backup snapshots.
        self.snapshot_ids = snapshot_ids
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instance backup
        # *   **UDM_ECS_DISK**: disk backup subtask of ECS instance backup
        # *   **UDM_DISK**: disk backup
        # 
        # This parameter is required.
        self.source_type = source_type
        # The beginning of the time range to query. The value must be a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The ID of the region where the ECS instance resides.
        # 
        # This parameter is required.
        self.udm_region_id = udm_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.udm_region_id is not None:
            result['UdmRegionId'] = self.udm_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UdmRegionId') is not None:
            self.udm_region_id = m.get('UdmRegionId')
        return self


class DescribeUdmSnapshotsShrinkRequest(TeaModel):
    def __init__(
        self,
        disk_id: str = None,
        end_time: int = None,
        instance_id: str = None,
        job_id: str = None,
        snapshot_ids_shrink: str = None,
        source_type: str = None,
        start_time: int = None,
        udm_region_id: str = None,
    ):
        # The ID of the disk.
        self.disk_id = disk_id
        # The end of the time range to query. The value must be a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # The ID of the backup job.
        self.job_id = job_id
        # The list of backup snapshots.
        self.snapshot_ids_shrink = snapshot_ids_shrink
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instance backup
        # *   **UDM_ECS_DISK**: disk backup subtask of ECS instance backup
        # *   **UDM_DISK**: disk backup
        # 
        # This parameter is required.
        self.source_type = source_type
        # The beginning of the time range to query. The value must be a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The ID of the region where the ECS instance resides.
        # 
        # This parameter is required.
        self.udm_region_id = udm_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.snapshot_ids_shrink is not None:
            result['SnapshotIds'] = self.snapshot_ids_shrink
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.udm_region_id is not None:
            result['UdmRegionId'] = self.udm_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('SnapshotIds') is not None:
            self.snapshot_ids_shrink = m.get('SnapshotIds')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UdmRegionId') is not None:
            self.udm_region_id = m.get('UdmRegionId')
        return self


class DescribeUdmSnapshotsResponseBodySnapshotsDetail(TeaModel):
    def __init__(
        self,
        consistent_level: str = None,
        contain_os_disk: bool = None,
        disk_category: str = None,
        disk_dev_name: str = None,
        disk_hbr_snapshot_id_with_device_map: Dict[str, Any] = None,
        disk_id_list: List[str] = None,
        downgrade_reason: str = None,
        host_name: str = None,
        instance_id_with_disk_id_list_map: Dict[str, Any] = None,
        instance_name: str = None,
        instance_type: str = None,
        instant_access: bool = None,
        native_snapshot_id_list: List[str] = None,
        os_disk_id: str = None,
        os_name: str = None,
        os_name_en: str = None,
        os_type: str = None,
        performance_level: str = None,
        platform: str = None,
        snapshot_group_id: str = None,
        system_disk: bool = None,
        vm_name: str = None,
    ):
        # The consistency level.
        self.consistent_level = consistent_level
        # Indicates whether the system disk is included.
        self.contain_os_disk = contain_os_disk
        # The type of the source disk.
        self.disk_category = disk_category
        # The name of the disk.
        self.disk_dev_name = disk_dev_name
        # The mapping between the device and the recovery point ID.
        self.disk_hbr_snapshot_id_with_device_map = disk_hbr_snapshot_id_with_device_map
        # The IDs of the disks that are backed up at the recovery point.
        self.disk_id_list = disk_id_list
        # The reason for the downgrade.
        self.downgrade_reason = downgrade_reason
        # The hostname.
        self.host_name = host_name
        # The mapping between the instance ID and the disk ID.
        self.instance_id_with_disk_id_list_map = instance_id_with_disk_id_list_map
        # The name of the instance.
        self.instance_name = instance_name
        # The specifications of the source instance.
        self.instance_type = instance_type
        # Indicates whether the backup is created by the instant clone feature.
        self.instant_access = instant_access
        # The list of snapshot IDs, corresponding to DiskIdList.
        self.native_snapshot_id_list = native_snapshot_id_list
        # The ID of the system disk.
        self.os_disk_id = os_disk_id
        # The name of the operating system.
        self.os_name = os_name
        # The English name of the operating system.
        self.os_name_en = os_name_en
        # The type of the operating system. Valid values: linux and windows.
        self.os_type = os_type
        # The performance level of the source disk.
        self.performance_level = performance_level
        # The system platform.
        self.platform = platform
        # The ID of the snapshot group.
        self.snapshot_group_id = snapshot_group_id
        # Indicates whether the disk is a system disk.
        self.system_disk = system_disk
        # The name of the instance.
        self.vm_name = vm_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consistent_level is not None:
            result['ConsistentLevel'] = self.consistent_level
        if self.contain_os_disk is not None:
            result['ContainOsDisk'] = self.contain_os_disk
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category
        if self.disk_dev_name is not None:
            result['DiskDevName'] = self.disk_dev_name
        if self.disk_hbr_snapshot_id_with_device_map is not None:
            result['DiskHbrSnapshotIdWithDeviceMap'] = self.disk_hbr_snapshot_id_with_device_map
        if self.disk_id_list is not None:
            result['DiskIdList'] = self.disk_id_list
        if self.downgrade_reason is not None:
            result['DowngradeReason'] = self.downgrade_reason
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_id_with_disk_id_list_map is not None:
            result['InstanceIdWithDiskIdListMap'] = self.instance_id_with_disk_id_list_map
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instant_access is not None:
            result['InstantAccess'] = self.instant_access
        if self.native_snapshot_id_list is not None:
            result['NativeSnapshotIdList'] = self.native_snapshot_id_list
        if self.os_disk_id is not None:
            result['OsDiskId'] = self.os_disk_id
        if self.os_name is not None:
            result['OsName'] = self.os_name
        if self.os_name_en is not None:
            result['OsNameEn'] = self.os_name_en
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.snapshot_group_id is not None:
            result['SnapshotGroupId'] = self.snapshot_group_id
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk
        if self.vm_name is not None:
            result['VmName'] = self.vm_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsistentLevel') is not None:
            self.consistent_level = m.get('ConsistentLevel')
        if m.get('ContainOsDisk') is not None:
            self.contain_os_disk = m.get('ContainOsDisk')
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')
        if m.get('DiskDevName') is not None:
            self.disk_dev_name = m.get('DiskDevName')
        if m.get('DiskHbrSnapshotIdWithDeviceMap') is not None:
            self.disk_hbr_snapshot_id_with_device_map = m.get('DiskHbrSnapshotIdWithDeviceMap')
        if m.get('DiskIdList') is not None:
            self.disk_id_list = m.get('DiskIdList')
        if m.get('DowngradeReason') is not None:
            self.downgrade_reason = m.get('DowngradeReason')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceIdWithDiskIdListMap') is not None:
            self.instance_id_with_disk_id_list_map = m.get('InstanceIdWithDiskIdListMap')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstantAccess') is not None:
            self.instant_access = m.get('InstantAccess')
        if m.get('NativeSnapshotIdList') is not None:
            self.native_snapshot_id_list = m.get('NativeSnapshotIdList')
        if m.get('OsDiskId') is not None:
            self.os_disk_id = m.get('OsDiskId')
        if m.get('OsName') is not None:
            self.os_name = m.get('OsName')
        if m.get('OsNameEn') is not None:
            self.os_name_en = m.get('OsNameEn')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('SnapshotGroupId') is not None:
            self.snapshot_group_id = m.get('SnapshotGroupId')
        if m.get('SystemDisk') is not None:
            self.system_disk = m.get('SystemDisk')
        if m.get('VmName') is not None:
            self.vm_name = m.get('VmName')
        return self


class DescribeUdmSnapshotsResponseBodySnapshots(TeaModel):
    def __init__(
        self,
        actual_bytes: str = None,
        advanced_retention_type: str = None,
        backup_type: str = None,
        bytes_total: int = None,
        can_be_deleted: bool = None,
        complete_time: int = None,
        create_time: int = None,
        created_time: int = None,
        detail: DescribeUdmSnapshotsResponseBodySnapshotsDetail = None,
        disk_id: str = None,
        expire_time: int = None,
        instance_id: str = None,
        job_id: str = None,
        native_snapshot_id: str = None,
        native_snapshot_info: str = None,
        parent_snapshot_hash: str = None,
        prefix: str = None,
        real_snapshot_time: int = None,
        retention: int = None,
        snapshot_hash: str = None,
        snapshot_id: str = None,
        source_type: str = None,
        start_time: int = None,
        status: str = None,
        updated_time: int = None,
    ):
        # The size of the backup snapshot. Unit: bytes.
        self.actual_bytes = actual_bytes
        # The special retention type, which is valid only for special backups. Valid values:
        # 
        # *   **WEEKLY**: weekly backups
        # *   **MONTHLY**: monthly backups
        # *   **YEARLY**: yearly backups
        self.advanced_retention_type = advanced_retention_type
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # The total amount of data. Unit: bytes.
        self.bytes_total = bytes_total
        # Indicates whether the disk backup point can be deleted. This parameter is valid only if the value of SourceType is UDM_ECS_DISK.
        self.can_be_deleted = can_be_deleted
        # The time when the backup snapshot was completed. The value is a UNIX timestamp. Unit: seconds.
        self.complete_time = complete_time
        # The time when the backup snapshot was created.
        self.create_time = create_time
        # The time when the backup snapshot was created. The value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The snapshot details.
        self.detail = detail
        # The ID of the cloud disk or local disk.
        self.disk_id = disk_id
        # The expiration time of the backup.
        self.expire_time = expire_time
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # The ID of the backup job.
        self.job_id = job_id
        # The ID of the backup snapshot.
        self.native_snapshot_id = native_snapshot_id
        # The snapshot information.
        self.native_snapshot_info = native_snapshot_info
        # The hash value of the parent backup snapshot.
        self.parent_snapshot_hash = parent_snapshot_hash
        # The prefix of the backup snapshot.
        self.prefix = prefix
        # The timestamp of the backup snapshot. The value is a UNIX timestamp. Unit: seconds.
        self.real_snapshot_time = real_snapshot_time
        # The retention period of the backup snapshot. Unit: days.
        self.retention = retention
        # The hash value of the backup snapshot.
        self.snapshot_hash = snapshot_hash
        # The ID of the backup snapshot.
        self.snapshot_id = snapshot_id
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instance backup
        # *   **UDM_ECS_DISK**: disk backup subtask of ECS instance backup
        # *   **UDM_DISK**: disk backup
        self.source_type = source_type
        # The time when the backup snapshot was created. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time
        # The status of the backup job. Valid values:
        # 
        # *   **COMPLETE**: The backup job is completed.
        # *   **PARTIAL_COMPLETE**: The backup job is partially completed.
        # *   **FAILED**: The backup job has failed.
        self.status = status
        # The time when the backup snapshot was updated. The value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_bytes is not None:
            result['ActualBytes'] = self.actual_bytes
        if self.advanced_retention_type is not None:
            result['AdvancedRetentionType'] = self.advanced_retention_type
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.bytes_total is not None:
            result['BytesTotal'] = self.bytes_total
        if self.can_be_deleted is not None:
            result['CanBeDeleted'] = self.can_be_deleted
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.native_snapshot_id is not None:
            result['NativeSnapshotId'] = self.native_snapshot_id
        if self.native_snapshot_info is not None:
            result['NativeSnapshotInfo'] = self.native_snapshot_info
        if self.parent_snapshot_hash is not None:
            result['ParentSnapshotHash'] = self.parent_snapshot_hash
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.real_snapshot_time is not None:
            result['RealSnapshotTime'] = self.real_snapshot_time
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.snapshot_hash is not None:
            result['SnapshotHash'] = self.snapshot_hash
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualBytes') is not None:
            self.actual_bytes = m.get('ActualBytes')
        if m.get('AdvancedRetentionType') is not None:
            self.advanced_retention_type = m.get('AdvancedRetentionType')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BytesTotal') is not None:
            self.bytes_total = m.get('BytesTotal')
        if m.get('CanBeDeleted') is not None:
            self.can_be_deleted = m.get('CanBeDeleted')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Detail') is not None:
            temp_model = DescribeUdmSnapshotsResponseBodySnapshotsDetail()
            self.detail = temp_model.from_map(m['Detail'])
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('NativeSnapshotId') is not None:
            self.native_snapshot_id = m.get('NativeSnapshotId')
        if m.get('NativeSnapshotInfo') is not None:
            self.native_snapshot_info = m.get('NativeSnapshotInfo')
        if m.get('ParentSnapshotHash') is not None:
            self.parent_snapshot_hash = m.get('ParentSnapshotHash')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('RealSnapshotTime') is not None:
            self.real_snapshot_time = m.get('RealSnapshotTime')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('SnapshotHash') is not None:
            self.snapshot_hash = m.get('SnapshotHash')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class DescribeUdmSnapshotsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        snapshots: List[DescribeUdmSnapshotsResponseBodySnapshots] = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The details about snapshots.
        self.snapshots = snapshots
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The total number of backup snapshots.
        self.total_count = total_count

    def validate(self):
        if self.snapshots:
            for k in self.snapshots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = DescribeUdmSnapshotsResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeUdmSnapshotsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUdmSnapshotsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUdmSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVaultReplicationRegionsRequest(TeaModel):
    def __init__(
        self,
        token: str = None,
        vault_id: str = None,
    ):
        # This parameter is deprecated.
        self.token = token
        # This parameter is deprecated.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeVaultReplicationRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region_id: List[str] = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeVaultReplicationRegionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        regions: DescribeVaultReplicationRegionsResponseBodyRegions = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The regions that support cross-region replication.
        self.regions = regions
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful.
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Regions') is not None:
            temp_model = DescribeVaultReplicationRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeVaultReplicationRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVaultReplicationRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVaultReplicationRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVaultsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The Value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeVaultsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        status: str = None,
        tag: List[DescribeVaultsRequestTag] = None,
        vault_id: str = None,
        vault_name: str = None,
        vault_region_id: str = None,
        vault_type: str = None,
    ):
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # The status of the backup vault. Valid values:
        # 
        # *   **UNKNOWN**: The backup vault is in an unknown state.
        # *   **INITIALIZING**: The backup vault is being initialized.
        # *   **CREATED**: The backup vault is created.
        # *   **ERROR**: An error occurs on the backup vault.
        self.status = status
        # Tag information. Supports up to 20 tags.
        self.tag = tag
        # Backup vault ID.
        self.vault_id = vault_id
        self.vault_name = vault_name
        # The region ID to which the backup vault belongs.
        self.vault_region_id = vault_region_id
        # Backup repository type. The values are as follows: 
        # - **STANDARD**: Represents a standard repository, which can be used for ECS file backups, OSS backups, NAS backups, etc. 
        # - **OTS_BACKUP**: Represents a TableStore repository, which is only used for TableStore backups, and TableStore must use this type of repository.
        self.vault_type = vault_type

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        if self.vault_name is not None:
            result['VaultName'] = self.vault_name
        if self.vault_region_id is not None:
            result['VaultRegionId'] = self.vault_region_id
        if self.vault_type is not None:
            result['VaultType'] = self.vault_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeVaultsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        if m.get('VaultName') is not None:
            self.vault_name = m.get('VaultName')
        if m.get('VaultRegionId') is not None:
            self.vault_region_id = m.get('VaultRegionId')
        if m.get('VaultType') is not None:
            self.vault_type = m.get('VaultType')
        return self


class DescribeVaultsResponseBodyVaultsVaultBackupPlanStatistics(TeaModel):
    def __init__(
        self,
        archive: int = None,
        common_file_system: int = None,
        common_nas: int = None,
        csg: int = None,
        ecs_file: int = None,
        ecs_hana: int = None,
        isilon: int = None,
        local_file: int = None,
        local_vm: int = None,
        my_sql: int = None,
        nas: int = None,
        oracle: int = None,
        oss: int = None,
        ots: int = None,
        sql_server: int = None,
    ):
        # The number of archive plans.
        self.archive = archive
        # The number of Cloud Parallel File Storage (CPFS) backup plans.
        self.common_file_system = common_file_system
        # The number of backup plans for General-purpose NAS file systems.
        self.common_nas = common_nas
        # The number of backup plans for Cloud Storage Gateway (CSG) gateways.
        self.csg = csg
        # The number of backup plans for ECS files.
        self.ecs_file = ecs_file
        # The number of backup plans for SAP HANA instances.
        self.ecs_hana = ecs_hana
        # The number of backup plans for Isilon storage systems.
        self.isilon = isilon
        # The number of backup plans for on-premises servers.
        self.local_file = local_file
        # The number of backup plans for on-premises virtual machines (VMs).
        self.local_vm = local_vm
        # The number of backup plans for MySQL databases.
        self.my_sql = my_sql
        # The number of backup plans for NAS file systems.
        self.nas = nas
        # The number of backup plans for Oracle databases.
        self.oracle = oracle
        # The number of backup plans for OSS buckets.
        self.oss = oss
        # The number of backup plans for Tablestore instances.
        self.ots = ots
        # The number of backup plans for SQL Server databases.
        self.sql_server = sql_server

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive is not None:
            result['Archive'] = self.archive
        if self.common_file_system is not None:
            result['CommonFileSystem'] = self.common_file_system
        if self.common_nas is not None:
            result['CommonNas'] = self.common_nas
        if self.csg is not None:
            result['Csg'] = self.csg
        if self.ecs_file is not None:
            result['EcsFile'] = self.ecs_file
        if self.ecs_hana is not None:
            result['EcsHana'] = self.ecs_hana
        if self.isilon is not None:
            result['Isilon'] = self.isilon
        if self.local_file is not None:
            result['LocalFile'] = self.local_file
        if self.local_vm is not None:
            result['LocalVm'] = self.local_vm
        if self.my_sql is not None:
            result['MySql'] = self.my_sql
        if self.nas is not None:
            result['Nas'] = self.nas
        if self.oracle is not None:
            result['Oracle'] = self.oracle
        if self.oss is not None:
            result['Oss'] = self.oss
        if self.ots is not None:
            result['Ots'] = self.ots
        if self.sql_server is not None:
            result['SqlServer'] = self.sql_server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Archive') is not None:
            self.archive = m.get('Archive')
        if m.get('CommonFileSystem') is not None:
            self.common_file_system = m.get('CommonFileSystem')
        if m.get('CommonNas') is not None:
            self.common_nas = m.get('CommonNas')
        if m.get('Csg') is not None:
            self.csg = m.get('Csg')
        if m.get('EcsFile') is not None:
            self.ecs_file = m.get('EcsFile')
        if m.get('EcsHana') is not None:
            self.ecs_hana = m.get('EcsHana')
        if m.get('Isilon') is not None:
            self.isilon = m.get('Isilon')
        if m.get('LocalFile') is not None:
            self.local_file = m.get('LocalFile')
        if m.get('LocalVm') is not None:
            self.local_vm = m.get('LocalVm')
        if m.get('MySql') is not None:
            self.my_sql = m.get('MySql')
        if m.get('Nas') is not None:
            self.nas = m.get('Nas')
        if m.get('Oracle') is not None:
            self.oracle = m.get('Oracle')
        if m.get('Oss') is not None:
            self.oss = m.get('Oss')
        if m.get('Ots') is not None:
            self.ots = m.get('Ots')
        if m.get('SqlServer') is not None:
            self.sql_server = m.get('SqlServer')
        return self


class DescribeVaultsResponseBodyVaultsVaultReplicationProgress(TeaModel):
    def __init__(
        self,
        historical_replication_progress: int = None,
        new_replication_progress: int = None,
    ):
        # The progress of historical data synchronization from the backup vault to the mirror vault. Valid values: 0 to 100.
        self.historical_replication_progress = historical_replication_progress
        # The latest synchronization time of incremental data in the mirror vault.
        self.new_replication_progress = new_replication_progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.historical_replication_progress is not None:
            result['HistoricalReplicationProgress'] = self.historical_replication_progress
        if self.new_replication_progress is not None:
            result['NewReplicationProgress'] = self.new_replication_progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HistoricalReplicationProgress') is not None:
            self.historical_replication_progress = m.get('HistoricalReplicationProgress')
        if m.get('NewReplicationProgress') is not None:
            self.new_replication_progress = m.get('NewReplicationProgress')
        return self


class DescribeVaultsResponseBodyVaultsVaultSourceTypes(TeaModel):
    def __init__(
        self,
        source_type: List[str] = None,
    ):
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class DescribeVaultsResponseBodyVaultsVaultTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the backup vault. Valid values of N: 1 to 20.
        # 
        # *   The tag key cannot start with `aliyun` or `acs:`.
        # *   The tag key cannot contain `http://` or `https://`.
        # *   The tag key cannot be an empty string.
        self.key = key
        # The tag value of the backup vault. Valid values of N: 1 to 20.
        # 
        # *   The tag value cannot start with `aliyun` or `acs:`.
        # *   The tag value cannot contain `http://` or `https://`.
        # *   The tag value cannot be an empty string.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeVaultsResponseBodyVaultsVaultTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeVaultsResponseBodyVaultsVaultTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeVaultsResponseBodyVaultsVaultTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeVaultsResponseBodyVaultsVaultTrialInfo(TeaModel):
    def __init__(
        self,
        keep_after_trial_expiration: bool = None,
        trial_expire_time: int = None,
        trial_start_time: int = None,
        trial_vault_release_time: int = None,
    ):
        # Indicates whether you are billed based on the pay-as-you-go method after the free trial ends.
        self.keep_after_trial_expiration = keep_after_trial_expiration
        # The expiration time of the free trial.
        self.trial_expire_time = trial_expire_time
        # The start time of the free trial.
        self.trial_start_time = trial_start_time
        # The time when the free-trial backup vault is released.
        self.trial_vault_release_time = trial_vault_release_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keep_after_trial_expiration is not None:
            result['KeepAfterTrialExpiration'] = self.keep_after_trial_expiration
        if self.trial_expire_time is not None:
            result['TrialExpireTime'] = self.trial_expire_time
        if self.trial_start_time is not None:
            result['TrialStartTime'] = self.trial_start_time
        if self.trial_vault_release_time is not None:
            result['TrialVaultReleaseTime'] = self.trial_vault_release_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeepAfterTrialExpiration') is not None:
            self.keep_after_trial_expiration = m.get('KeepAfterTrialExpiration')
        if m.get('TrialExpireTime') is not None:
            self.trial_expire_time = m.get('TrialExpireTime')
        if m.get('TrialStartTime') is not None:
            self.trial_start_time = m.get('TrialStartTime')
        if m.get('TrialVaultReleaseTime') is not None:
            self.trial_vault_release_time = m.get('TrialVaultReleaseTime')
        return self


class DescribeVaultsResponseBodyVaultsVault(TeaModel):
    def __init__(
        self,
        archive_bytes_done: int = None,
        archive_storage_size: int = None,
        backup_plan_statistics: DescribeVaultsResponseBodyVaultsVaultBackupPlanStatistics = None,
        bucket_name: str = None,
        bytes_done: int = None,
        charge_type: str = None,
        charged_storage_size: int = None,
        compression_algorithm: str = None,
        created_time: int = None,
        dedup: bool = None,
        description: str = None,
        encrypt_type: str = None,
        index_available: bool = None,
        index_level: str = None,
        index_update_time: int = None,
        kms_key_id: str = None,
        latest_replication_time: int = None,
        redundancy_type: str = None,
        replication: bool = None,
        replication_progress: DescribeVaultsResponseBodyVaultsVaultReplicationProgress = None,
        replication_source_region_id: str = None,
        replication_source_vault: bool = None,
        replication_source_vault_id: str = None,
        replication_target_region_id: str = None,
        resource_group_id: str = None,
        retention: int = None,
        search_enabled: bool = None,
        snapshot_count: int = None,
        source_types: DescribeVaultsResponseBodyVaultsVaultSourceTypes = None,
        status: str = None,
        storage_size: int = None,
        tags: DescribeVaultsResponseBodyVaultsVaultTags = None,
        trial_info: DescribeVaultsResponseBodyVaultsVaultTrialInfo = None,
        updated_time: int = None,
        vault_id: str = None,
        vault_name: str = None,
        vault_region_id: str = None,
        vault_status_message: str = None,
        vault_storage_class: str = None,
        vault_type: str = None,
        worm_enabled: bool = None,
    ):
        # Archival tier backup data volume. Unit: bytes.
        self.archive_bytes_done = archive_bytes_done
        # The billable storage usage of the Archive tier. Unit: bytes.
        self.archive_storage_size = archive_storage_size
        # The statistics of backup plans that use the backup vault.
        self.backup_plan_statistics = backup_plan_statistics
        # The name of the OSS bucket used by the backup vault.
        self.bucket_name = bucket_name
        # The amount of data that is backed up. Unit: bytes.
        self.bytes_done = bytes_done
        # The billing method of the backup vault.
        self.charge_type = charge_type
        # The billable storage usage of the archive vault. Unit: bytes.
        self.charged_storage_size = charged_storage_size
        # The encryption algorithm used to compress the backup vault. Valid values:
        # 
        # *   DISABLED: The backup vault is not compressed.
        # *   SNAPPY: The backup vault is compressed by using the SNAPPY encryption algorithm.
        # *   ZSTD: The backup vault is compressed by using Zstandard, a fast lossless compression algorithm.
        self.compression_algorithm = compression_algorithm
        # The time when the backup vault was created. The value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # Indicates whether the deduplication feature is enabled.
        self.dedup = dedup
        # The description of the backup vault.
        self.description = description
        # The encryption type of the backup vault. Valid values:
        # 
        # *   NONE: The backup vault is not encrypted.
        # *   HBR_PRIVATE (default): The backup vault is encrypted by using a key provided by Cloud Backup.
        # *   KMS: The backup vault is encrypted by using a custom master key (CMK) created in Key Management Service (KMS).
        self.encrypt_type = encrypt_type
        # Indicates whether indexes are available. Indexes are available when they are not being updated.
        self.index_available = index_available
        # The index level.
        # 
        # *   OFF: No indexes are created.
        # *   META: Metadata indexes are created.
        # *   ALL: Full-text indexes are created.
        self.index_level = index_level
        # The time when the index was updated.
        self.index_update_time = index_update_time
        # The ID or alias of the CMK created in KMS. This parameter is returned only when EncryptType is set to KMS.
        self.kms_key_id = kms_key_id
        # The time when the last remote backup was synchronized. The value is a UNIX timestamp. Unit: seconds.
        self.latest_replication_time = latest_replication_time
        # The data redundancy type of the backup vault. Valid values:
        # 
        # *   LRS: Locally redundant storage (LRS) is enabled for the backup vault. Cloud Backup stores the copies of each object on multiple devices of different facilities in the same zone. This way, Cloud Backup ensures data durability and availability even if hardware failures occur.
        # *   ZRS: Zone-redundant storage (ZRS) is enabled for the backup vault. Cloud Backup uses the multi-zone mechanism to distribute data across three zones within the same region. If a zone fails, the data that is stored in the other two zones is still accessible.
        self.redundancy_type = redundancy_type
        # Indicates whether the backup vault is a remote backup vault. Valid values:
        # 
        # *   true: The backup vault is a remote backup vault.
        # *   false: The backup vault is a local backup vault.
        self.replication = replication
        # The progress of data synchronization from the backup vault to the mirror vault.
        self.replication_progress = replication_progress
        # The ID of the region in which the source vault resides. This parameter is valid only for remote backup vaults.
        self.replication_source_region_id = replication_source_region_id
        # Indicate whether the backup vault is the source vault that corresponds to the remote backup vault. Valid values:
        # 
        # *   true
        # *   false
        self.replication_source_vault = replication_source_vault
        # The ID of the source vault that corresponds to the remote backup vault.
        self.replication_source_vault_id = replication_source_vault_id
        # Target region for remote backup repository.
        self.replication_target_region_id = replication_target_region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The retention period of the backup vault. Unit: days.
        self.retention = retention
        # Indicates whether the backup search feature is enabled.
        self.search_enabled = search_enabled
        # The number of snapshots in the backup vault.
        self.snapshot_count = snapshot_count
        # The data source types of the backup vault.
        self.source_types = source_types
        # The status of the backup vault. Valid values:
        # 
        # *   **UNKNOWN**: The backup vault is in an unknown state.
        # *   **INITIALIZING**: The backup vault is being initialized.
        # *   **CREATED**: The backup vault is created.
        # *   **ERROR**: An error occurs on the backup vault.
        self.status = status
        # The usage of the backup vault. Unit: bytes.
        self.storage_size = storage_size
        # The tags of the backup vault.
        self.tags = tags
        # The free trial information.
        self.trial_info = trial_info
        # The time when the backup vault was updated. The value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time
        # The ID of the backup vault.
        self.vault_id = vault_id
        # The name of the backup vault.
        self.vault_name = vault_name
        # The ID of the region in which the backup vault resides.
        self.vault_region_id = vault_region_id
        # The status message that is returned when the backup vault is in the ERROR state. This parameter is valid only for remote backup vaults. Valid values:
        # 
        # *   **UNKNOWN_ERROR**: An unknown error occurs.
        # *   **SOURCE_VAULT_ALREADY_HAS_REPLICATION**: A mirror vault is configured for the source vault.
        self.vault_status_message = vault_status_message
        # The storage class of the backup vault. Valid value: **STANDARD**, which indicates standard storage.
        self.vault_storage_class = vault_storage_class
        # The type of the backup vault. Valid value: **STANDARD**, which indicates a standard backup vault.
        self.vault_type = vault_type
        # Indicates whether the immutable backup feature is enabled.
        self.worm_enabled = worm_enabled

    def validate(self):
        if self.backup_plan_statistics:
            self.backup_plan_statistics.validate()
        if self.replication_progress:
            self.replication_progress.validate()
        if self.source_types:
            self.source_types.validate()
        if self.tags:
            self.tags.validate()
        if self.trial_info:
            self.trial_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_bytes_done is not None:
            result['ArchiveBytesDone'] = self.archive_bytes_done
        if self.archive_storage_size is not None:
            result['ArchiveStorageSize'] = self.archive_storage_size
        if self.backup_plan_statistics is not None:
            result['BackupPlanStatistics'] = self.backup_plan_statistics.to_map()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.bytes_done is not None:
            result['BytesDone'] = self.bytes_done
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.charged_storage_size is not None:
            result['ChargedStorageSize'] = self.charged_storage_size
        if self.compression_algorithm is not None:
            result['CompressionAlgorithm'] = self.compression_algorithm
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.dedup is not None:
            result['Dedup'] = self.dedup
        if self.description is not None:
            result['Description'] = self.description
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.index_available is not None:
            result['IndexAvailable'] = self.index_available
        if self.index_level is not None:
            result['IndexLevel'] = self.index_level
        if self.index_update_time is not None:
            result['IndexUpdateTime'] = self.index_update_time
        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id
        if self.latest_replication_time is not None:
            result['LatestReplicationTime'] = self.latest_replication_time
        if self.redundancy_type is not None:
            result['RedundancyType'] = self.redundancy_type
        if self.replication is not None:
            result['Replication'] = self.replication
        if self.replication_progress is not None:
            result['ReplicationProgress'] = self.replication_progress.to_map()
        if self.replication_source_region_id is not None:
            result['ReplicationSourceRegionId'] = self.replication_source_region_id
        if self.replication_source_vault is not None:
            result['ReplicationSourceVault'] = self.replication_source_vault
        if self.replication_source_vault_id is not None:
            result['ReplicationSourceVaultId'] = self.replication_source_vault_id
        if self.replication_target_region_id is not None:
            result['ReplicationTargetRegionId'] = self.replication_target_region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.search_enabled is not None:
            result['SearchEnabled'] = self.search_enabled
        if self.snapshot_count is not None:
            result['SnapshotCount'] = self.snapshot_count
        if self.source_types is not None:
            result['SourceTypes'] = self.source_types.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.trial_info is not None:
            result['TrialInfo'] = self.trial_info.to_map()
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        if self.vault_name is not None:
            result['VaultName'] = self.vault_name
        if self.vault_region_id is not None:
            result['VaultRegionId'] = self.vault_region_id
        if self.vault_status_message is not None:
            result['VaultStatusMessage'] = self.vault_status_message
        if self.vault_storage_class is not None:
            result['VaultStorageClass'] = self.vault_storage_class
        if self.vault_type is not None:
            result['VaultType'] = self.vault_type
        if self.worm_enabled is not None:
            result['WormEnabled'] = self.worm_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveBytesDone') is not None:
            self.archive_bytes_done = m.get('ArchiveBytesDone')
        if m.get('ArchiveStorageSize') is not None:
            self.archive_storage_size = m.get('ArchiveStorageSize')
        if m.get('BackupPlanStatistics') is not None:
            temp_model = DescribeVaultsResponseBodyVaultsVaultBackupPlanStatistics()
            self.backup_plan_statistics = temp_model.from_map(m['BackupPlanStatistics'])
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('BytesDone') is not None:
            self.bytes_done = m.get('BytesDone')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ChargedStorageSize') is not None:
            self.charged_storage_size = m.get('ChargedStorageSize')
        if m.get('CompressionAlgorithm') is not None:
            self.compression_algorithm = m.get('CompressionAlgorithm')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Dedup') is not None:
            self.dedup = m.get('Dedup')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('IndexAvailable') is not None:
            self.index_available = m.get('IndexAvailable')
        if m.get('IndexLevel') is not None:
            self.index_level = m.get('IndexLevel')
        if m.get('IndexUpdateTime') is not None:
            self.index_update_time = m.get('IndexUpdateTime')
        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')
        if m.get('LatestReplicationTime') is not None:
            self.latest_replication_time = m.get('LatestReplicationTime')
        if m.get('RedundancyType') is not None:
            self.redundancy_type = m.get('RedundancyType')
        if m.get('Replication') is not None:
            self.replication = m.get('Replication')
        if m.get('ReplicationProgress') is not None:
            temp_model = DescribeVaultsResponseBodyVaultsVaultReplicationProgress()
            self.replication_progress = temp_model.from_map(m['ReplicationProgress'])
        if m.get('ReplicationSourceRegionId') is not None:
            self.replication_source_region_id = m.get('ReplicationSourceRegionId')
        if m.get('ReplicationSourceVault') is not None:
            self.replication_source_vault = m.get('ReplicationSourceVault')
        if m.get('ReplicationSourceVaultId') is not None:
            self.replication_source_vault_id = m.get('ReplicationSourceVaultId')
        if m.get('ReplicationTargetRegionId') is not None:
            self.replication_target_region_id = m.get('ReplicationTargetRegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('SearchEnabled') is not None:
            self.search_enabled = m.get('SearchEnabled')
        if m.get('SnapshotCount') is not None:
            self.snapshot_count = m.get('SnapshotCount')
        if m.get('SourceTypes') is not None:
            temp_model = DescribeVaultsResponseBodyVaultsVaultSourceTypes()
            self.source_types = temp_model.from_map(m['SourceTypes'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('Tags') is not None:
            temp_model = DescribeVaultsResponseBodyVaultsVaultTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('TrialInfo') is not None:
            temp_model = DescribeVaultsResponseBodyVaultsVaultTrialInfo()
            self.trial_info = temp_model.from_map(m['TrialInfo'])
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        if m.get('VaultName') is not None:
            self.vault_name = m.get('VaultName')
        if m.get('VaultRegionId') is not None:
            self.vault_region_id = m.get('VaultRegionId')
        if m.get('VaultStatusMessage') is not None:
            self.vault_status_message = m.get('VaultStatusMessage')
        if m.get('VaultStorageClass') is not None:
            self.vault_storage_class = m.get('VaultStorageClass')
        if m.get('VaultType') is not None:
            self.vault_type = m.get('VaultType')
        if m.get('WormEnabled') is not None:
            self.worm_enabled = m.get('WormEnabled')
        return self


class DescribeVaultsResponseBodyVaults(TeaModel):
    def __init__(
        self,
        vault: List[DescribeVaultsResponseBodyVaultsVault] = None,
    ):
        self.vault = vault

    def validate(self):
        if self.vault:
            for k in self.vault:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Vault'] = []
        if self.vault is not None:
            for k in self.vault:
                result['Vault'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vault = []
        if m.get('Vault') is not None:
            for k in m.get('Vault'):
                temp_model = DescribeVaultsResponseBodyVaultsVault()
                self.vault.append(temp_model.from_map(k))
        return self


class DescribeVaultsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        vaults: DescribeVaultsResponseBodyVaults = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # Page number for pagination, starting from 1. The default value is 1.
        self.page_number = page_number
        # Page size, with a minimum value of 1, a maximum value of 99, and a default value of 10.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Whether the request was successful.
        # - true: Success - false: Failure
        self.success = success
        # Returns the total number of backup repositories.
        self.total_count = total_count
        # The backup vaults.
        self.vaults = vaults

    def validate(self):
        if self.vaults:
            self.vaults.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vaults is not None:
            result['Vaults'] = self.vaults.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Vaults') is not None:
            temp_model = DescribeVaultsResponseBodyVaults()
            self.vaults = temp_model.from_map(m['Vaults'])
        return self


class DescribeVaultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVaultsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVaultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachNasFileSystemRequest(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        file_system_id: str = None,
    ):
        # The time when the file system was created. The value must be a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.create_time = create_time
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up and restore data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Specifies whether data is backed up and restored within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up and restored within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up and restored across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up and restore data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DetachNasFileSystemResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code
        # The message that is returned. If the request is successful, a value of successful is returned. If the request fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        # 
        # *   true: The request is successful.
        # *   false: The request fails.
        self.success = success
        # The ID of the asynchronous job. You can call the DescribeTask operation to query the execution result of the asynchronous job.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DetachNasFileSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachNasFileSystemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachNasFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableBackupPlanRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        source_type: str = None,
        vault_id: str = None,
    ):
        # The ID of the backup plan.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS (NAS) file systems
        self.source_type = source_type
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DisableBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableHanaBackupPlanRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        plan_id: str = None,
        resource_group_id: str = None,
        vault_id: str = None,
    ):
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the backup plan.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the backup vault.
        # 
        # This parameter is required.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DisableHanaBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableHanaBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableHanaBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableHanaBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableBackupPlanRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        source_type: str = None,
        vault_id: str = None,
    ):
        # The ID of the backup plan.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: ECS files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS (NAS) file systems
        self.source_type = source_type
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class EnableBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableHanaBackupPlanRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        plan_id: str = None,
        resource_group_id: str = None,
        vault_id: str = None,
    ):
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the backup plan.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the backup vault.
        # 
        # This parameter is required.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class EnableHanaBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableHanaBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableHanaBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableHanaBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteBackupPlanRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        rule_id: str = None,
        source_type: str = None,
        vault_id: str = None,
    ):
        # The ID of the backup plan.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The ID of the backup rule.
        self.rule_id = rule_id
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS (NAS) file systems
        self.source_type = source_type
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class ExecuteBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        job_id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The ID of the backup job.
        self.job_id = job_id
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExecuteBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecuteBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecutePolicyV2Request(TeaModel):
    def __init__(
        self,
        data_source_id: str = None,
        policy_id: str = None,
        rule_id: str = None,
        source_type: str = None,
    ):
        # Data source ID.
        self.data_source_id = data_source_id
        # Policy ID.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # Rule ID, limited to executing rules of **RuleType** **BACKUP**.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # Data source type, with the value range as follows:
        # 
        # - **UDM_ECS**: Represents ECS full machine backup.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class ExecutePolicyV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        job_id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Return code, 200 indicates success.
        self.code = code
        # Backup job ID.
        self.job_id = job_id
        # Description of the return message, usually returns \\"successful\\" on success, and corresponding error messages on failure.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # - true: Success
        # - false: Failure
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExecutePolicyV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecutePolicyV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecutePolicyV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateRamPolicyRequest(TeaModel):
    def __init__(
        self,
        action_type: str = None,
        require_base_policy: bool = None,
        resource_group_id: str = None,
        vault_id: str = None,
    ):
        # The type of policy that you want to generate. Valid values:
        # 
        # *   BACKUP: the permission to back up data to a backup vault
        # *   RESTORE: the permission to restore data from a backup vault
        # 
        # This parameter is required.
        self.action_type = action_type
        # Specifies whether to generate the policy based on an existing instance-specific rule. Valid values:
        # 
        # *   true
        # *   false
        self.require_base_policy = require_base_policy
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the backup vault.
        # 
        # This parameter is required.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.require_base_policy is not None:
            result['RequireBasePolicy'] = self.require_base_policy
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('RequireBasePolicy') is not None:
            self.require_base_policy = m.get('RequireBasePolicy')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class GenerateRamPolicyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        policy_document: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The content of the policy.
        self.policy_document = policy_document
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GenerateRamPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateRamPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateRamPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTempFileDownloadLinkRequest(TeaModel):
    def __init__(
        self,
        temp_file_key: str = None,
    ):
        # The key that is used to download a file.
        # 
        # This parameter is required.
        self.temp_file_key = temp_file_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.temp_file_key is not None:
            result['TempFileKey'] = self.temp_file_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TempFileKey') is not None:
            self.temp_file_key = m.get('TempFileKey')
        return self


class GetTempFileDownloadLinkResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        url: str = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code
        # The message that is returned. If the request is successful, a value of successful is returned. If the request fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        # 
        # *   true: The request is successful.
        # *   false: The request fails.
        self.success = success
        # The download URL of the file.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetTempFileDownloadLinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTempFileDownloadLinkResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTempFileDownloadLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallBackupClientsRequest(TeaModel):
    def __init__(
        self,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        instance_ids: Dict[str, Any] = None,
    ):
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The IDs of the ECS instances. You can specify up to 20 IDs.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class InstallBackupClientsShrinkRequest(TeaModel):
    def __init__(
        self,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        instance_ids_shrink: str = None,
    ):
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The IDs of the ECS instances. You can specify up to 20 IDs.
        # 
        # This parameter is required.
        self.instance_ids_shrink = instance_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')
        return self


class InstallBackupClientsResponseBodyInstanceStatuses(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        instance_id: str = None,
        valid_instance: bool = None,
    ):
        # The error code that is returned. Valid values:
        # 
        # *   If the value is empty, the call is successful.
        # *   **InstanceNotExists**: The ECS instance does not exist.
        # *   **InstanceNotRunning**: The ECS instance is not running.
        # *   **CloudAssistNotRunningOnInstance**: Cloud Assistant is unavailable.
        self.error_code = error_code
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # Indicates whether an HBR client can be installed on the ECS instance. Valid values:
        # 
        # *   true: An HBR client can be installed on the ECS instance.
        # *   false: An HBR client cannot be installed on the ECS instance.
        self.valid_instance = valid_instance

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.valid_instance is not None:
            result['ValidInstance'] = self.valid_instance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ValidInstance') is not None:
            self.valid_instance = m.get('ValidInstance')
        return self


class InstallBackupClientsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        instance_statuses: List[InstallBackupClientsResponseBodyInstanceStatuses] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The status of the ECS instance.
        self.instance_statuses = instance_statuses
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The ID of the asynchronous job. You can call the DescribeTask operation to query the execution result of an asynchronous job.
        self.task_id = task_id

    def validate(self):
        if self.instance_statuses:
            for k in self.instance_statuses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['InstanceStatuses'] = []
        if self.instance_statuses is not None:
            for k in self.instance_statuses:
                result['InstanceStatuses'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.instance_statuses = []
        if m.get('InstanceStatuses') is not None:
            for k in m.get('InstanceStatuses'):
                temp_model = InstallBackupClientsResponseBodyInstanceStatuses()
                self.instance_statuses.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class InstallBackupClientsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InstallBackupClientsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InstallBackupClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenHbrServiceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenHbrServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenHbrServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OpenHbrServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchHistoricalSnapshotsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        order: str = None,
        query: List[Any] = None,
        sort_by: str = None,
        source_type: str = None,
    ):
        # The maximum number of rows that you want the current query to return. To query only the number of matched rows without the need to return specific data, you can set the Limit parameter to `0`. Then, the operation returns only the number of matched rows.
        self.limit = limit
        # The token that is required to obtain the next page of backup snapshots.
        self.next_token = next_token
        # The ordering mode. Valid values:
        # 
        # *   ASC (default): ascending order
        # *   DESC: descending order
        self.order = order
        # The query conditions. Example:
        # 
        #     [
        #       {
        #         "field": "VaultId",
        #         "value": "v-0003rf9m*****qx5",
        #         "operation": "MATCH_TERM"
        #       },
        #       {
        #         "field": "InstanceId",
        #         "value": "i-bp1i20zq2*****e9368m",
        #         "operation": "MATCH_TERM"
        #       },
        #       {
        #         "field": "PlanId",
        #         "value": "plan-0005vk*****gkd1iu4f",
        #         "operation": "MATCH_TERM"
        #       },
        #       {
        #         "field": "CompleteTime",
        #         "value": "1626769913",
        #         "operation": "GREATER_THAN_OR_EQUAL"
        #       }
        #     ]
        # 
        # *   The following fields are supported:
        # 
        #     *   VaultId: specifies the ID of the backup vault. This field is required.
        #     *   InstanceId: specifies the ID of the Elastic Compute Service (ECS) instance. If the SourceType parameter is set to ECS_FILE, this field is required.
        #     *   Bucket: specifies the name of the Object Storage Service (OSS) bucket. If the SourceType parameter is set to OSS, this field is required.
        #     *   FileSystemId: specifies the ID of the File Storage NAS (NAS) file system. If the SourceType parameter is set to NAS, this field is required.
        #     *   CreateTime: specifies the time when the NAS file system was created. If the SourceType parameter is set to NAS, this field is required.
        #     *   CompleteTime: specifies the time when the backup snapshot was completed.
        #     *   PlanId: the ID of a backup plan.
        # 
        # *   The following operations are supported:
        # 
        #     *   MATCH_TERM: exact match.
        #     *   GREATER_THAN: greater than.
        #     *   GREATER_THAN_OR_EQUAL: greater than or equal to.
        #     *   LESS_THAN: less than.
        #     *   LESS_THAN_OR_EQUAL: less than or equal to.
        #     *   BETWEEN: specifies a JSON array as a range. The results must fall within the range in the `[Minimum value,Maximum value]` format.
        #     *   IN: specifies an array as a collection. The results must fall within the collection.
        #     *   NOT_IN: specifies an array as a collection. The results cannot fall within the collection.
        self.query = query
        # The field that is used to sort data.
        self.sort_by = sort_by
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: backup snapshots for Elastic Compute Service (ECS) files
        # *   **OSS**: backup snapshots for Object Storage Service (OSS) buckets
        # *   **NAS**: backup snapshots for Apsara File Storage NAS file systems
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.query is not None:
            result['Query'] = self.query
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class SearchHistoricalSnapshotsShrinkRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        order: str = None,
        query_shrink: str = None,
        sort_by: str = None,
        source_type: str = None,
    ):
        # The maximum number of rows that you want the current query to return. To query only the number of matched rows without the need to return specific data, you can set the Limit parameter to `0`. Then, the operation returns only the number of matched rows.
        self.limit = limit
        # The token that is required to obtain the next page of backup snapshots.
        self.next_token = next_token
        # The ordering mode. Valid values:
        # 
        # *   ASC (default): ascending order
        # *   DESC: descending order
        self.order = order
        # The query conditions. Example:
        # 
        #     [
        #       {
        #         "field": "VaultId",
        #         "value": "v-0003rf9m*****qx5",
        #         "operation": "MATCH_TERM"
        #       },
        #       {
        #         "field": "InstanceId",
        #         "value": "i-bp1i20zq2*****e9368m",
        #         "operation": "MATCH_TERM"
        #       },
        #       {
        #         "field": "PlanId",
        #         "value": "plan-0005vk*****gkd1iu4f",
        #         "operation": "MATCH_TERM"
        #       },
        #       {
        #         "field": "CompleteTime",
        #         "value": "1626769913",
        #         "operation": "GREATER_THAN_OR_EQUAL"
        #       }
        #     ]
        # 
        # *   The following fields are supported:
        # 
        #     *   VaultId: specifies the ID of the backup vault. This field is required.
        #     *   InstanceId: specifies the ID of the Elastic Compute Service (ECS) instance. If the SourceType parameter is set to ECS_FILE, this field is required.
        #     *   Bucket: specifies the name of the Object Storage Service (OSS) bucket. If the SourceType parameter is set to OSS, this field is required.
        #     *   FileSystemId: specifies the ID of the File Storage NAS (NAS) file system. If the SourceType parameter is set to NAS, this field is required.
        #     *   CreateTime: specifies the time when the NAS file system was created. If the SourceType parameter is set to NAS, this field is required.
        #     *   CompleteTime: specifies the time when the backup snapshot was completed.
        #     *   PlanId: the ID of a backup plan.
        # 
        # *   The following operations are supported:
        # 
        #     *   MATCH_TERM: exact match.
        #     *   GREATER_THAN: greater than.
        #     *   GREATER_THAN_OR_EQUAL: greater than or equal to.
        #     *   LESS_THAN: less than.
        #     *   LESS_THAN_OR_EQUAL: less than or equal to.
        #     *   BETWEEN: specifies a JSON array as a range. The results must fall within the range in the `[Minimum value,Maximum value]` format.
        #     *   IN: specifies an array as a collection. The results must fall within the collection.
        #     *   NOT_IN: specifies an array as a collection. The results cannot fall within the collection.
        self.query_shrink = query_shrink
        # The field that is used to sort data.
        self.sort_by = sort_by
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: backup snapshots for Elastic Compute Service (ECS) files
        # *   **OSS**: backup snapshots for Object Storage Service (OSS) buckets
        # *   **NAS**: backup snapshots for Apsara File Storage NAS file systems
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.query_shrink is not None:
            result['Query'] = self.query_shrink
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Query') is not None:
            self.query_shrink = m.get('Query')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class SearchHistoricalSnapshotsResponseBodySnapshotsSnapshotPaths(TeaModel):
    def __init__(
        self,
        path: List[str] = None,
    ):
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class SearchHistoricalSnapshotsResponseBodySnapshotsSnapshot(TeaModel):
    def __init__(
        self,
        actual_bytes: int = None,
        actual_items: int = None,
        archive_time: int = None,
        backup_type: str = None,
        bucket: str = None,
        bytes_done: int = None,
        bytes_total: int = None,
        client_id: str = None,
        complete_time: int = None,
        create_time: int = None,
        created_time: int = None,
        error_file: str = None,
        exclude: str = None,
        expire_time: int = None,
        file_system_id: str = None,
        include: str = None,
        instance_id: str = None,
        instance_name: str = None,
        items_done: int = None,
        items_total: int = None,
        job_id: str = None,
        parent_snapshot_hash: str = None,
        path: str = None,
        paths: SearchHistoricalSnapshotsResponseBodySnapshotsSnapshotPaths = None,
        prefix: str = None,
        range_end: int = None,
        range_start: int = None,
        retention: int = None,
        snapshot_hash: str = None,
        snapshot_id: str = None,
        source_parent_snapshot_hash: str = None,
        source_snapshot_hash: str = None,
        source_type: str = None,
        start_time: int = None,
        status: str = None,
        storage_class: str = None,
        table_name: str = None,
        updated_time: int = None,
        use_common_nas: bool = None,
        vault_id: str = None,
    ):
        # The actual data amount of backup snapshots after duplicates are removed. Unit: bytes.
        self.actual_bytes = actual_bytes
        # The actual number of backup snapshots.
        # 
        # >  This parameter is available only for file backup.
        self.actual_items = actual_items
        # Time to archive
        self.archive_time = archive_time
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # This parameter is returned only if the **SourceType** parameter is set to **OSS**. This parameter indicates the name of the OSS bucket.
        self.bucket = bucket
        # The actual amount of data that is generated by incremental backups. Unit: bytes.
        self.bytes_done = bytes_done
        # The total amount of data. Unit: bytes.
        self.bytes_total = bytes_total
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the ID of the HBR client.
        self.client_id = client_id
        # The time when the backup snapshot was completed. The value is a UNIX timestamp. Unit: seconds.
        self.complete_time = complete_time
        # This parameter is returned only if the **SourceType** parameter is set to **NAS**. This parameter indicates the time when the file system was created. The value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time
        # The time when the backup snapshot was created. The value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The files that record the information about backup failures, including the information about partially completed backups.
        self.error_file = error_file
        # Backup paths not included in the backup job.
        self.exclude = exclude
        # The time when the snapshot expired. The value is a UNIX timestamp. Unit: seconds.
        self.expire_time = expire_time
        # This parameter is returned only if the **SourceType** parameter is set to **NAS**. This parameter indicates the ID of the NAS file system.
        self.file_system_id = file_system_id
        # Backup paths included in the backup job.
        self.include = include
        # This parameter is valid only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the ID of the ECS instance.
        self.instance_id = instance_id
        # The name of the Tablestore instance.
        self.instance_name = instance_name
        # The number of objects that are backed up.
        # 
        # >  This parameter is available only for file backup.
        self.items_done = items_done
        # The total number of objects in the data source.
        # 
        # >  This parameter is available only for file backup.
        self.items_total = items_total
        # The ID of the backup job.
        self.job_id = job_id
        # The hash value of the parent backup snapshot.
        self.parent_snapshot_hash = parent_snapshot_hash
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the path to the files that are backed up.
        self.path = path
        # The source paths.
        self.paths = paths
        # This parameter is returned only if the **SourceType** parameter is set to **OSS**. This parameter indicates the prefix of objects that are backed up.
        self.prefix = prefix
        # The time when the backup job ended. The value is a UNIX timestamp. Unit: milliseconds.
        self.range_end = range_end
        # The time when the backup job started. The value is a UNIX timestamp. Unit: milliseconds.
        self.range_start = range_start
        # The retention period of the backup snapshot. Unit: days.
        self.retention = retention
        # The hash value of the backup snapshot.
        self.snapshot_hash = snapshot_hash
        # The ID of the backup snapshot.
        self.snapshot_id = snapshot_id
        # Parent snapshot HASH value before archiving.
        self.source_parent_snapshot_hash = source_parent_snapshot_hash
        # Snapshot HASH value before archiving
        self.source_snapshot_hash = source_snapshot_hash
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: backup snapshots for ECS files
        # *   **OSS**: backup snapshots for OSS buckets
        # *   **NAS**: backup snapshots for NAS file systems
        self.source_type = source_type
        # The time when the backup snapshot started. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time
        # The status of the backup job. Valid values:
        # 
        # *   **COMPLETE**: The backup job is completed.
        # *   **PARTIAL_COMPLETE**: The backup job is partially completed.
        # *   **FAILED**: The backup job has failed.
        self.status = status
        # Storage type. Values: 
        # - **Standard**: Standard. 
        # - **Archive**: Archive. 
        # - **ColdArchive**: Cold Archive.
        self.storage_class = storage_class
        # The name of a table in the Tablestore instance.
        self.table_name = table_name
        # The time when the backup snapshot was updated. The value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time
        # Whether to use local NAS.
        self.use_common_nas = use_common_nas
        # The ID of the backup vault that stores the backup snapshot.
        self.vault_id = vault_id

    def validate(self):
        if self.paths:
            self.paths.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_bytes is not None:
            result['ActualBytes'] = self.actual_bytes
        if self.actual_items is not None:
            result['ActualItems'] = self.actual_items
        if self.archive_time is not None:
            result['ArchiveTime'] = self.archive_time
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.bytes_done is not None:
            result['BytesDone'] = self.bytes_done
        if self.bytes_total is not None:
            result['BytesTotal'] = self.bytes_total
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.error_file is not None:
            result['ErrorFile'] = self.error_file
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.include is not None:
            result['Include'] = self.include
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.items_done is not None:
            result['ItemsDone'] = self.items_done
        if self.items_total is not None:
            result['ItemsTotal'] = self.items_total
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.parent_snapshot_hash is not None:
            result['ParentSnapshotHash'] = self.parent_snapshot_hash
        if self.path is not None:
            result['Path'] = self.path
        if self.paths is not None:
            result['Paths'] = self.paths.to_map()
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.range_end is not None:
            result['RangeEnd'] = self.range_end
        if self.range_start is not None:
            result['RangeStart'] = self.range_start
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.snapshot_hash is not None:
            result['SnapshotHash'] = self.snapshot_hash
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.source_parent_snapshot_hash is not None:
            result['SourceParentSnapshotHash'] = self.source_parent_snapshot_hash
        if self.source_snapshot_hash is not None:
            result['SourceSnapshotHash'] = self.source_snapshot_hash
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.use_common_nas is not None:
            result['UseCommonNas'] = self.use_common_nas
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualBytes') is not None:
            self.actual_bytes = m.get('ActualBytes')
        if m.get('ActualItems') is not None:
            self.actual_items = m.get('ActualItems')
        if m.get('ArchiveTime') is not None:
            self.archive_time = m.get('ArchiveTime')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('BytesDone') is not None:
            self.bytes_done = m.get('BytesDone')
        if m.get('BytesTotal') is not None:
            self.bytes_total = m.get('BytesTotal')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ErrorFile') is not None:
            self.error_file = m.get('ErrorFile')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ItemsDone') is not None:
            self.items_done = m.get('ItemsDone')
        if m.get('ItemsTotal') is not None:
            self.items_total = m.get('ItemsTotal')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ParentSnapshotHash') is not None:
            self.parent_snapshot_hash = m.get('ParentSnapshotHash')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Paths') is not None:
            temp_model = SearchHistoricalSnapshotsResponseBodySnapshotsSnapshotPaths()
            self.paths = temp_model.from_map(m['Paths'])
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('RangeEnd') is not None:
            self.range_end = m.get('RangeEnd')
        if m.get('RangeStart') is not None:
            self.range_start = m.get('RangeStart')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('SnapshotHash') is not None:
            self.snapshot_hash = m.get('SnapshotHash')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SourceParentSnapshotHash') is not None:
            self.source_parent_snapshot_hash = m.get('SourceParentSnapshotHash')
        if m.get('SourceSnapshotHash') is not None:
            self.source_snapshot_hash = m.get('SourceSnapshotHash')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('UseCommonNas') is not None:
            self.use_common_nas = m.get('UseCommonNas')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class SearchHistoricalSnapshotsResponseBodySnapshots(TeaModel):
    def __init__(
        self,
        snapshot: List[SearchHistoricalSnapshotsResponseBodySnapshotsSnapshot] = None,
    ):
        self.snapshot = snapshot

    def validate(self):
        if self.snapshot:
            for k in self.snapshot:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Snapshot'] = []
        if self.snapshot is not None:
            for k in self.snapshot:
                result['Snapshot'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.snapshot = []
        if m.get('Snapshot') is not None:
            for k in m.get('Snapshot'):
                temp_model = SearchHistoricalSnapshotsResponseBodySnapshotsSnapshot()
                self.snapshot.append(temp_model.from_map(k))
        return self


class SearchHistoricalSnapshotsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        limit: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        snapshots: SearchHistoricalSnapshotsResponseBodySnapshots = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The number of historical backup snapshots that are displayed on the current page.
        self.limit = limit
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The token that is required to obtain the next page of backup snapshots.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The historical backup snapshots.
        self.snapshots = snapshots
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The total number of returned backup snapshots that meet the specified conditions.
        self.total_count = total_count

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Snapshots') is not None:
            temp_model = SearchHistoricalSnapshotsResponseBodySnapshots()
            self.snapshots = temp_model.from_map(m['Snapshots'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchHistoricalSnapshotsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchHistoricalSnapshotsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SearchHistoricalSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartHanaDatabaseAsyncRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        database_name: str = None,
        vault_id: str = None,
    ):
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The database name.
        # 
        # This parameter is required.
        self.database_name = database_name
        # The ID of the backup vault.
        # 
        # This parameter is required.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class StartHanaDatabaseAsyncResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The ID of the job that is used to initialize the backup vault. You can call the DescribeTask operation to query the job status.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StartHanaDatabaseAsyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartHanaDatabaseAsyncResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartHanaDatabaseAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopHanaDatabaseAsyncRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        database_name: str = None,
        vault_id: str = None,
    ):
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The database name.
        # 
        # This parameter is required.
        self.database_name = database_name
        # The ID of the backup vault.
        # 
        # This parameter is required.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class StopHanaDatabaseAsyncResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The ID of the asynchronous job. You can call the DescribeTask operation to query the execution result of an asynchronous job.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StopHanaDatabaseAsyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopHanaDatabaseAsyncResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopHanaDatabaseAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallBackupClientsRequest(TeaModel):
    def __init__(
        self,
        client_ids: Dict[str, Any] = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        instance_ids: Dict[str, Any] = None,
    ):
        # The IDs of Cloud Backup clients. The sum of the number of Cloud Backup client IDs and the number of ECS instance IDs cannot exceed 20. Otherwise, an error occurs.
        self.client_ids = client_ids
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up and restore data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Specifies whether data is backed up and restored within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up and restored within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up and restored across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up and restore data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The IDs of Elastic Compute Service (ECS) instances. You can specify a maximum of 20 ECS instances.
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class UninstallBackupClientsShrinkRequest(TeaModel):
    def __init__(
        self,
        client_ids_shrink: str = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        instance_ids_shrink: str = None,
    ):
        # The IDs of Cloud Backup clients. The sum of the number of Cloud Backup client IDs and the number of ECS instance IDs cannot exceed 20. Otherwise, an error occurs.
        self.client_ids_shrink = client_ids_shrink
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up and restore data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Specifies whether data is backed up and restored within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up and restored within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up and restored across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up and restore data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The IDs of Elastic Compute Service (ECS) instances. You can specify a maximum of 20 ECS instances.
        self.instance_ids_shrink = instance_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids_shrink is not None:
            result['ClientIds'] = self.client_ids_shrink
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids_shrink = m.get('ClientIds')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')
        return self


class UninstallBackupClientsResponseBodyInstanceStatuses(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        instance_id: str = None,
        valid_instance: bool = None,
    ):
        # The error code. Valid values:
        # 
        # *   If the value is empty, the request is successful.
        # *   **InstanceNotExists**: The ECS instance does not exist.
        # *   **InstanceNotRunning**: The ECS instance is not running.
        # *   **CloudAssistNotRunningOnInstance**: Cloud Assistant is unavailable.
        self.error_code = error_code
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # Indicates whether a backup client can be installed on the ECS instance.
        # 
        # *   true: A backup client can be installed on the ECS instance.
        # *   false: A backup client cannot be installed on the ECS instance.
        self.valid_instance = valid_instance

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.valid_instance is not None:
            result['ValidInstance'] = self.valid_instance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ValidInstance') is not None:
            self.valid_instance = m.get('ValidInstance')
        return self


class UninstallBackupClientsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        instance_statuses: List[UninstallBackupClientsResponseBodyInstanceStatuses] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code
        # The status of the ECS instance.
        self.instance_statuses = instance_statuses
        # The message that is returned. If the request is successful, a value of successful is returned. If the request fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        # 
        # *   true: The request is successful.
        # *   false: The request fails.
        self.success = success
        # The ID of the asynchronous job. You can call the DescribeTask operation to query the execution result of the asynchronous job.
        self.task_id = task_id

    def validate(self):
        if self.instance_statuses:
            for k in self.instance_statuses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['InstanceStatuses'] = []
        if self.instance_statuses is not None:
            for k in self.instance_statuses:
                result['InstanceStatuses'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.instance_statuses = []
        if m.get('InstanceStatuses') is not None:
            for k in m.get('InstanceStatuses'):
                temp_model = UninstallBackupClientsResponseBodyInstanceStatuses()
                self.instance_statuses.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UninstallBackupClientsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UninstallBackupClientsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UninstallBackupClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallClientRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        resource_group_id: str = None,
        vault_id: str = None,
    ):
        # The ID of the HBR client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class UninstallClientResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The ID of the asynchronous job. You can call the DescribeTask operation to query the execution result of an asynchronous job.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UninstallClientResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UninstallClientResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UninstallClientResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBackupPlanRequestRule(TeaModel):
    def __init__(
        self,
        backup_type: str = None,
        destination_region_id: str = None,
        destination_retention: int = None,
        disabled: bool = None,
        do_copy: bool = None,
        retention: int = None,
        rule_name: str = None,
        schedule: str = None,
    ):
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # The ID of the region where the remote backup vault resides.
        self.destination_region_id = destination_region_id
        # The retention period of the backup data. Unit: days.
        self.destination_retention = destination_retention
        # Specifies whether to disable the policy.
        self.disabled = disabled
        # Specifies whether to enable remote replication.
        self.do_copy = do_copy
        # The retention period of the backup data. Minimum value: 1. Unit: days.
        self.retention = retention
        # The name of the backup policy.
        self.rule_name = rule_name
        # The backup policy. Format: I|{startTime}|{interval}. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, I|1631685600|P1D specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # startTime: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds. interval: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of one hour. P1D specifies an interval of one day.
        self.schedule = schedule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id
        if self.destination_retention is not None:
            result['DestinationRetention'] = self.destination_retention
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.do_copy is not None:
            result['DoCopy'] = self.do_copy
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')
        if m.get('DestinationRetention') is not None:
            self.destination_retention = m.get('DestinationRetention')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('DoCopy') is not None:
            self.do_copy = m.get('DoCopy')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class UpdateBackupPlanRequest(TeaModel):
    def __init__(
        self,
        change_list_path: str = None,
        detail: Dict[str, Any] = None,
        exclude: str = None,
        include: str = None,
        keep_latest_snapshots: int = None,
        options: str = None,
        ots_detail: OtsDetail = None,
        path: List[str] = None,
        plan_id: str = None,
        plan_name: str = None,
        prefix: str = None,
        retention: int = None,
        rule: List[UpdateBackupPlanRequestRule] = None,
        schedule: str = None,
        source_type: str = None,
        speed_limit: str = None,
        update_paths: bool = None,
        vault_id: str = None,
    ):
        # The configurations of the incremental file synchronization. This parameter is required for data synchronization only.
        self.change_list_path = change_list_path
        # The details about ECS instance backup. The value is a JSON string.
        # 
        # *   snapshotGroup: specifies whether to use a snapshot-consistent group. This parameter is valid only if all disks of the ECS instance are enhanced SSDs (ESSDs).
        # *   appConsistent: specifies whether to enable application consistency. If you set this parameter to true, you must also specify the preScriptPath and postScriptPath parameters.
        # *   preScriptPath: the path to the pre-freeze scripts.
        # *   postScriptPath: the path to the post-thaw scripts.
        self.detail = detail
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the paths to the files that are excluded from the backup job. The value must be 1 to 255 characters in length.
        self.exclude = exclude
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the paths to the files that you want to back up. The value must be 1 to 255 characters in length.
        self.include = include
        # Specifies whether to enable the feature of keeping at least one backup version. Valid values:
        # 
        # *   0: The feature is disabled.
        # *   1: The feature is enabled.
        self.keep_latest_snapshots = keep_latest_snapshots
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies whether to use Windows Volume Shadow Copy Service (VSS) to define a source path.
        # 
        # *   This parameter is available only for Windows ECS instances.
        # *   If data changes occur in the backup source, the source data must be the same as the data to be backed up before you can set this parameter to `["UseVSS":true]`.
        # *   If you use VSS, you cannot back up data from multiple directories.
        self.options = options
        # The details about the Tablestore instance.
        self.ots_detail = ots_detail
        # The source paths.
        self.path = path
        # The ID of the backup plan.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The name of the backup plan.
        self.plan_name = plan_name
        # This parameter is required only if the **SourceType** parameter is set to **OSS**. This parameter specifies the prefix of objects that you want to back up. After a prefix is specified, only objects whose names start with the prefix are backed up.
        self.prefix = prefix
        # The retention period of the backup data. Minimum value: 1. Unit: days.
        self.retention = retention
        # The rule of the backup plan.
        self.rule = rule
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the `{startTime}` parameter and the subsequent backup jobs at an interval that is specified in the `{interval}` parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   **startTime**: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds.
        # *   **interval**: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of one hour. P1D specifies an interval of one day.
        self.schedule = schedule
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS file systems
        # *   **OTS**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        self.source_type = source_type
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the throttling rules. To ensure business continuity, you can limit the bandwidth that is used for file backup during peak hours. Format: `{start}|{end}|{bandwidth}`. Separate multiple throttling rules with vertical bars (|). A specified time range cannot overlap with another time range.
        # 
        # *   **start**: the start hour
        # *   **end**: the end hour.
        # *   **bandwidth**: the bandwidth. Unit: KB/s.
        self.speed_limit = speed_limit
        # Specifies whether to update the source path if the backup source is empty. Valid values:
        # 
        # *   true: The system replaces the original source path with the specified source path.
        # *   false: The system does not update the original source path. The system backs up data based on the source path that you specified when you created the backup plan.
        self.update_paths = update_paths
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        if self.ots_detail:
            self.ots_detail.validate()
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_list_path is not None:
            result['ChangeListPath'] = self.change_list_path
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.include is not None:
            result['Include'] = self.include
        if self.keep_latest_snapshots is not None:
            result['KeepLatestSnapshots'] = self.keep_latest_snapshots
        if self.options is not None:
            result['Options'] = self.options
        if self.ots_detail is not None:
            result['OtsDetail'] = self.ots_detail.to_map()
        if self.path is not None:
            result['Path'] = self.path
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.retention is not None:
            result['Retention'] = self.retention
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        if self.update_paths is not None:
            result['UpdatePaths'] = self.update_paths
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeListPath') is not None:
            self.change_list_path = m.get('ChangeListPath')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('KeepLatestSnapshots') is not None:
            self.keep_latest_snapshots = m.get('KeepLatestSnapshots')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OtsDetail') is not None:
            temp_model = OtsDetail()
            self.ots_detail = temp_model.from_map(m['OtsDetail'])
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = UpdateBackupPlanRequestRule()
                self.rule.append(temp_model.from_map(k))
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        if m.get('UpdatePaths') is not None:
            self.update_paths = m.get('UpdatePaths')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class UpdateBackupPlanShrinkRequestRule(TeaModel):
    def __init__(
        self,
        backup_type: str = None,
        destination_region_id: str = None,
        destination_retention: int = None,
        disabled: bool = None,
        do_copy: bool = None,
        retention: int = None,
        rule_name: str = None,
        schedule: str = None,
    ):
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # The ID of the region where the remote backup vault resides.
        self.destination_region_id = destination_region_id
        # The retention period of the backup data. Unit: days.
        self.destination_retention = destination_retention
        # Specifies whether to disable the policy.
        self.disabled = disabled
        # Specifies whether to enable remote replication.
        self.do_copy = do_copy
        # The retention period of the backup data. Minimum value: 1. Unit: days.
        self.retention = retention
        # The name of the backup policy.
        self.rule_name = rule_name
        # The backup policy. Format: I|{startTime}|{interval}. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, I|1631685600|P1D specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # startTime: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds. interval: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of one hour. P1D specifies an interval of one day.
        self.schedule = schedule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id
        if self.destination_retention is not None:
            result['DestinationRetention'] = self.destination_retention
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.do_copy is not None:
            result['DoCopy'] = self.do_copy
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')
        if m.get('DestinationRetention') is not None:
            self.destination_retention = m.get('DestinationRetention')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('DoCopy') is not None:
            self.do_copy = m.get('DoCopy')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class UpdateBackupPlanShrinkRequest(TeaModel):
    def __init__(
        self,
        change_list_path: str = None,
        detail_shrink: str = None,
        exclude: str = None,
        include: str = None,
        keep_latest_snapshots: int = None,
        options: str = None,
        ots_detail_shrink: str = None,
        path: List[str] = None,
        plan_id: str = None,
        plan_name: str = None,
        prefix: str = None,
        retention: int = None,
        rule: List[UpdateBackupPlanShrinkRequestRule] = None,
        schedule: str = None,
        source_type: str = None,
        speed_limit: str = None,
        update_paths: bool = None,
        vault_id: str = None,
    ):
        # The configurations of the incremental file synchronization. This parameter is required for data synchronization only.
        self.change_list_path = change_list_path
        # The details about ECS instance backup. The value is a JSON string.
        # 
        # *   snapshotGroup: specifies whether to use a snapshot-consistent group. This parameter is valid only if all disks of the ECS instance are enhanced SSDs (ESSDs).
        # *   appConsistent: specifies whether to enable application consistency. If you set this parameter to true, you must also specify the preScriptPath and postScriptPath parameters.
        # *   preScriptPath: the path to the pre-freeze scripts.
        # *   postScriptPath: the path to the post-thaw scripts.
        self.detail_shrink = detail_shrink
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the paths to the files that are excluded from the backup job. The value must be 1 to 255 characters in length.
        self.exclude = exclude
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the paths to the files that you want to back up. The value must be 1 to 255 characters in length.
        self.include = include
        # Specifies whether to enable the feature of keeping at least one backup version. Valid values:
        # 
        # *   0: The feature is disabled.
        # *   1: The feature is enabled.
        self.keep_latest_snapshots = keep_latest_snapshots
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies whether to use Windows Volume Shadow Copy Service (VSS) to define a source path.
        # 
        # *   This parameter is available only for Windows ECS instances.
        # *   If data changes occur in the backup source, the source data must be the same as the data to be backed up before you can set this parameter to `["UseVSS":true]`.
        # *   If you use VSS, you cannot back up data from multiple directories.
        self.options = options
        # The details about the Tablestore instance.
        self.ots_detail_shrink = ots_detail_shrink
        # The source paths.
        self.path = path
        # The ID of the backup plan.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The name of the backup plan.
        self.plan_name = plan_name
        # This parameter is required only if the **SourceType** parameter is set to **OSS**. This parameter specifies the prefix of objects that you want to back up. After a prefix is specified, only objects whose names start with the prefix are backed up.
        self.prefix = prefix
        # The retention period of the backup data. Minimum value: 1. Unit: days.
        self.retention = retention
        # The rule of the backup plan.
        self.rule = rule
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the `{startTime}` parameter and the subsequent backup jobs at an interval that is specified in the `{interval}` parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   **startTime**: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds.
        # *   **interval**: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of one hour. P1D specifies an interval of one day.
        self.schedule = schedule
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS file systems
        # *   **OTS**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        self.source_type = source_type
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the throttling rules. To ensure business continuity, you can limit the bandwidth that is used for file backup during peak hours. Format: `{start}|{end}|{bandwidth}`. Separate multiple throttling rules with vertical bars (|). A specified time range cannot overlap with another time range.
        # 
        # *   **start**: the start hour
        # *   **end**: the end hour.
        # *   **bandwidth**: the bandwidth. Unit: KB/s.
        self.speed_limit = speed_limit
        # Specifies whether to update the source path if the backup source is empty. Valid values:
        # 
        # *   true: The system replaces the original source path with the specified source path.
        # *   false: The system does not update the original source path. The system backs up data based on the source path that you specified when you created the backup plan.
        self.update_paths = update_paths
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_list_path is not None:
            result['ChangeListPath'] = self.change_list_path
        if self.detail_shrink is not None:
            result['Detail'] = self.detail_shrink
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.include is not None:
            result['Include'] = self.include
        if self.keep_latest_snapshots is not None:
            result['KeepLatestSnapshots'] = self.keep_latest_snapshots
        if self.options is not None:
            result['Options'] = self.options
        if self.ots_detail_shrink is not None:
            result['OtsDetail'] = self.ots_detail_shrink
        if self.path is not None:
            result['Path'] = self.path
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.retention is not None:
            result['Retention'] = self.retention
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        if self.update_paths is not None:
            result['UpdatePaths'] = self.update_paths
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeListPath') is not None:
            self.change_list_path = m.get('ChangeListPath')
        if m.get('Detail') is not None:
            self.detail_shrink = m.get('Detail')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('KeepLatestSnapshots') is not None:
            self.keep_latest_snapshots = m.get('KeepLatestSnapshots')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OtsDetail') is not None:
            self.ots_detail_shrink = m.get('OtsDetail')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = UpdateBackupPlanShrinkRequestRule()
                self.rule.append(temp_model.from_map(k))
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        if m.get('UpdatePaths') is not None:
            self.update_paths = m.get('UpdatePaths')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class UpdateBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClientSettingsRequest(TeaModel):
    def __init__(
        self,
        alert_on_partial_complete: bool = None,
        client_id: str = None,
        data_network_type: str = None,
        data_proxy_setting: str = None,
        max_cpu_core: int = None,
        max_memory: int = None,
        max_worker: int = None,
        proxy_host: str = None,
        proxy_password: str = None,
        proxy_port: int = None,
        proxy_user: str = None,
        resource_group_id: str = None,
        use_https: bool = None,
        vault_id: str = None,
    ):
        # Specifies whether to generate alert for partially completed jobs. This parameter is valid only for on-premises file backup and ECS file backup.
        self.alert_on_partial_complete = alert_on_partial_complete
        # The ID of the HBR client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The type of the endpoint on the data plane. Valid values:
        # 
        # *   **PUBLIC**: Internet
        # *   **VPC**: virtual private cloud (VPC)
        # *   **CLASSIC**: classic network
        self.data_network_type = data_network_type
        # The proxy configuration on the data plane. Valid values:
        # 
        # *   **DISABLE**: The proxy is not used.
        # *   **USE_CONTROL_PROXY** (default): The configuration is the same as that on the control plane.
        # *   **CUSTOM**: The configuration is customized (HTTP).
        self.data_proxy_setting = data_proxy_setting
        # The number of CPU cores used by a single backup job. The value 0 indicates that the number is unlimited.
        self.max_cpu_core = max_cpu_core
        # The maximum memory that can be used by the client. Unit: bytes. Only V2.13.0 and later are supported.
        self.max_memory = max_memory
        # The number of concurrent backup jobs. The value 0 indicates that the number is unlimited.
        self.max_worker = max_worker
        # The custom host IP address of the proxy server on the data plane.
        self.proxy_host = proxy_host
        # The custom password of the proxy server on the data plane.
        self.proxy_password = proxy_password
        # The custom host port of the proxy server on the data plane.
        self.proxy_port = proxy_port
        # The custom username of the proxy server on the data plane.
        self.proxy_user = proxy_user
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Specifies whether to transmit the data on the data plane over HTTPS. Valid values:
        # 
        # *   true: Data is transmitted over HTTPS.
        # *   false: Data is transmitted over HTTP.
        self.use_https = use_https
        # The ID of the backup vault. This parameter is required for the old HBR client.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_on_partial_complete is not None:
            result['AlertOnPartialComplete'] = self.alert_on_partial_complete
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.data_network_type is not None:
            result['DataNetworkType'] = self.data_network_type
        if self.data_proxy_setting is not None:
            result['DataProxySetting'] = self.data_proxy_setting
        if self.max_cpu_core is not None:
            result['MaxCpuCore'] = self.max_cpu_core
        if self.max_memory is not None:
            result['MaxMemory'] = self.max_memory
        if self.max_worker is not None:
            result['MaxWorker'] = self.max_worker
        if self.proxy_host is not None:
            result['ProxyHost'] = self.proxy_host
        if self.proxy_password is not None:
            result['ProxyPassword'] = self.proxy_password
        if self.proxy_port is not None:
            result['ProxyPort'] = self.proxy_port
        if self.proxy_user is not None:
            result['ProxyUser'] = self.proxy_user
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.use_https is not None:
            result['UseHttps'] = self.use_https
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertOnPartialComplete') is not None:
            self.alert_on_partial_complete = m.get('AlertOnPartialComplete')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('DataNetworkType') is not None:
            self.data_network_type = m.get('DataNetworkType')
        if m.get('DataProxySetting') is not None:
            self.data_proxy_setting = m.get('DataProxySetting')
        if m.get('MaxCpuCore') is not None:
            self.max_cpu_core = m.get('MaxCpuCore')
        if m.get('MaxMemory') is not None:
            self.max_memory = m.get('MaxMemory')
        if m.get('MaxWorker') is not None:
            self.max_worker = m.get('MaxWorker')
        if m.get('ProxyHost') is not None:
            self.proxy_host = m.get('ProxyHost')
        if m.get('ProxyPassword') is not None:
            self.proxy_password = m.get('ProxyPassword')
        if m.get('ProxyPort') is not None:
            self.proxy_port = m.get('ProxyPort')
        if m.get('ProxyUser') is not None:
            self.proxy_user = m.get('ProxyUser')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('UseHttps') is not None:
            self.use_https = m.get('UseHttps')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class UpdateClientSettingsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateClientSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateClientSettingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateClientSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateContainerClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        description: str = None,
        name: str = None,
        network_type: str = None,
        renew_token: bool = None,
    ):
        # Cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Cluster description.
        self.description = description
        # Cluster name.
        self.name = name
        # Network type, with possible values including:
        # * **CLASSIC**: Classic Network.
        # * **VPC**: Virtual Private Cloud.
        self.network_type = network_type
        # Whether to regenerate the token.
        self.renew_token = renew_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.renew_token is not None:
            result['RenewToken'] = self.renew_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('RenewToken') is not None:
            self.renew_token = m.get('RenewToken')
        return self


class UpdateContainerClusterResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        token: str = None,
        token_updated: bool = None,
    ):
        # Return code, 200 indicates success.
        self.code = code
        # Return information.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates if the request was successful.
        # 
        # - true: Success
        # - false: Failure
        self.success = success
        # Cluster token, used for registering HBR clients within the cluster.
        self.token = token
        # Indicates whether the cluster token has been updated.
        self.token_updated = token_updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.token is not None:
            result['Token'] = self.token
        if self.token_updated is not None:
            result['TokenUpdated'] = self.token_updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('TokenUpdated') is not None:
            self.token_updated = m.get('TokenUpdated')
        return self


class UpdateContainerClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateContainerClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateContainerClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHanaBackupPlanRequest(TeaModel):
    def __init__(
        self,
        backup_prefix: str = None,
        cluster_id: str = None,
        plan_id: str = None,
        plan_name: str = None,
        resource_group_id: str = None,
        schedule: str = None,
        vault_id: str = None,
    ):
        # The backup prefix.
        self.backup_prefix = backup_prefix
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the backup plan.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The name of the backup plan.
        self.plan_name = plan_name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` indicates that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   startTime: the time at which the system starts to run a backup job. The time follows the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system runs a backup job. The interval follows the ISO 8601 standard. For example, PT1H indicates an interval of 1 hour. P1D indicates an interval of one day.
        self.schedule = schedule
        # The ID of the backup vault.
        # 
        # This parameter is required.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_prefix is not None:
            result['BackupPrefix'] = self.backup_prefix
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPrefix') is not None:
            self.backup_prefix = m.get('BackupPrefix')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class UpdateHanaBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateHanaBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateHanaBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateHanaBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHanaBackupSettingRequest(TeaModel):
    def __init__(
        self,
        catalog_backup_parameter_file: str = None,
        catalog_backup_using_backint: bool = None,
        cluster_id: str = None,
        data_backup_parameter_file: str = None,
        database_name: str = None,
        enable_auto_log_backup: bool = None,
        log_backup_parameter_file: str = None,
        log_backup_timeout: int = None,
        log_backup_using_backint: bool = None,
        vault_id: str = None,
    ):
        # The configuration file for catalog backup.
        self.catalog_backup_parameter_file = catalog_backup_parameter_file
        # Specifies whether to use Backint to back up catalogs. Valid values:
        # 
        # *   true: Backint is used to back up catalogs.
        # *   false: Backint is not used to back up catalogs.
        # 
        # This parameter is required.
        self.catalog_backup_using_backint = catalog_backup_using_backint
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The configuration file for data backup.
        self.data_backup_parameter_file = data_backup_parameter_file
        # The name of the database.
        # 
        # This parameter is required.
        self.database_name = database_name
        # Specifies whether to enable automatic log backup. Valid values:
        # 
        # *   **true**: enables automatic log backup.
        # *   **false**: disables automatic log backup.
        # 
        # This parameter is required.
        self.enable_auto_log_backup = enable_auto_log_backup
        # The configuration file for log backup.
        self.log_backup_parameter_file = log_backup_parameter_file
        # The interval at which logs are backed up. Unit: seconds.
        self.log_backup_timeout = log_backup_timeout
        # Specifies whether to use Backint to back up logs. Valid values:
        # 
        # *   true: Backint is used to back up logs.
        # *   false: Backint is not used to back up logs.
        # 
        # This parameter is required.
        self.log_backup_using_backint = log_backup_using_backint
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_backup_parameter_file is not None:
            result['CatalogBackupParameterFile'] = self.catalog_backup_parameter_file
        if self.catalog_backup_using_backint is not None:
            result['CatalogBackupUsingBackint'] = self.catalog_backup_using_backint
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_backup_parameter_file is not None:
            result['DataBackupParameterFile'] = self.data_backup_parameter_file
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.enable_auto_log_backup is not None:
            result['EnableAutoLogBackup'] = self.enable_auto_log_backup
        if self.log_backup_parameter_file is not None:
            result['LogBackupParameterFile'] = self.log_backup_parameter_file
        if self.log_backup_timeout is not None:
            result['LogBackupTimeout'] = self.log_backup_timeout
        if self.log_backup_using_backint is not None:
            result['LogBackupUsingBackint'] = self.log_backup_using_backint
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogBackupParameterFile') is not None:
            self.catalog_backup_parameter_file = m.get('CatalogBackupParameterFile')
        if m.get('CatalogBackupUsingBackint') is not None:
            self.catalog_backup_using_backint = m.get('CatalogBackupUsingBackint')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataBackupParameterFile') is not None:
            self.data_backup_parameter_file = m.get('DataBackupParameterFile')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EnableAutoLogBackup') is not None:
            self.enable_auto_log_backup = m.get('EnableAutoLogBackup')
        if m.get('LogBackupParameterFile') is not None:
            self.log_backup_parameter_file = m.get('LogBackupParameterFile')
        if m.get('LogBackupTimeout') is not None:
            self.log_backup_timeout = m.get('LogBackupTimeout')
        if m.get('LogBackupUsingBackint') is not None:
            self.log_backup_using_backint = m.get('LogBackupUsingBackint')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class UpdateHanaBackupSettingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateHanaBackupSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateHanaBackupSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateHanaBackupSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHanaInstanceRequest(TeaModel):
    def __init__(
        self,
        alert_setting: str = None,
        cluster_id: str = None,
        hana_name: str = None,
        host: str = None,
        instance_number: int = None,
        password: str = None,
        resource_group_id: str = None,
        use_ssl: bool = None,
        user_name: str = None,
        validate_certificate: bool = None,
        vault_id: str = None,
    ):
        # The alert settings. Valid value: INHERITED, which indicates that the Cloud Backup client sends alert notifications by using the same method configured for the backup vault.
        self.alert_setting = alert_setting
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id
        # The name of the SAP HANA instance.
        self.hana_name = hana_name
        # The private or internal IP address of the host where the primary node of the SAP HANA instance resides.
        self.host = host
        # The instance number of the SAP HANA system.
        # 
        # This parameter is required.
        self.instance_number = instance_number
        # The password that is used to connect with the SAP HANA database.
        self.password = password
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Specifies whether to connect with the SAP HANA database over Secure Sockets Layer (SSL). Valid values:
        # 
        # *   true: The SAP HANA database is connected over SSL.
        # *   false: The SAP HANA database is not connected over SSL.
        # 
        # This parameter is required.
        self.use_ssl = use_ssl
        # The username of the SYSTEMDB database.
        self.user_name = user_name
        # Specifies whether to verify the SSL certificate of the SAP HANA database. Valid values:
        # 
        # *   true: The SSL certificate of the SAP HANA database is verified.
        # *   false: The SSL certificate of the SAP HANA database is not verified.
        # 
        # This parameter is required.
        self.validate_certificate = validate_certificate
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_setting is not None:
            result['AlertSetting'] = self.alert_setting
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.hana_name is not None:
            result['HanaName'] = self.hana_name
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number
        if self.password is not None:
            result['Password'] = self.password
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.use_ssl is not None:
            result['UseSsl'] = self.use_ssl
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.validate_certificate is not None:
            result['ValidateCertificate'] = self.validate_certificate
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertSetting') is not None:
            self.alert_setting = m.get('AlertSetting')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('HanaName') is not None:
            self.hana_name = m.get('HanaName')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('UseSsl') is not None:
            self.use_ssl = m.get('UseSsl')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('ValidateCertificate') is not None:
            self.validate_certificate = m.get('ValidateCertificate')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class UpdateHanaInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateHanaInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateHanaInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateHanaInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHanaRetentionSettingRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        database_name: str = None,
        disabled: bool = None,
        retention_days: int = None,
        schedule: str = None,
        vault_id: str = None,
    ):
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The database name.
        # 
        # This parameter is required.
        self.database_name = database_name
        # Specifies whether to permanently retain the backup. Valid values:
        # 
        # *   true: The backup is permanently retained.
        # *   false: The backup is retained for the specified number of days.
        # 
        # This parameter is required.
        self.disabled = disabled
        # The retention period of the backup data. Unit: days. If you set the Disabled parameter to false, the backup is retained for the number of days specified by this parameter.
        # 
        # This parameter is required.
        self.retention_days = retention_days
        # The policy to update the retention period. Format: `I|{startTime}|{interval}`. The retention period is updated at an interval of {interval} starting from {startTime}.
        # 
        # *   startTime: the time at which the system starts to run a backup job. The time follows the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system runs a backup job. The interval follows the ISO 8601 standard. For example, PT1H indicates an interval of 1 hour, and P1D indicates an interval of one day.
        # 
        # This parameter is required.
        self.schedule = schedule
        # The ID of the backup vault.
        # 
        # This parameter is required.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class UpdateHanaRetentionSettingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateHanaRetentionSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateHanaRetentionSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateHanaRetentionSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePolicyBindingRequestAdvancedOptionsCommonFileSystemDetail(TeaModel):
    def __init__(
        self,
        fetch_slice_size: int = None,
        full_on_increment_fail: bool = None,
    ):
        # The size of backup shards (the number of files).
        self.fetch_slice_size = fetch_slice_size
        # Specifies whether the system performs full backup if incremental backup fails. Valid values:
        # 
        # *   **true**: The system performs full backup if incremental backup fails.
        # *   **false**: The system does not perform full backup if incremental backup fails.
        self.full_on_increment_fail = full_on_increment_fail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fetch_slice_size is not None:
            result['FetchSliceSize'] = self.fetch_slice_size
        if self.full_on_increment_fail is not None:
            result['FullOnIncrementFail'] = self.full_on_increment_fail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FetchSliceSize') is not None:
            self.fetch_slice_size = m.get('FetchSliceSize')
        if m.get('FullOnIncrementFail') is not None:
            self.full_on_increment_fail = m.get('FullOnIncrementFail')
        return self


class UpdatePolicyBindingRequestAdvancedOptionsOssDetail(TeaModel):
    def __init__(
        self,
        ignore_archive_object: bool = None,
        inventory_cleanup_policy: str = None,
        inventory_id: str = None,
    ):
        # Do not prompt for archival type objects in task statistics and failed file lists.
        self.ignore_archive_object = ignore_archive_object
        # Specifies whether the system deletes the inventory lists when a backup is completed. This parameter is valid only when OSS inventories are used. Valid values:
        # 
        # *   **NO_CLEANUP**: does not delete inventory lists.
        # *   **DELETE_CURRENT**: deletes the current inventory list.
        # *   **DELETE_CURRENT_AND_PREVIOUS**: deletes all inventory lists.
        self.inventory_cleanup_policy = inventory_cleanup_policy
        # The name of the OSS inventory. If this parameter is not empty, the OSS inventory is used for performance optimization.
        # 
        # *   If you want to back up more than 100 million OSS objects, we recommend that you use inventory lists to accelerate incremental backup. Storage fees for inventory lists are included into your OSS bills.
        # *   A certain amount of time is required for OSS to generate inventory lists. Before inventory lists are generated, OSS objects may fail to be backed up. In this case, you can back up the OSS objects in the next backup cycle.
        self.inventory_id = inventory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ignore_archive_object is not None:
            result['IgnoreArchiveObject'] = self.ignore_archive_object
        if self.inventory_cleanup_policy is not None:
            result['InventoryCleanupPolicy'] = self.inventory_cleanup_policy
        if self.inventory_id is not None:
            result['InventoryId'] = self.inventory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoreArchiveObject') is not None:
            self.ignore_archive_object = m.get('IgnoreArchiveObject')
        if m.get('InventoryCleanupPolicy') is not None:
            self.inventory_cleanup_policy = m.get('InventoryCleanupPolicy')
        if m.get('InventoryId') is not None:
            self.inventory_id = m.get('InventoryId')
        return self


class UpdatePolicyBindingRequestAdvancedOptionsUdmDetail(TeaModel):
    def __init__(
        self,
        app_consistent: bool = None,
        disk_id_list: List[str] = None,
        enable_fs_freeze: bool = None,
        enable_writers: bool = None,
        exclude_disk_id_list: List[str] = None,
        post_script_path: str = None,
        pre_script_path: str = None,
        ram_role_name: str = None,
        snapshot_group: bool = None,
        timeout_in_seconds: int = None,
    ):
        # Specifies whether to enable application consistency. You can enable application consistency only if all disks are ESSDs.
        self.app_consistent = app_consistent
        # The IDs of the disks that need to be protected. If all disks need to be protected, this parameter is empty.
        self.disk_id_list = disk_id_list
        # This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies whether to enable Linux fsfreeze to put file systems into the read-only state before application-consistent snapshots are created. Default value: true.
        self.enable_fs_freeze = enable_fs_freeze
        # This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies whether to create application-consistent snapshots. Valid values:
        # 
        # *   true: creates application-consistent snapshots
        # *   false: creates file system-consistent snapshots
        # 
        # Default value: true.
        self.enable_writers = enable_writers
        # The IDs of the disks that do not need to be protected. If the DiskIdList parameter is not empty, this parameter is ignored.
        self.exclude_disk_id_list = exclude_disk_id_list
        # This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies the path of the post-thaw scripts that are executed after application-consistent snapshots are created.
        self.post_script_path = post_script_path
        # This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies the path of the pre-freeze scripts that are executed before application-consistent snapshots are created.
        self.pre_script_path = pre_script_path
        # This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies the name of the Resource Access Management (RAM) role that is required to create application-consistent snapshots.
        self.ram_role_name = ram_role_name
        # Specifies whether to create a snapshot-consistent group. You can create a snapshot-consistent group only if all disks are Enterprise SSDs (ESSDs).
        self.snapshot_group = snapshot_group
        # This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies the I/O freeze timeout period. Default value: 30. Unit: seconds.
        self.timeout_in_seconds = timeout_in_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_consistent is not None:
            result['AppConsistent'] = self.app_consistent
        if self.disk_id_list is not None:
            result['DiskIdList'] = self.disk_id_list
        if self.enable_fs_freeze is not None:
            result['EnableFsFreeze'] = self.enable_fs_freeze
        if self.enable_writers is not None:
            result['EnableWriters'] = self.enable_writers
        if self.exclude_disk_id_list is not None:
            result['ExcludeDiskIdList'] = self.exclude_disk_id_list
        if self.post_script_path is not None:
            result['PostScriptPath'] = self.post_script_path
        if self.pre_script_path is not None:
            result['PreScriptPath'] = self.pre_script_path
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.snapshot_group is not None:
            result['SnapshotGroup'] = self.snapshot_group
        if self.timeout_in_seconds is not None:
            result['TimeoutInSeconds'] = self.timeout_in_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppConsistent') is not None:
            self.app_consistent = m.get('AppConsistent')
        if m.get('DiskIdList') is not None:
            self.disk_id_list = m.get('DiskIdList')
        if m.get('EnableFsFreeze') is not None:
            self.enable_fs_freeze = m.get('EnableFsFreeze')
        if m.get('EnableWriters') is not None:
            self.enable_writers = m.get('EnableWriters')
        if m.get('ExcludeDiskIdList') is not None:
            self.exclude_disk_id_list = m.get('ExcludeDiskIdList')
        if m.get('PostScriptPath') is not None:
            self.post_script_path = m.get('PostScriptPath')
        if m.get('PreScriptPath') is not None:
            self.pre_script_path = m.get('PreScriptPath')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('SnapshotGroup') is not None:
            self.snapshot_group = m.get('SnapshotGroup')
        if m.get('TimeoutInSeconds') is not None:
            self.timeout_in_seconds = m.get('TimeoutInSeconds')
        return self


class UpdatePolicyBindingRequestAdvancedOptions(TeaModel):
    def __init__(
        self,
        common_file_system_detail: UpdatePolicyBindingRequestAdvancedOptionsCommonFileSystemDetail = None,
        oss_detail: UpdatePolicyBindingRequestAdvancedOptionsOssDetail = None,
        udm_detail: UpdatePolicyBindingRequestAdvancedOptionsUdmDetail = None,
    ):
        # The details about large-scale file system backup.
        self.common_file_system_detail = common_file_system_detail
        # The details about Object Storage Service (OSS) backup.
        self.oss_detail = oss_detail
        # The details about Elastic Compute Service (ECS) instance backup.
        self.udm_detail = udm_detail

    def validate(self):
        if self.common_file_system_detail:
            self.common_file_system_detail.validate()
        if self.oss_detail:
            self.oss_detail.validate()
        if self.udm_detail:
            self.udm_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_file_system_detail is not None:
            result['CommonFileSystemDetail'] = self.common_file_system_detail.to_map()
        if self.oss_detail is not None:
            result['OssDetail'] = self.oss_detail.to_map()
        if self.udm_detail is not None:
            result['UdmDetail'] = self.udm_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonFileSystemDetail') is not None:
            temp_model = UpdatePolicyBindingRequestAdvancedOptionsCommonFileSystemDetail()
            self.common_file_system_detail = temp_model.from_map(m['CommonFileSystemDetail'])
        if m.get('OssDetail') is not None:
            temp_model = UpdatePolicyBindingRequestAdvancedOptionsOssDetail()
            self.oss_detail = temp_model.from_map(m['OssDetail'])
        if m.get('UdmDetail') is not None:
            temp_model = UpdatePolicyBindingRequestAdvancedOptionsUdmDetail()
            self.udm_detail = temp_model.from_map(m['UdmDetail'])
        return self


class UpdatePolicyBindingRequest(TeaModel):
    def __init__(
        self,
        advanced_options: UpdatePolicyBindingRequestAdvancedOptions = None,
        data_source_id: str = None,
        disabled: bool = None,
        exclude: str = None,
        include: str = None,
        policy_binding_description: str = None,
        policy_id: str = None,
        source: str = None,
        source_type: str = None,
        speed_limit: str = None,
    ):
        # The advanced options.
        self.advanced_options = advanced_options
        # The ID of the data source.
        # 
        # This parameter is required.
        self.data_source_id = data_source_id
        # Specifies whether to disable the backup policy for the data source. Valid values:
        # 
        # *   true: disables the backup policy for the data source
        # *   false: enables the backup policy for the data source
        self.disabled = disabled
        # This parameter is required only if you set the **SourceType** parameter to **ECS_FILE** or **File**. This parameter specifies the type of files that do not need to be backed up. No files of the specified type are backed up. The value can be up to 255 characters in length.
        self.exclude = exclude
        # This parameter is required only if you set the **SourceType** parameter to **ECS_FILE** or **File**. This parameter specifies the type of files to be backed up. All files of the specified type are backed up. The value can be up to 255 characters in length.
        self.include = include
        # The description of the association.
        self.policy_binding_description = policy_binding_description
        # The ID of the backup policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # *   If the SourceType parameter is set to **OSS**, set the Source parameter to the prefix of the path to the folder that you want to back up. If you do not specify the Source parameter, the entire bucket (root directory) is backed up.
        # *   If the SourceType parameter is set to **ECS_FILE** or **File**, set the Source parameter to the path to the files that you want to back up. If you do not specify the Source parameter, all paths backed up.
        self.source = source
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instance backup
        # 
        # This parameter is required.
        self.source_type = source_type
        # This parameter is required only if you set the **SourceType** parameter to **ECS_FILE** or **File**. This parameter specifies the throttling rules. Format: `{start}{end}{bandwidth}`. Separate multiple throttling rules with vertical bars (|). The time ranges of the throttling rules cannot overlap.
        # 
        # *   **start**: the start hour.
        # *   **end**: the end hour.
        # *   **bandwidth**: the bandwidth. Unit: KB/s.
        self.speed_limit = speed_limit

    def validate(self):
        if self.advanced_options:
            self.advanced_options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_options is not None:
            result['AdvancedOptions'] = self.advanced_options.to_map()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.include is not None:
            result['Include'] = self.include
        if self.policy_binding_description is not None:
            result['PolicyBindingDescription'] = self.policy_binding_description
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedOptions') is not None:
            temp_model = UpdatePolicyBindingRequestAdvancedOptions()
            self.advanced_options = temp_model.from_map(m['AdvancedOptions'])
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('PolicyBindingDescription') is not None:
            self.policy_binding_description = m.get('PolicyBindingDescription')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        return self


class UpdatePolicyBindingShrinkRequest(TeaModel):
    def __init__(
        self,
        advanced_options_shrink: str = None,
        data_source_id: str = None,
        disabled: bool = None,
        exclude: str = None,
        include: str = None,
        policy_binding_description: str = None,
        policy_id: str = None,
        source: str = None,
        source_type: str = None,
        speed_limit: str = None,
    ):
        # The advanced options.
        self.advanced_options_shrink = advanced_options_shrink
        # The ID of the data source.
        # 
        # This parameter is required.
        self.data_source_id = data_source_id
        # Specifies whether to disable the backup policy for the data source. Valid values:
        # 
        # *   true: disables the backup policy for the data source
        # *   false: enables the backup policy for the data source
        self.disabled = disabled
        # This parameter is required only if you set the **SourceType** parameter to **ECS_FILE** or **File**. This parameter specifies the type of files that do not need to be backed up. No files of the specified type are backed up. The value can be up to 255 characters in length.
        self.exclude = exclude
        # This parameter is required only if you set the **SourceType** parameter to **ECS_FILE** or **File**. This parameter specifies the type of files to be backed up. All files of the specified type are backed up. The value can be up to 255 characters in length.
        self.include = include
        # The description of the association.
        self.policy_binding_description = policy_binding_description
        # The ID of the backup policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # *   If the SourceType parameter is set to **OSS**, set the Source parameter to the prefix of the path to the folder that you want to back up. If you do not specify the Source parameter, the entire bucket (root directory) is backed up.
        # *   If the SourceType parameter is set to **ECS_FILE** or **File**, set the Source parameter to the path to the files that you want to back up. If you do not specify the Source parameter, all paths backed up.
        self.source = source
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instance backup
        # 
        # This parameter is required.
        self.source_type = source_type
        # This parameter is required only if you set the **SourceType** parameter to **ECS_FILE** or **File**. This parameter specifies the throttling rules. Format: `{start}{end}{bandwidth}`. Separate multiple throttling rules with vertical bars (|). The time ranges of the throttling rules cannot overlap.
        # 
        # *   **start**: the start hour.
        # *   **end**: the end hour.
        # *   **bandwidth**: the bandwidth. Unit: KB/s.
        self.speed_limit = speed_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_options_shrink is not None:
            result['AdvancedOptions'] = self.advanced_options_shrink
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.include is not None:
            result['Include'] = self.include
        if self.policy_binding_description is not None:
            result['PolicyBindingDescription'] = self.policy_binding_description
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedOptions') is not None:
            self.advanced_options_shrink = m.get('AdvancedOptions')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('PolicyBindingDescription') is not None:
            self.policy_binding_description = m.get('PolicyBindingDescription')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        return self


class UpdatePolicyBindingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdatePolicyBindingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePolicyBindingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePolicyBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePolicyV2RequestRulesDataSourceFilters(TeaModel):
    def __init__(
        self,
        data_source_ids: List[str] = None,
        source_type: str = None,
    ):
        # This parameter is deprecated.
        self.data_source_ids = data_source_ids
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: Elastic Compute Service (ECS) instance This type of data source is supported only if the **RuleType** parameter is set to **UDM_ECS_ONLY**.
        # *   **OSS**: Object Storage Service (OSS) bucket This type of data source is supported only if the **RuleType** parameter is set to **STANDARD**.
        # *   **NAS**: File Storage NAS (NAS) file system This type of data source is supported only if the **RuleType** parameter is set to **STANDARD**.
        # *   **ECS_FILE**: ECS file This type of data source is supported only if the **RuleType** parameter is set to **STANDARD**.
        # *   **OTS**: Tablestore instance This type of data source is supported only if the **RuleType** parameter is set to **STANDARD**.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_ids is not None:
            result['DataSourceIds'] = self.data_source_ids
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceIds') is not None:
            self.data_source_ids = m.get('DataSourceIds')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class UpdatePolicyV2RequestRulesRetentionRules(TeaModel):
    def __init__(
        self,
        advanced_retention_type: str = None,
        retention: int = None,
        which_snapshot: int = None,
    ):
        # The type of the special retention rule. Valid values:
        # 
        # *   **WEEKLY**: retains weekly backups
        # *   **MONTHLY**: retains monthly backups
        # *   **YEARLY**: retains yearly backups
        self.advanced_retention_type = advanced_retention_type
        # The special retention period of backups. Minimum value: 1. Unit: days.
        self.retention = retention
        # Specifies which backup is retained based on the special retention rule. Only the first backup can be retained.
        self.which_snapshot = which_snapshot

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_retention_type is not None:
            result['AdvancedRetentionType'] = self.advanced_retention_type
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.which_snapshot is not None:
            result['WhichSnapshot'] = self.which_snapshot
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedRetentionType') is not None:
            self.advanced_retention_type = m.get('AdvancedRetentionType')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('WhichSnapshot') is not None:
            self.which_snapshot = m.get('WhichSnapshot')
        return self


class UpdatePolicyV2RequestRulesTagFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag-based matching rule. Valid values:
        # 
        # *   **EQUAL**: Both the tag key and tag value are matched.
        # *   **NOT**: The tag key is matched and the tag value is not matched.
        self.operator = operator
        # The tag value. If you leave this parameter empty, the value is any value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdatePolicyV2RequestRules(TeaModel):
    def __init__(
        self,
        archive_days: int = None,
        backup_type: str = None,
        cold_archive_days: int = None,
        data_source_filters: List[UpdatePolicyV2RequestRulesDataSourceFilters] = None,
        immutable: bool = None,
        keep_latest_snapshots: int = None,
        replication_region_id: str = None,
        retention: int = None,
        retention_rules: List[UpdatePolicyV2RequestRulesRetentionRules] = None,
        rule_id: str = None,
        rule_type: str = None,
        schedule: str = None,
        tag_filters: List[UpdatePolicyV2RequestRulesTagFilters] = None,
        vault_id: str = None,
    ):
        # This parameter is required only if the **RuleType** parameter is set to **TRANSITION**. This parameter specifies the time when data is dumped from a backup vault to an archive vault. Unit: days.
        self.archive_days = archive_days
        # This parameter is required only if the **RuleType** parameter is set to **BACKUP**. This parameter specifies the backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # This parameter is required only if the **RuleType** parameter is set to **TRANSITION**. This parameter specifies the time when data is dumped from a backup vault to a cold archive vault. Unit: days.
        self.cold_archive_days = cold_archive_days
        # This parameter is required only if the **RuleType** parameter is set to **TAG**. This parameter specifies the data source filter rule.
        self.data_source_filters = data_source_filters
        # This parameter is required only if the **PolicyType** parameter is set to **UDM_ECS_ONLY**. This parameter specifies whether to enable the immutable backup feature.
        self.immutable = immutable
        # Specifies whether to enable the feature of keeping at least one backup version. Valid values:
        # 
        # *   0: The feature is disabled.
        # *   1: The feature is enabled.
        self.keep_latest_snapshots = keep_latest_snapshots
        # This parameter is required only if the **RuleType** parameter is set to **REPLICATION**. This parameter specifies the ID of the destination region.
        self.replication_region_id = replication_region_id
        # This parameter is required only if the **RuleType** parameter is set to **TRANSITION** or **REPLICATION**.
        # 
        # *   If the **RuleType** parameter is set to **TRANSITION**, this parameter specifies the retention period of the backup data. Minimum value: 1. Unit: days.
        # *   If the **RuleType** parameter is set to **REPLICATION**, this parameter specifies the retention period of remote backups. Minimum value: 1. Unit: days.
        self.retention = retention
        # This parameter is required only if the value of the **RuleType** parameter is **TRANSITION**. This parameter specifies the special retention rules.
        self.retention_rules = retention_rules
        # The rule ID.
        self.rule_id = rule_id
        # The type of the rule. Each backup policy must have at least one rule of the **BACKUP** type and only one rule of the **TRANSITION** type. Valid values:
        # 
        # *   **BACKUP**: backup rule
        # *   **TRANSITION**: lifecycle rule
        # *   **REPLICATION**: replication rule
        self.rule_type = rule_type
        # This parameter is required only if the **RuleType** parameter is set to **BACKUP**. This parameter specifies the backup schedule settings. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   startTime: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of 1 hour. P1D specifies an interval of one day.
        self.schedule = schedule
        # This parameter is required only if the **RuleType** parameter is set to **TAG**. This parameter specifies the resource tag filter rule.
        self.tag_filters = tag_filters
        # This parameter is required only if the RuleType parameter is set to BACKUP. The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        if self.data_source_filters:
            for k in self.data_source_filters:
                if k:
                    k.validate()
        if self.retention_rules:
            for k in self.retention_rules:
                if k:
                    k.validate()
        if self.tag_filters:
            for k in self.tag_filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_days is not None:
            result['ArchiveDays'] = self.archive_days
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.cold_archive_days is not None:
            result['ColdArchiveDays'] = self.cold_archive_days
        result['DataSourceFilters'] = []
        if self.data_source_filters is not None:
            for k in self.data_source_filters:
                result['DataSourceFilters'].append(k.to_map() if k else None)
        if self.immutable is not None:
            result['Immutable'] = self.immutable
        if self.keep_latest_snapshots is not None:
            result['KeepLatestSnapshots'] = self.keep_latest_snapshots
        if self.replication_region_id is not None:
            result['ReplicationRegionId'] = self.replication_region_id
        if self.retention is not None:
            result['Retention'] = self.retention
        result['RetentionRules'] = []
        if self.retention_rules is not None:
            for k in self.retention_rules:
                result['RetentionRules'].append(k.to_map() if k else None)
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        result['TagFilters'] = []
        if self.tag_filters is not None:
            for k in self.tag_filters:
                result['TagFilters'].append(k.to_map() if k else None)
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveDays') is not None:
            self.archive_days = m.get('ArchiveDays')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('ColdArchiveDays') is not None:
            self.cold_archive_days = m.get('ColdArchiveDays')
        self.data_source_filters = []
        if m.get('DataSourceFilters') is not None:
            for k in m.get('DataSourceFilters'):
                temp_model = UpdatePolicyV2RequestRulesDataSourceFilters()
                self.data_source_filters.append(temp_model.from_map(k))
        if m.get('Immutable') is not None:
            self.immutable = m.get('Immutable')
        if m.get('KeepLatestSnapshots') is not None:
            self.keep_latest_snapshots = m.get('KeepLatestSnapshots')
        if m.get('ReplicationRegionId') is not None:
            self.replication_region_id = m.get('ReplicationRegionId')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        self.retention_rules = []
        if m.get('RetentionRules') is not None:
            for k in m.get('RetentionRules'):
                temp_model = UpdatePolicyV2RequestRulesRetentionRules()
                self.retention_rules.append(temp_model.from_map(k))
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        self.tag_filters = []
        if m.get('TagFilters') is not None:
            for k in m.get('TagFilters'):
                temp_model = UpdatePolicyV2RequestRulesTagFilters()
                self.tag_filters.append(temp_model.from_map(k))
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class UpdatePolicyV2Request(TeaModel):
    def __init__(
        self,
        policy_description: str = None,
        policy_id: str = None,
        policy_name: str = None,
        rules: List[UpdatePolicyV2RequestRules] = None,
    ):
        # The description of the backup policy.
        self.policy_description = policy_description
        # The ID of the backup policy.
        self.policy_id = policy_id
        # The name of the backup policy.
        self.policy_name = policy_name
        # The rules in the backup policy.
        self.rules = rules

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = UpdatePolicyV2RequestRules()
                self.rules.append(temp_model.from_map(k))
        return self


class UpdatePolicyV2ShrinkRequest(TeaModel):
    def __init__(
        self,
        policy_description: str = None,
        policy_id: str = None,
        policy_name: str = None,
        rules_shrink: str = None,
    ):
        # The description of the backup policy.
        self.policy_description = policy_description
        # The ID of the backup policy.
        self.policy_id = policy_id
        # The name of the backup policy.
        self.policy_name = policy_name
        # The rules in the backup policy.
        self.rules_shrink = rules_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.rules_shrink is not None:
            result['Rules'] = self.rules_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('Rules') is not None:
            self.rules_shrink = m.get('Rules')
        return self


class UpdatePolicyV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdatePolicyV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePolicyV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePolicyV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVaultRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        resource_group_id: str = None,
        vault_id: str = None,
        vault_name: str = None,
        worm_enabled: bool = None,
    ):
        # The description of the backup vault. The description must be 0 to 255 characters in length.
        self.description = description
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the backup vault.
        # 
        # This parameter is required.
        self.vault_id = vault_id
        # The name of the backup vault. The name must be 1 to 64 characters in length.
        self.vault_name = vault_name
        # Whether to enable the vault worm feature. Once the worm feature is enabled, the vault and all its backup data cannot be deleted before they automatically expire. After enabling the worm feature, it is not supported to disable it. The worm feature is only effective for standard and archive backup vault.
        self.worm_enabled = worm_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        if self.vault_name is not None:
            result['VaultName'] = self.vault_name
        if self.worm_enabled is not None:
            result['WormEnabled'] = self.worm_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        if m.get('VaultName') is not None:
            self.vault_name = m.get('VaultName')
        if m.get('WormEnabled') is not None:
            self.worm_enabled = m.get('WormEnabled')
        return self


class UpdateVaultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateVaultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateVaultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateVaultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeBackupClientsRequest(TeaModel):
    def __init__(
        self,
        client_ids: Dict[str, Any] = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        instance_ids: Dict[str, Any] = None,
    ):
        # The IDs of Cloud Backup clients. The total number of Cloud Backup client IDs and ECS instance IDs cannot exceed 100.
        self.client_ids = client_ids
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The IDs of Elastic Compute Service (ECS) instances. The total number of ECS instance IDs and Cloud Backup client IDs cannot exceed 100.
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class UpgradeBackupClientsShrinkRequest(TeaModel):
    def __init__(
        self,
        client_ids_shrink: str = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        instance_ids_shrink: str = None,
    ):
        # The IDs of Cloud Backup clients. The total number of Cloud Backup client IDs and ECS instance IDs cannot exceed 100.
        self.client_ids_shrink = client_ids_shrink
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The IDs of Elastic Compute Service (ECS) instances. The total number of ECS instance IDs and Cloud Backup client IDs cannot exceed 100.
        self.instance_ids_shrink = instance_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids_shrink is not None:
            result['ClientIds'] = self.client_ids_shrink
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids_shrink = m.get('ClientIds')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')
        return self


class UpgradeBackupClientsResponseBodyInstanceStatuses(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        instance_id: str = None,
        valid_instance: bool = None,
    ):
        # The error code that is returned. Valid values:
        # 
        # *   If the value is empty, the call is successful.
        # *   **InstanceNotExists**: The ECS instance does not exist.
        # *   **InstanceNotRunning**: The ECS instance is not running.
        # *   **CloudAssistNotRunningOnInstance**: Cloud Assistant is unavailable.
        self.error_code = error_code
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # Indicates whether an HBR client can be installed on the ECS instance. Valid values:
        # 
        # *   true: An HBR client can be installed on the ECS instance.
        # *   false: An HBR client cannot be installed on the ECS instance.
        self.valid_instance = valid_instance

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.valid_instance is not None:
            result['ValidInstance'] = self.valid_instance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ValidInstance') is not None:
            self.valid_instance = m.get('ValidInstance')
        return self


class UpgradeBackupClientsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        instance_statuses: List[UpgradeBackupClientsResponseBodyInstanceStatuses] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The status of the ECS instance. If the status of an ECS instance cannot meet the requirements to install an HBR client and the value of the InstanceIds parameter is greater than 1, an error message is returned based on the value of this parameter.
        self.instance_statuses = instance_statuses
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The ID of the asynchronous job. You can call the DescribeTask operation to query the execution result of an asynchronous job.
        self.task_id = task_id

    def validate(self):
        if self.instance_statuses:
            for k in self.instance_statuses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['InstanceStatuses'] = []
        if self.instance_statuses is not None:
            for k in self.instance_statuses:
                result['InstanceStatuses'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.instance_statuses = []
        if m.get('InstanceStatuses') is not None:
            for k in m.get('InstanceStatuses'):
                temp_model = UpgradeBackupClientsResponseBodyInstanceStatuses()
                self.instance_statuses.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpgradeBackupClientsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeBackupClientsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpgradeBackupClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeClientRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        resource_group_id: str = None,
        vault_id: str = None,
    ):
        # The ID of the Cloud Backup client.
        self.client_id = client_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class UpgradeClientResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The ID of the asynchronous job. You can call the DescribeTask operation to query the execution result of an asynchronous job.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpgradeClientResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeClientResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpgradeClientResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


